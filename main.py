import mysql.connector
import os
from datetime import datetime as dt
import datetime as date
import time
import collections
import move_file as move

PATH = 'Project/'
input_dir = PATH + 'inputs/'
backup_dir = PATH + 'backup_inputs/'

conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()

def calculate_hours_worked():
    hours = []
    current_time = dt.now().time()
    weekday = dt.now().isoweekday()
    if weekday < 6 and current_time > date.time(20,0):
        cursor .execute("select * from access where direction = 'in'")
        rows = cursor.fetchall()  
        a = []
        for row in rows:
            date_today = row[2].date()
            if date_today == dt.now().date():
                entry = row[2]
                cursor .execute("select * from access where direction = 'out'")
                x = cursor.fetchall() 
                for y in x:
                    if y[0] == row[0]:
                        out = y[2]
                        if entry not in a and out not in a:
                            q = out - entry
                            a.append(entry)
                            a.append(out)
                            h = {y[0]:q.seconds//3600}
                            hours.append(h)
                                     
        counter = collections.Counter()
        for t in hours:
            counter.update(t)
        total_hours = dict(counter)
        print(total_hours)
        for key,value in total_hours.items():
            if value < 8:
                print(f'Employee with ID {key} did not work 8 hours on {date_today}')

def main():
    old_files = []
    while True:
        files = os.listdir(input_dir)
        if len(old_files) != len(files):
            for new_file in files:
                move.move_db(new_file)
                # os.replace(input_dir+new_file, backup_dir+new_file)                    
        old_files = files
        # time.sleep(10)


main()

conn.close()
cursor.close()
