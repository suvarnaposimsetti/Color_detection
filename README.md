Project Title: Color Identification in Images using OpenCV and Pandas
1. Introduction
The goal of this project is to develop a tool that identifies the color name of a specific point in an image. By leveraging OpenCV for image processing and pandas for handling a dataset of colors, the tool allows users to click on any point in the image to get the name of the color and its RGB values. This can be particularly useful for designers, artists, and anyone working with digital images.

2. Objectives
To read and display an image using OpenCV.
To detect mouse clicks on the image.
To read a CSV file containing color names and their corresponding RGB values using pandas.
To calculate the closest matching color name from the CSV file for the clicked point in the image.
To display the color name and RGB values on the image.
3. Tools and Technologies
Programming Language: Python
Libraries:
OpenCV (cv2): For image processing and handling mouse events.
pandas: For reading and manipulating the CSV file containing color data.
4. Methodology
Reading the Image:

The image is read using OpenCV's cv2.imread function.
Reading the Color Data:

The color data is stored in a CSV file with columns for color name and RGB values.
The CSV file is read using pandas into a DataFrame for easy manipulation.
Mouse Callback Function:

A function is set up to handle mouse double-click events.
When the user double-clicks on a point in the image, the function captures the RGB values at that point.
Color Matching:

The tool calculates the minimum distance between the clicked color's RGB values and each color in the CSV file.
The color with the minimum distance is identified as the closest matching color.
Displaying the Results:

A rectangle is drawn on the image to display the color name and RGB values.
The text is displayed in a color that contrasts with the background for readability.

This report outlines the project’s objectives, methodology, implementation details, and results, providing a comprehensive overview of the color identification tool developed using Python, OpenCV, and pandas.
