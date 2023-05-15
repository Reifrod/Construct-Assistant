import psycopg2


class DBac:

	def get_cursor_and_connection(self):
		self.conn = psycopg2.connect(database = 'ConstructAssistant',
									 host = 'localhost',
									 user = 'postgres',
									 password = 'postgres',
									 port = '5432')
		self.cursor = self.conn.cursor()
		return self.conn, self.cursor