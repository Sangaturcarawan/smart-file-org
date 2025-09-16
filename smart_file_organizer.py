#!/usr/bin/env python3
# IMPORT MODULES
from pathlib import Path
import shutil
from typing import Dict, Iterable

# USER CONFIGURATION: future CLI input
SRC_FOL = Path.home() / "Downloads" # SOURCE FOLDER: dynamically detects Downloads file path, cross-OS
DST_FOL = SRC_FOL # DESTINATION FOLDER
OTH_CAT = "Others"

# FILE CATEGORIES: add / remove extensions here, future CLI, GUI, JSON
FIL_CAT: Dict[str, Iterable[str]] = {
    "Audio": [".aac", ".flac", ".mp3", ".wav"],
    "Archives": [".gz", ".rar", ".zip"],
    "Documents": [".docx", ".pdf", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".avi", ".mkv", ".mov", ".mp4"]
}

# HELPER FUNCTIONS
def mak_dir(path: Path) -> None: 
    """Makes a directory if it does not exist."""
    if not path.exists(): # Check that the file path not available in the system
        path.mkdir(parents=True, exist_ok=True) # Create folders including parent folders if they do not exist
        print(f"{path.name} subfolder created")

def _nam_col(dst: Path) -> Path: 
    """Generates a new file path if there is a naming conflict."""
    if not dst.exists():
        return dst # no conflict, name available so returns the original Path
    par = dst.parent # extract parent folder path
    stm = dst.stem # file name without extension
    ext = dst.suffix # file extension with '.'

    i = 1
    while True:
        pos_nam = par / f"{stm} ({i}){ext}" 
        # Create a new filename like "file (1).ext", etc.
        if not pos_nam.exists(): # Check whether file name is available
            return pos_nam # Return available new path
        i += 1 # Increments number, try again

def mov_fil(src: Path, dst: Path) -> None:
    """Move files from source folder to destination folder."""
    mak_dir(dst) # Make directory for destination file path
    fin_dst = _nam_col(dst / src.name) # Check that there is no naming conflict for file
    shutil.move(str(src), str(fin_dst)) #shutil.move requires str paths
    print(f"Moved {src.name:<30} \u2192 {fin_dst}")

def org_fil(src: Path, dst: Path, cats: Dict[str, Iterable[str]]) -> None:
    """Organize files in file system."""
    if not src.exists() or not src.is_dir(): # Check whether source folder exists & is a folder
        raise ValueError(f"{src} does not exist or is not a directory")

    for item in src.iterdir(): # Iterate through contents of source folder
        if item.is_dir():
            continue # Filter out directories
        if item.name.startswith('.'):
            continue # Filter out hidden files

        ext = item.suffix.lower()
        for cat, ext_lst in cats.items(): # CHECK EXTENSION CATEGORY
            if ext in ext_lst:
                mov_fil(item, dst / cat)
                break
        else: # IF NO CATEGORY FOUND, MOVE TO OTHERS FOLDER
            mov_fil(item, dst / OTH_CAT)

    print("Files organized successfully")

# ENTRY POINT
def main() -> None:
    """Isolates the running of the code so it is not run if imported."""
    org_fil(SRC_FOL, DST_FOL, FIL_CAT)

if __name__ == "__main__":
    main()