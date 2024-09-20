#https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps

'''
To send mail 
    enable in gmail the 2 step verification 
Then 
    use below link to create app password
    with app password and your mail id try to run the below code

    #https://support.google.com/accounts/answer/185833?hl=en
'''



import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'rohithyadav1705@gmail.com'
email_passwd = 'pgjs kvfs rhfv xgpc'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='gmaheswaranmca@gmail.com', msg="Hello sir")
connection.close()
print('Mail sent successfully')