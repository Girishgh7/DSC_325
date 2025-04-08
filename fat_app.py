import streamlit as st

# Function to predict diabetes with a sassy twist
def predict_diabetes(bmi):
    if bmi >= 25:
        return "🔥 Uh-oh, sugar! Your BMI says you're on the risky side. Time to sip on some water, not soda. Consult a doc, stat!"
    else:
        return "🎉 You're rocking that healthy vibe! Your BMI is chill. Keep slaying with those veggies and vibes."

# Streamlit app
st.title("💃 The Sassy Diabetes Risk Checker 🍩")
st.write("Hey, fabulous! Enter your stats and let’s spill the tea on your diabetes risk. ☕")

# Input fields with some flair
weight = st.number_input("💪 Enter your weight (kg):", min_value=30, max_value=200, help="Don’t worry, we won’t judge your pizza nights.")
height = st.number_input("📏 Enter your height (cm):", min_value=100, max_value=250, help="Height check—no need to be tall to be fabulous!")

# Calculate BMI with style
if height and weight:
    bmi = weight / ((height / 100) ** 2)
    st.write(f"💥 Your BMI is: **{bmi:.2f}**")
    st.write(predict_diabetes(bmi))
else:
    st.write("Oops! Looks like you forgot to fill in the details. Don’t worry, we’ve all been there. 😜")
