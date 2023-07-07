import os
from move_file import move_db,move_backup
from worked import calculate_hours_worked as calculate
import schedule
import threading
import office_server
import time
import subprocess



PATH = 'Project/'
input_dir = PATH + 'inputs/'
backup_dir = PATH + 'backup_inputs/'


def main():
    old_files = []
    schedule.every().day.at("20:00").do(calculate)
    while True:
        files = os.listdir(input_dir)
        if len(old_files) != len(files):
            for new_file in files:
                move_db(new_file)
                move_backup(new_file)                   
        old_files = files
        schedule.run_pending()

def server():
    subprocess.run(["python", PATH+"office_server.py"], check=True)

t1 = threading.Thread(target=main)
t2 = threading.Thread(target=server)

t1.start()
t2.start()

t1.join()
t2.join()







