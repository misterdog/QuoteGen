from flask import Flask, render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
							title = 'Home',
							user = 'Blake')

@app.route('/fullmove', methods = ['POST', 'GET'])
def fullmove():
	if request.method == 'POST':
		if request.form['fullmove'] == "Full Move":
			return render_template('fullmove.html')

