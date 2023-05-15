from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QAction, QMessageBox
from PyQt5.QtGui import QFont
import datetime, random, string

class RememberPasswdWindow(QMainWindow):

	def __init__(self, db_requests, back_window):
		super().__init__()
		
		#Used data

		self.db_requests = db_requests
		self.back_window = back_window

		#Widget customization

		self.widget_font = QFont('Arial',16)

		#Window structure

		self.main_vboxlayout = QVBoxLayout()
		self.acc_data_gridlayout = QGridLayout()

		#Account Data

		self.username_label = QLabel('Логин')
		self.username_label.setFont(self.widget_font)
		self.username_lineedit = QLineEdit()
		self.username_lineedit.setFont(self.widget_font)
		self.recovery_code_label = QLabel('Код восстановления')
		self.recovery_code_label.setFont(self.widget_font)
		self.recovery_code_lineedit = QLineEdit()
		self.recovery_code_lineedit.setFont(self.widget_font)
		self.new_passwd_label = QLabel('Новый пароль')
		self.new_passwd_label.setFont(self.widget_font)
		self.new_passwd_lineedit = QLineEdit()
		self.new_passwd_lineedit.setFont(self.widget_font)
		self.wrong_data_label = QLabel('')
		self.wrong_data_label.setFont(self.widget_font)
		self.change_passwd_button = QPushButton('Сменить пароль')
		self.change_passwd_button.setFont(self.widget_font)
		self.change_passwd_button.clicked.connect(self.change_passwd)

		self.acc_data_gridlayout.addWidget(self.username_label,0,0)
		self.acc_data_gridlayout.addWidget(self.username_lineedit,0,1)
		self.acc_data_gridlayout.addWidget(self.recovery_code_label,1,0)
		self.acc_data_gridlayout.addWidget(self.recovery_code_lineedit,1,1)
		self.acc_data_gridlayout.addWidget(self.new_passwd_label,2,0)
		self.acc_data_gridlayout.addWidget(self.new_passwd_lineedit,2,1)
		self.acc_data_gridlayout.addWidget(self.wrong_data_label,3,1)
		self.acc_data_gridlayout.addWidget(self.change_passwd_button,4,0,1,3)

		self.main_vboxlayout.addLayout(self.acc_data_gridlayout)

		#Window settings

		widget = QWidget()
		widget.setLayout(self.main_vboxlayout)
		self.setCentralWidget(widget)
		self.setWindowTitle('Construct Assistant')
		self.setMinimumSize(540,200)
		self.setMaximumSize(540,200)

		close_action = QAction('Quit',self)
		close_action.triggered.connect(self.closeEvent)

	def change_passwd(self):
		username = self.username_lineedit.text()
		recovery_code = self.recovery_code_lineedit.text()
		passwd = self.new_passwd_lineedit.text()
		id_user = self.db_requests.find_id_user_by_username_and_recovery_code(username,recovery_code)
		if id_user == None:
			self.wrong_data_label.setText('Аккаунт не существует')
			self.wrong_data_label.setStyleSheet('color: Red')
		else:
			if passwd != '':
				self.db_requests.update_passwd_by_id_user(passwd,id_user)
				dlg = QMessageBox(self)
				dlg.setWindowTitle('Успешно')
				dlg.setText('Пароль изменён!')
				dlg.setIcon(QMessageBox.Information)
				dlg.setFont(self.widget_font)
				button = dlg.exec()
				self.close()
				self.back_window.show()
			else:
				self.wrong_data_label.setText('Не все данные заполнены')
				self.wrong_data_label.setStyleSheet('color: Red')

	def closeEvent(self,event):
		self.back_window.show()
