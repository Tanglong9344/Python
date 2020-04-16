from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage

# qq邮箱smtp服务器
host_server = 'smtp.qq.com'
# sender_qq为发件人的qq号码
sender_qq = '1654200709'
# qq邮箱的授权码
autho_code = 'eimfodklvltgcgha'
# 发件人的邮箱
sender_qq_mail = '1654200709@qq.com'
# 收件人邮箱
receiver = 'flyingfish9344@gmail.com'
#  邮件的正文内容
mail_content = '\nHello,this is just a test...\n附件是成绩表\n'
#  邮件标题
mail_title = 'A test from Tanglong'
#  ssl登录
smtp = SMTP_SSL(host_server)
#  set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)

smtp.ehlo(host_server)
smtp.login(sender_qq, autho_code)

msg = MIMEMultipart()
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver
msg.attach(MIMEText(mail_content,'plain','utf-8'))

#  构造附件，传送当前目录下的 result.txt 文件
att = MIMEText(open('result.txt', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
#  这里的filename可以任意写，写什么名字，邮件中显示什么名字
att["Content-Disposition"] = 'attachment; filename="attach_result.txt"'
msg.attach(att)

#  attach a image
#  读取图片
import os
str = os.getcwd() + ''
strs = str.split("\\")
root = strs[0]+"/"+strs[1]

fp = open(root+'/picture/python-logo.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
#  添加图片
msgImage.add_header('Content-ID', 'send_image')
msg.attach(msgImage)
print(msg)
#  send mail
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()