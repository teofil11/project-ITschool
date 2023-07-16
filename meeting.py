from functions.sendmail import send_email

def meet_email(list_of_persons,subject,content):
    email = 'teodorescu_teofil@yahoo.com'
    for person in list_of_persons:
        send_email(email,subject,content)