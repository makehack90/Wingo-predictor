import streamlit as st
import random

st.set_page_config(page_title="Wingo Predictor", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .main {
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
        }
        .stButton > button {
            background-color: #FF4B4B;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #FF3333;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔮 Wingo Predictor")
st.markdown("<h5 style='text-align: center; color: grey;'>AI se paayen color prediction ka idea — bas 3 number daalein!</h5>", unsafe_allow_html=True)

def get_color(number):
    if number in [1, 3, 7, 9]:
        return "Red"
    elif number in [0, 2, 4, 6, 8]:
        return "Green"
    elif number == 5:‎
