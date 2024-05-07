import streamlit as st
import numpy as np


@st.cache_data()
def generate_result_image(background, overlay, coordinates):
    result = background.copy()  # Use previous image

    # Paste the image to paste
    for x, y in coordinates:
        result = overlay_image(result, overlay, x, y)

    return result


def overlay_image(background, overlay, x, y):
    # Copy background image
    output = background.copy()

    # Resize the image to paste
    overlay_height, overlay_width = overlay.shape[:2]

    # Get the coordinates of the area to paste
    y_end = y + overlay_height
    x_end = x + overlay_width

    # If the dimensions of the area to be pasted are larger than the dimensions of the background, adjust the
    # dimensions to the background
    if y_end > background.shape[0]:
        overlay_height -= y_end - background.shape[0]
        y_end = background.shape[0]
    if x_end > background.shape[1]:
        overlay_width -= x_end - background.shape[1]
        x_end = background.shape[1]

    # Take the area to be glued and make the appropriate dimensioning
    overlay_area = overlay[:overlay_height, :overlay_width]

    # Check for alpha channel
    if overlay.shape[2] == 4:
        alpha = overlay_area[:, :, 3] / 255.0  # Normalise if there is an Alpha channel
        for c in range(0, 3):
            output[y:y_end, x:x_end, c] = (1 - alpha) * output[y:y_end, x:x_end, c] + alpha * overlay_area[:, :, c]
            # Merge using the Alpha channel
    else:
        output[y:y_end, x:x_end] = overlay_area  # If there is no alpha channel, simply paste

    return output


def random_data(data):
    # Calculate the proportions of unique values in each remaining column
    column_proportions = {}
    for column in data.columns:
        column_proportions[column] = data[column].value_counts(normalize=True)

    num_samples = 38  # Number of random samples
    generated_data = {}  # Dictionary to store random data for each column

    for _ in range(num_samples):
        # Generate random data for each column based on the proportions
        for column, proportions in column_proportions.items():
            generated_data.setdefault(column, []).append(
                np.random.choice(proportions.index, p=proportions.values)
            )
    return generated_data
