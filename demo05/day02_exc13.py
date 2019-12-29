#codng:utf-8
"""
控制台输入邮箱地址，程序识别用户名和公司名后将用户名和公司名输出到控制台
要求：
1、校验输入内容是否符合规范（xx@yy.com）,如果是进入下一步，
如果否则抛出提示"incorrent email format".邮箱必须以.com结尾
2、可以循环"输入--输出判断结果"整个过程
3、按字母Q不区分大小写退出循环结束程序
"""
def main():
    while True:
        email = input("请输入您的邮箱，输入Q或q退出程序：")
        if email == "Q" or email == "q":
            break
        if email.endswith(".com"):
            print("您的用户名是：",email.split("@")[0])
            print("您的公司名是：",(email.split("@")[1]).replace(".com",""))
        else:
            print("incorrent email format")

if __name__ == "__main__":
    main()