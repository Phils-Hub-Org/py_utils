# utils/position_to_edge.py

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QWidget

from .get_screen_dimensions import getScreenDimensions
from .get_taskbar_size import getTaskbarSize
from .get_taskbar_position import getTaskbarPosition
from .widget_has_titlebar import widgetHasTitlebar

def positionToEdge(widget: QWidget, edge_position: str, y_offset: int = 0) -> None:
        
    screen_width, screen_height = getScreenDimensions()

    taskbar_size = getTaskbarSize()
    taskbar_position = getTaskbarPosition()

    widget_width = widget.width()
    widget_height = widget.height()

    # Adjust available screen dimensions based on taskbar position and size
    available_width = screen_width - (taskbar_size if taskbar_position in ['left', 'right'] else 0)
    available_height = screen_height - (taskbar_size if taskbar_position in ['top', 'bottom'] else 0)

    # Calculate offset for x and y if taskbar is at left or top
    offset_x = taskbar_size if taskbar_position == 'left' else 0
    offset_y = taskbar_size if taskbar_position == 'top' else 0

    # Add titlebar height if widget has a titlebar
    if widgetHasTitlebar(widget) and taskbar_position == 'top':
        offset_y += 30

    offset_y = offset_y + y_offset

    # Initialize x and y
    x, y = 0, 0

    # Determine the widget position based on the edge_position argument
    if edge_position == 'top':
        # Positioned at the top, centered horizontally
        x = offset_x + (available_width - widget_width) // 2
        y = offset_y

    elif edge_position == 'bottom':
        # Positioned at the bottom, centered horizontally
        x = offset_x + (available_width - widget_width) // 2
        y = offset_y + available_height - widget_height

    elif edge_position == 'left':
        # Positioned on the left, centered vertically
        x = offset_x
        y = offset_y + (available_height - widget_height) // 2

    elif edge_position == 'right':
        # Positioned on the right, centered vertically
        x = offset_x + available_width - widget_width
        y = offset_y + (available_height - widget_height) // 2

    elif edge_position == 'top-left':
        # Positioned at the top-left corner
        x, y = offset_x, offset_y

    elif edge_position == 'top-right':
        # Positioned at the top-right corner
        x = offset_x + available_width - widget_width
        y = offset_y

    elif edge_position == 'bottom-left':
        # Positioned at the bottom-left corner
        x = offset_x
        y = offset_y + available_height - widget_height

    elif edge_position == 'bottom-right':
        # Positioned at the bottom-right corner
        x = offset_x + available_width - widget_width
        y = offset_y + available_height - widget_height

    else:
        raise ValueError("Invalid edge_position argument. Choose from 'left', 'right', 'top', 'bottom', 'top-left', 'top-right', 'bottom-left', 'bottom-right'.")

    widget.setGeometry(QRect(x, y, widget_width, widget_height))