import requests
from concurrent.futures import ThreadPoolExecutor
from retrying import retry
import threading

lock = threading.Lock()

MAX_RETRIES = 10
RETRY_INTERVAL = 1000


headars = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.146 Safari/537.36',
    }
def request_douban(url):

    try:
        response = requests.get(url, headers=headars)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None
#得到原始页面


def get_dl_url(soup):
    list = soup.find(class_='table table-bordered table-hover table-striped torrent-list').find_all('tr')
    urls = []
    for item in list:
        item_titleall = item.find_all('a')
        item_title = item_titleall[1].get('title')

        item_magnetall = item.find_all('a')
        bt_url = item_magnetall[2].get('href')
        bt_url = 'https://sukebei.nyaa.si' + bt_url

        urls.append(bt_url)
    return urls
#得到批量下载链接并存入数组

def get_SDDE_695_url(soup):

    the_ones = float('-inf')
    max_tr = None
    list = soup.find(class_='table table-bordered table-hover table-striped torrent-list').find_all('tr')
    urls = []
    for tr_tag in list:
        td_tags = tr_tag.find_all('td')
        if len(td_tags) >= 8:
            eighth_td = td_tags[7]
            text = eighth_td.get_text().strip()
            try:
                the_one = float(text)
                if the_one > the_ones:
                    the_ones = the_one
                    max_tr = tr_tag
            except ValueError:
                continue
    item_magnetall = max_tr.find_all('a')
    bt_url = item_magnetall[2].get('href')
    bt_url = 'https://sukebei.nyaa.si' + bt_url
    urls.append(bt_url)
    return urls

def can_find(soup):
    h3 = soup.find('h3')
    if h3:

        return False
    else:
        return True






@retry(stop_max_attempt_number=MAX_RETRIES, wait_fixed=RETRY_INTERVAL)
def download_file(url):
    response = requests.get(url,headers=headars)
    response.raise_for_status()
    filename = url.split("/")[-1]
    with lock:  # 加锁，确保写入文件时是独占的
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
#下载

def parallel_downloads(urls, max_workers):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(download_file, urls)

#设置线程并将数组传入下载函数




