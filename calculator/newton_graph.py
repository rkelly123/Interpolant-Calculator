import matplotlib.pyplot
import numpy as np
import scipy.linalg as la
import config

def find_domain(abscissae):
    max_num = -1000000000
    min_num = 1000000000
    for val in abscissae:
        val = float(val)
        if val > max_num:
            max_num = val
        if val < min_num:
            min_num = val
    return [min_num, max_num]


def interpolating_coefficients(abscissae, data_values):
    A = []
    for x_val in abscissae:
        float_x = float(x_val)
        i = 1
        arr = []
        arr.append(1)
        while i < len(abscissae):
            j = i
            factor = 1
            while j > 0:
                factor *= float_x - float(abscissae[j-1])
                j -= 1
            arr.append(factor)
            i += 1
        A.append(arr)

    y = []
    for y_val in data_values:
        float_y = float(y_val)
        y.append(float_y)
    
    c = np.linalg.solve(A, y)
    
    return c

def interpolating_newton_phi(t, abscissae, length):
    newton_phi = 1
    j = length
    while j >= 0:
        newton_phi *= (t - float(abscissae[j]))
        config.interpolant += f"(t - {float(abscissae[j])})"
        config.full_interpolant += f"(t - {float(abscissae[j])})"
        j -= 1
    return newton_phi

def interpolating_function(t, abscissae, c, length):
    if length < 0:
        return 0
    if length == 0:
        config.interpolant += f"{round(c[length], 3)}"
        config.full_interpolant += f"{c[length]}"
    else:
        config.interpolant += f"{round(c[length], 3)}*"
        config.full_interpolant += f"{c[length]}*"
    newton_phi = interpolating_newton_phi(t, abscissae, length - 1)
    if length != 0:
        config.interpolant += " + "
        config.full_interpolant += " + "
    return newton_phi*c[length] + interpolating_function(t, abscissae, c, length - 1)

def create_figure(abscissae, data_values):
    domain = find_domain(abscissae)
    coefficients = interpolating_coefficients(abscissae, data_values)
    config.figure = matplotlib.figure.Figure(figsize=(5, 4), dpi = 100)
    t = np.arange(domain[0], domain[1], 0.01)
    interpolant = interpolating_function(t, abscissae, coefficients, len(coefficients) - 1)
    config.figure.add_subplot(111).plot(t, interpolant)