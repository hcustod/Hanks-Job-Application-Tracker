import sys
from PyQt5.QtWidgets import QApplication
from database_actions import setup_db
from main_window import JobTrackerApp

if __name__ == '__main__':
    setup_db()
    app = QApplication(sys.argv)
    window = JobTrackerApp()
    window.show()
    sys.exit(app.exec_())

