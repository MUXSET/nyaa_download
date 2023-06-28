from find_dl import parallel_downloads


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

    return input_urls


def main():
    urls = cho1()
    print('开始下载')
    max_workers = 5
    # 最大线程数
    parallel_downloads(urls, max_workers)
    # 并行下载文件

    print('下载完成')
    input("按下任意键返回首页...")


if __name__ == "__main__":
    main()
