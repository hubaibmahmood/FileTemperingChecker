import hashlib
import os
from datetime import datetime
import time


def hash_file(filename):


   h = hashlib.sha1()


   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':

           chunk = file.read(1024)
           h.update(chunk)


   return h.hexdigest()






def check_files(folder):
    files = {}

    while True:
        try:
            for filename in os.listdir(folder):
                message = hash_file(folder+filename)
                
                if filename in files:
                    if files[filename] != str(message):
                        f = open('files_logs.txt','a')
                        f.write(str(datetime.now())+" "+path+"/"+filename+" changed\n")
                        print(str(datetime.now())+" "+path+"/"+filename+" changed")
                        f.close()

                
                files[filename] = message
                
        except KeyboardInterrupt:
            print("\nClosing Script...............\n")
            time.sleep(1)
            break


    print(files)


def check_folders(path):
    files = {}

    while True:
        try:
            for folder in os.listdir(path):
                for filename in os.listdir(path+folder):
                    message = hash_file(path+folder+"/"+filename)
                    
                    if folder+"/"+filename in files:
                        if files[folder+"/"+filename] != str(message):
                            f = open('files_in_folders_logs.txt','a')                            
                            f.write(str(datetime.now())+" "+path+folder+"/"+filename+" changed")
                            print(str(datetime.now())+" "+path+folder+"/"+filename+" changed")
                            f.close()

                    
                    files[folder+"/"+filename] = message
                
        except KeyboardInterrupt:
            print("\nClosing Script...............\n")
            time.sleep(1)
            break


    print(files)


choice = input("1. Check files in a folder\n2. Check files in folders\nChoice: ")
if choice == '1':
    path = input("Enter the path of the files: ")
    folder = path+"/"
    check_files(folder)
elif choice == '2':
    path = input("Enter the path of the folders (Drive): ")
    folder = path+"/"
    check_folders(folder)
