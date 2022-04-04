from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector

import re
import datetime

app = Flask(__name__)
mysql = MySQLConnector('bdgbg')

@app.route('/addjogo')
def addjogopage():
	return render_template('/addjogo.html')

@app.route("/edit/<id>")
def editjogopage(id):
	jogos = mysql.fetch("SELECT * FROM jogos WHERE id = '{}' LIMIT 1".format(id))
	return render_template('edit.html', jogos=jogos)

@app.route('/addjogo', methods=['POST'])
def addjogo():
	query = "INSERT INTO jogos (nome, categoria) VALUES ('{}', '{}', NOW(), NOW())".format(request.form['nome'], request.form['categoria'])
	print (query)
	mysql.run_mysql_query(query)
	return redirect('/')

@app.route('/delete/<id>')
def destroy(id):
	query = "DELETE FROM jogos WHERE id = '{}'".format(id)
	print (query)
	mysql.run_mysql_query(query)
	return redirect('/')

@app.route('/edit/<id>', methods=['POST'])
def editjogo(id):
	query = "UPDATE jogos SET nome = '{}', categoria = '{}' WHERE id = '{}'".format(request.form['nome'], request.form['categoria'],id)
	print (query)
	mysql.run_mysql_query(query)
	return redirect('/')

@app.route('/back')
def logout():
	return redirect('/')
if __name__ == "__main__":
	app.run(debug=True)