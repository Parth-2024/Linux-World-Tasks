from email.message import EmailMessage
import ssl
import smtplib

def sendEmail(sender,receiver,password,subject,body):
    Em=EmailMessage()
    Em['From']=sender
    Em['To']=receiver
    Em['Subject']=subject
    Em.set_content(body)

    context=ssl.create_default_context()#used to keep the internal connection secure

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,Em.as_string())
        
sender=input("Enter the email fro which you are gonna send the mail:")
password=input("Enter its password:")
receiver=input("Enter the email to which you are gonna send the mail:")
subject=input("Enter the subject of the mail:\n")
body=input("Enter the body of the mail:\n")
sendEmail(sender,receiver,password,subject,body)