#!/usr/bin/env python2.7
from flask import Flask, render_template
from flask import request, redirect, url_for
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Account
app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///accounts.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Home Page
@app.route('/')
def showHome():
    return render_template('home.html')


# Show all Accounts
@app.route('/')
@app.route('/list/')
def showAccounts():
    accounts = session.query(Account).order_by(asc(Account.name))
    return render_template('list.html', accounts=accounts)


# Create a new Account
@app.route('/add', methods=['GET', 'POST'])
def newCompetetion():
    if request.method == 'POST':
        newAccount = Account(
            name=request.form['name'], email=request.form['email'])
        session.add(newAccount)
        session.commit()
        return redirect(url_for('showHome'))
    else:
        return render_template('add.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
