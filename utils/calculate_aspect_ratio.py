def calculateAspectRatio(parent_width: int, parent_height: int) -> tuple:
    # Define the aspect ratio
    aspect_ratio = 16 / 9

    # Get padding value
    padding = 0

    # Calculate the available size after padding
    available_width = max(1, parent_width - 2 * padding)
    available_height = max(1, parent_height - 2 * padding)

    # Determine the new content_layout size while maintaining the aspect ratio
    if available_width / available_height > aspect_ratio:
        # Limit by height if the width is too large
        content_layout_height = available_height
        content_layout_width = int(content_layout_height * aspect_ratio)
    else:
        # Limit by width if the height is too large
        content_layout_width = available_width
        content_layout_height = int(content_layout_width / aspect_ratio)

    # Calculate the top-left position to center the content_layout
    x = (parent_width - content_layout_width) // 2
    y = (parent_height - content_layout_height) // 2

    # Adjust position by adding padding
    x += padding
    y += padding

    # Ensure the rectangle does not exceed window boundaries
    x = min(x, parent_width - content_layout_width - padding)
    y = min(y, parent_height - content_layout_height - padding)

    return x, y, content_layout_width, content_layout_height