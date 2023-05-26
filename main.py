import mysql.connector
import os
import functions as fc
from datetime import datetime as dt
import csv
import time

PATH = 'Project/'

conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()

class Employee():
    def __init__(self):
        print('Your welcome! To register you must enter the following data:')
        self.fName = input('First name: ')
        self.lName = input('Last name: ')
        self.company = input('Company: ')
        def registration(self): 
            try:
                fNameMg = input("Enter the manager's first name: ")
                lNameMg = input('Enter the last name of the manager: ')
                cursor.execute('select * from employees')
                rows = cursor.fetchall()
                for row in rows:
                    if fc.wUpper(fNameMg) == row[1] and fc.wUpper(lNameMg) == row[2]:
                        if fc.wUpper(self.company) == row[3]:
                            idMg = row[0]      
                cursor.execute(f"insert into employees values (null, '{fc.wUpper(self.fName)}', '{fc.wUpper(self.lName)}', '{fc.wUpper(self.company)}', '{idMg}');")
                conn.commit()
                print('You have successfully registered')

            except UnboundLocalError:
                print(f'The manager {fc.wUpper(fNameMg)} {fc.wUpper(lNameMg)} is not from the {fc.wUpper(self.company)} company')
                print('Try again')
                registration(self)
        registration(self)



class Gate_csv():
    def __init__(self,id_gate):
        self.id_gate = id_gate
    def acces_in(self):
        now = dt.now()
        acces_id = int(input('Enter the id: '))
        cursor.execute('select * from employees')
        rows = cursor.fetchall()
        for row in rows:
            if acces_id == row[0]:
                print('Access granted')
                data = [acces_id, now.strftime("%Y-%m-%d %H:%M:%S"), 'in']
                with open(PATH+'Inputs/Gate'+str(self.id_gate)+'.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(data)
                    break

        else:
            print('Access denied')
            print('Try again')
            Gate_csv(self.id_gate).acces_in()       
    
    def acces_out(self):
        now = dt.now()
        acces_id = int(input('Enter the id: '))
        cursor.execute('select * from employees')
        rows = cursor.fetchall()
        for row in rows:
            if acces_id == row[0]:
                print('Access granted')
                data = [acces_id, now.strftime("%Y-%m-%d %H:%M:%S"), 'out']
                with open(PATH+'Inputs/Gate'+str(self.id_gate)+'.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(data)
                    break

        else:
            print('Access denied')
            print('Try again')
            Gate_csv(self.id_gate).acces_out()

def transfer_to_DB():
    old_files = []
    while True:
        files = os.listdir(PATH+'inputs')
        if len(old_files) != len(files):
            for new_file in files:
                if not new_file in old_files:
                    with open(PATH+'inputs/'+new_file, 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            cursor.execute(f"insert into access values ('{row[0]}', '{row[2]}', '{row[1]}', '{new_file[4]}')")
                            conn.commit()
        old_files = files
        time.sleep(5) 



def transfer_to_backup():
    head = ['IdPersoana', 'Data', 'Sens']
    input_dir = PATH + 'inputs/'
    backup_dir = PATH + 'backup_inputs/'
    
    while True:
        files = os.listdir(input_dir)
        for f in files:
            with open(input_dir + f, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                
            if f not in os.listdir(backup_dir):
                with open(backup_dir + f, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(head)
            else:
                with open(backup_dir + f, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                os.remove(os.path.join(input_dir,f))






conn.close()
cursor.close()

