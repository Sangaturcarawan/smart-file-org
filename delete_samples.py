#!/usr/bin/env python3
from pathlib import Path
import shutil

TST_DIR = Path.home() / "Downloads" / "Test_Files"

def dl8_samples():
    if not TST_DIR.exists() and not TST_DIR.is_dir():
        print("No sample files or folders found")
        return
    confirm = input(f"Are you sure you want to delete ALL files in {TST_DIR}? [y/n]:").strip().lower()
    if confirm == "y":
        shutil.rmtree(TST_DIR)
        print(f"All sample files & folders deleted in {TST_DIR}")
    else:
        print(f"Deletion of {TST_DIR} cancelled")
        

if __name__ == "__main__":
    dl8_samples()