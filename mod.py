from flask import flask
from flask_sqlalchemy import SQLAlchemy

app = flask(__name__)
app.config[]

app.config['SQLACHEMY_DATABASE-URI'] = 'SQLITE:///data/users.db'

db = SQLAlchemy(app)


# Web ATM project

# Create a web interface for an ATM using Bootstrap
# We should be able to login with a account number and PIN
# We do not need to have a signup form, you can insert the data in the db manually
# When a user tries to log in, you need to check that their account number and PIN are correct based on the info you have in the db
# When the add / remove money from the account you need to take it off or add it to the balance




# def get_int():




 # Build the inventory with your newly created Model
 # Create withdrawe and deposit routes to be able to add / remove money from the account, 
 # you will need to add a balance attribute to your model.
 # put it on github



class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	account_number = db.Column(db.Integer, unique=True , nullable=False)
	pin = db.Column(db.Integer, unique=False, nullable=False)




	# def_init__(self, account_number, pin):
	# self.account_number = account_number
	# self.pin = pin


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