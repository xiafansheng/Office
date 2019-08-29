import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from Office.get_path import getPath

courses = ['自然辩证法概论','公司财务学','基金投资策略','互联网金融'
           ,'金融市场学','金融市场时间序列分析','金融专题研究'
    ,'高级计量经济学','经济研究方法与学术规范']

#根据课程判断及生成文件夹
def mkdir(course):
    path = r'C:\Users\Administrator\Desktop\%s'%course
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
    else:
        pass


def write_log(path,pptname):
    with open(path,'a+') as f:
        content = pptname + '\n'
        f.write(content)


def read_log(logpath):
    if os.path.exists(log_path) == False:
        with open(log_path, 'w') as f:
            f.write(log_path)
            send_ppt = log_path
            return  send_ppt
    else:
        f = open(log_path,'r')
        sent_ppt = [i.strip('\n') for i in  f.readlines()]
        return sent_ppt

def list_file(course_path):
    all_ppt  = os.listdir(courese_path)
    return all_ppt

def send_ppt(file_path,subject,body,filename):
    smtpserver = "smtp.163.com"
    port = 465
    sender = "xfs9619@163.com"
    psw = "xfs9619"
    receiver = ["cufe2018jrxs@163.com"]  #"cufe2018jrxs@163.com"  'xfs9619@163.com'
    msg = MIMEMultipart()
    msg["from"] = sender
    msg["to"] = ','.join(receiver)
    msg["subject"] = subject
    body = MIMEText(body, "plain", "utf-8")
    msg.attach(body)
    part = MIMEApplication(open(file_path, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=('gbk', '', filename) )
    msg.attach(part)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('%s发送成功'%file_path)

for c in courses:
    courese_path = r'C:\Users\Administrator\Desktop\%s' % c
    log_path = courese_path+'\log.txt'
    sent_ppt_path = read_log(log_path)
    all_ppt_path,name = getPath(courese_path)
    newppt = [i for i in all_ppt_path if i not in sent_ppt_path]
    for ppt in newppt:
        mail_content = ppt.split('\\')[-1]
        ct = c +'-'+ mail_content
        send_ppt(ppt,ct,mail_content,mail_content)
        write_log(log_path,ppt)



