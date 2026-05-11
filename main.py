#project - CRUD Operation 
import os
from pathlib import Path
def readfileandfolder():
    try:
        p = Path('')
        items = list(p.rglob('*'))
        for index , file in enumerate(items):
            print(f'{index+1} - {file}')
    except Exception as e:
        print(e)


def create_file():
    try:
        readfileandfolder()
        #D:\FILE HANDING\main.py
        file_name = input('entre name of the file: ')
        p = Path(file_name)
        if p.exists():
            print('FILE ALREADY EXISTS')
        else:
            with open(file_name , 'w') as file:
                content = input('entre your file content: ')
                file.write(content)
                print('FILE ADDED!')
    except Exception as e:
        print(e)

def read_file():
    try:
        readfileandfolder()
        file_name = input('Entre name of your file: ')
        p = Path(file_name)
        if p.exists():
            with open(file_name , 'r') as file:
                print(file.read())
        else:
            print('FILE NOT FOUND')
    except Exception as e:
        print(e)
#--
def update_file():
    try:
        readfileandfolder()
        file_name = input('Entre name of your file: ')
        p = Path(file_name)
        
        if p.exists():
            print('Press 1 to overwrite the content')
            print('Press 2 to append new content')

            option = int(input('entre your choice for updating file: '))
            if option == 1:
                with open(file_name, 'w') as file:
                    content = input('Entre your content')
                    file.write(content)
                    print('CONTENT CHANGED....')

            elif option == 2:
                with open(file_name, 'a') as file:
                    content = input('Entre your content')
                    file.write(content)
                    print('CONTENT CHANGED....')

            else:
                print("INVALID INPUT")
        else:
            print("FILE DOESN'T EXISTS!")
    
    except Exception as e:
        print(e)


def delete_file():
    readfileandfolder()
    file_name = input('Entre name of your file: ')
    p = Path(file_name)
    if p.exists():
        os.remove(p) #oS is removing path of that file completely from the system
        print("FILE DELETED")
    else:
        print('FILE DOES NOT EXISTS!!')

def rename_file():
    readfileandfolder()
    file_name = input('Entre name of your file:')
    p = Path(file_name)
    if p.exists():
        new_file = input('Entre new name of your file: ')
        p.rename(new_file)
        print('FILE RENAMED!')
    else:
        print('FILE NOT FOUND')

def create_folder():
    readfileandfolder()
    folder_name = input("Entre name of your folderr: ")
    p = Path(folder_name)
    if p.exists():
        print('FOLDER ALREADY EXISTS!')
    else:
        p.mkdir()
        print('FOLDER CREATED !')

def delete_folder():
    readfileandfolder()
    folder_name = input("Entre name of your folderr: ")
    p = Path(folder_name)
    if p.exists():
        p.rmdir()
        print('FOLDER DELETED!')
    else:
        print('FOLDER NOT FOUND !')


while True:
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")
    print("Press 5 for renaming a file")
    print("Press 6 for creating a folder")
    print("Press 7 for delete a folder")
    print("Press 0 for existing...")

    option = int(input("Entre your choice"))
    if option == 1:
        create_file()

    if option ==2:
        read_file()

    if option == 3:
        update_file()

    if option == 4:
        delete_file()

    if option == 5:
        rename_file()
  
    if option == 6:
        create_folder()

    if option == 7:
        delete_folder()

    if option == 0:
        break
