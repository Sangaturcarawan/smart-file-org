#!/usr/bin/env python3
# IMPORT MODULES
from pathlib import Path
import shutil
from typing import Dict, Iterable

class FileOrg:
    def __init__(self, src:Path, dst:Path=None, cats:Dict[str, Iterable[str]]=None, oth:str="Others"):
        self.src = src
        self.dst = dst if dst else src
        self.cats = cats if cats else {
            "Audio": [".aac", ".flac", ".mp3", ".wav"],
            "Archives": [".gz", ".rar", ".zip"],
            "Documents": [".docx", ".pdf", ".txt", ".xlsx"],
            "Images": [".bmp",".gif",".jpeg",".jpg", ".png"],
            "Videos": [".avi", ".mkv", ".mov", ".mp4"]
            }
        self.oth = oth

    def org_fil(self) -> None:
        """Organize files in source folder by categorizing it."""
        if not self.src.exists() or not self.src.is_dir(): # Check whether source folder exists & is a folder
            raise ValueError(f"{self.src} does not exist or is not a directory")

        for item in self.src.iterdir(): # Iterate through contents of source folder
            if item.is_dir() or item.name.startswith("."):
                continue # Filter out directories and hidden files
            self._cat_fil(item)

        print("Files organized successfully")

    def _cat_fil(self, fil:Path) -> None:
        """Identify file category & move file."""
        fil_ext = fil.suffix.lower()
        for cat, exts in self.cats.items():
            if fil_ext in exts: # check file extension is extension list of all categories
                self._mov_fil(fil, self.dst / cat) # move file to new category folder
                return
        self._mov_fil(fil, self.dst / self.oth)
            
    def _mov_fil(self, src: Path, dst: Path) -> None:
        """Move files from source folder to destination folder."""
        self._mak_dir(dst) # Make directory for destination file path
        dst_fil_pth = self._nam_chk(dst / src.name) # Check that there is no naming conflict for file name in destination folder
        shutil.move(str(src), str(dst_fil_pth)) # shutil.move requires str paths
        print(f"Moved {src.name:<30} \u2192 {dst_fil_pth.name}")
        
    def _mak_dir(self, pth: Path) -> None: 
        """Makes a directory if it does not exist."""
        if not pth.exists(): # Check that the file path not available in the system
            pth.mkdir(parents=True, exist_ok=True) # Create folders including parent folders if they do not exist
            print(f"{pth.name} subfolder created")

    def _nam_chk(self, pth: Path) -> Path: 
        """Generates a new file path by appending (1), (2), etc. if there is a naming conflict."""
        if not pth.exists():
            return pth # no conflict, name available so returns the original Path
        par, stm, ext = pth.parent, pth.stem, pth.suffix # extract parent folder path, file name without extension, file extension with '.'

        i = 1
        while True:
            alt_nam = par / f"{stm} ({i}){ext}" # Create a alternate filename like "file (1).ext", etc.
            if not alt_nam.exists(): # Check whether file name is available (does not exist)
                return alt_nam # Return available new path
            i += 1 # Increment number, try again

# ENTRY POINT
def main() -> None:
    """Isolates the running of the code so it is not run if imported."""
    your_src = Path.home() / "Downloads" / "Test_Files"
    org = FileOrg(src=your_src)
    org.org_fil()

if __name__ == "__main__":
    main()