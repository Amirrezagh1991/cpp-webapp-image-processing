## Image Processing WebApp with Streamlit and C++ Backend

This project is a C++ web app for image processing that allows users to upload an image and 
apply various image processing operations, such as grayscale conversion and Canny edge detection. 
The web app is powered by Streamlit, and the image processing is performed by a C++ backend.

## Demo

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: You should have Python installed on your system.
- **C++ Compiler**: Ensure you have a C++ compiler (e.g., g++) installed for building the C++ backend.
- **OpenCV**: You'll need the OpenCV library for image processing. Install it using your system's package manager or by building it from source.
- **[Optional] CMake**: If you don't have CMake installed, you can get it from [cmake.org](https://cmake.org/download/).


## Installation

   ```bash
   git clone https://github.com/Amirrezagh1991/cpp-webapp-image-processing.git
   cd cpp-webapp-image-processing
   make
   pip install -e .
   ```

## Usage

To run the C++ web app, use the following command:

   ```bash
   streamlit run app.py
   ```

This will start the Streamlit app locally, and you can access it in your web browser.