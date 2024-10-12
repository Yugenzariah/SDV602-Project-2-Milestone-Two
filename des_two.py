# des_two.py
import PySimpleGUI as sg
from helpers import draw_chart, clear_canvas, draw_figure

# Sample data for demonstration
demographics_data = [
    {"age_range": "18-25", "region": "North America", "sales": 300},
    {"age_range": "26-35", "region": "Europe", "sales": 250},
    {"age_range": "36-50", "region": "Asia", "sales": 280},
    {"age_range": "18-25", "region": "Europe", "sales": 320},
    {"age_range": "26-35", "region": "North America", "sales": 310},
    # Additional data...
]

def des_two_layout(exclude_nav=False):
    """
    Returns the layout for DES Two (Customer Demographics Insights).
    The parameter exclude_nav controls whether navigation buttons, including Exit, are included.
    """
    layout = [
        [sg.Text("Customer Demographics Insights")],
        [sg.Text("Select Age Range:"), sg.Combo(['18-25', '26-35', '36-50'], key="-AGE_RANGE-")],
        [sg.Text("Select Region:"), sg.Combo(['North America', 'Europe', 'Asia'], key="-REGION-")],
        [sg.Canvas(key="-CANVAS2-")],
        
        # New input fields for manually adding a data point
        [sg.Text("Enter Age Range (e.g., 18-25):"), sg.Input(key="-NEW_AGE_RANGE-")],
        [sg.Text("Enter Region (e.g., North America):"), sg.Input(key="-NEW_REGION-")],
        [sg.Text("Enter Sales Value:"), sg.Input(key="-NEW_SALES-")],
        [sg.Button("Add Data Point"), sg.Button("Filter")],  # Add button for submitting new data points
    ]
    
    # Add navigation and exit buttons if not excluded
    if not exclude_nav:
        layout.append([sg.Button("Previous"), sg.Button("Next"), sg.Button("Exit")])

    return layout

def filter_demographics_data(age_range, region):
    """
    Filters the demographics data based on the selected age range and region.
    """
    return [item for item in demographics_data if item["age_range"] == age_range and item["region"] == region]

def add_demographics_data(new_age_range, new_region, new_sales):
    """
    Adds a new demographics data point to the demographics_data list.
    """
    try:
        # Ensure sales is an integer
        new_sales = int(new_sales)
        
        # Add new data point
        demographics_data.append({"age_range": new_age_range, "region": new_region, "sales": new_sales})
    except ValueError:
        print("Invalid sales value. Must be an integer.")

def update_des_two(window, values):
    """
    Updates the canvas with a bar chart for DES Two, filtering data based on user input.
    """
    age_range = values.get("-AGE_RANGE-", "18-25")  # Default to '18-25' if not set
    region = values.get("-REGION-", "North America")  # Default to 'North America' if not set
    
    # Filter the data
    filtered_data = filter_demographics_data(age_range, region)
    
    # Prepare data for the chart
    regions = [item["region"] for item in filtered_data]
    sales = [item["sales"] for item in filtered_data]
    
    data = {'x': regions, 'y': sales}
    
    # Update the chart
    fig = draw_chart(data, chart_type="bar")
    canvas_elem = window["-CANVAS2-"].TKCanvas
    clear_canvas(canvas_elem)
    draw_figure(canvas_elem, fig)