import streamlit as st

st.title("BMI Calculator")

## Input fields
col1, col2 = st.columns(2)

name = col1.text_input("Enter your name:").strip().title()
age = col1.number_input("Enter your age:", min_value=0, step=1)
weight = col2.number_input("Enter your weight (pounds):", min_value=1, step=1)
height = col2.number_input("Enter your height (inches):", min_value=1.0, step=0.1)
bmi = st.button("Calculate BMI")


## Calculate BMI function
bmi = (weight * 703) / (height ** 2)


# Display BMI Report
st.write("\n")
st.write(" ## BMI SCORE")
st.write(f"Hello {name}, your BMI score is {bmi:.2f}")



# Display BMI Category based on calculated BMI
st.write("\n")
st.write(" ## BMI REPORT")
if bmi <= 18.5:
    st.write("Underweight -- You need to eat more")
elif 18.5 < bmi <= 24.9:
    st.write("Normal weight -- Good job, keep it up")
elif 25.0 <= bmi <= 29.9:
    st.write("Overweight -- Time to start working out")
elif 30.0 <= bmi <= 34.9:
    st.write("Obesity Class I -- Consult a doctor")
elif 35.0 <= bmi <= 39.9:
    st.write("Obesity CLass II -- Seek medical advice urgently")
else:
    st.write("Obesity Class III -- You need immediate medical attention else you will get too fat")



## Display BMI Categories
st.write("\n")
st.write(" ### Categories")
st.write(" Underweight: BMI less than 18.5")
st.write(" Normal weight: BMI is 18.5 to 24.9")
st.write(" Overweight: BMI is 25 to 29.9")
st.write(" Obesity Class I: BMI is 30 to 34.9")
st.write(" Obesity Class II: BMI is 35 to 39.9")
st.write(" Obesity Class III: BMI is 40 or more")
st.write("\n")
st.markdown("<p style='color:red;'> Note: This is a simple BMI calculator and should " \
"not replace professional medical advice.</p>", unsafe_allow_html=True)



if st.button("Reset"):
    pass # Streamlit automatially resets inputs on rerun

if st.button("About"):
    st.info("This BMI Calculator was dveloped using Streamlit. It helps you calculate your Body Mass Index (bmi) based" \
    "on your weight and height, and provides insights into your health status.")


if st.button("Contact"):
    st.info("For any inquiries or feedback, please contact us at richardsyeb23@gmail.com")