import os

import cho123


def clear_screen():
    os.system('cls')


def print_menu():
    clear_screen()
    print("请选择一个选项:")
    print("1. 单链接下载")
    print("2. 批量下载")
    print("3. 搜索番号下载")
    print("4. 退出")


def get_user_choice():
    while True:
        user_choice = input("请输入选项数字: ")
        if user_choice.isdigit():
            return int(user_choice)
        else:
            print("无效的输入，请输入一个数字")


def process_choice(choice_menu):
    if choice_menu == 1:
        print("你选择了选项 1. 单链接下载")
        cho123.cho1()
    elif choice_menu == 2:
        print("你选择了选项 2. 批量下载")
        cho123.cho2()
    elif choice_menu == 3:
        print("你选择了选项 3. 搜索番号下载")
        cho123.cho3()
    elif choice_menu == 4:
        print("程序已退出")
    else:
        print("无效的选择")


if __name__ == "__main__":
    while True:
        print_menu()
        choice = get_user_choice()
        process_choice(choice)
        if choice == 4:
            break
