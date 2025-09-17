#!/usr/bin/env python3

from pathlib import Path

TST_DIR = Path.home() / "Downloads" / "Test_Files"
CATS = {
    "Audio": [".aac", ".flac", ".mp3", ".wav"],
    "Archives": [".gz", ".rar", ".zip"],
    "Documents": [".docx", ".pdf", ".txt", ".xlsx"],
    "Images": [".bmp",".gif",".jpeg",".jpg", ".png"],
    "Videos": [".avi", ".mkv", ".mov", ".mp4"]
}

def _nam_chk(pth: Path) -> Path:
    """Creates a new file path by appending (1), (2), etc. if there is a duplicate file / naming conflict"""
    if not pth.exists():
        return pth
    
    par, stm, ext = pth.parent, pth.stem, pth.suffix
    i = 1
    while True:
        alt_nam = par / f"{stm} ({i}){ext}"
        if not alt_nam.exists():
            return alt_nam
        i += 1

def cr8_fil():
    TST_DIR.mkdir(parents=True, exist_ok=True)
    for cat, exts in CATS.items():
        for ext in exts:
            fil_pth = TST_DIR / f"{cat}_sample{ext}"
            fil_pth = _nam_chk(fil_pth)
            fil_pth.write_text(f"This is a sample text for {cat} file: {fil_pth.name}")
            print(f"Created {fil_pth}")

if __name__ == "__main__":
    cr8_fil()
    print(f"\nAll sample files created in {TST_DIR}")