import os
import shutil

bold = "\033[1m"
reset = "\033[0m"
red = "\033[91m"
os_name = os.uname()[0]
folder_dir = os.path.expanduser("~/downloads.bak/")
folder_contents = os.listdir(folder_dir)

print(
    f"This will delete all downloads in {bold + red + os.uname()[1] + reset}")
print(f"OS: {os_name}")

user_input = input("are you sure (y/n)? ").lower()
if user_input == 'y' and os_name == 'Linux':
    shutil.rmtree("~/downloads.bak")
if user_input == 'n':
    print("Best not to rush")
