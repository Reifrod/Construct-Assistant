from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtGui import QFont

class WorkProjectWindow(QMainWindow):

	def __init__(self, db_requests, id_project):
		super().__init__()

		#Used data

		self.db_requests = db_requests
		self.id_project = id_project

		print(self.id_project)

		#Widget customization

		self.widget_font = QFont('Arial',16)

		#Window settings

		widget = QWidget()
		self.setCentralWidget(widget)
		self.setWindowTitle('Construct Assistant')
		self.setMinimumSize(1280,720)
		self.setMaximumSize(1280,720)
