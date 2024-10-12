# main.py
import PySimpleGUI as sg
from des_one import des_one_layout, update_des_one, add_sales_data
from des_two import des_two_layout, update_des_two, add_demographics_data
from des_three import des_three_layout, update_des_three, add_ad_data
from helpers import draw_figure, clear_canvas

# Set theme
sg.theme("DarkBlue3")

# Function to create the window with the top command interface
def create_window(des_num):
    """
    Creates a window for the given DES number with a top command interface (menu bar).
    """
    menu_def = [['&Navigation', ['&DES One', '&DES Two', '&DES Three', '&Show All DES']]]

    if des_num == "all":
        # Layout showing all DES screens horizontally, only with a single Exit button
        layout = [
            [sg.Menu(menu_def)],  # Add menu bar
            [
                sg.Column([
                    [sg.Text("Sales Trends Over Time")],
                    *des_one_layout(exclude_nav=True)[1:],  # Reuse layout from DES 1 without navigation buttons
                    [sg.Canvas(key="-CANVAS1-")]
                ]),
                sg.VerticalSeparator(),
                sg.Column([
                    [sg.Text("Customer Demographics Insights")],
                    *des_two_layout(exclude_nav=True)[1:],  # Reuse layout from DES 2 without navigation buttons
                    [sg.Canvas(key="-CANVAS2-")]
                ]),
                sg.VerticalSeparator(),
                sg.Column([
                    [sg.Text("Advertisement Performance")],
                    *des_three_layout(exclude_nav=True)[1:],  # Reuse layout from DES 3 without navigation buttons
                    [sg.Canvas(key="-CANVAS3-")]
                ])
            ],
            [sg.Button("Exit")]  # Single Exit button at the bottom
        ]
        window = sg.Window("Insight-inator App", layout, finalize=True)

        # Display charts for all DES screens
        update_des_one(window, {'-PRODUCT_CATEGORY-': 'Category A', '-DATE_RANGE-': 'Last Month'})
        update_des_two(window, {'-AGE_RANGE-': '18-25', '-REGION-': 'North America'})
        update_des_three(window, {'-CAMPAIGN-': 'Campaign 1'})

    else:
        # Individual DES screens with navigation buttons and exit buttons
        layout = des_one_layout() if des_num == 1 else des_two_layout() if des_num == 2 else des_three_layout()
        window = sg.Window("Sales and Marketing Insights", [[sg.Menu(menu_def)], *layout], finalize=True)
        if des_num == 1:
            update_des_one(window, {'-PRODUCT_CATEGORY-': 'Category A', '-DATE_RANGE-': 'Last Month'})
        elif des_num == 2:
            update_des_two(window, {'-AGE_RANGE-': '18-25', '-REGION-': 'North America'})
        elif des_num == 3:
            update_des_three(window, {'-CAMPAIGN-': 'Campaign 1'})

    return window

# Start with DES 1
current_des = 1
window = create_window(current_des)

# Event Loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    # Handling Add Data Point event for DES One
    if event == "Add Data Point":
        if current_des == 1:
            # Get the new data entered by the user
            new_date = values.get("-NEW_DATE-", "")
            new_category = values.get("-NEW_CATEGORY-", "")
            new_sales = values.get("-NEW_SALES-", "")
            
            # Add the new data point
            add_sales_data(new_date, new_category, new_sales)
            
            # Update the chart with the new data point
            update_des_one(window, values)
        
        elif current_des == 2:
            # Get the new data entered by the user
            new_age_range = values.get("-NEW_AGE_RANGE-", "")
            new_region = values.get("-NEW_REGION-", "")
            new_sales = values.get("-NEW_SALES-", "")
            
            # Add the new data point
            add_demographics_data(new_age_range, new_region, new_sales)
            
            # Update the chart with the new data point
            update_des_two(window, values)
        
        elif current_des == 3:
            # Get the new data entered by the user
            new_campaign = values.get("-NEW_CAMPAIGN-", "")
            new_clicks = values.get("-NEW_CLICKS-", "")
            new_impressions = values.get("-NEW_IMPRESSIONS-", "")
            
            # Add the new data point
            add_ad_data(new_campaign, new_clicks, new_impressions)
            
            # Update the chart with the new data point
            update_des_three(window, values)

    # Handling Filter button events for each DES
    if event == "Filter":
        if current_des == 1:
            update_des_one(window, values)
        elif current_des == 2:
            update_des_two(window, values)
        elif current_des == 3:
            update_des_three(window, values)

    # Handling menu bar navigation
    if event == "DES One":
        current_des = 1
        window.close()
        window = create_window(current_des)

    elif event == "DES Two":
        current_des = 2
        window.close()
        window = create_window(current_des)

    elif event == "DES Three":
        current_des = 3
        window.close()
        window = create_window(current_des)

    elif event == "Show All DES":
        window.close()
        window = create_window("all")

    # Handling Next/Previous button events
    if event == "Next":
        current_des += 1
        if current_des > 3:
            current_des = 1
        window.close()
        window = create_window(current_des)

    if event == "Previous":
        current_des -= 1
        if current_des < 1:
            current_des = 3
        window.close()
        window = create_window(current_des)

window.close()