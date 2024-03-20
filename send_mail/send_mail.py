import smtplib
from email.mime.text import MIMEText
# using multipart is so i can attach both a plain text email and an html email or i can also attach files 
from email.mime.multipart import MIMEMultipart
username = 'infobot@mushroom.solutions'
# username = 'roshnisingh882000@gmail.com'
# password = 'tjfezqsfgxbxeckr'
password = 'Qoq61514'
def send_mail(text='Email body', subject='hello world', from_email='infobot <infobot@mushroom.solutions>', to_emails=None):
    assert isinstance(to_emails, list)
    # msg = MIMEMultipart('alternative')
    # msg['Form'] = from_email
    # msg['To'] = to_emails
    # msg['Subject'] = subject
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText('<h1>This is working</h1>', 'html')
    # msg.attach(html_part)

    msg_str = msg.as_string()
    # login to smpt server
    server = smtplib.SMTP(host='smtp.office365.com', port=587)
    # server = smtplib.SMTP(host='smtp.gmail.com', port=587)

    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()

send_mail(to_emails=['jyoti@mushroom.solutions'])

    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass


    # my_list =['abc, '123', "1234"]
    # "".join(my_list)
    # 'abc1231234'