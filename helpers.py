# helpers.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to draw charts using Matplotlib
def draw_chart(data, chart_type="line"):
    """
    Draws a matplotlib chart based on the provided data and chart type.
    """
    fig, ax = plt.subplots()
    
    if chart_type == "line":
        ax.plot(data['x'], data['y'])  # Line chart data
    elif chart_type == "bar":
        ax.bar(data['x'], data['y'])  # Bar chart data
    elif chart_type == "pie":
        ax.pie(data['y'], labels=data['x'], autopct='%1.1f%%')  # Pie chart data
    
    return fig

# Function to display Matplotlib figure in PySimpleGUI window
def draw_figure(canvas, figure):
    """
    Embeds a matplotlib figure into the PySimpleGUI Canvas element.
    """
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)

# Function to clear the previous figure when switching screens
def clear_canvas(canvas):
    """
    Clears the canvas to prevent overlap of multiple charts.
    """
    for widget in canvas.winfo_children():
        widget.destroy()