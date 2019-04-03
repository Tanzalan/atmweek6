from flask import Flask
from flask import flash, render_template, request, url_for, redirect

from users import User
from money import Money

app = Flask(__name__)
app.secret_key = b'aj(>,m&*@#NxmaiOxH23Kkmlb128($'


# Web ATM project

# Create a web interface for an ATM using Bootstrap
# We should be able to login with a account number and PIN
# We do not need to have a signup form, you can insert the data in the db manually
# When a user tries to log in, you need to check that their account number and PIN are correct based on the info you have in the db
# When the add / remove money from the account you need to take it off or add it to the balance

@app.route('/', methods=['POST', 'GET'])
def login():
	if request.method == 'GET':
		return render_template('login.html')

	account_number = request.form.get('account_number', None)
	pin = request.form.get('pin', None)
	users = User()
	if users.login(account_number, pin) == True:
		return redirect(url_for('get_account'))

	else:
		flash('Wrong account and/or pin. Please Try again.')
		return render_template('login.html')

@app.route('/bank_statement')
def get_account():
	return render_template('bank_statement.html')













@app.route("/logout/")
def logout():
	users = User()
	users.logout()
	return redirect(url_for('login.html'))



	# Once you are done with your ATM

# Move your account logic into its own class

# We want to create script to feed random accounts into our database
# You will need to create a class with 3 functions:
# - generate_account_number()
# - generate_pin()
# - generate_balance()

# Calling this generator class and your account class, you should automate the create of 100 accounts numbers
