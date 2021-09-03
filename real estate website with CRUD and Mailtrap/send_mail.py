import smtplib
from email.mime.text import MIMEText

def send_mail(name, email, description):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'Mailtrap User id'
    password = 'Mailtrap Password '
    message = f"<h3>New Contact US form</h3><ul><li>Name:{name}</li><li>E-mail address:{email}</li><li>Description:{description.rstrip()}</li></ul>"

    sender_email = email
    receiver_email = 'PropertyFY.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Contact US'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send mail
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())