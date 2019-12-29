#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def send_mail():
    #发送邮箱
    sender = "imdcc@sina.com"
    #接收邮箱
    receiver = "imdcc@sina.com"
    #发送邮件主题
    subject = "python eamil test"
    #发送邮件服务器
    smtpserver = "smtp.sina.com"
    #发送邮箱用户/密码
    username = "imdcc@sina.com"
    password = 'dong159753'
    #编写text类型邮件正文
    msg = MIMEText("<html><h1>你好</h1></html>",_subtype="html",_charset="utf-8")
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = Header(sender)
    smtp = smtplib.SMTP("smtp.sina.com")
    smtp.set_debuglevel(1)   #调试邮箱
    smtp.starttls()
    #smtp.connect("smtp.sina.com")
    # import smtplib
    #smtplib.SMTP_SSL(host='smtp.sina.com').connect(host='smtp.sina.com')
    # smtp.ehlo()
    # smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.close()

#最新的文件的获取
import os
#定义文件目录
result_dir = os.path.join(os.path.dirname(__file__),"report")
lists = os.listdir(result_dir)
print(lists)
#按最新时间对目录下文件进行排序
lists.sort(key=lambda fn:os.path.getmtime(result_dir))
print('最新的文件是：'+lists[-1])
file = os.path.join(result_dir,lists[-1])
print(file)

