from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

class User():

    def __init__(self, name, age, address, phone, email):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email

user1 = User('Jim', 26, '106 East 30th', 7703319495, 'jim@kn4lra.com')

users = [user1]

@app.route('/')
def index():
    return render_template('bootstrap_table.html', title='Bootstrap Table', users=users)

@app.route('/found')
def found():
    return render_template('form.html', title='N5XU Fox')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
