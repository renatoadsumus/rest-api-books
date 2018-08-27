from flask import Flask, render_template, redirect, \
      url_for, request, session, flash, g
import requests
from functools import wraps
import sqlite3

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/home',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        total = request.form['total_purchase']
        r = requests.get('https://api.github.com/events')
        #r.json()
        return r.text
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('login'))


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)