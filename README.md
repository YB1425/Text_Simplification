# Text Simplification with Hugging Face and Gradio

## Overview

This project demonstrates how to integrate Hugging Face's text-to-text pipeline with Gradio to create an interactive web application for text simplification. The application allows users to input complex text and receive a simplified version using the `t5-base` model from Hugging Face.

This project was made to assist people who are weak in English or those who have difficulties reading long texts, providing them with a tool to make complex information more accessible and easier to understand.

## Project Structure

The project includes the following files:

- `app.py`: The main Python script that defines the Gradio interface and integrates the Hugging Face text-to-text pipeline for text simplification.
- `1_simple_pipeline_notebook.ipynb`: Demonstrates how the Hugging Face text-to-text pipeline works without Gradio.
- `2_gradio_example_notebook.ipynb`: Showcases various Gradio components with hardcoded data.

## Features

- **Text Simplification**: Utilizes Hugging Face’s `t5-base` model to transform complex text into simpler forms.
- **Interactive GUI**: Built using Gradio to offer an intuitive user interface.
- **Customizable Output Length**: Users can set the maximum length of the simplified text using a slider.

## How It Works

1. **Loading the Model**: The `t5-base` model is loaded using Hugging Face's `pipeline` for text-to-text generation.
2. **Text Simplification Function**: The `text_simplifying` function processes the input text and a maximum length parameter through the model to generate simplified text.
3. **Gradio Interface**: Provides an interactive GUI where users can input text and adjust the maximum length for the output.

## Running the Code

### From the Hugging Face Space

1. **Access the Application**: Go to [Text Simplification on Hugging Face](https://huggingface.co/spaces/YB1425/Text_Simplification).
2. **Enter Text**: In the "Enter complex text here..." field, input the text you want to simplify.
3. **Set Maximum Length**: Use the slider to select the maximum length for the simplified text.
4. **View Output**: The simplified text will appear in the output area below.

### Video Description of ProjectGo to [Link](https://youtu.be/9kUUXbstXG0).

### From PyCharm

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YB1425/Text_Simplification
