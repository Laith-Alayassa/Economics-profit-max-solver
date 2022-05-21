from flask import Flask, redirect, request, render_template, url_for, flash
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
    if len(solution) > 0:
        return render_template('index.html', solution = solution, scroll='something') 
    else:
        return render_template('index.html', error = True)

@app.route('/solution')
def show_solution():
    return redirect(url_for('index')+'#solution')


@app.route('/graph')
def show_graph():
        return redirect(url_for('index')+'#graph_div')

if __name__ == "__main__":
    app.run(debug=True, port= 8000)