#!/usr/bin/env python3

import os
import shutil
from time import strftime, localtime

bold = "\033[1m"
reset = "\033[0m"
red = "\033[91m"
os_name = os.uname()[0]
folder_dir = os.path.expanduser("~/Downloads/")
folder_contents = os.listdir(folder_dir)
home_dir = os.path.join(os.path.expanduser("~/"))

# Starting display
print(
    f"This will delete all downloads in {bold + red + os.uname()[1] + reset}")
print(f"OS: {os_name}")

# Get user confirmation
user_input = input("Continue (y/n)? ").lower()

deletion_mode = False
if user_input == 'y':
    deletion_mode = True
elif user_input == 'n':
    print("Best not to rush")

while deletion_mode:
    choice = int(input(
        "1. List files in the directory/folder\n2. Proceed to delete\n3.Exit\n"))

    if choice == 1:
        for file in folder_contents:
            path = f"{folder_dir}/{file}"
            metadata = strftime('%d-%m-%Y %H:%M:%S',
                                localtime(os.path.getctime(path)))
            print(
                f"Filename {bold + red +file + reset} | Last modification: {metadata}")
        continue

    elif choice == 2:
        if not os.path.exists(f"{home_dir}/tbd"):
            dummy_dir = "tbd"
            tbd = os.path.join(os.path.expanduser("~/"), dummy_dir)
            os.mkdir(tbd)
        else:
            print(folder_dir)
            tbd = f"{home_dir}tbd"
        for file in folder_contents:
            print(f"Deleted: {bold + red + file + reset}")
            shutil.move(f"{home_dir}/Downloads/{file}", tbd)
        shutil.rmtree(tbd)
        if not tbd:
            print("Operation successful")
            break
        else:
            print("Operation unsuccessful")
            break
    elif choice == 3:
        print("It's best we wait...")
        break
    else:
        print("invalid entry")
        break
    print(tbd)
    print(f"{folder_contents}")
