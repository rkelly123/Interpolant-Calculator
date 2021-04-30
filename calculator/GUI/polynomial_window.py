import PySimpleGUI as wd

def create_polynomial_window():
    # Define polynomial window layout
    polynomial_layout = [
        [wd.Text("Which Form of Polynomial Interpolation?")],
        [wd.Canvas(key="start_window")],
        [wd.Button("Monomial")],
        [wd.Button("Lagrange")],
        [wd.Button("Newton")],
    ]

    # Create the polynomial window
    polynomial_window = wd.Window(
        "Interpolation Calculator",
        polynomial_layout,
        location=(0, 0),
        finalize=True,
        element_justification="center",
        font="Helvetica 18",
        size = (950, 200)
    )

    while True:
        event, values = polynomial_window.read()
        # End program if user closes window
        # Open graph_window otherwise
        # if "Monomial" create monomial figure
        # if "Lagrange" create lagrange figure
        # if "Newton" create newton figure
        if event == wd.WIN_CLOSED:
            break
        if event == "Monomial":
            polynomial_window.close()
            return 1
        if event == "Lagrange":
            polynomial_window.close()
            return 2
        if event == "Newton":
            polynomial_window.close()
            return 3

    polynomial_window.close()