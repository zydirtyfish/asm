# asm
Auto Send Mail Tool ( ASM )

This tool can help you to send emails in the form of HTML automatically. The only thing you need to do is to write the `mail_content` according to the format given in the source file. You can also modify this file by using the api given in writeAPI.py.

Start your "Hello world" mail by excuting `sh auto_send.sh` if you have finished the `mail_content` metioned above.

1. send_mail.py
   This is the kernel file by encapsulating `smtplib`. There is no need for you to know how it is realized, because you only need to modify the `mail_content` if you want to send mails automatically.

2. writeAPI.py
    You can modify the `mail_content` much easier by using the api in this file.
    `write_content(html)` : To modify the mail_msg
    `write_send_list(send_list)` : To modify the send_list
    `write_accessory_list(accessory_list)` : To modify the accessory list
    `write_img_list(img_list)` : To modify the images contained in the main_msg
    `write_all(content,subject,encoding,send_list,accessory_list,img_list)` : To modify the parameters all above
  
3. mail_config
    Always likes this.
      [mail_config]
      sender = XXXX@yyy.com `It is your own email address`
      sender_name = your_name `Your own name`
      password = ****         `Password of you email, always the smtp password`
      mail_host = smtp.yyy.com `SMTP server domain. You can always find it on the Internet`
      mail_postfix = yyy.com


4. mail_content
    Always likes this.
      [mail_content]
      send_list = XXXX@yyy.com `who will receive this mail`
      subject = Pic            `Subject of this mail`
      encoding = utf-8         `Encoding of the main content`
      accessory_list =          `Accessories contained in the mail`
      mail_msg = <html><head><title>picture</title></head>
			 	<body>
				<p>Pic：</p>
				<p>Pic1<br/><img src="cid:image1"></p> `image label, the src attribution always set as [cid:imageN]`
				<p>Pic2<br/><img src="cid:image2"></p>
				</body></html>            `main_content of the mail, always the html`  
      img_list = **.jpg|**.jpg    `images contained in the mail_msg`





