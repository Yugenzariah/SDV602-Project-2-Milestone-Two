# des_one.py
import PySimpleGUI as sg
from helpers import draw_chart, clear_canvas, draw_figure

# Sample data for demonstration
sales_data = [
    {"date": "2024-01-01", "category": "Category A", "sales": 150},
    {"date": "2024-01-02", "category": "Category B", "sales": 200},
    {"date": "2024-01-03", "category": "Category C", "sales": 180},
    {"date": "2024-01-04", "category": "Category A", "sales": 160},
    {"date": "2024-01-05", "category": "Category B", "sales": 210},
    # Additional data...
]

def des_one_layout(exclude_nav=False):
    """
    Returns the layout for DES One (Sales Trends Over Time).
    The parameter exclude_nav controls whether navigation buttons, including Exit, are included.
    """
    layout = [
        [sg.Text("Sales Trends Over Time")],
        [sg.Text("Select Date Range:"), sg.Combo(['Last Week', 'Last Month', 'Last Year'], key="-DATE_RANGE-")],
        [sg.Text("Select Product Category:"), sg.Combo(['Category A', 'Category B', 'Category C'], key="-PRODUCT_CATEGORY-")],
        [sg.Canvas(key="-CANVAS1-")],
        
        # New input fields for manually adding a data point
        [sg.Text("Enter Date (YYYY-MM-DD):"), sg.Input(key="-NEW_DATE-")],
        [sg.Text("Enter Product Category:"), sg.Input(key="-NEW_CATEGORY-")],
        [sg.Text("Enter Sales Value:"), sg.Input(key="-NEW_SALES-")],
        [sg.Button("Add Data Point"), sg.Button("Filter")],  # Add button for submitting new data points
    ]
    
    # Add navigation and exit buttons if not excluded
    if not exclude_nav:
        layout.append([sg.Button("Next"), sg.Button("Exit")])

    return layout

def filter_sales_data(date_range, category):
    """
    Filters the sales data based on the selected date range and product category.
    """
    # For now, only filter by category (date range logic can be added based on data)
    filtered_data = [item for item in sales_data if item["category"] == category]
    return filtered_data

def add_sales_data(new_date, new_category, new_sales):
    """
    Adds a new sales data point to the sales_data list.
    """
    try:
        # Ensure sales is an integer
        new_sales = int(new_sales)
        
        # Add new data point
        sales_data.append({"date": new_date, "category": new_category, "sales": new_sales})
    except ValueError:
        print("Invalid sales value. Must be an integer.")

def update_des_one(window, values):
    """
    Updates the canvas with a line chart for DES One, filtering data based on user input.
    """
    category = values.get("-PRODUCT_CATEGORY-", "Category A")  # Default to 'Category A' if not set
    date_range = values.get("-DATE_RANGE-", "Last Month")  # Default to 'Last Month' if not set
    
    # Filter the data
    filtered_data = filter_sales_data(date_range, category)
    
    # Prepare data for the chart
    dates = [item["date"] for item in filtered_data]
    sales = [item["sales"] for item in filtered_data]
    
    data = {'x': dates, 'y': sales}
    
    # Update the chart
    fig = draw_chart(data, chart_type="line")
    canvas_elem = window["-CANVAS1-"].TKCanvas
    clear_canvas(canvas_elem)
    draw_figure(canvas_elem, fig)