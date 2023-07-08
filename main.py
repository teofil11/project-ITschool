import os
from move_file import move_db,move_backup
from worked import calculate_hours_worked as calculate
import schedule
import threading
import time
import subprocess



input_dir = 'inputs/'
backup_dir = 'backup_inputs/'

def main():
    """
    Main function for file processing and scheduling.

    """
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
    """
    Start the office server using a subprocess.

    Raises:
        subprocess.CalledProcessError: If the subprocess fails to execute.
    """
    subprocess.run(["python", "office_server.py"], check=True)

t1 = threading.Thread(target=main)
t2 = threading.Thread(target=server)

t1.start()
t2.start()

t1.join()
t2.join()








