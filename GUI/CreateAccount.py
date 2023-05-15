from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QAction, QMessageBox
from PyQt5.QtGui import QFont
import datetime, random, string

class CreateAccWindow(QMainWindow):

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
		self.passwd_label = QLabel('Пароль')
		self.passwd_label.setFont(self.widget_font)
		self.passwd_lineedit = QLineEdit()
		self.passwd_lineedit.setFont(self.widget_font)
		self.recovery_code_label = QLabel('Код восстановления')
		self.recovery_code_label.setFont(self.widget_font)
		self.recovery_code_lineedit = QLineEdit()
		self.recovery_code_lineedit.setFont(self.widget_font)
		self.generate_code_button = QPushButton('Сгенерировать')
		self.generate_code_button.setFont(self.widget_font)
		self.generate_code_button.clicked.connect(self.generate_code)
		self.wrong_data_label = QLabel('')
		self.wrong_data_label.setFont(self.widget_font)
		self.register_button = QPushButton('Зарегистрироваться')
		self.register_button.setFont(self.widget_font)
		self.register_button.clicked.connect(self.register)

		self.acc_data_gridlayout.addWidget(self.username_label,0,0)
		self.acc_data_gridlayout.addWidget(self.username_lineedit,0,1,1,2)
		self.acc_data_gridlayout.addWidget(self.passwd_label,1,0)
		self.acc_data_gridlayout.addWidget(self.passwd_lineedit,1,1,1,2)
		self.acc_data_gridlayout.addWidget(self.recovery_code_label,2,0)
		self.acc_data_gridlayout.addWidget(self.recovery_code_lineedit,2,1)
		self.acc_data_gridlayout.addWidget(self.generate_code_button,2,2)
		self.acc_data_gridlayout.addWidget(self.wrong_data_label,3,1,1,2)
		self.acc_data_gridlayout.addWidget(self.register_button,4,0,1,3)

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

	def register(self):
		username = self.username_lineedit.text()
		passwd = self.passwd_lineedit.text()
		recovery_code = self.recovery_code_lineedit.text()
		id_user = self.db_requests.find_id_user_by_username_and_passwd(username,passwd)
		if id_user != None:
			self.wrong_data_label.setText('Аккаунт уже зарегистрирован')
			self.wrong_data_label.setStyleSheet('color: Red')
		else:
			if recovery_code != '':
				dt = datetime.datetime.now()
				class UserData:
					def __init__(self):
						self.username = username
						self.passwd = passwd
						self.recovery_code = recovery_code
						self.create_date = '%s-%s-%s'%(dt.strftime('%Y'),dt.strftime('%m'),dt.strftime('%d'))
				user = UserData()
				self.db_requests.add_user(user)
				dlg = QMessageBox(self)
				dlg.setWindowTitle('Успешно')
				dlg.setText('Аккаунт добавлен!')
				dlg.setIcon(QMessageBox.Information)
				dlg.setFont(self.widget_font)
				button = dlg.exec()
				self.close()
				self.back_window.show()
			else:
				self.wrong_data_label.setText('Не все данные заполнены')
				self.wrong_data_label.setStyleSheet('color: Red')

	def generate_code(self):
		characters = string.ascii_letters + string.digits + string.punctuation
		recovery_code = ''
		for i in range(8):
			recovery_code += random.choice(characters)
		self.recovery_code_lineedit.setText(recovery_code)
		self.wrong_data_label.setText('Скопируйте код восстановления')
		self.wrong_data_label.setStyleSheet('color: Black')

	def closeEvent(self,event):
		self.back_window.show()
