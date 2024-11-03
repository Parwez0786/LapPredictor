import streamlit as st
import pickle
import numpy as np
import pandas as pd

# import the model
pipe = pd.read_pickle(r"pipe.pkl")
df = pd.read_pickle(r"df.pkl")

# Set page title and favicon
st.set_page_config(
    page_title="LapPricer",
    page_icon="💻",
    layout="wide"
)

# Page Header
st.title("LapPricer-Laptop Price Predictor")
st.write(
    "Welcome to the Laptop Price Predictor. Input the details of the laptop configuration and predict its price!"
)

# Sidebar with additional information
st.sidebar.header("About")
st.sidebar.markdown(
    "This web app predicts the price of laptops based on various features. "
    "Please input the details on the left side, and we'll provide you with the estimated price."
)

# Details about the person who made the project
st.sidebar.markdown("## Made by:")
st.sidebar.markdown("- **Name:** Md Parwez Ansari")
st.sidebar.markdown("- **College:** IIIT Allahabad")
st.sidebar.markdown("- **Enrollment No:** IIT2021113")

# Input Section
with st.form("laptop_form"):
    col1, col2 = st.columns(2)

    # Brand and Laptop Type
    company = col1.selectbox('Brand', df['Company'].unique())
    type = col2.selectbox('Type', df['TypeName'].unique())

    # RAM and Weight
    ram = col1.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = col2.number_input('Weight (kg)', min_value=0.1, max_value=10.0, step=0.1, value=2.0)

    # Touchscreen and IPS
    touchscreen = col1.selectbox('Touchscreen', ['No', 'Yes'])
    ips = col2.selectbox('IPS', ['No', 'Yes'])

    # Screen Size and Resolution
    screen_size = col1.number_input('Screen Size (inches)', min_value=10, max_value=21, value=15)
    resolution = col2.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800',
                                                      '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

    # CPU, HDD, SSD, GPU, OS
    cpu = col1.selectbox('CPU', df['Cpu brand'].unique())
    hdd = col2.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = col1.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
    gpu = col2.selectbox('GPU', df['Gpu brand'].unique())
    os = col1.selectbox('OS', df['os'].unique())

    # Predict Button
    predict_button = col2.form_submit_button('Predict Price')

# User satisfaction feedback
if predict_button:
    # Check if HDD or SSD is set to zero and prompt the user
    if hdd == 0 and ssd == 0:
        st.warning("Please fill in either HDD or SSD value.")
    else:
        # Query and prediction logic
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
        query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

        query = query.reshape(1, 12)
        predicted_price = int(np.exp(pipe.predict(query)[0]))

        # Display Prediction
        st.success(f"The predicted price of this configuration is ₹ {predicted_price}")

        # User satisfaction feedback
        satisfaction = st.selectbox("Are you satisfied with the predicted price?", ["Yes", "No"])

        if satisfaction == "Yes":
            st.success("Thank you!")
        else:
            # Reset values
            st.experimental_rerun()
            
# Add some space
st.write("\n\n")

# Footer with copyright symbol
st.markdown("<hr>", unsafe_allow_html=True)
st.info(
    "Atul B Raj©2023. All rights reserved. | This web app is created for educational purposes."
)
