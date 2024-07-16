from openai import OpenAI
import streamlit as st
client= OpenAI(api_key=st.secrets['OpenAI_key'])

def generate_story(string):
  prompt = f'Write an ispiring story about {string}'
  story_response = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[{
          "role": 'system',
          "content": """You are a bestseller story writer.
          You will take user's prompt and generate a 1000 words short story for adults age 20-30"""
          },
          {
              "role": "user",
              "content": f'{prompt}',

          }],
      max_tokens = 400,
      temperature= 0.8
  )

  story = story_response.choices[0].message.content
  return story

def design_image_prompt(story):
  design_response = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=[{
          "role": 'system',
          "content": f"""Based on the story given.You will design a detailed image prompt for the cover image
          of this story.THe image prompt should include the theme of the story with relevant color,
          suitable for adults.
          The output should be within 100 characters.

          Here is the story:
          {story}"""
          },
          {
              "role": "user",
              "content": f'{story}',

          }],
      max_tokens = 400,
      temperature= 0.8
  )
  design_prompt = design_response.choices[0].message.content
  return design_prompt

def create_image(design_prompt):
  cover_response=client.images.generate(
      model='dall-e-2',
      prompt = f"{design_prompt} in anime style",
      size = "256x256",
      quality = 'standard',
      n=1
  )
  image_url = cover_response.data[0].url
  return image_url

def convert_code_to_dbml(code):
  dbml_code = client.chat.completions.create(
      model='gpt-4',
      messages=[{
          "role": 'system',
          "content": """Based on the code given by the users, you will convert it to a DBML.
          
The output format should be like this:
```DBML
{insert dblm_code here}
```"""
          },
          {
              "role": "user",
              "content": f'''Please convert this code into a DBML. Just give the DBML output
Here is the code
```
{code}
```''',

          }],
      temperature= 0.8
  )
  dbml_code = dbml_code.choices[0].message.content
  return dbml_code


