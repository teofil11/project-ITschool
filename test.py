

import mysql.connector
import os
import functions as fc

PATH = 'Project/'

conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()

class Office():
    def registration(self):
        pass
    def acces_in(self):
        acces_id = int(input('Enter the id: '))

class Manager(Office):
    def __init__(self):
        print('Your welcome! To register you must enter the following data:')
        self.fName = input('First name: ')
        self.lName = input('Last name: ')
        self.company = input('Company: ')

    def registration():
        cursor.execute(f"insert into managers values (null, '{fc.wUpper(self.fName)}', '{fc.wUpper(self.lName)}', '{fc.wUpper(self.company)}');")
        conn.commit()
    def acces_in(self):
        super().acces_in()
        cursor.execute('select * from managers')
        rows = cursor.fetchall()
        for row in rows:
            if acces_id == row[0]:
                print('Access granted')
                break
        else:
            print('Access denied')
            print('Try again')
            Gate_csv(self.id_gate).acces_in(x)



class Employee(Office):
    def __init__(self):
        print('Your welcome! To register you must enter the following data:')
        self.fName = input('First name: ')
        self.lName = input('Last name: ')
        self.company = input('Company: ')
        
    
    def registration(self):
        try:
            fNameMg = input("Enter the manager's first name: ")
            lNameMg = input('Enter the last name of the manager: ')
            cursor.execute('select * from managers')
            rows = cursor.fetchall()
            for row in rows:
                if fc.wUpper(fNameMg) == row[1] and fc.wUpper(lNameMg) == row[2]:
                    if fc.wUpper(self.company) == row[3]:
                        idMg = row[0]      
            cursor.execute(f"insert into employees values (null, '{fc.wUpper(self.fName)}', '{fc.wUpper(self.lName)}', '{fc.wUpper(self.company)}', '{idMg}');")
            conn.commit()

        except UnboundLocalError:
            print(f'The manager {fc.wUpper(fNameMg)} {fc.wUpper(lNameMg)} is not from the {fc.wUpper(self.company)} company')
            print('Try again')
            Employee.registration(self)
    
    def acces_in(self):
        super().acces_in()
        cursor.execute('select * from employees')
        rows = cursor.fetchall()
        for row in rows:
            if acces_id == row[0]:
                print('Access granted')
                break
        else:
            print('Access denied')
            print('Try again')



class Gate_csv():
    def __init__(self,id_gate):
        self.id_gate = id_gate
    def acces_in(self,x):
        acces_id = int(input('Enter the id: '))
        if x == Manager:
            cursor.execute('select * from managers')
            rows = cursor.fetchall()
            for row in rows:
                if acces_id == row[0]:
                    print('Access granted')
                    break
            else:
                print('Access denied')
                print('Try again')
                Gate_csv(self.id_gate).acces_in(x)
        if x == Employee:
            cursor.execute('select * from employees')
            rows = cursor.fetchall()
            for row in rows:
                if acces_id == row[0]:
                    print('Access granted')
                    break
            else:
                print('Access denied')
                print('Try again')


gate = Gate_csv(1)
gate.acces_in(Manager)


conn.close()
cursor.close()
