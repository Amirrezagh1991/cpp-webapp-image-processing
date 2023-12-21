import streamlit as st
import subprocess
import os


def main():
    # Setting page layout
    st.set_page_config(
        page_title="Image Processing",
        page_icon="👁️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Image Processing with C++ Backend")

    # Upload an image file
    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    # Dropdown for processing options
    option = st.sidebar.selectbox("Choose a processing option", ["Convert to Grayscale", "Canny Edge Detection"])

    col1, col2 = st.columns(2)

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with open("input_image.jpg", "wb") as f:
            f.write(uploaded_file.read())

        if option == "Convert to Grayscale":
            # Call the C++ backend for grayscale conversion
            st.text("Converting the image to grayscale...")
            subprocess.run(["./build/image_processing", "input_image.jpg", "output_image.jpg", "grayscale"])
        elif option == "Canny Edge Detection":
            # Call the C++ backend for Canny edge detection
            st.text("Performing Canny edge detection on the image...")
            subprocess.run(["./build/image_processing", "input_image.jpg", "output_image.jpg", "canny"])

        with col1:
            st.image("input_image.jpg", caption="Uploaded Image", use_column_width=True)
        with col2:
            st.image("output_image.jpg", caption="Processed Image", use_column_width=True)

        # # Clean up
        # os.remove("input_image.jpg")
        # os.remove("output_image.jpg")


if __name__ == '__main__':
    main()