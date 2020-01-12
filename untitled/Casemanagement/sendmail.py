#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#发送测试报告到邮箱
def send_mail(sender,psw,receiver,smtpserver,report_file,port):
    "第四步：发送最新测试报告内容；"
    with open(report_file,"rb") as f:
        mail_body = f.read()
    subject = u"自动化测试报告"
    #定义邮件内容：
    msg = MIMEMultipart()
    msg = MIMEText(mail_body,_subtype="html",_charset="utf-8")
    msg["Subject"] = Header(subject,"utf-8")
    msg["From"] = Header(sender)
    smtp = smtplib.SMTP(smtpserver)
    smtp.set_debuglevel(1)  #调试邮箱
    smtp.starttls()
    #添加附件
    #att = MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    att = MIMEText(mail_body,"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att)
    try:
        #smtp = smtplib.SMTP_SSL(smtpserver,port)
        smtp.login(user=sender,password=psw)
    except Exception as e:
        print(e)
        #smtp = smtplib.SMTP()
        #smtp.connect(smtpserver,port)
    #用户名密码
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print('test report email has send out!')


if __name__=="__main__":
    sender = "dc111000@hotmail.com"
    psw = "dong159753"
    receiver = "dc111000@hotmail.com"
    smtplib = "smtp.hotmail.com"
    report_file = "report.html"
    send_mail(sender,psw,receiver,smtplib,report_file,23    )