import sqlite3

class Money():
	def __init__(self):
		self.connection = sqlite3.connection(users.db)
		self.cursor = self.connection.cursor()

	def get_account(self):
		query = "SELECT * FROM users WHERE account_number = {}".format(account_number)
		self.cursor.execute(query)
		money = self.cursor.fetchall()
		return money

	