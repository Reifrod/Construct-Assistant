from .DBAccess import DBac

class DBreq:

	def __init__(self):
		db = DBac()
		self.conn,self.cursor = DBac.get_cursor_and_connection(self)