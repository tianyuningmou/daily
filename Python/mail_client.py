# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by tianyuningmou

FILE: redis_manager.py
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/12/8 下午4:32

DESCRIPTION:  .

VERSION: : #2 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2018/1/18 下午4:32
"""

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os


_MAIL_SIGNATURE_ = """
签名部分
"""


class SMTP_Client(object):
    def __init__(self, account, password, server_host="smtp.easyto.com", server_port=25):
        """
        SMTPClient的构造函数
        :param account: such as "xin.liu@easyto.com"
        :param password: the password used to login to smtp server
        :param server_host: the smtp server host
        :param server_port: the smtp server port
        """
        assert isinstance(account, str)
        assert isinstance(password, str)
        assert isinstance(server_host, str)
        assert isinstance(server_port, int)
        self.account = account
        self.password = password
        self.server_host = server_host
        self.server_port = server_port

    @staticmethod
    def file_valid(file_path):
        return True if os.path.exists(file_path) and os.path.isfile(file_path) else False

    def send_mail(self, mail_to, cc, subject, content, embedded_img_list, attachment_img_list=list(), attachment_list=list()):
        """
        send_mail
        :param mail_to: destination mail account
        :param subject: topic
        :param content: content
        :param embeded_img_list:  内嵌的图片
        :param attachment_img_list:  作为附件的图片
        :param attachment_list:  attachment_list 非图片类的附件
        :return:
        """
        assert isinstance(mail_to, str)
        assert isinstance(cc, list)
        assert isinstance(subject, str)
        assert isinstance(content, str)
        assert isinstance(embedded_img_list, list)
        assert isinstance(attachment_img_list, list)
        assert isinstance(attachment_list, list)
        if not all([os.path.exists(i) and os.path.isfile(i) for i in embedded_img_list]):
            return False, "not all image exist {LIST}".format(LIST=embedded_img_list)
        mail = self.get_mail(subject, self.account, mail_to, cc, content, embedded_img_list, attachment_img_list, attachment_list)
        self.real_send(mail_to, cc, mail)
        return True, "success"

    def real_send(self, mail_to, cc, mail):
        import smtplib
        try:
            smtp = smtplib.SMTP()
            smtp.set_debuglevel(1)
            smtp.connect(self.server_host)
            smtp.login(self.account, self.password)
            toaddrs = [mail_to] + cc
            smtp.sendmail(self.account, toaddrs, mail.as_string())
            smtp.quit()
        except Exception as e:
            print("real_send got exception, err is " + str(e))

    @staticmethod
    def get_mail(subject, mail_from, mail_to, cc, content, embedded_img_list, attachment_img_list, attachment_list):
        """

        :param subject: topic
        :param mail_from: source mail account
        :param mail_to: destination mail sccount
        :param content: content
        :param embedded_img_list: 内嵌的图片
        :param attachment_img_list: 作为附件的图片
        :param attachment_list: 非图片类的附件
        :return:
        """
        msg_root = MIMEMultipart('related')
        msg_root['Subject'] = subject
        msg_root['From'] = mail_from
        msg_root['To'] = mail_to
        msg_root['CC'] = ','.join(cc)
        msg_root.preamble = 'This is a multi-part message in MIME format.'
        msg_root.attach(MIMEText(content, 'plain', 'utf-8'))
        msg_root.attach(MIMEText('\n\n\n', 'plain', 'utf-8'))
        msg_alternative = MIMEMultipart('alternative')
        msg_root.attach(msg_alternative)
        text = MIMEText(_MAIL_SIGNATURE_, 'plain', 'utf-8')
        msg_root.attach(text)

        # 解析内嵌的图片并添加到邮件中
        for index, image in enumerate(embedded_img_list, start=1):
            msg_text = MIMEText('图片加载不正常')
            msg_alternative.attach(msg_text)
            tmp_txt = MIMEText('<img src="cid:image{INDEX}"><br>'.format(INDEX=index), 'html')
            msg_alternative.attach(tmp_txt)
            with open(image, "rb") as f:
                tmp_img = MIMEImage(f.read())
                tmp_img.add_header("Content-ID", "<image{INDEX}>".format(INDEX=index))
                msg_root.attach(tmp_img)

        # 解析图片附件并添加
        for attach_image in attachment_img_list:
            with open(attach_image, 'rb') as f:
                mime = MIMEBase('image', 'png', filename=os.path.basename(attach_image))
                mime.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attach_image))
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg_root.attach(mime)

        # 解析非图片类的附加并添加
        for attach_file in attachment_list:
            att = MIMEText(open(attach_file, 'rb').read(), 'base64', 'gb2312')
            att["Content-Type"] = 'application/octet-stream'
            att.add_header("Content-Disposition", "attachment", filename=os.path.basename(attach_file))
            msg_root.attach(att)
        return msg_root


if __name__ == '__main__':
    from datetime import datetime
    subject = u"{SUFFIX}".format(SUFFIX=datetime.now().strftime('%Y-%m-%d'))
    s = SMTP_Client("mail_address", "mail_passwd")
    img_list = []
    attachment_list = ['/Users/tianyuningmou/Desktop/日报.docx']
    s.send_mail("mail_1", ["mail_2", "mail_3", "mail_4"], subject, u"您好：\n&#12288&#12288附件是{SUFFIX}日报，请查收！".format(SUFFIX=datetime.now().strftime('%Y-%m-%d')), img_list, attachment_list=attachment_list)
