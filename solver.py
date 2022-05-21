
from sympy import *
from sympy.abc import ns
from plot_maker import create_plot



# TODO: make it so that you can input the equations in different forms, either revenue equation directly or price equation

def solve_profit_max(price, cost, market):
    """
    solves profit maximization problems for firms using user input for the price [P(Q)] and the cost [C(Q)] functions

    @param market: type of market (e.g. competitive, monopoly)
    @return: Tuple (profit maximizing quantity, profit generated at that quantity)
    """
    # market_types = ["competitive", "monopoly", "monopsony"]

    # # Get market type from user
    # while True:
    #     market = input("What is the market structure (competitive, monopoly, or monopsony)? ").lower()
    #     if market not in market_types:
    #         print(f"I'm unfamiliar with that market, try one of those: {market_types}")
    #     else:
    #         break

    # print(f"You are solving a {market} problem: ")

    # Create unknown variable as a symbol
    Q = symbols("Q")  # symbol means the same thing as a variable in normal language

    # # Set up equations
    # print("example input for price function: -100 * Q + 4")
    # print("example input for cost function: Q ^ 2 + 4 * Q - 3 \n")

    ns["Q"] = Symbol("Q")
    market = market

    # Get price and cost function from user

    price = sympify(price, locals=ns) 
    cost = sympify(cost, locals=ns)

    p = 0  # price
    revenue =  price * Q  # setting up revenue equation


    create_plot(price, cost, revenue) # This is here because the error occurs here if user gives wrong input


    # write solving process
    output = "Profit = Revenue - Cost\n" + "Profit = P * Q - Cost\n" + "max Profit =\n∆ Profit/ ∆ Q = 0\nMR - MC = 0\n" + "max Profit = MR - MC = 0\n" + f"max Profit = {diff(revenue)} - ({diff(cost)}) = 0\n" + f"max Profit = {diff(revenue)} = {diff(cost)}\n"

    # Solve for possible quantities
    quantities = solve(diff(revenue) - diff(cost), Q)

    # find possible quantities solutions (could be 0 or higher, if higher choose the higher)
    q = 0
    for x in quantities:
        if x >= 0:
            print(f"Q could be: {x} units")
            print(f"Q could be: {N(x, 3)} units")
        if x > 0:
            q = x

    # TODO: test this
    if market != "monopsony":
        p = price.subs(Q, q)  # finds price for competitive and monopoly markets by finding price at optimal Q
    else:
        p = cost.subs(Q, q) # finds price for monopsony by substituting optimal Q in the cost function

    # replacing Q in cost with found quantity value
    costText = str(cost).replace("Q", "(" + str(q) + ")")  # TODO: just use cost and revenue instead of new variables
    revenueText = str(revenue).replace("Q", "(" + str(q) + ")")

    # find profit with found quantity
    profit = eval(revenueText) - eval(costText)

    # Print output
    output += "\nProfit = P * Q - C \n" + f"Profit = {revenueText.replace('**', '^')} - ({costText.replace('**', '^')})\n" + f"profit = ${profit}\n" + f"profit = ${round(profit, 4)}"

    # print("\n")

    # # TODO: find monopsony welfare loss
    # if market == "monopoly":
    #     welfareLoss = find_monopoly_welfare_loss(Q, cost, p, price, q)
    #     return q, profit, welfareLoss

    return output


def find_monopoly_welfare_loss(Q, cost, p, price, q):
    a = p  # upper corner substitute Q into the MC (derivative of cost function)
    print(f"a = {a}")
    c = diff(cost).subs(Q, q)  # lower  corner where MC is evaluated at new Q
    print(f"c = {c}")
    b = solve(diff(cost) - price, Q)  # right corner of the triangle
    print(f"b = {b}, and it's type is {type(b)}")
    print(f"b[0] = {b[0]}")
    b = b[0]
    welfareLoss = 1 / 2 * (a - c) * (b - q)  # b-q because q is the monopoly quant and b is the free market quant
    print(f"\nWelfare loss is equal to {welfareLoss}")
    return welfareLoss



if __name__ == '__main__':
    solve_profit_max()
