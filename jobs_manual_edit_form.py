class JobEditForm():
    def __init__(self, parent, job):
        super().__init__(parent)
        self.setWindowTitle("Manual Job Entry Form")
        self.setGeometry(400, 400, 400, 400)
        self.job = job

        layout = QVBoxLayout()

        # fields
        self.title_label = QLabel("Job Title: ")
        self.title_input = QLineEdit()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)


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
