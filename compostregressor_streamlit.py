import streamlit as st
import joblib
import numpy as np
from PIL import Image

# Load the trained model
model = joblib.load('dt_regressor.pkl')

# Define the Streamlit app
st.set_page_config(page_title="NPK Ratio Predictor", layout="wide", initial_sidebar_state="expanded")

# Title and description with company logo
col1, col2 = st.columns([1, 1])  # Adjust the ratio as needed

with col1:
    st.title("NPK Ratio Predictor")

with col2:
    st.image("logo.png")

st.markdown("""
This application predicts the NPK Ratio based on user inputs for various environmental and soil factors.
""")

# Input fields
st.sidebar.header("Input Features")

phosphorous = st.sidebar.number_input('Phosphorous', min_value=0.0, max_value=100.0, value=10.0)
nitrogen = st.sidebar.number_input('Nitrogen', min_value=0.0, max_value=100.0, value=10.0)
potassium = st.sidebar.number_input('Potassium', min_value=0.0, max_value=100.0, value=10.0)
temp = st.sidebar.number_input('Temperature (°C)', min_value=-10.0, max_value=50.0, value=25.0)
hum = st.sidebar.number_input('Humidity (%)', min_value=0.0, max_value=100.0, value=50.0)
heat = st.sidebar.number_input('Heat Index', min_value=-10.0, max_value=50.0, value=25.0)
soil_moisture = st.sidebar.number_input('Soil Moisture (%)', min_value=0.0, max_value=100.0, value=50.0)
hour = st.sidebar.number_input('Hour', min_value=0, max_value=23, value=12)
minute = st.sidebar.number_input('Minute', min_value=0, max_value=59, value=30)

# Prediction button with animation
if st.sidebar.button('Predict NPK Ratio'):
    with st.spinner('Predicting...'):
        input_data = np.array([[phosphorous, nitrogen, potassium, temp, hum, heat, soil_moisture, hour, minute]])
        prediction = model.predict(input_data)
        st.success(f"Predicted NPK Ratio: {prediction[0]:.2f}")
        st.markdown(f"""
        The predicted NPK ratio is {prediction[0]:.2f}. This ratio helps to understand the nutrient composition in the soil,
        which is crucial for optimal plant growth.
        """)
        
        st.snow()

# Additional content
st.markdown("""
### How It Works
Input the environmental and soil factors in the sidebar to predict the NPK ratio.
""")


# Load and display the GIF, centered and enlarged
st.image("https://sapro.moderncampus.com/hs-fs/hubfs/Destiny/Imported_Blog_Media/9139e7423bfe7bbd967f3cfaeaeed635_original-Apr-05-2022-03-10-30-13-PM.gif?width=680&height=383&name=9139e7423bfe7bbd967f3cfaeaeed635_original-Apr-05-2022-03-10-30-13-PM.gif", width=900, caption="Soil Analysis GIF", use_column_width=True)

# Add some CSS for better visuals
st.markdown("""
<style>
body {
    font-family: Arial, sans-serif;
}

.sidebar .sidebar-content {
    background-color: #f0f0f5;
}

.sidebar .sidebar-content h2 {
    color: #333;
}

.stButton button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 24px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    transition-duration: 0.4s;
}

.stButton button:hover {
    background-color: white;
    color: black;
    border: 2px solid #4CAF50;
}
</style>
""", unsafe_allow_html=True)