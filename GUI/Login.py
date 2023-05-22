from GUI.CreateAccount import CreateAccWindow
from GUI.RememberPasswd import RememberPasswdWindow
from GUI.Main import MainWindow

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QFont

class LoginWindow(QMainWindow):

	def __init__(self, db_requests):
		super().__init__()
		
		#Used data

		self.db_requests = db_requests

		#Widget customization

		self.widget_font = QFont('Arial',16)
		self.link_font = QFont('Arial',14)

		#Window structure

		self.main_vboxlayout = QVBoxLayout()
		self.acc_data_gridlayout = QGridLayout()
		self.acc_help_hboxlayout = QHBoxLayout()

		#Account Data

		self.username_label = QLabel('Логин')
		self.username_label.setFont(self.widget_font)
		self.username_lineedit = QLineEdit()
		self.username_lineedit.setFont(self.widget_font)
		self.passwd_label = QLabel('Пароль')
		self.passwd_label.setFont(self.widget_font)
		self.passwd_lineedit = QLineEdit()
		self.passwd_lineedit.setFont(self.widget_font)
		self.passwd_lineedit.setEchoMode(QLineEdit.Password)
		self.wrong_data_label = QLabel('')
		self.wrong_data_label.setFont(self.widget_font)
		self.sign_in_button = QPushButton('Войти')
		self.sign_in_button.setFont(self.widget_font)
		self.sign_in_button.clicked.connect(self.sign_in)

		self.acc_data_gridlayout.addWidget(self.username_label,0,0)
		self.acc_data_gridlayout.addWidget(self.username_lineedit,0,1)
		self.acc_data_gridlayout.addWidget(self.passwd_label,1,0)
		self.acc_data_gridlayout.addWidget(self.passwd_lineedit,1,1)
		self.acc_data_gridlayout.addWidget(self.wrong_data_label,2,1)
		self.acc_data_gridlayout.addWidget(self.sign_in_button,3,0,1,2)

		self.main_vboxlayout.addLayout(self.acc_data_gridlayout)

		#Help with account

		self.create_acc_pushbutton = QPushButton('Создать аккаунт')
		self.create_acc_pushbutton.setFont(self.link_font)
		self.create_acc_pushbutton.clicked.connect(self.create_acc)
		self.remember_passwd_pushbutton = QPushButton('Восстановить пароль')
		self.remember_passwd_pushbutton.setFont(self.link_font)
		self.remember_passwd_pushbutton.clicked.connect(self.remember_passwd)

		self.acc_help_hboxlayout.addWidget(self.create_acc_pushbutton)
		self.acc_help_hboxlayout.addWidget(self.remember_passwd_pushbutton)

		self.main_vboxlayout.addLayout(self.acc_help_hboxlayout)

		#Window settings

		widget = QWidget()
		widget.setLayout(self.main_vboxlayout)
		self.setCentralWidget(widget)
		self.setWindowTitle('Construct Assistant')
		self.setMinimumSize(500,200)
		self.setMaximumSize(500,200)

	def sign_in(self):
		username = self.username_lineedit.text()
		passwd = self.passwd_lineedit.text()
		id_user = self.db_requests.find_id_user_by_username_and_passwd(username,passwd)
		if username != '' and passwd != '':
			if id_user == None:
				self.wrong_data_label.setText('Неверные данные для входа')
				self.wrong_data_label.setStyleSheet('color: Red')
			else:
				self.close()
				self.main_window = MainWindow(self.db_requests, id_user)
				self.main_window.show()
		else:
			self.wrong_data_label.setText('Данные не заполнены')
			self.wrong_data_label.setStyleSheet('color: Red')

	def create_acc(self):
		self.wrong_data_label.setText('')
		self.close()
		self.create_acc_window = CreateAccWindow(self.db_requests, self)
		self.create_acc_window.show()

	def remember_passwd(self):
		self.wrong_data_label.setText('')
		self.close()
		self.remember_passwd_window = RememberPasswdWindow(self.db_requests, self)
		self.remember_passwd_window.show()
