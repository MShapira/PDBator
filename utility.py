import time
import os

# simple function converting numpy.bytes_ to human-readable string
def b2str(bytes):
    return str(bytes)[2:-1]


# Folder creation to store files
def folder_creation(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    return folder_name


# Creating path of new folder
def folder_path_generation():
    user_folder_name = input("Please, enter the folder name for storing files: ")
    folder_name = str(time.ctime()).replace(':', '-').replace(' ', '_')

    if user_folder_name == '':
        path = "data/" + folder_name
    else:
        path = user_folder_name + "/" + folder_name

    return path


# simple writing to file and generating folder
# Params: filename (string), extension (string), data(string)
def write_to_file(filename, extension, data, folder_path):
    file = open(folder_path + "/" + filename + "." + extension, "w")
    file.write(data)
    file.close()

    return file