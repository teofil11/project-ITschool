import mysql.connector
import os
from functions import functions as fc
from datetime import datetime as dt
import datetime as date
import csv
import time
import collections

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
                if fc.IsCsv(new_file) is True:
                    lines = []
                    with open(input_dir+new_file, 'r') as file:
                        reader = csv.reader(file)
                        for line in reader:
                            cleaned_row = [item.replace("T", " ").replace("Z", "") for item in line]
                            lines.append(cleaned_row)
                    for row in lines:    
                        if len(row) >= 3:
                            if row[0] == "IdPersoana":
                                continue
                            cursor.execute(f"insert into access values ('{row[0]}', '{row[2]}', '{row[1]}', '{new_file[6]}')")
                            conn.commit()
                if fc.IsTxt(new_file) is True:
                    with open(input_dir+new_file, 'r') as file:
                        text = (file.readlines())
                    for line in text:
                        new_line = line.rstrip(";\n ").replace('T', " ").replace('Z', '')
                        x = new_line.split(',')
                        if len(x) >= 3:
                            cursor.execute(f"insert into access values ('{x[0]}', '{x[2]}', '{x[1]}', '{new_file[6]}')")
                            conn.commit()
                # os.replace(input_dir+new_file, backup_dir+new_file)                    
        old_files = files
        # time.sleep(10)


main()

conn.close()
cursor.close()
