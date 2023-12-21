from setuptools import setup, find_packages

setup(
    name='my_image_processing_app',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'opencv-python-headless',
    ],
)