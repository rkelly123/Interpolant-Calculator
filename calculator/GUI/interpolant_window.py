import PySimpleGUI as wd
import config

def create_interpolant_window():
    # Define interpolant window layout
    interpolant_layout = [
        [wd.Text("Full Interpolant")],
        [wd.Canvas(key="interpolant_window")],
        [wd.Text("y = ")],
        [wd.Multiline(config.full_interpolant, size=(65, 10))],
        [wd.Button("Back")],
    ]

    # Create the interpolant window
    interpolant_window = wd.Window(
        "Interpolation Calculator",
        interpolant_layout,
        location=(0, 0),
        finalize=True,
        element_justification="center",
        font="Helvetica 18",
        size = (950, 450)
    )

    while True:
        event, values = interpolant_window.read()
        # End program if user closes window
        # Open graph_window if "Back"
        if event == wd.WIN_CLOSED:
            break
        if event == "Back":
            interpolant_window.close()
            return 1

    interpolant_window.close()