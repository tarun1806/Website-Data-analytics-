from email.mime.text import MIMEText
import smtplib

def send_email(email,height,avg_height):
    from_email="tarun18061991@gmail.com"
    from_pass="Shumacher@1"
    to_email=email

    subject="Height data"
    message="Hi, your height is <strong>%s</strong><br>Average height of the population is <strong>%s</strong>" %(height,avg_height)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_pass)
    gmail.send_message(msg)
