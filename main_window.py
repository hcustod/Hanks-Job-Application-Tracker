from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem
from database_actions import get_jobs, delete_job
from job_addition_options import JobAdditionOptionsDialog
from functools import partial


class JobTrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_jobs()

    def initUI(self):
        self.setWindowTitle("Job Tracker")
        self.setGeometry(200, 200, 900, 500)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Job Title", "Company", "Location", "Status", "Date Applied", "Actions"])
        layout.addWidget(self.table)

        self.add_job_button = QPushButton("Add New Job")
        self.add_job_button.clicked.connect(self.open_job_options)
        layout.addWidget(self.add_job_button)

        self.setLayout(layout)

    def load_jobs(self):
        jobs = get_jobs()
        self.table.setRowCount(len(jobs))

        for row, job in enumerate(jobs):
            job_id = job[0]
            for col, data in enumerate(job[1:]):
                self.table.setItem(row, col, QTableWidgetItem(str(data)))

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(partial(self.remove_job, job_id))
            self.table.setCellWidget(row, 5, delete_button)

    def remove_job(self, job_id):
        delete_job(job_id)
        self.load_jobs()

    def open_job_options(self):
        # We cant to pass the function reference load_jobs not call it.
        self.job_options = JobAdditionOptionsDialog(self, self.load_jobs)
        self.job_options.show()

    # TODO;
    def edit_job(self, job_id):
        edit_job(job_id)
        self.load_jobs()




