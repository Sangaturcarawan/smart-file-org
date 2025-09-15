# Changelog

All notable changes to this project will be documented here.

---

## [v1.0] – 2025-09-15
### Added
- Minimal Python script (`organizer.py`) that organizes files in the Downloads folder into categorized subfolders using `os` and `shutil`.
- Categories: Archives (`.zip`, `.rar`, `.gz`), Documents (`.docx`, `.pdf`, `.txt`, `.xlsx`), Images (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`), Videos (`.avi`, `.mkv`, `.mov`, `.mp4`).
- Creates category folders automatically if they do not exist yet.
- Requires manually specifying the Downloads folder path.

### Future
- Auto-detect Downloads folder path.
- CLI input for source/destination folders.
- Sort files by creation/modification date using `datetime`.
- Cross-OS support (Windows, macOS, Linux).
