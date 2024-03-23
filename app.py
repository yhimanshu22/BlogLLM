import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_keys,openai_api_keys
from openai import OpenAI
client = OpenAI(api_key=openai_api_keys)

genai.configure(api_key=google_gemini_api_keys)

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

st.set_page_config(layout="wide")

# Title of our app
st.title('BlogLLM: Your AI writer')

# Create a subheader
#st.subheader('Enter the text you want to generate a blog post about')

# Define the blog text
blog_text = """
The Rise of the Machines: Exploring the Effects of Generative AI

The realm of artificial intelligence (AI) is rapidly evolving, and at the forefront of this progress stands **generative AI**. This technology, capable of producing entirely new content like text, images, and even music, is blurring the lines between human and machine creativity, raising fascinating questions about the future of art, innovation, and the very essence of human expression.

One of the most captivating aspects of generative AI is its potential to unlock **artificial creativity**. Imagine algorithms composing symphonies, painting breathtaking landscapes, or writing captivating novels. This prospect, once relegated to science fiction, is now within our grasp. Tools like DALL-E 2 and GPT-3 are already demonstrating the ability to generate stunning visuals and compelling narratives, pushing the boundaries of what we thought machines were capable of.

However, with this burgeoning technology comes a slew of **ethical implications**. Concerns around authorship, authenticity, and the potential for misuse are at the forefront of the discussion. If AI can create art indistinguishable from human-made works, how do we define artistic ownership? Could this technology be used to spread misinformation or create harmful content? Navigating these ethical dilemmas will be crucial in ensuring responsible development and deployment of generative AI.

Despite the challenges, the potential benefits of this **technology innovation** are undeniable. Generative AI has the potential to revolutionize numerous industries. In healthcare, it could accelerate drug discovery and personalize treatment plans. In education, it could create customized learning experiences and automate tedious tasks like grading. The possibilities are endless, and the impact on society could be profound.

However, the widespread adoption of generative AI also raises concerns about its **impact on society**. Will this technology displace human workers, exacerbating unemployment? Could it widen the digital divide and further marginalize certain groups? It's crucial to address these concerns proactively and ensure that the benefits of generative AI are distributed equitably.

As with any powerful tool, the impact of generative AI will ultimately depend on how we choose to use it. By fostering open dialogue, engaging in ethical development practices, and prioritizing the well-being of society, we can harness the power of this technology to foster innovation, enhance creativity, and ultimately create a better future for all.

The rise of generative AI marks a pivotal moment in our history. It compels us to re-evaluate what it means to be human, to create, and to express ourselves. By approaching this technology with caution, responsibility, and a commitment to ethical principles, we can navigate the uncharted waters of artificial creativity and ensure that it serves as a force for good in our world.
"""

# Sidebar for user input
with st.sidebar:
    st.title('Input your blog title')
    st.subheader('Enter the title of your blog post')
    blog_title = st.text_input('Title')
    keywords = st.text_area('Keywords (separated by commas)')
    num_words = st.slider('Number of Words', min_value=250, max_value=1000, step=250)
    num_images = st.number_input('Number of Images', min_value=1, max_value=2, step=1)

    # Start a conversation with the model
    prompt =[ f"Generate a blog post titled '{blog_title}' with the following keywords: {keywords}. The blog should be {num_words} words long and include {num_images} images. Here is the text to generate the blog post: {blog_text}"]
 
    submit_button = st.button('Generate Blog')

# Generate the blog post upon button click
if submit_button:
   # st.image('https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif', use_column_width=True)
    
    response = model.generate_content(prompt)

   # Generate a single image using DALL-E model
   # image_response = client.images.generate(
   #     model="dall-e-3",
    #    prompt=f"Generate an image that represents the blog post titled '{blog_title}' with the following keywords: {keywords}.",
     #   size="1024x1024",
     #   quality="standard",
      #  n=1,
    #)

    # Get the URL of the generated image
   # image_url = image_response.data[0].url

    # Display the image
   # st.image(image_url)

    # Display the generated blog post
   # st.title('YOUR BLOG POST:')
    st.write(response.text)