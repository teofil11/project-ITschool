import mysql.connector
from functions import functions as fc
import files as f
from datetime import datetime as dt


PATH = 'Project/'
input_dir = PATH + 'inputs/'
backup_dir = PATH + 'backup_inputs/'

conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()

def move_db(file_name):
    qwery = "insert into access values"
    if fc.IsCsv(file_name) is True:
        file = f.File_csv(input_dir,file_name)
        content = file.read_file()
        f_content = fc.format_file(file_name,content)
        for row in f_content:
            if len(row) >= 3:
                if row[0] == "IdPersoana":
                    continue
                cursor.execute(f"{qwery} ('{row[0]}', '{row[2]}', '{row[1]}', '{file_name[6]}')")
                conn.commit()

    if fc.IsTxt(file_name) is True:
        file = f.File_txt(input_dir,file_name)
        content = file.read_file()
        f_content = fc.format_file(file_name,content)
        for rows in f_content:
            row = rows.split(',')
            if len(row) >= 3:
                cursor.execute(f"{qwery} ('{row[0]}', '{row[2]}', '{row[1]}', '{file_name[6]}')")
                conn.commit()


# def move_backup(file_name):
x = dt.today()
print(x)