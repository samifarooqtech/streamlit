import streamlit as st
import app1  # Import App 1 (Image Generation)
import app2  # Import App 2 (Background Removal)

# Title and Instructions
st.title("AI-Powered Tools")
st.markdown("### Welcome to the AI Image Generation and Background Removal Services.")
st.markdown("""
Here’s what you can do with our AI-powered tools:
- **🔹 Image Generation**: Provide a text prompt, and our AI will generate an image based on your description.
- **🔹 Background Removal**: Upload an image, and our AI will automatically remove the background for you.
- **🔹 Future Tools**: Stay tuned for more exciting features coming soon!
""")

# Scrollable Terms and Conditions
st.markdown("### Terms and Conditions")

scrollable_terms = """
<div style='height:300px; overflow-y:scroll; border:1px solid #ccc; padding: 10px;'>
    <p><strong>1. Use of Service</strong>: This service provides AI-based image generation and background removal tools. You are responsible for the images and prompts you upload and create.</p>
    <p><strong>2. License</strong>: The AI models used in this service (including models hosted on Hugging Face and Gradio) are open-source, but their use may be subject to certain licensing restrictions. You must comply with the model’s license, which may include non-commercial clauses.</p>
    <p><strong>3. Copyright and Intellectual Property</strong>: Any content generated through this service may be subject to copyright and intellectual property laws. You agree not to use the generated content in any way that infringes on the intellectual property rights of others.</p>
    <p><strong>4. Liability</strong>: The service is provided "as is" without any warranties. We are not responsible for any damages, legal or otherwise, that result from the use of the service.</p>
    <p><strong>5. User-Generated Content</strong>: You agree not to upload any content that is illegal, harmful, or violates any laws or the rights of others.</p>
    <p><strong>6. Indemnification</strong>: You agree to indemnify and hold harmless the service provider from any claims or liabilities that arise from your use of the service.</p>
</div>
"""
st.markdown(scrollable_terms, unsafe_allow_html=True)

# Checkbox for agreeing to terms
agree_to_terms = st.checkbox("I have read and agree to the terms and conditions.")

# Only allow app access if terms are agreed to
if agree_to_terms:
    st.markdown("### Available AI Tools")

    # Bullet points for Image Generation and Background Removal
    st.markdown("""
    - **🔹 Image Generation**: Use AI to generate images based on the prompts you provide.
    - **🔹 Background Removal**: Automatically remove the background from uploaded images using AI.
    """)
    
    # Sidebar for navigation between apps
    st.sidebar.title("Choose an App")
    app_choice = st.sidebar.radio("Select a Service", ["Image Generation", "Background Removal", "Future Program (Coming Soon)"])

    # Routing based on user selection
    if app_choice == "Image Generation":
        app1.run()  # Call the run function from app1.py
    elif app_choice == "Background Removal":
        app2.run()  # Call the run function from app2.py
    elif app_choice == "Future Program (Coming Soon)":
        st.info("This feature is coming soon. Stay tuned!")
else:
    st.warning("You must agree to the terms and conditions to use the application.")
