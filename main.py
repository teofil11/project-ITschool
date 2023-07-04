import os
import time
from move_file import move_db,move_backup
from worked import calculate_hours_worked as calculate
import schedule
import time

PATH = 'Project/'
input_dir = PATH + 'inputs/'
backup_dir = PATH + 'backup_inputs/'


def main():
    old_files = []
    while True:
        files = os.listdir(input_dir)
        if len(old_files) != len(files):
            for new_file in files:
                move_db(new_file)
                move_backup(new_file)                   
        old_files = files
        # time.sleep(10)
        schedule.every().day.at("23:07:20").do(calculate)
        time.sleep(1)
        schedule.run_pending()

main()

