import mysql.connector
from functions.sendmail import send_email


conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()


def meet_email(list_of_persons,subject,content):
    """
    Sends an email to multiple persons.

    Args:
        list_of_persons (list): A  list of ids of the persons.
        subject (str): The subject of the email.
        content (str): The content of the email.
    """
    for person in list_of_persons:
        cursor.execute(f'select email from employees where Id = {person}')
        row = cursor.fetchone()
        email = row[0]
        send_email(email,subject,content)
        return f'The mail was sent to address {email}'