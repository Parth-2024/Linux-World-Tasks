import smtplib

# list of email_id to send the mail
li = ["akshatkhandelwal28@gmail.com", "parthjain.pro.2045@gmail.com"]

for dest in li:
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("kashifauddeen7@gmail.com", "cqjkwphkvffrgeax")
	message = "hye this is bulk email"
	s.sendmail("kashifauddeen7@gmail.com", dest, message)
	s.quit()