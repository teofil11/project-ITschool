import mysql.connector
from functions.sendmail import send_email
from datetime import date as dt

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='project')
cursor = conn.cursor()

def calculate_hours_worked():
    cursor.execute("select * from access where cast(access.date as date) = curdate()")
    rows = cursor.fetchall()
    hours = {}
    persons = {}

    for row in rows:
        employee_id = row[0]
        direction = row[1]
        timestamp = row[2]

        if direction == "in":
            for out_row in rows:
                if out_row[0] == employee_id and out_row[1] == "out" and out_row[2] > timestamp:
                    exit_time = out_row[2]
                    break
            else:
                continue 

            duration = (exit_time - timestamp).seconds // 3600

            if employee_id in hours:
                hours[employee_id] += duration
            else:
                hours[employee_id] = duration
    for key,value in hours.items():
        persons[key] = {'email': 'Teodorescu_teofil@yahoo.com'}
    for key in persons.items():
        email = key[1]['email']
        send_email(email, 'Employee hours worked', f"Employee with id {key[0]} didn't work 8 hours in {dt.today()}")
