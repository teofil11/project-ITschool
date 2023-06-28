import mysql.connector
from functions.write import wUpper


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
                    if wUpper(fNameMg) == row[1] and wUpper(lNameMg) == row[2]:
                        if wUpper(self.company) == row[3]:
                            idMg = row[0]      
                cursor.execute(f"insert into employees values (null, '{wUpper(self.fName)}', '{wUpper(self.lName)}', '{wUpper(self.company)}', '{idMg}');")
                conn.commit()
                print('You have successfully registered')

            except UnboundLocalError:
                print(f'The manager {wUpper(fNameMg)} {wUpper(lNameMg)} is not from the {wUpper(self.company)} company')
                print('Try again')
                registration(self)
        registration(self)

x = Employee()

conn.close()
cursor.close()
