import streamlit as st
‎import random
‎
‎st.set_page_config(page_title="Wingo Predictor", layout="centered")
‎
# ‎Custom CSS for styling
‎st.markdown("""
‎    <style>
‎        body {
‎            background-color: #f0f2f6;
‎        }
‎        .main {
‎            background-color: white;
‎            padding: 30px;
‎            border-radius: 12px;
‎            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
‎        }
‎        .stButton > button {
‎            background-color: #FF4B4B;
‎            color: white;
‎            font-size: 18px;
‎            border-radius: 10px;
‎            height: 3em;
‎            width: 100%;
‎            transition: 0.3s;
‎        }
‎        .stButton > button:hover {
‎            background-color: #FF3333;
‎        }
‎    </style>
‎""", unsafe_allow_html=True)
‎
‎st.title("🔮 Wingo Predictor")
‎st.markdown("<h5 style='text-align: center; color: grey;'>AI se paayen color prediction ka idea — bas 3 number daalein!</h5>", unsafe_allow_html=True)
‎
‎def get_color(number):
‎    if number in [1, 3, 7, 9]:
‎        return "Red"
‎    elif number in [0, 2, 4, 6, 8]:
‎        return "Green"
‎    elif number == 5:
‎return "Violet"
‎
‎col1, col2, col3 = st.columns(3)
‎with col1:
‎    n1 = st.number_input("Number 1", 0, 9, step=1)
‎with col2:
‎    n2 = st.number_input("Number 2", 0, 9, step=1)
‎with col3:
‎    n3 = st.number_input("Number 3", 0, 9, step=1)
‎
‎if 'history' not in st.session_state:
‎    st.session_state.history = []
‎
‎if st.button("🔮 Predict"):
‎    colors = [get_color(n) for n in [n1, n2, n3]]
‎    prediction = random.choice(["Red", "Green", "Violet"])
‎    st.session_state.history.append((colors, prediction))
‎
‎    st.success(f"Prediction: {prediction}")
‎    st.info(f"Pattern: {colors}")
‎
‎if st.session_state.history:
‎    st.subheader("📜 Previous Predictions:")
‎    for idx, (pattern, result) in enumerate(reversed(st.session_state.history[-5:]), 1):
‎        st.write(f"{idx}. Pattern: {pattern} → Prediction: {result}")
