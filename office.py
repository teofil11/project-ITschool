import mysql.connector
from functions import functions as fc
from datetime import datetime as dt
import csv

PATH = 'Project/'
input_dir = PATH + 'Inputs/'

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



class Gate():
    def __init__(self,id_gate):
        self.id_gate = id_gate
    def access_in(self):
        pass
    def access_out(self):
        pass


class Gate_csv(Gate):
    def __init__(self,id_gate):
        super().__init__(id_gate)
    def access_in(self):
        now = dt.now()
        access_id = int(input('Enter the id: '))
        cursor.execute('select * from employees')
        rows = cursor.fetchall()
        for row in rows:
            if access_id == row[0]:
                print('Access granted')
                data = [access_id, now.strftime("%Y-%m-%d %H:%M:%S"), 'in']
                with open(input_dir+'Gate'+str(self.id_gate)+'('+str(now.strftime("%Y-%m-%d %H-%M-%S"))+')'+'.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(data)
                    break

        else:
            print('Access denied')
            print('Try again')
            Gate_csv(self.id_gate).acces_in()       
    
    def access_out(self):
        now = dt.now()
        access_id = int(input('Enter the id: '))
        cursor.execute('select * from employees')
        rows = cursor.fetchall()
        for row in rows:
            if access_id == row[0]:
                print('access granted')
                data = [access_id, now.strftime("%Y-%m-%d %H:%M:%S"), 'out']
                with open(input_dir+'Gate'+str(self.id_gate)+'('+str(now.strftime("%Y-%m-%d %H-%M-%S"))+')'+'.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(data)
                    break

        else:
            print('Access denied')
            print('Try again')
            Gate_csv(self.id_gate).acces_out()

class Gate_txt(Gate):
    def __init__(self,id_gate):
        super().__init__(id_gate)
    def access_in(self):
        now = dt.now()
        access_id = int(input('Enter the id: '))
        cursor.execute('select * from employees')
        rows = cursor.fetchall()
        for row in rows:
            if access_id == row[0]:
                print('Access granted')
                data = [str(f"{access_id},"),now.strftime("%Y-%m-%d %H:%M:%S"),',','in']
                with open(input_dir+'Gate'+str(self.id_gate)+'('+str(now.strftime("%Y-%m-%d %H-%M-%S"))+')'+'.txt', 'w') as file:
                    file.writelines(data)
                    break
        else:
            print('Access denied')
            print('Try again')
            Gate_txt(self.id_gate).access_in() 

    def access_out(self):
        now = dt.now()
        access_id = int(input('Enter the id: '))
        cursor.execute('select * from employees')
        rows = cursor.fetchall()
        for row in rows:
            if access_id == row[0]:
                print('Access granted')
                data = [str(f"{access_id},"),now.strftime("%Y-%m-%d %H:%M:%S"),',','out']
                with open(input_dir+'Gate'+str(self.id_gate)+'('+str(now.strftime("%Y-%m-%d %H-%M-%S"))+')'+'.txt', 'w') as file:
                    file.writelines(data)
                    break

        else:
            print('Access denied')
            print('Try again')
            Gate_txt(self.id_gate).access_out()

def menu():
    gate1 = Gate_csv(1)
    gate2 = Gate_csv(2)
    gate3 = Gate_txt(3)
    gate4 = Gate_txt(4)
    while True:
        print("""1.Registration
2.Access in
3.Access out""")
        x = int(input('Choice: '))
        if x == 1:
            Employee()
        if x == 2:
            y = int(input('Choice gate: '))
            if y == 1:
                gate1.access_in()
            if y == 2:
                gate2.access_in()
            if y == 3:
                gate3.access_in()
            if y == 4:
                gate4.access_in()
        if x ==3:
            y = int(input('Choice gate: '))
            if y == 1:
                gate1.access_out()
            if y == 2:
                gate2.access_out()
            if y == 3:
                gate3.access_out()
            if y == 4:
                gate4.access_out()

menu()

conn.close()
cursor.close()
