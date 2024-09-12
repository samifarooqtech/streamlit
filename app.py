import streamlit as st
import app1  # Import App 1
import app2  # Import App 2

# Sidebar for navigation between apps
st.sidebar.title("Choose an App")
app_choice = st.sidebar.radio("Select App", ["Image Generation", "Background Removal"])

# Routing based on user selection
if app_choice == "Image Generation":
    app1.run()  # Call the run function from app1.py
elif app_choice == "Background Removal":
    app2.run()  # Call the run function from app2.py
