# -*- coding:utf-8 -*-
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(subject,body):
    smtpserver = "smtp.163.com"
    port = 465
    sender = "xfs9619@163.com"
    psw = "xiafansheng9619"
    receiver = "2467028805@qq.com"
    # file_path = "result.html"
    # with open(file_path, "rb") as fp:
    #     mail_body = fp.read()

    msg = MIMEMultipart()
    msg["from"] = sender
    msg["to"] = receiver
    msg["subject"] = subject
    body = MIMEText(body, "plain", "utf-8")
    msg.attach(body)
    # 附件
    # att = MIMEText(mail_body, "base64", "utf-8")
    # att["Content-Type"] = "application/octet-stream"
    # att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    # msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)                      # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)                       # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()
    return  '发送成功'
zw = time.asctime(time.localtime(time.time()))
sendmail('邮件', zw)