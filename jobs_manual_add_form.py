from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, pyqtSignal
from database_actions import add_job

class JobEntryForm(QDialog):

    def __init__(self, parent, load_jobs_callback):
        super().__init__(parent)
        self.setWindowTitle("Manual Job Entry Form")
        self.setGeometry(400, 400, 400, 400)
        self.load_jobs = load_jobs_callback

        layout = QVBoxLayout()

        #fields
        self.title_label = QLabel("Job Title: ")
        self.title_input = QLineEdit()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)

        self.company_label = QLabel("Company Name: ")
        self.company_input = QLineEdit()
        layout.addWidget(self.company_label)
        layout.addWidget(self.company_input)

        self.location_label = QLabel("Location: ")
        self.location_input = QLineEdit()
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_input)

        self.status_label = QLabel("Status: ")
        self.status_input = QComboBox()
        self.status_input.addItems(["Applied", "Interviewing", "Offer", "Rejected"])
        layout.addWidget(self.status_label)
        layout.addWidget(self.status_input)

        self.applied_date_label = QLabel("Applied Date:")
        self.applied_date_input = QDateEdit()
        self.applied_date_input.setDate(QDate.currentDate())
        layout.addWidget(self.applied_date_label)
        layout.addWidget(self.applied_date_input)

        self.notes_label = QLabel("Notes:")
        self.notes_input = QTextEdit()
        layout.addWidget(self.notes_label)
        layout.addWidget(self.notes_input)

        # Buttons
        button_layout = QHBoxLayout()

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)
        button_layout.addWidget(self.back_button)

        self.done_button = QPushButton("Done")
        self.done_button.clicked.connect(self.save_job)
        button_layout.addWidget(self.done_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def go_back(self):
        self.close()
        self.parent().show()

    def save_job(self):
        job_title = self.title_input.text().strip()
        company = self.company_input.text().strip()
        location = self.location_input.text().strip()
        status = self.status_input.currentText()
        applied_date = self.applied_date_input.date().toString("yyyy-MM-dd")
        notes = self.notes_input.toPlainText().strip()

        if not job_title or not company:
            QMessageBox.warning(self, "Missing Information", "Job Title and Company are required.")
            return

        add_job(job_title, company, location, status, applied_date, notes)
        self.load_jobs()
        self.close()


