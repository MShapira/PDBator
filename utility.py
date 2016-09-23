import time
import os

# simple function converting numpy.bytes_ to human-readable string
def b2str(bytes):
    return str(bytes)[2:-1]


#Folder creation to store PDB files
def folder_creation(folder_path=None):
    foldername = str(time.ctime())

    if folder_path is None:
        newpath = "data/" + foldername
    else:
        newpath = folder_path + "/" + foldername

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    return newpath


# simple writing to file and generating folder
#Params: filename (string), extension (string), data(string)
def write_to_file(filename, extension, data, folder_path):
    file = open(folder_path + "/" + filename + "." + extension, "w")
    file.write(data)
    file.close()

    return file