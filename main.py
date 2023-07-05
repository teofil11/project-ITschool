import os
from move_file import move_db,move_backup
from worked import calculate_hours_worked as calculate
import schedule



PATH = 'Project/'
input_dir = PATH + 'inputs/'
backup_dir = PATH + 'backup_inputs/'


def main():
    old_files = []
    schedule.every().day.at("19:04:00").do(calculate)
    while True:
        files = os.listdir(input_dir)
        if len(old_files) != len(files):
            for new_file in files:
                move_db(new_file)
                move_backup(new_file)                   
        old_files = files
        schedule.run_pending()

main()

