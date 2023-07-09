import mysql.connector
from functions.write import wUpper


conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()

class Employee():
    def __init__(self,fName,lName,company,idManager):
        self.fName = fName
        self.lName = lName
        self.company = company
        self.idManager = idManager

        def registration(self):
            """
            Register an employee in the database.

            """
            if self.idManager == 'CEO':
                cursor.execute(f"insert into employees values (null, '{wUpper(self.fName)}', '{wUpper(self.lName)}', '{wUpper(self.company)}', '{self.idManager}');")
                conn.commit()
                print('You have successfully registered')
            
            cursor.execute('select * from employees')
            rows = cursor.fetchall()
            if len(rows)==0:
                print(f'The manager with id {self.idManager} is not from the {wUpper(self.company)} company')
                print('Try again')
            for row in rows:
                if self.idManager == str(row[0]):
                    if wUpper(self.company) == row[3]:
                        cursor.execute(f"insert into employees values (null, '{wUpper(self.fName)}', '{wUpper(self.lName)}', '{wUpper(self.company)}', '{self.idManager}');")   
                        conn.commit()
                        print('You have successfully registered')
                else:
                    print(f'The manager with id {self.idManager} is not from the {wUpper(self.company)} company')
                    print('Try again')

        registration(self)