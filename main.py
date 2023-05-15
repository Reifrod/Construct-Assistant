from DBWork.DBRequests import DBreq
from GUI.Login import LoginWindow

from PyQt5.QtWidgets import QApplication
import sys

db_requests = DBreq()

app = QApplication(sys.argv)
login_window = LoginWindow(db_requests)
login_window.show()
app.exec()
