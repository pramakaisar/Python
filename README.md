# Story Generator with Image

This project is a simple web application that allows users to generate a story based on a given topic and creates an image to visually represent the story. The application uses Streamlit for the web interface and three utility functions (`generate_story`, `design_image_prompt`, and `create_image`) to handle the core functionality.

## Prerequisites

- Python 3.x
- Streamlit
- `utils.py` file containing the functions: `generate_story`, `design_image_prompt`, and `create_image`

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python installed on your machine.
3. Install Streamlit using pip:

   ```sh
   pip install streamlit
   ```

4. Ensure the `utils.py` file is in the same directory as the script.

## Usage

1. Open a terminal and navigate to the directory containing the script.
2. Run the Streamlit app:

   ```sh
   streamlit run <script_name>.py
   ```

   Replace `<script_name>` with the name of your script file.

3. The application will open in a web browser.

## Application Workflow

1. **Title**: The app displays the title "Story Generator with Image" at the top of the page.
2. **User Input**: Users enter a topic for their story in a text input box.
3. **Generate Story Button**: When the "Generate Story" button is clicked:
   - The app checks if the user has entered a valid topic.
   - If a valid topic is provided:
     1. The `generate_story` function creates a story based on the user input.
     2. The `design_image_prompt` function generates an image prompt from the story.
     3. The `create_image` function creates an image based on the image prompt and returns the image URL.
     4. The generated image and story are displayed on the page.
   - If no topic is provided, the app shows a warning message requesting the user to enter a valid topic.

## Utility Functions

- `generate_story(topic)`: Generates a story based on the provided topic.
- `design_image_prompt(story)`: Designs an image prompt from the generated story.
- `create_image(image_prompt)`: Creates an image based on the image prompt and returns the URL of the generated image.

## Notes

- Ensure the `utils.py` file contains the correct implementation of the required functions.
- The `create_image` function should handle any API calls or image generation logic as needed.

## Example

Here is an example of how the application might be used:

1. The user enters the topic "A day in the life of a dragon".
2. The user clicks the "Generate Story" button.
3. The application generates a story about a dragon's daily life.
4. An image representing the story is created and displayed along with the story and the image prompt used to create it.

Enjoy creating stories with accompanying images!
