# Changelog

All notable changes to this project will be documented here.

---
## [v5.0] – 2025-09-18
### Added / Improved
- Added **PyQt6 GUI** for selecting source and destination folders.
- Added input for specifying folder for uncategorized files.
- Fully cross-OS compatible, including Windows, macOS, Linux, and WSL.
- Integrated with `FileOrg` class (v4.0) for modular file organization.
- Prevents file name conflicts by auto-renaming duplicates.
- GUI signals properly connected to browsing and organizing functions.

### Future
- Add metadata-based sorting and file filtering using regex.
- GUI enhancements (drag-and-drop support).
- Optional web app with Flask or Django.
---
## **[v4.0] – 2025-09-18**
### Refactored / Improved
- Added **OOP structure** using `FileOrg` class.
- Added **CLI input** for user to specify:
  - Source folder (default = `~/Downloads`)
  - Destination folder (default = same as source)
  - Folder name for uncategorized files (default = `Others`)
- Improved **error handling**:
  - Checks if source/destination folder exists.
  - Option to create destination folder if it does not exist.
- Enhanced **cross-OS support** (Windows, macOS, Linux) via `pathlib`.
- Modular code with helper methods:
  - `_cat_fil()` → identifies file category
  - `_mov_fil()` → moves files and resolves naming conflicts
  - `_mak_dir()` → creates directories if they don’t exist
  - `_nam_chk()` → generates unique filenames to prevent overwrites
- Updated README and documentation to reflect CLI input and OOP changes.
- Added two helper Python scripts for testing:
  - create_samples.py → generates sample files for testing file organization.
  - delete_samples.py → deletes the generated sample files.

### Documentation
- Added **Mermaid UML diagram** to show architecture

### Future
- Handle multi-part file extensions (e.g., `.tar.gz`) correctly.
- Sort files by creation or modification date using `datetime`.
- Add GUI input to customize source/destination folders.
- Auto-detect file types without hardcoding extensions in dictionaries.
- Cross-OS enhancements and configuration via JSON.

---

## **[v3.0] – 2025-09-16**
### Refactored / Improved
- Refactored code to use `pathlib` for path manipulations instead of `os.path`.
- Added `typing` annotations for better readability and maintainability.
- Modularized code with improved helper functions:
  - `mak_dir()` → creates subfolders if they do not exist  
  - `mov_fil()` → moves files to the correct subfolder and prints a status message  
  - `_nam_col()` → handles naming conflicts by generating unique filenames  
  - `org_fil()` → orchestrates file organization by category
- Added **Others** category for unmatched files.
- Updated README and documentation to reflect the new structure and version.

### Documentation
- Added sample file tree diagrams for before and after running the code

### Future
- Handle multi-part file extensions (e.g., `.tar.gz`) correctly.
- Sort files by creation/modification date using `datetime`.
- Add optional GUI or CLI input to customize source/destination folders.
- Auto-detect file types without hardcoding extensions.
- Cross-OS enhancements and configuration via JSON.

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
