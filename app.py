import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, 
QPushButton, QFileDialog, QTabWidget)
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Excel-Downloader")
        self.setFixedSize(QSize(400,300))

        container = QWidget()
        main_layout = QVBoxLayout()

        self.title = QLabel("Download Excel Sheets In a Go")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(self.title)

        self.tabs = QTabWidget()
        self.welcome_tab  = QWidget()
        self.name_tab = QWidget()
        self.comment_tab = QWidget()

        self.tabs.addTab(self.welcome_tab, "Welcome Page")
        self.tabs.addTab(self.name_tab, "Name")
        self.tabs.addTab(self.comment_tab, "Comment")
        main_layout.addWidget(self.tabs)

        self.upload_button = QPushButton("Upload Excel")
        self.upload_button.clicked.connect(self.handle_file_upload)
        main_layout.addWidget(self.upload_button)
        
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def handle_file_upload(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Excel file",
            "",
            "Excel Files (*.xlsm *.xlsx)"
        )
        if file_path:
            print(f"File selected: {file_path}")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()