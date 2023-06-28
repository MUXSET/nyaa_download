def cho_page():

    input_page1 = input('想从第几页开始下载？')
    input_page2 = input('想从第几页结束下载？')
    p1 = int(input_page1)
    p2 = int(input_page2)
    return p1, p2
cho_page()
print(cho_page())