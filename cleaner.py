import glob
import os
# import glob, os


def clean_image():
    try:
        for f in glob.glob("static/*.jpg"):
            os.remove(f)
        print('Files Deleted')
    except:
        print('Error deleting files.')
# def clean_image():
#     try:
#         print('In cleaner')
#         path = '/static/'
#         os.remove(path + "**.jpg")
#         print("File Removed!")
#     except:
#         print("File not present")


# def clean_image():
#     # get a recursive list of file paths that matches pattern including sub directories
#     fileList = glob.glob('/static/*.jpg', recursive=True)

#     # Iterate over the list of filepaths & remove each file.
#     for filePath in fileList:
#         try:
#             os.remove(filePath)
#         except OSError:
#             print("Error while deleting file")
