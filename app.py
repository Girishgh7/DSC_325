import streamlit as st
import joblib

# Load trained model and label encoder from predictor.py
MODEL_PATH = "bias_model.pkl"
ENCODER_PATH = "label_encoder.pkl"

@st.cache_resource
def load_model():
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)
    return model, label_encoder

model, label_encoder = load_model()
st.title("⚖️ Bias Finder")
st.markdown(
    """🎭 **Welcome to the Political Bias Predictor!** 🗞️  
    Ever wondered if a news article leans left, right, or stays neutral? 🧐  
    Just drop the title and text below, and let our model do the guesswork! 🚀"""
)
st.sidebar.title("📌 About the Developer")
st.sidebar.markdown(
    """
    **👤 Developed by:** Girish G Hegde 
    **📧 Contact:** girishgh22@example.com  
    **🌍 GitHub:** [GitHubProfile](https://github.com/Girishgh7)
    """
)

st.sidebar.title("⚖️ Terms & Conditions")
st.sidebar.markdown(
    """
    - This tool predicts political bias based on text input.  
    - Predictions may not always be accurate.  
    - Use at your own discretion.
    """
)
st.sidebar.title("📅About the Database")
st.sidebar.markdown(
    """
    -This Dataset was taken from Kaggle 
    
    -🖇️Link:[Dataset](https://www.kaggle.com/datasets/mayobanexsantana/political-bias)
    """
)

# Initialize 
if "title" not in st.session_state:
    st.session_state.title = ""
if "text" not in st.session_state:
    st.session_state.text = ""


title = st.text_input("Enter News Title:", st.session_state.title)
text = st.text_area("Enter News Text:", st.session_state.text)

if st.button("Predict Bias"):
    if title.strip() == "" and text.strip() == "":
        st.warning("Please enter at least a title or text.")
    else:
        combined_text = title + " " + text
        prediction = model.predict([combined_text])[0]
        predicted_bias = label_encoder.inverse_transform([prediction])[0]
        
        st.success(f"Predicted Bias: {predicted_bias}")

if st.button("Clear"):
    st.session_state.title = ""
    st.session_state.text = ""
    st.rerun()

