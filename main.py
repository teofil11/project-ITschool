import os
import time
import move_file as move

PATH = 'Project/'
input_dir = PATH + 'inputs/'
backup_dir = PATH + 'backup_inputs/'


def main():
    old_files = []
    while True:
        files = os.listdir(input_dir)
        if len(old_files) != len(files):
            for new_file in files:
                move.move_db(new_file)
                # os.replace(input_dir+new_file, backup_dir+new_file)                    
        old_files = files
        # time.sleep(10)


main()

