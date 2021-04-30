import GUI.start_window as start_window
import GUI.polynomial_window as polynomial_window
import GUI.graph_window as graph_window
import monomial_graph
import lagrange_graph
import newton_graph
import GUI.interpolant_window as interpolant_window
import config

def create_gui():
    success = start_window.create_start_window()
    if success != 1:
        return
    while True:
        config.interpolant = ""
        config.full_interpolant = ""
        interpolation_type = polynomial_window.create_polynomial_window()
        if interpolation_type == 1:
            monomial_graph.create_figure(config.abscissae, config.data_values)
        elif interpolation_type == 2:
            lagrange_graph.create_figure(config.abscissae, config.data_values)
        elif interpolation_type == 3:
            newton_graph.create_figure(config.abscissae, config.data_values)
        else:
            return
        while True:
            graph = graph_window.create_graph_window()
            if graph == 1:
                interp = interpolant_window.create_interpolant_window()
                if interp != 1:
                    return
            elif graph == 2:
                break
            else:
                 return