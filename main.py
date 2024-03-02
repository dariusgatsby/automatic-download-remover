import os
import shutil
from time import strftime, localtime

bold = "\033[1m"
reset = "\033[0m"
red = "\033[91m"
os_name = os.uname()[0]
folder_dir = os.path.expanduser("~/downloads.bak/")
folder_contents = os.listdir(folder_dir)
#    shutil.rmtree("~/downloads.bak")

print(
    f"This will delete all downloads in {bold + red + os.uname()[1] + reset}")
print(f"OS: {os_name}")

user_input = input("Continue (y/n)? ").lower()
deletion_mode = False
if user_input == 'y':
    deletion_mode = True
elif user_input == 'n':
    print("Best not to rush")
while deletion_mode:
    choice = int(input(
        "1. List files in the directory/folder\n2. Proceed to delete\n"))
    if choice == 1:
        for file in folder_contents:
            path = f"{folder_dir}/{file}"
            metadata = strftime('%d-%m-%Y %H:%M:%S',
                                localtime(os.path.getctime(path)))
            print(f"Filename {file} | Last modification: {metadata}")
        continue
    elif choice == 2:
        dummy_dir = "tbd"
        tbd = os.path.join(os.path.expanduser("~/"), dummy_dir)
        os.mkdir(tbd)
        print(os.listdir(folder_dir))
        shutil.move(folder_dir, tbd)
        print(os.listdir(tbd))
        print(os.listdir(folder_dir))
        shutil.rmtree(tbd)
        if not tbd:
            print("Operation successful")
            break
        else:
            print("Operation unsuccessful")
        break
    else:
        print("Invalid entry")
