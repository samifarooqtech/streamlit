from gradio_client import Client, handle_file
import streamlit as st
import os
import shutil

def run():
    # Set up the client for Hugging Face background removal
    client = Client("not-lain/background-removal")

    # Create a directory to save images
    save_dir = "images"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Streamlit app layout with style
    st.markdown(
        """
        <style>
        .css-1d391kg {
            background-color: #f5f5f5 !important;
        }
        .title-text {
            color: #2E86C1;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .instruction-text {
            font-size: 18px;
            color: #212F3D;
            text-align: center;
        }
        .uploaded-img {
            text-align: center;
        }
        .footer-text {
            text-align: center;
            margin-top: 50px;
            font-size: 16px;
            color: #AEB6BF;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Title and instructions with emoji
    st.markdown("<h1 class='title-text'>🖼️ AI-Powered Background Removal Tool</h1>", unsafe_allow_html=True)
    st.markdown("<p class='instruction-text'>Upload your image, remove the background with a single click, and download the result! 🚀</p>", unsafe_allow_html=True)

    # File uploader for the image
    uploaded_file = st.file_uploader("🎯 Choose an image to upload:", type=["png", "jpg", "jpeg", "webp"])

    # Always display "Remove Background" button and progress above the image
    if uploaded_file is not None:
        # Save the uploaded image
        input_image_path = os.path.join(save_dir, uploaded_file.name)
        
        with open(input_image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Add the "Remove Background" button and loading spinner above the image
        if st.button("💡 Remove Background"):
            with st.spinner("Processing... Please wait"):
                # Call Hugging Face API to remove the background
                result = client.predict(
                    image=handle_file(input_image_path),
                    api_name="/image"
                )
                
                # Extract the path of the image with background removed
                image_path = result[0]
                output_image_path = os.path.join(save_dir, "output_" + uploaded_file.name)
                
                # Move the generated image to the desired directory
                shutil.move(image_path, output_image_path)
                
                # Replace the old image with the new one (with background removed)
                input_image_path = output_image_path
                
            # Display success message
            st.success(f"🎉 Background removed successfully! Scroll down a little bit :)")

        # Display the uploaded image or the image with background removed
        st.image(input_image_path, caption="🔍 Image with Background Removed. ", use_column_width=True)

        # Provide download link for the processed image
        with open(input_image_path, "rb") as file:
            st.download_button(
                label="📥 Download Image",
                data=file,
                file_name="background_removed_" + uploaded_file.name,
                mime="image/webp"
            )

    # Footer for additional styling and spacing
    st.markdown("<p class='footer-text'>Made with ❤️ using Hugging Face & Streamlit</p>", unsafe_allow_html=True)
