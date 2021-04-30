import PySimpleGUI as wd
import re
import config

def create_points(points):
    # Turn input string into readable point inputs
    restrictions = re.compile(r'[^0-9. ]+')
    str = re.sub(restrictions, '', points).lower()

    # Make string splits for points
    # if no inputs, add point (0,0)
    # if only x input, add y value of 0
    splits = str.split()
    
    if len(splits) % 2 != 0:
            splits.append('0')
    if len(splits) == 0:
            splits.append('0')
            splits.append('0')
    # Create points with splits
    counter = 0
    for split in splits:
        if counter == 0:
            if split in config.abscissae:
                    counter += 2
            else:
                config.abscissae.append(split)
                counter += 1
        elif counter == 1:
            config.data_values.append(split)
            counter -= 1



def create_start_window():
    wd.theme('Dark Green 4')
    # Define start window layout
    start_layout = [
        [wd.Text("Interpolation Calculator")],
        [wd.Canvas(key="start_window")],
        [wd.Text("Please enter a list of points. For example: (1 2), (3 2), ...")], 
        [wd.Text("Points:"), wd.InputText()],
        [wd.Button("Continue")],
    ]
    # Create the start window
    start_window = wd.Window(
        "Interpolation Calculator",
        start_layout,
        location=(0, 0),
        finalize=True,
        element_justification="center",
        font="Helvetica 18",
        size = (950, 200),
    )

    while True:
        event, values = start_window.read()
        # End program if user closes window
        # Open polynomial_window if "Continue"
        if event == wd.WIN_CLOSED:
            break
        if event == "Continue":
            create_points(values[0])
            start_window.close()
            return 1
        start_window.close()
                