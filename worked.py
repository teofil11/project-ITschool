import mysql.connector
from functions.sendmail import send_email
from datetime import date as dt

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='project')
cursor = conn.cursor()

def calculate_hours_worked():
    """
    Calculate the hours worked by employees and send email notifications for those who didn't work a full 8 hours.

    """
    cursor.execute("select * from access where cast(access.date as date) = curdate()")
    rows = cursor.fetchall()
    hours = {}

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
        if value < 8:
            cursor.execute(f"""SELECT t1.id,t2.email AS 'email_manager'
                                FROM employees AS t1
                                JOIN employees AS t2 ON t1.idmanager = t2.id
                                where t1.id = {key};""")
        rows = cursor.fetchall()
        for row in rows:
            id_employee = row[0]
            email = row[1]
            send_email(email, 'Employee hours worked', f"Employee with id {id_employee} didn't work 8 hours in {dt.today()}")
            return f'The email was sent to address {email}'