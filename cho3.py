from bs4 import BeautifulSoup

from find_dl import request_douban, get_SDDE_695_url, parallel_downloads, can_find


def main():
    SDDE_695 = input('输入要下载的番号(回车确定)：')
    url = 'https://sukebei.nyaa.si/?f=0&c=0_0&q=' + SDDE_695
    html = request_douban(url)
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


if __name__ == '__main__':
    main()
