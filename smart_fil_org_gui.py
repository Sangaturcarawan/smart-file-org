from PyQt6.QtWidgets import(QApplication, QWidget, QMessageBox,
                            QVBoxLayout, QLabel, QPushButton, 
                            QFileDialog, QLineEdit)
from pathlib import Path
from smart_fil_org import FileOrg
import sys
import os

win_pth = Path()

class FileOrgGUI(QWidget): # inheritance
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
        self.src_lab = QLabel("Source Folder: ") # composition
        self.src_inp = QLineEdit(str(dwn_pth))
        self.src_btn = QPushButton("Browse")

        self.dst_lab = QLabel("Destination Folder: ")
        self.dst_inp = QLineEdit(str(dwn_pth))
        self.dst_btn = QPushButton("Browse")

        self.oth_lab = QLabel("Uncategorized Folder Name: ")
        self.oth_inp = QLineEdit("Others")

        self.org_btn = QPushButton("Organize Files")

        # Layout
        lay = QVBoxLayout() # local object

        lay.addWidget(self.src_lab)
        lay.addWidget(self.src_inp)
        lay.addWidget(self.src_btn)

        lay.addWidget(self.dst_lab)
        lay.addWidget(self.dst_inp)
        lay.addWidget(self.dst_btn)

        lay.addWidget(self.oth_lab)
        lay.addWidget(self.oth_inp)

        lay.addWidget(self.org_btn)


        self.setLayout(lay) # composition, previously association

        # Signals
        self.src_btn.clicked.connect(self.brw_src)
        self.dst_btn.clicked.connect(self.brw_dst)
        self.org_btn.clicked.connect(self.org_fil)

    def brw_src(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Source Folder", str(self.src_inp.text()))
        if folder:
            self.src_inp.setText(folder)

    def brw_dst(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Destination Folder", str(self.dst_inp.text()))
        if folder:
            self.dst_inp.setText(folder)

    def org_fil(self):
        src = Path(self.src_inp.text()).expanduser().resolve()
        dst = Path(self.dst_inp.text()).expanduser().resolve()
        oth = self.oth_inp.text().strip() or "Others"

        try:
            org = FileOrg(src=src, dst=dst, oth=oth) # dependency
            org.org_fil()
            QMessageBox.information(self, "Success", "Files organized successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FileOrgGUI()
    win.show()
    sys.exit(app.exec())