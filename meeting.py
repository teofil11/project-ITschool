from functions.sendmail import send_email

def meet_email(list_of_persons,subject,content):
    """
    Sends an email to multiple persons.

    Args:
        list_of_persons (list): A  list of ids of the persons.
        subject (str): The subject of the email.
        content (str): The content of the email.
    """
    
    email = 'teodorescu_teofil@yahoo.com'
    for person in list_of_persons:
        send_email(email,subject,content)
