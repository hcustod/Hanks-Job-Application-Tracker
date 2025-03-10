from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton
from jobs_manual_add_form import JobEntryForm


class JobAdditionOptionsDialog(QDialog):
    def __init__(self, parent, load_jobs_callback):
        super().__init__(parent)
        self.setWindowTitle("Add Job Application")
        self.setGeometry(300, 300, 300, 200)
        self.load_jobs = load_jobs_callback


        layout = QVBoxLayout()

        self.manual_entry_button = QPushButton("Manual Entry")
        self.manual_entry_button.clicked.connect(self.open_manual_entry)
        layout.addWidget(self.manual_entry_button)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def open_manual_entry(self):
        self.manual_entry = JobEntryForm(self, self.load_jobs)
        self.manual_entry.show()
        self.close()

