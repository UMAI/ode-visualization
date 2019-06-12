import math
from sympy.parsing import sympy_parser
import sympy as sp
from scipy.integrate import solve_ivp

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
    
    solution = solve_ivp(f, [t0, tmax], y0, atol=tolerance, max_step=1e-3)
    points = solution.y
    return points

#print(solve(['x**2', 'x - y'], [1, 1], 0, 10, 'dopri5', 1e-6))