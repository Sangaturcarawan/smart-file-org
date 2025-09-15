![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-2.0-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-lightgrey)
![Code Size](https://img.shields.io/github/languages/code-size/Sangaturcarawan/smart-file-org)
![Last Commit](https://img.shields.io/github/last-commit/Sangaturcarawan/smart-file-org)

# Smart File Organizer

A personal Python project that automatically organizes files in your **Downloads** folder into categorized subfolders using `os` and `shutil` modules. 

This is the **second iteration (v2.0)**. Future iterations will include `datetime` module for sorting by date, CLI input, and cross-OS support.

---

## Features
- Organizes files in your Downloads folder
  - Dynamically detects the Downloads folder
  - Moves unmatched files to **Others** subfolder
- Categorizes files into:
  - Future versions will auto-detect file type without much or any hardcoding

**Subfolder** | **File Extensions**
:---: | :---
**Audio** | - `.aac`<br> - `.flac`<br> - `.mp3`<br> - `.wav`
**Archives** | - `.zip`<br> - `.rar`<br> - `.gz`
**Documents** | - `.docx`<br> - `.pdf`<br> - `.txt`<br> - `.xlsx`
**Images** | - `.jpg`<br> - `.jpeg`<br> - `.png`<br> - `.gif`<br> - `.bmp`
**Videos** | - `.avi`<br> - `.mkv`<br> - `.mov`<br> - `.mp4`
  
- Modular code with helper functions:
  - `get_fil_pth()` &rarr; generates file path
  - `mak_dir()` &rarr; creates subfolders if they do not exist
  - `mov_fil()` &rarr; moves files to correct subfolder & prints an update

---

## Installation & Usage
1. Open a terminal (Linux/macOS) or Gitbash / WSL (Windows)
2. Clone the repo:
```bash
git clone https://github.com/Sangaturcarawan/smart-file-org.git
cd smart-file-org
```
3. Run the script:
```bash
python3 organizer.py
```
Future updates will allow you to use CLI input to customize your source & destination folders

# Updates / Version History
Please visit [CHANGELOG.md](CHANGELOG.md)

## License
This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.
