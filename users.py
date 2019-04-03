#users
import sqlite3
# from flask import Flask

DB_FILE_PATH = "data/users.db"

class User():
	def __init__(self):
		self.connection = sqlite3.connect(DB_FILE_PATH)
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()

	def login(self, account_number, pin):
		data = (account_number, pin)
		cursor = self.connection.cursor()
		self.cursor.execute('select * from users where account_number = ? and pin = ?', data)
		row = self.cursor.fetchone()
		if row is not None:
			return True
			# return render_template('bank_statement.html', users=cursor.fetchone())
			# ['account_number'] = account_number
			# return True

		return False

