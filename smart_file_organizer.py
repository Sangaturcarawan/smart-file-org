# IMPORT OF MODULES
import os
import shutil

# USER CONFIGURATION 
    # to be expanded later by using CLI input

    # SOURCE FOLDER
src_fol = r"C:\Users\marce\Downloads"
    # need to change this to your own user name
    # will update to allow user input to change it
    # maybe can autodetect when user runs the code itself

    # DESTINATION FOLDER
dst_fol = src_fol
    # can be changed manually
    # will allow CLI input later

# FILE CATEGORIES
fil_cat = {
    "Archives": [".gz", ".rar", ".zip"],
    "Documents": [".docx", ".pdf", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".avi", ".mkv", ".mov", ".mp4"]
}
    # will add on to this dictionary later
    # maybe can find a way to automate this section so that it autodetects without a dictionary or list

# ORGANIZE FILES IN SOURCE FOLDER
for fil_nam in os.listdir(src_fol):
    fil_pth = os.path.join(src_fol, fil_nam)

    # SKIP DIRECTORIES
    if os.path.isdir(fil_pth):
        continue

    # GET FILE EXTENSION
    fil_ext = os.path.splitext(fil_nam)[-1].lower()

    # CHECK EXTENSION CATEGORY
    for cat, ext in fil_cat.items():
        if fil_ext in ext:

            # MAKE CATEGORY FOLDER IF NOT EXISTENT
            cat_fol = os.path.join(dst_fol, cat)
            os.makedirs(cat_fol, exist_ok=True)

            # MOVE FILE TO CATEGORY FOLDER
            shutil.move(fil_pth, os.path.join(cat_fol, fil_nam))
                # handle files that do not match those files, to do later
            break

print("Files organized successfully")






