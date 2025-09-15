# Smart File Organizer

A personal Python project that automatically organizes files in your **Downloads** folder into categorized subfolders using `os` and `shutil` modules. 

This is the **first MVP (minimum viable product)**. Future iterations will include `datetime` module for sorting by date, CLI input, and cross-OS support.

---

## Features
- Organizes files in your Downloads folder
  - Currently requires specifying the Downloads folder path manually
  - Future versions will auto-detect Downloads folder path
- Categorizes files into:
  - Future versions will auto-detect file type without much or any hardcoding

**Subfolder** | **File Extensions**
:---: | :---
**Archives** | - `.zip`<br> - `.rar`<br> - `.gz`<br>
**Documents** | - `.docx`<br> - `.pdf`<br> - `.txt`<br> - `.xlsx`<br>
**Images** | - `.jpg`<br> - `.jpeg`<br> - `.png`<br> - `.gif`<br> - `.bmp`<br>
**Videos** | - `.avi`<br> - `.mkv`<br> - `.mov`<br> - `.mp4`<br>
  
- Creates category folders automatically if they do not exist

---

## Installation & Usage

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/smart-file-org.git
cd smart-file-org
```
2. Open the Python file `organizer.py` and update the `src_fol` variable with your Downloads folder path.

```python
# Set your Downloads folder path
src_fol = r"C:\Users\YOUR_USERNAME\Downloads"
```

3. Run the script:
```bash
python3 organizer.py
```
Files in your Downloads folder will be moved to the appropriate category subfolder

# Updates / Version History
Please visit [CHANGELOG.md](CHANGELOG.md)

## License
This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.
