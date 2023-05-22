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

	def find_id_user_by_username(self, username):
		self.cursor.execute('SELECT id FROM user_identity WHERE username = %s;',
							(username,))
		id_user = self.cursor.fetchone()
		return id_user

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

	#Project changing module

	def find_projects_by_id_user(self, id_user):
		self.cursor.execute('SELECT id, name, create_date FROM projects WHERE id_user = %s;',
							(id_user,))
		projects = self.cursor.fetchall()
		return projects

	def find_last_id_project(self):
		self.cursor.execute('SELECT id FROM projects ORDER BY id DESC;')
		id_project = self.cursor.fetchone()
		return id_project

	def add_project(self, project):
		self.cursor.execute('INSERT INTO projects (id_user, name, id_region, create_date) VALUES (%s, %s, %s, %s);',
							(project.user_id,project.name,project.region_id,project.create_date))
		self.conn.commit()

	def delete_project(self, id_project):
		self.cursor.execute('DELETE FROM projects WHERE id = %s;',
							(id_project,))
		self.conn.commit()

	#Work with regions

	def find_id_and_name_regions(self):
		self.cursor.execute('SELECT id, name FROM regions;')
		regions = self.cursor.fetchall()
		return regions

	def find_data_by_id_region(self,id_region):
		self.cursor.execute('SELECT * FROM regions WHERE id = %s;',
							(id_region,))
		region_data = self.cursor.fetchone()
		return region_data
