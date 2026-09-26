import os
folder = input("Enter folder path: ")
list_files = os.listdir(folder)
for file in list_files:
    extension = os.path.splitext(file)[1]
    print(f'{file} >> {extension}')