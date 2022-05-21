from crypt import methods
import tempfile
from tkinter import scrolledtext
from flask import Flask, redirect, request, render_template, url_for
from sympy import *
from sympy.abc import ns
from plot_maker import create_plot
import solver



app = Flask(__name__)


@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/solve', methods = ['POST','GET'])
def solve():
    price = request.form['price']
    cost = request.form['cost']
    market = request.form['market']
    solution = solver.solve_profit_max(price, cost, market)
    return render_template('index.html', solution = solution, scroll='something') 

@app.route('/solution')
def show_solution():
    return redirect(url_for('index')+'#solution')


@app.route('/graph')
def show_graph():
    return render_template('index.html', graph_path = '/static/plot.png', scroll='something')
    # return redirect(url_for('index') + '#graph_div') 

# def update_solution():
#     return redirect(url_for('index')+'#solution')

if __name__ == "__main__":
    app.run(debug=True, port= 8000)