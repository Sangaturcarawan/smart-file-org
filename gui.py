from PyQt6.QtWidgets import(QApplication, QWidget, QMessageBox,
                            QVBoxLayout, QLabel, QPushButton, 
                            QFileDialog, QLineEdit)
from pathlib import Path
from smart_file_organizer import FileOrg
import sys
import os

win_pth = Path()

class FileOrgGUI(QWidget):
    def __init__(self):
        super().__init__()
        
        # Window
        self.setWindowTitle("Smart File Organizer")
        self.setGeometry(300, 300, 1000, 500)

        if os.name == "nt": #windows
            dwn_pth = Path.home() / "Downloads"
        else:
            if "microsoft" in os.uname().release.lower():
                win_usr = os.getenv("USER") or os.getenv("USERNAME")
                dwn_pth = Path(f"/mnt/c/Users/{win_usr}/Downloads")
            else:
                dwn_pth = Path.home() / "Downloads"

        # Widgets
        self.src_lab = QLabel("Source Folder: ")
        self.src_inp = QLineEdit(str(dwn_pth))
        self.src_btn = QPushButton("Browse")


        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.src_lab)
        layout.addWidget(self.src_inp)
        layout.addWidget(self.src_btn)
        self.setLayout(layout)

        # Signals
        self.src_btn.clicked.connect(self.brw_src)
    
    def brw_src(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Source Folder", str(self.src_inp.text()))
        if folder:
            self.src_inp.setText(folder)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOrgGUI()
    window.show()
    sys.exit(app.exec())