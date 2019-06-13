import math
from sympy.parsing import sympy_parser
import sympy as sp
from scipy.integrate import solve_ivp
import numpy as np

def parseEquations(equations):
    t, x, y, z = sp.symbols('t x y z')
    variables = [x]
    if len(equations) >= 2:
        variables.append(y)
    if len(equations) == 3:
        variables.append(z)

    functions = []
    for equation in equations:
        functions.append(sp.lambdify([t, variables], sympy_parser.parse_expr(equation)))

    def f(t, v):
        result = []
        for g in functions:
            result.append(g(t, v))
        return result
    return f

def solveODE(equations, y0, t0, tmax, integrator, tolerance):
    f = parseEquations(equations)

    if math.isnan(tolerance):
        tolerance = 1e-6
    
    solution = solve_ivp(f, [t0, tmax], y0, atol=tolerance, t_eval=np.arange(t0, tmax, 0.01))
    return solution.t, solution.y