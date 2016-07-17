#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import ConfigParser
import string,os,sys

def send_list():
	try:
		cf = ConfigParser.ConfigParser()
		cf.read("mail_content")
		send_str=cf.get("mail_content","send_list")
		return send_str.split("|")
	except:
		print "请在mail_content文件的[mail_content]元素下添加sendlist项"
		exit()

def get_config():
	cf = ConfigParser.ConfigParser()
	try:
		cf.read("mail_config")
		mail_config={}
		mail_config["sender"]=cf.get("mail_config","sender")
		mail_config["sender_name"]=cf.get("mail_config","sender_name")
		mail_config["password"]=cf.get("mail_config","password")
		mail_config["mail_host"]=cf.get("mail_config","mail_host")
		mail_config["mail_postfix"]=cf.get("mail_config","mail_postfix")
	except:
		print "请给出完整的mail_config文件，否则无法完成邮件发送，mail_config示例在源码中含有"
		exit()
	return mail_config

def get_accessory_list():
	cf =ConfigParser.ConfigParser()
	try:
		cf.read("mail_content")
		accessory_list = cf.get("mail_content","accessory_list")
		if accessory_list != "": 
			return accessory_list.split("|")
		else:
			return []
	except:
		return []

def get_content():
	mail_content = {}
	cf = ConfigParser.ConfigParser()
	try:
		cf.read("mail_content")
	except:
		print "请给出完整的mail_content文件，否则无法完成邮件发送，mail_content示例在源码中含有"
		exit()
	
	try:
		mail_content["subject"]=cf.get("mail_content","subject")
	except:
		mail_content["subject"]="NO TITLE"
	
	try:		
		mail_content["encoding"]=cf.get("mail_content","encoding")
	except:
		mail_content["encoding"]="utf-8"

	try:
		mail_content["mail_msg"]=cf.get("mail_content","mail_msg")
	except:
		mail_content["mail_msg"]=""
	
	try:
		img_list = cf.get("mail_content","img_list")
		mail_content["img_list"]=[]
		if img_list != "":
			mail_content["img_list"]=img_list.split("|")
	except:
		mail_content["img_list"]=[]

	return mail_content

def send_mail_function(mail_config,content,send_list,accessory_list):
	#设置SMTP服务器、发送者、口令
	sender = mail_config["sender"]
	password = mail_config["password"]
	mail_host= mail_config["mail_host"] 

	#设置接受者列表
	receivers = send_list  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

	msgRoot = MIMEMultipart('related')
	msgRoot['From'] = mail_config["sender_name"]+"<"+sender+">"
 	#msgRoot['To'] =  ""
	msgRoot['Subject'] = Header(content["subject"], content["encoding"])
	
	msgAlternative = MIMEMultipart('alternative')
 	msgRoot.attach(msgAlternative)

	msgAlternative.attach(MIMEText(content["mail_msg"], 'html', 'utf-8'))

	i = 1;
	for img in content["img_list"]:
		# 指定图片为当前目录
		fp = open(img, 'rb')
		msgImage = MIMEImage(fp.read())
		fp.close()

		# 定义图片 ID，在 HTML 文本中引用
		msgImage.add_header('Content-ID', '<image%d>'%i)
		msgRoot.attach(msgImage)
		i=i+1
	
	for accessory in accessory_list : 
		fp = open(accessory, 'rb')
		accessory_file = MIMEImage(fp.read())
		fp.close()
		msgRoot.attach(accessory_file)

	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host)
		smtpObj.login(sender,password)
		smtpObj.sendmail(sender, receivers, msgRoot.as_string())
		print "Success!!!"
	except smtplib.SMTPException,e:
		print e
    		print "Error: Fail To Send"
	smtpObj.close()

def main():
	#print get_content()
	send_mail_function(get_config(),get_content(),send_list(),get_accessory_list())

if __name__ == "__main__":
	main()
