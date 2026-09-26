import os
folder = input("Enter folder path: ")
list_files = os.listdir(folder)
for file in list_files:
    print(file)