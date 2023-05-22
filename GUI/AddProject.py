from GUI.WorkProject import WorkProjectWindow

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, QLineEdit, QComboBox, QPushButton, QWidget
from PyQt5.QtGui import QFont
import datetime

class AddProjectWindow(QMainWindow):

	def __init__(self, db_requests, id_user):
		super().__init__()
		
		#Used data

		self.db_requests = db_requests
		self.id_user = id_user
		regions = self.db_requests.find_id_and_name_regions()

		#Widget customization

		self.widget_font = QFont('Arial',16)

		#Window structure

		self.main_gridlayout = QGridLayout()

		#Project data

		self.project_name_label = QLabel('Название проекта')
		self.project_name_label.setFont(self.widget_font)
		self.project_name_lineedit = QLineEdit()
		self.project_name_lineedit.setFont(self.widget_font)
		self.region_label = QLabel('Регион')
		self.region_label.setFont(self.widget_font)
		self.region_combobox = QComboBox()
		self.region_combobox.setFont(self.widget_font)
		self.region_combobox.clear()
		self.region_combobox.addItem('')
		for i in range(len(regions)):
			self.region_combobox.addItem(regions[i][1])
		self.wrong_data_label = QLabel('')
		self.wrong_data_label.setFont(self.widget_font)
		self.create_project_pushbutton = QPushButton('Создать')
		self.create_project_pushbutton.setFont(self.widget_font)
		self.create_project_pushbutton.clicked.connect(self.add_project)

		self.main_gridlayout.addWidget(self.project_name_label,0,0)
		self.main_gridlayout.addWidget(self.project_name_lineedit,0,1)
		self.main_gridlayout.addWidget(self.region_label,1,0)
		self.main_gridlayout.addWidget(self.region_combobox,1,1)
		self.main_gridlayout.addWidget(self.wrong_data_label,2,1)
		self.main_gridlayout.addWidget(self.create_project_pushbutton,3,0,1,2)

		#Window settings

		widget = QWidget()
		widget.setLayout(self.main_gridlayout)
		self.setCentralWidget(widget)
		self.setWindowTitle('Construct Assistant')
		self.setMinimumSize(420,160)
		self.setMaximumSize(420,160)

	def add_project(self):
		project_name = self.project_name_lineedit.text()
		region = self.region_combobox.currentText()
		id_user = self.id_user
		if project_name != '' and region != '':
			dt = datetime.datetime.now()
			id_region = self.region_combobox.currentIndex()
			class ProjectData:
				def __init__(self):
					self.user_id = id_user
					self.name = project_name
					self.region_id = id_region
					self.create_date = '%s-%s-%s'%(dt.strftime('%Y'),dt.strftime('%m'),dt.strftime('%d'))
			project = ProjectData()
			self.db_requests.add_project(project)
			id_project = self.db_requests.find_last_id_project()
			self.close()
			self.work_project_window = WorkProjectWindow(self.db_requests, id_project)
			self.work_project_window.show()
		else:
			self.wrong_data_label.setText('Данные не заполнены')
			self.wrong_data_label.setStyleSheet('color: Red')
