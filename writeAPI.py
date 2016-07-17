# -*- coding: UTF-8 -*-
import ConfigParser

def main():
	content = """<html><head><title>图片</title></head>
		 	<body>
			<p>图片演示：</p>
			<p>图片1<br/><img src="cid:image1"></p>
			<p>图片2<br/><img src="cid:image2"></p>
			</body></html>"""
	encoding = "utf-8"
	subject = """图片演示"""
	#accessory_list = ['2016-07-14_bar-1.jpg','2016-07-14_curve-1.jpg']
	accessory_list = []
	img_list = ['XXX.jpg','XXX.jpg']
	#img_list=[]
	send_list = ['XXXXg@yyy.com']

	write_all(content,subject,encoding,send_list,accessory_list,img_list)


def write_content(html):
	conf = ConfigParser.ConfigParser()
	conf.read("mail_content")
	conf.set("mail_content","mail_msg",html)
	fh = open("mail_content" ,'w')
	conf.write(fh)#把要修改的节点的内容写到文件中
	fh.close()

def write_send_list(send_list):
	ans=""
	for list in send_list:
		ans += list
		ans += "|"
	conf = ConfigParser.ConfigParser()
	conf.read("mail_content")
	conf.set("mail_content","send_list",ans[0:len(ans)-1])
	fh = open("mail_content" ,'w')
	conf.write(fh)#把要修改的节点的内容写到文件中
	fh.close()

def write_accessory_list(accessory_list):
	ans=""
	for list in accessory_list:
		ans += list
		ans += "|"
	conf = ConfigParser.ConfigParser()
	conf.read("mail_content")
	conf.set("mail_content","accessory_list",ans[0:len(ans)-1])
	fh = open("mail_content" ,'w')
	conf.write(fh)#把要修改的节点的内容写到文件中
	fh.close()

def write_img_list(img_list):
	ans=""
	for list in img_list:
		ans += list
		ans += "|"
	conf = ConfigParser.ConfigParser()
	conf.read("mail_content")
	conf.set("mail_content","img_list",ans[0:len(ans)-1])
	fh = open("mail_content" ,'w')
	conf.write(fh)#把要修改的节点的内容写到文件中
	fh.close()



def write_subject(subject):
	conf = ConfigParser.ConfigParser()
	conf.read("mail_content")
	conf.set("mail_content","subject",subject)
	fh = open("mail_content" ,'w')
	conf.write(fh)#把要修改的节点的内容写到文件中
	fh.close()

def write_encoding(encoding):
	conf = ConfigParser.ConfigParser()
	conf.read("mail_content")
	conf.set("mail_content","encoding",encoding)
	fh = open("mail_content" ,'w')
	conf.write(fh)#把要修改的节点的内容写到文件中
	fh.close()

def write_all(content,subject,encoding,send_list,accessory_list,img_list):
	conf = ConfigParser.ConfigParser()
	conf.read("mail_content")
	conf.set("mail_content","mail_msg",content)
	conf.set("mail_content","subject",subject)
	conf.set("mail_content","encoding",encoding)
	
	ans=""
	for list in send_list:
		ans += list
		ans += "|"
	conf.set("mail_content","send_list",ans[0:len(ans)-1])

	ans=""
	for list in accessory_list:
		ans += list
		ans += "|"
	conf.set("mail_content","accessory_list",ans[0:len(ans)-1])

	ans=""
	for list in img_list:
		ans += list
		ans += "|"
	conf.set("mail_content","img_list",ans[0:len(ans)-1])

	fh = open("mail_content" ,'w')

	conf.write(fh)#把要修改的节点的内容写到文件中
	fh.close()

if __name__=="__main__":
	main()
