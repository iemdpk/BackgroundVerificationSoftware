import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(email,bgvVerification):
    smtp_server = "smtp.office365.com"
    smtp_port = 587
    email = "deepakdevlo@outlook.com"
    password = "aW5478901#"


    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = "m.deepak1824@gmail.com"
    msg['Subject'] = "Test Email from Python You have to verify these two things" +  str(bgvVerification)


    body = "This is a test email sent from Python!"
    msg.attach(MIMEText(body, 'plain'))

    try:

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(email, password)
        server.sendmail(email, msg['To'], msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
