import os
import shutil
import streamlit as st
from gradio_client import Client

def run():  # Define the run function
    # Define the directory where you want to save the image
    save_dir = "images"
 
    # Create the directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Initialize the client
    client = Client("black-forest-labs/FLUX.1-schnell")

    # Streamlit layout with sidebar for input and main area for image display
    st.sidebar.title("Image Generation Prompt")
    prompt = st.sidebar.text_area("Enter your prompt:", "")

    generate_image = st.sidebar.button("Generate Image")

    if generate_image:
        if prompt:
            # Generate the image using the prompt provided by the user
            result = client.predict(
                prompt=prompt,
                seed=0,
                randomize_seed=True,
                width=1024,
                height=1024,
                num_inference_steps=4,
                api_name="/infer"
            )
            # Extract the file path from the result tuple
            image_path = result[0]  # This is the path to the generated image

            # Define the destination path where you want to save the image
            save_path = os.path.join(save_dir, "generated_image.webp")

            # Move the image from the temporary location to the desired directory
            shutil.move(image_path, save_path)

            # Display the image in Streamlit
            st.image(save_path, caption="Generated Image", use_column_width=True)

            # Provide download link
            with open(save_path, "rb") as file:
                st.download_button(
                    label="Download Image",
                    data=file,
                    file_name="generated_image.webp",
                    mime="image/webp"
                )

            st.success(f"Image generated and saved at: {save_path}")
        else:
            st.error("Please enter a prompt to generate the image.")
