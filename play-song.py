import os
from playsound import playsound

dir_open = ""
dir_folder = ""

while True:
    try:
        directory = input(">>> ")
        if directory.find(".mp3") == -1:
            dir_open = directory + "\\"
            dir_folder += dir_open
            print(dir_folder)
            print(os.listdir(dir_folder))
        else:
            dir_folder += "\\" + directory
            print(dir_open)
            playsound(dir_folder)
            break

    except FileNotFoundError:
        print("File Not Found! Please Try Again.")
        break
