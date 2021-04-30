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


def interpolating_coefficients(data_values):
    c = []
    for y_val in data_values:
        float_y = float(y_val)
        c.append(float_y)

    return c

def interpolating_function(t, abscissae, c, length, it):
    if it < 0:
        return 0
    factor = 1
    divisor = 1
    config.interpolant += f"{c[it]}"
    for i in range(0, length + 1):
        if i != it:
            factor *= t - float(abscissae[i])
            config.interpolant += f"*(t - {abscissae[i]})"
            divisor *= float(abscissae[it]) - float(abscissae[i])
    config.interpolant += f"/{divisor}"
    if it >= 1:
        config.interpolant += " + "

    return c[it]*factor/divisor + interpolating_function(t, abscissae, c, length, it - 1)

def create_figure(abscissae, data_values):
    domain = find_domain(abscissae)
    coefficients = interpolating_coefficients(data_values)
    config.figure = matplotlib.figure.Figure(figsize=(5, 4), dpi = 100)
    t = np.arange(domain[0], domain[1], 0.01)
    interpolant = interpolating_function(t, abscissae, coefficients, len(coefficients) - 1, len(coefficients) - 1)
    config.full_interpolant = config.interpolant
    config.figure.add_subplot(111).plot(t, interpolant)