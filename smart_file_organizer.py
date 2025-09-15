import os
import shutil

def get_fil_pth(fol, fil_nam):
    return os.path.join(fol, fil_nam)

def mak_dir(fol_pth):
    if not os.path.exists(fol_pth):
        os.makedirs(fol_pth) # make folder if it does not exist
        print(f"{os.path.basename(fol_pth)} subfolder has been created.")

def mov_fil(fil_pth, dst_fol, fil_nam):
    mak_dir(dst_fol)
    new_fil_pth = get_fil_pth(dst_fol, fil_nam)
    shutil.move(fil_pth, new_fil_pth)
    print(f"Moved {fil_nam} to {os.path.basename(dst_fol)}")

# USER CONFIGURATION 
# to be expanded later by using CLI input
# SOURCE FOLDER
src_fol = os.path.join(os.path.expanduser("~"), "Downloads")
#  dynamically generates file path to Downloads folder
#  works cross-OS

# DESTINATION FOLDER
dst_fol = src_fol
# can be changed manually
# will allow CLI input later

# FILE CATEGORIES: add / remove extensions here
fil_cat = {
    "Audio": [".aac", ".flac", ".mp3", ".wav"],
    "Archives": [".gz", ".rar", ".zip"],
    "Documents": [".docx", ".pdf", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".avi", ".mkv", ".mov", ".mp4"]
}
# allow for user input in the future using CLI and or GUI
# allow for use of JSON file

# ORGANIZE FILES IN SOURCE FOLDER
for fil_nam in os.listdir(src_fol): # list out all items inside source folder
    fil_pth = get_fil_pth(src_fol, fil_nam) # generate file paths to each item

    if os.path.isdir(fil_pth): # filter out folders first
        continue

    fil_ext = os.path.splitext(fil_nam)[-1].lower() # get file extension

    # CHECK EXTENSION CATEGORY
    for cat, ext_lst in fil_cat.items():
        if fil_ext in ext_lst:
            cat_fol = get_fil_pth(dst_fol, cat) # make category subfolder
            mov_fil(fil_pth, cat_fol, fil_nam)
            break

    # IF NO CATEGORY FOUND, MOVE TO OTHERS FOLDER
    else:
        oth_fol = get_fil_pth(dst_fol, "Others")
        mov_fil(fil_pth, oth_fol, fil_nam)

print("Files organized successfully")