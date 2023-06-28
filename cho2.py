from bs4 import BeautifulSoup
import re
from find_dl import request_douban, get_dl_url, parallel_downloads


def main(page):
    input_url = input('请输入链接：')
    if '&p=' in input_url:
        text = re.sub(r'abc\d+', '', input_url)
    input_page1 = input('想从第几页开始下载？')
    input_page2 = input('想从第几页结束下载？')
    p1 = int(input_page1)
    p2 = int(input_page2)
    print('开始下载')
    url = input_url + '&p=' + str(page)
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    get_dl_url(soup)
    max_workers = 5
    # 最大线程数
    parallel_downloads(get_dl_url(soup), max_workers)
    # 并行下载文件
    print('下载完成')
    input("按下任意键返回首页...")


if __name__ == '__main__':
    for i in range(p1, p2 + 1):
        main(i)
