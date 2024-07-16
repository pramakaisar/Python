import streamlit as st

st.title("UML Diagram Generator")

# Get user code input
user_code = st.text_area("Enter your code here", height=400)

if st.button(label="Generate ERD Diagram"):
  if user_code:
    
  else:
    st.warning("Enter your code before generating the UML diagram.")
