

import streamlit as st
import streamlit.components.v1 as components

# Example image URL or path
image_url = 'https://via.placeholder.com/800x600.png'

# Define custom HTML and CSS
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {{
            position: relative;
            width: 100%;
        }}
        .image {{
            width: 100%;
        }}
        .button {{
            position: absolute;
            top: 50px; /* Adjust position */
            left: 50px; /* Adjust position */
            background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <div class="container">
        <img src="C:/Users/jord5/Desktop/image_test.png">
        <button class="button" onclick="alert('Button 1 clicked!')">Button 1</button>
        <button class="button" style="top: 100px; left: 50px;" onclick="alert('Button 2 clicked!')">Button 2</button>
    </div>
</body>
</html>
"""

# Render the HTML in Streamlit
components.html(html_code, height=600)
