from utils import generate_story, design_image_prompt, create_image
import streamlit as st

st.title("Story Generator with Image")
user_input = st.text_input("Enter a topic for your story")

if st.button('Generate Story'):
  if user_input:
    story = generate_story(user_input)
    image_prompt = design_image_prompt(story)
    image_url = create_image(image_prompt)
  
    st.image(image_url)
    st.write(f'story: {story}')
    st.write(f'image prompt: {image_prompt}')
  else:
    st.warning("Please enter a valid topic for your story")