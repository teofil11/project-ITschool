import smtplib, ssl


class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "teodorescuteofil@gmail.com"
        self.password = ""

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        
        result = service.sendmail(self.sender_mail, emails, f"Subject: {subject}\n\n{content}")

        service.quit()


def send_email(mails,subject,content):
    """
    Send an email to the specified recipients.

    Args:
        mails (str or list): The email address or a list of email addresses to send the email to.
        subject (str): The subject of the email.
        content (str): The content or body of the email.

    """
    mail = Mail()
    mail.send(mails, subject, content)
