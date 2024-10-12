# des_three.py
import PySimpleGUI as sg
from helpers import draw_chart, clear_canvas, draw_figure

# Sample data for demonstration
ad_performance_data = [
    {"campaign": "Campaign 1", "clicks": 150, "impressions": 500},
    {"campaign": "Campaign 2", "clicks": 120, "impressions": 450},
    {"campaign": "Campaign 3", "clicks": 200, "impressions": 600},
    # Additional data...
]

def des_three_layout(exclude_nav=False):
    """
    Returns the layout for DES Three (Advertisement Performance).
    The parameter exclude_nav controls whether navigation buttons, including Exit, are included.
    """
    layout = [
        [sg.Text("Advertisement Performance")],
        [sg.Text("Select Ad Campaign:"), sg.Combo(['Campaign 1', 'Campaign 2', 'Campaign 3'], key="-CAMPAIGN-")],
        [sg.Canvas(key="-CANVAS3-")],
        
        # New input fields for manually adding a data point
        [sg.Text("Enter Campaign (e.g., Campaign 1):"), sg.Input(key="-NEW_CAMPAIGN-")],
        [sg.Text("Enter Clicks:"), sg.Input(key="-NEW_CLICKS-")],
        [sg.Text("Enter Impressions:"), sg.Input(key="-NEW_IMPRESSIONS-")],
        [sg.Button("Add Data Point"), sg.Button("Filter")],  # Add button for submitting new data points
    ]
    
    # Add navigation and exit buttons if not excluded
    if not exclude_nav:
        layout.append([sg.Button("Previous"), sg.Button("Exit")])

    return layout

def filter_ad_data(campaign):
    """
    Filters the ad performance data based on the selected campaign.
    """
    return [item for item in ad_performance_data if item["campaign"] == campaign]

def add_ad_data(new_campaign, new_clicks, new_impressions):
    """
    Adds a new ad performance data point to the ad_performance_data list.
    """
    try:
        # Ensure clicks and impressions are integers
        new_clicks = int(new_clicks)
        new_impressions = int(new_impressions)
        
        # Add new data point
        ad_performance_data.append({"campaign": new_campaign, "clicks": new_clicks, "impressions": new_impressions})
    except ValueError:
        print("Invalid input. Clicks and Impressions must be integers.")

def update_des_three(window, values):
    """
    Updates the canvas with a pie chart for DES Three, filtering data based on user input.
    """
    campaign = values.get("-CAMPAIGN-", "Campaign 1")  # Default to 'Campaign 1' if not set
    
    # Filter the data
    filtered_data = filter_ad_data(campaign)
    
    # Prepare data for the pie chart
    clicks = [item["clicks"] for item in filtered_data]
    impressions = [item["impressions"] for item in filtered_data]
    
    # Prepare pie chart data
    data = {'x': ['Clicks', 'Impressions'], 'y': [sum(clicks), sum(impressions)]}
    
    # Update the chart
    fig = draw_chart(data, chart_type="pie")
    canvas_elem = window["-CANVAS3-"].TKCanvas
    clear_canvas(canvas_elem)
    draw_figure(canvas_elem, fig)