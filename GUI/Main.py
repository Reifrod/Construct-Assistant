from GUI.AddProject import AddProjectWindow
from GUI.WorkProject import WorkProjectWindow

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QWidget, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

	def __init__(self, db_requests, id_user):
		super().__init__()
		
		#Used data

		self.db_requests = db_requests
		self.id_user = id_user
		self.id_project = -1

		#Widget customization

		self.widget_font = QFont('Arial',16)

		#Window structure

		self.main_hboxlayout = QHBoxLayout()
		self.project_changing_buttons_vboxlayout = QVBoxLayout()

		#Project table

		self.projects = self.db_requests.find_projects_by_id_user(id_user)
		self.projects_table = QTableWidget()
		self.projects_table.setFont(self.widget_font)
		self.projects_table.setRowCount(len(self.projects))
		self.projects_table.setColumnCount(2)
		self.projects_table.setHorizontalHeaderLabels(['Название проекта','Дата создания'])
		self.projects_table.verticalHeader().setVisible(False)
		for i in range(len(self.projects)):
			project_name = QTableWidgetItem(self.projects[i][1])
			project_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
			self.projects_table.setItem(i,0, project_name)
			project_date = QTableWidgetItem(f'{self.projects[i][2]:%Y-%m-%d}')
			project_date.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
			self.projects_table.setItem(i,1, project_date)
		self.projects_table.resizeColumnsToContents()
		self.projects_table.clicked.connect(self.find_id_project)

		self.main_hboxlayout.addWidget(self.projects_table)

		#Project Changing buttons

		self.add_project_pushbutton = QPushButton('Создать')
		self.add_project_pushbutton.setFont(self.widget_font)
		self.add_project_pushbutton.clicked.connect(self.add_project)
		self.open_project_pushbutton = QPushButton('Открыть')
		self.open_project_pushbutton.setFont(self.widget_font)
		self.open_project_pushbutton.clicked.connect(self.open_project)
		self.delete_project_pushbutton = QPushButton('Удалить')
		self.delete_project_pushbutton.setFont(self.widget_font)
		self.delete_project_pushbutton.clicked.connect(self.delete_project)

		self.project_changing_buttons_vboxlayout.addWidget(self.add_project_pushbutton)
		self.project_changing_buttons_vboxlayout.addWidget(self.open_project_pushbutton)
		self.project_changing_buttons_vboxlayout.addWidget(self.delete_project_pushbutton)

		self.main_hboxlayout.addLayout(self.project_changing_buttons_vboxlayout)

		#Window settings

		widget = QWidget()
		widget.setLayout(self.main_hboxlayout)
		self.setCentralWidget(widget)
		self.setWindowTitle('Construct Assistant')
		self.setMinimumSize(480,210)
		self.setMaximumSize(480,210)

	def find_id_project(self):
		index = self.projects_table.currentIndex()
		self.id_project = index.row()

	def add_project(self):
		self.close()
		self.add_project_window = AddProjectWindow(self.db_requests, self.id_user)
		self.add_project_window.show()

	def open_project(self):
		if self.id_project != -1:
			id_project = self.projects[self.id_project][0]
			self.close()
			self.work_project_window = WorkProjectWindow(self.db_requests, id_project)
			self.work_project_window.show()
		else:
			dlg = QMessageBox(self)
			dlg.setWindowTitle('Ошибка')
			dlg.setText('Не выбран проект!')
			dlg.setIcon(QMessageBox.Critical)
			dlg.setFont(self.widget_font)
			button = dlg.exec()

	def delete_project(self):
		if self.id_project != -1:
			id_project = self.projects[self.id_project][0]
			self.db_requests.delete_project(id_project)
			self.projects_table.removeRow(self.id_project)
			self.projects.remove(self.projects[self.id_project])
			self.id_project = -1
		else:
			dlg = QMessageBox(self)
			dlg.setWindowTitle('Ошибка')
			dlg.setText('Не выбран проект!')
			dlg.setIcon(QMessageBox.Critical)
			dlg.setFont(self.widget_font)
			button = dlg.exec()
