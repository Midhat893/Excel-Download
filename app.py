import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, 
QPushButton, QFileDialog)
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Excel-Downloader")
        self.setFixedSize(QSize(400,300))
        self.set_excel_uploader()

    def set_excel_uploader(self):
        layout = QVBoxLayout()
        title = QLabel("Download Excel Sheets In a Go")
        layout.addWidget(title)

        button = QPushButton("Upload Excel")
        button.clicked.connect(self.handle_file_upload)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
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