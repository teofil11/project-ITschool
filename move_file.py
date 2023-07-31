import mysql.connector
import files as f
from datetime import date as dt
from functions.typefile import isCsv,isTxt
from functions.formatfile import format_file
import os


input_dir = 'inputs/'
backup_dir = 'backup_inputs/'


conn = mysql.connector.connect(host='localhost',user='root', password='root',database = 'project')
cursor = conn.cursor()


def move_db(file_name)-> str:
    """
    Move the contents of a file to a database.

    Args:
        file_name (str): The name of the file to be processed.
    """
    qwery = "insert into access values"
    if isCsv(file_name) is True:
        file = f.File_csv(input_dir,file_name)
        content = file.read_file()
        f_content = format_file(file_name,content)
        for i,row in enumerate(f_content):
            if len(row) >= 3:
                if i != 0:
                    cursor.execute(f"{qwery} ('{row[0]}', '{row[2]}', '{row[1]}', '{file_name[6]}')")
                    conn.commit()

    if isTxt(file_name) is True:
        file = f.File_txt(input_dir,file_name)
        content = file.read_file()
        f_content = format_file(file_name,content)
        for i,rows in enumerate(f_content):
            row = rows.split(',')
            if len(row) >= 3:
                if i != 0:
                    cursor.execute(f"{qwery} ('{row[0]}', '{row[2]}', '{row[1]}', '{file_name[6]}')")
                    conn.commit()
    return f'The data from file {file_name} has been entered into the database successfully'

def move_backup(file_name) -> str:
    """
    Moves a file to the backup directory with a timestamp appended to its name.

    Args:
        file_name (str): The name of the file to be moved.

    Raises:
        FileExistsError: If a file with the same name already exists in the backup directory.

    """
    try:
        time_today = (dt.today())
        f_name = file_name.split('.')[0]
        ext_file = file_name.split('.')[1]
        new_file_name = f'{f_name}({time_today}).{ext_file}'
        os.rename(input_dir+file_name, backup_dir + new_file_name)
        return f'File {file_name} has been moved to the backup folder'
    except FileExistsError:        
        return 'This file already exists'
    
