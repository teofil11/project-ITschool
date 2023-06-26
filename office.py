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



class File():
    def __init__(self,name,path):
        self.name = name
        self.path = path
    def read_file():
        pass
    def write_file():
        pass


class File_csv(File):
    def __init__(self,name,path):
        super().__init__(name,path)
    def read_file():
        pass
    def write_file():
        pass

class File_txt(File):
    def __init__(self,name,path):
        super().__init__(name,path)
    def read_file():
        pass
    def write_file():
        pass



conn.close()
cursor.close()
