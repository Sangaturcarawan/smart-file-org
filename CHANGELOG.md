# Changelog

All notable changes to this project will be documented here.

---

## **[v2.0] – 2025-09-16**
### Added / Improved
- Dynamically detects the user's Downloads folder path using `os.path.expanduser("~")`.
- Added new file category:
  - **Audio**: `.aac`, `.flac`, `.mp3`, `.wav`
- Moves unmatched files to **Others** subfolder.
- Modularized code with helper functions:
  - `get_fil_pth()` → generates file paths
  - `mak_dir()` → creates subfolders if they do not exist
  - `mov_fil()` → moves files to the correct subfolder and prints a status message
- Improved maintainability for future extensions:
  - Ready for CLI input, JSON configuration, and cross-OS support.

### Future
- Sort files by creation/modification date using `datetime`.
- CLI input for source/destination folders.
- Auto-detect file type without hardcoding extensions.
- Add GUI option for non-CLI users.

---

## **[v1.0] – 2025-09-15**
### Added
- Minimal Python script (`organizer.py`) that organizes files in the Downloads folder into categorized subfolders using `os` and `shutil`.
- File categories:
  - **Archives**: `.zip`, `.rar`, `.gz`
  - **Documents**: `.docx`, `.pdf`, `.txt`, `.xlsx`
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
  - **Videos**: `.avi`, `.mkv`, `.mov`, `.mp4`
- Creates category folders automatically if they don’t exist.
- Requires manually specifying the Downloads folder path.

### Documentation / Repo Setup
- Added `README.md` with project overview, features, installation & usage instructions.
- Added `CHANGELOG.md` for version tracking.
- Added `LICENSE` file (MIT License).

### Future
- Auto-detect Downloads folder path.
- CLI input for source/destination folders.
- Sort files by creation/modification date using `datetime`.
- Cross-OS support (Windows, macOS, Linux).
