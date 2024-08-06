import os
folders = input("please provide folder names:").split()

for folder in folders:
    print (folder)

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("enter valid file name")
        continue
    for file in files:
        print(file)