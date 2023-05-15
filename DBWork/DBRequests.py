from .DBAccess import DBac

class DBreq:

	def __init__(self):
		db = DBac()
		self.conn,self.cursor = DBac.get_cursor_and_connection(self)

	#Authorization module

	def add_user(self, user):
		self.cursor.execute('INSERT INTO user_identity (username, passwd, recovery_code, create_date) VALUES (%s, %s, %s, %s);',
							(user.username,user.passwd,user.recovery_code,user.create_date))
		self.conn.commit()

	def find_id_user_by_username_and_passwd(self, username, passwd):
		self.cursor.execute('SELECT id FROM user_identity WHERE username = %s AND passwd = %s;',
							(username,passwd))
		id_user = self.cursor.fetchone()
		return id_user

	def find_id_user_by_username_and_recovery_code(self, username, recovery_code):
		self.cursor.execute('SELECT id FROM user_identity WHERE username = %s AND recovery_code = %s;',
							(username,recovery_code))
		id_user = self.cursor.fetchone()
		return id_user

	def update_passwd_by_id_user(self, passwd, id_user):
		self.cursor.execute('UPDATE user_identity SET passwd = %s WHERE id = %s;',
							(passwd,id_user))
		self.conn.commit()
