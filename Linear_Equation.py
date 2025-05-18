def solve_linear_equation(a, b):
    # ax + b = 0
    if a == 0:
        if b == 0:
            return "Infinite solutions (any value of x satisfies the equation)."
        else:
            return "No solution (inconsistent equation)."
    else:
        x = -b / a
        return f"The solution is x = {x}"
