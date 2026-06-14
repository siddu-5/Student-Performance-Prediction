import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

model=pickle.load(open("models/student_model.pkl", "rb"))

st.title("🎓 Student Performance Prediction System")
st.markdown(
    "Predict a student's final grade (G3) using Machine Learning."
)
st.divider()
studytime=st.slider(
    "Study Time (1-4)",
    min_value=1,
    max_value=4,
    value=2
)
failures=st.number_input(
    "Past Failures",
    min_value=0,
    max_value=10,
    value=0
)
absences=st.number_input(
    "Absences",
    min_value=0,
    max_value=100,
    value=0
)
g1=st.number_input(
    "G1 Grade",
    min_value=0,
    max_value=20,
    value=10
)
g2=st.number_input(
    "G2 Grade",
    min_value=0,
    max_value=20,
    value=10
)

if st.button("Predict Final Grade"):
    input_df=pd.DataFrame({
        "studytime": [studytime],
        "failures": [failures],
        "absences": [absences],
        "G1": [g1],
        "G2": [g2]
    })
    prediction=model.predict(input_df)
    st.success(
        f"Predicted Final Grade (G3): {prediction[0]:.2f}"
    )
    
    if prediction[0]>=16:
        st.balloons()
        st.info("Excellent Performance Expected 🌟")
    elif prediction[0]>=10:
        st.info("Good Performance Expected 👍")
    else:
        st.warning("Student may require additional academic support 📚")
st.divider()
st.caption(
    "Built using Python, Pandas, Scikit-Learn, and Streamlit"
)