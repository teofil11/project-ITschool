import mysql.connector
import functions as fc

conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()


class Manager():
    def __init__(self):
        print('Your welcome! To register you must enter the following data:')
        self.fName = input('First name: ')
        self.lName = input('Last name: ')
        self.company = input('Company: ')


        cursor.execute(f"insert into managers values (null, '{fc.wUpper(self.fName)}', '{fc.wUpper(self.lName)}', '{fc.wUpper(self.company)}');")
        conn.commit()


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
            cursor.execute('select * from managers')
            rows = cursor.fetchall()
            for row in rows:
                if fc.wUpper(fNameMg) == row[1] and fc.wUpper(lNameMg) == row[2]:
                    if fc.wUpper(self.company) == row[3]:
                        idMg = row[0]
                    else:
                        print(f'The manager {fc.wUpper(fNameMg)} {fc.wUpper(lNameMg)} is not from the {fc.wUpper(self.company)} company')
                        Employee.registration(self)
            cursor.execute(f"insert into employees values (null, '{fc.wUpper(self.fName)}', '{fc.wUpper(self.lName)}', '{fc.wUpper(self.company)}', '{idMg}');")
            conn.commit()
        except UnboundLocalError:
            print(f'The manager {fc.wUpper(fNameMg)} {fc.wUpper(lNameMg)} not exist')
            print('Try again')
            Employee.registration(self)


conn.close()
cursor.close()


