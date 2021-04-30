import PySimpleGUI as wd
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import config

matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

def create_graph_window():
    # Define graph window layout
    graph_layout = [
        [wd.Text("Interpolation Calculator")],
        [wd.Text("Interpolant (coefficients rounded to 3 decimal places)")],
        [wd.Multiline(config.interpolant, size=(60, 2))],
        [wd.Canvas(key="graph_window")],
        [wd.Text("View full, unrounded interpolant?")],
        [wd.Button("Yes"), wd.Button("Back"),],
    ]

    # Create the graph window
    graph_window = wd.Window(
        "Interpolation Calculator",
        graph_layout,
        location=(0, 0),
        finalize=True,
        element_justification="center",
        font="Helvetica 16",
        size = (950, 650)
    )

    # Add the plot to the window
    draw_figure(graph_window["graph_window"].TKCanvas, config.figure)

    while True:
        event, values = graph_window.read()
        # End program if user closes window
        # Open interpolant_window if "Yes"
        # Open polynomial_window if "Back"
        if event == wd.WIN_CLOSED:
            break
        if event == "Yes":
            graph_window.close()
            return 1
        if event == "Back":
            graph_window.close()
            return 2

    graph_window.close()