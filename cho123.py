import re
from bs4 import BeautifulSoup
from find_dl import request_nyaa, get_dl_url ,get_SDDE_695_url, parallel_downloads, can_find


def cho1():
    input_urls = []  # 创建空数组

    print("请输入元素，每行一个用回车分隔（回车输入'quit'退出）：")

    while True:
        url = input()  # 逐行读取用户输入的元素
        if url == "quit":
            break
        segments = url.split("/")
        input_number = segments[-1]
        input_url = 'https://sukebei.nyaa.si/download/' + input_number + '.torrent'
        input_urls.append(input_url)  # 将元素追加到数组中

    urls = input_urls
    print('开始下载')
    max_workers = 5
    # 最大线程数
    parallel_downloads(urls, max_workers)
    # 并行下载文件


def cho2():
    input_url = input('请输入链接：')
    if '&p=' in input_url:
        text = re.sub(r'abc\d+', '', input_url)
    input_page1 = input('想从第几页开始下载？')
    input_page2 = input('想从第几页结束下载？')
    p1 = int(input_page1)
    p2 = int(input_page2)

    print('开始下载')

    max_workers = 5  # 最大线程数

    for page in range(p1, p2 + 1):
        url = input_url + '&p=' + str(page)
        html = request_nyaa(url)
        soup = BeautifulSoup(html, 'lxml')
        get_dl_url(soup)
        parallel_downloads(get_dl_url(soup), max_workers)

    print('下载完成')
    input("按下任意键返回首页...")


def cho3():
    SDDE_695 = input('输入要下载的番号(回车确定)：')
    url = 'https://sukebei.nyaa.si/?f=0&c=0_0&q=' + SDDE_695
    html = request_nyaa(url)
    soup = BeautifulSoup(html, 'lxml')

    if can_find(soup) is True:
        get_SDDE_695_url(soup)
        print('开始下载')
        max_workers = 5
        # 最大线程数
        parallel_downloads(get_SDDE_695_url(soup), max_workers)
        # 并行下载文件
        print('下载完成')
        input("按下任意键返回首页...")
    else:
        print('没有找到番号！')
        input("按下任意键返回首页...")
