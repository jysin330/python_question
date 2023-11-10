import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
username= "roshnisingh882000@gmail.com"
password = 'hw8ygqgbdgsqibxqs'

def send_mail(text= "email body" , subject ="hello world",from_email='Roshni <roshnisingh882000@gmail.com>', to_emails=None, html =None):
    if isinstance(to_emails, list):
    # login  to my smpt server
        msg = MIMEMultipart('alternative')
        msg['From'] = from_email
        msg['TO'] = ', '.join(to_emails)
        msg['subject'] = subject
        print(msg)
        text_part = MIMEText(text, 'plain')
        msg.attach(text_part)
        if html !=None:
            html_part = MIMEText('<h1> hello jyoti </h1>', 'html')
            msg.attach(html_part)
        msg_str = msg.as_string()
        print(msg_str)
        
        server = smtplib.SMTP(host='smpt.gmail.com', port = 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_emails, msg_str)
        server.quit()
    
    
    
    
send_mail(to_emails='roshnisingh882000@gmail.com')
    
    
    
    
    
    # another way ---->
    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass