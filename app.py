import streamlit as st
import pickle
import pandas as pd

model=pickle.load(open("models/student_model.pkl","rb"))
st.title("🎓 Student Performance Prediction")
studytime=st.slider("Study Time",1,4,2)
failures=st.number_input("Past Failures",0,10,0)
absences=st.number_input("Absences",0,100,0)
g1=st.number_input("G1 Grade",0,20,10)
g2=st.number_input("G2 Grade",0,20,10)

if st.button("Predict Final Grade"):
    input_df=pd.DataFrame({
        "studytime":[studytime],
        "failures":[failures],
        "absences":[absences],
        "G1":[g1],
        "G2":[g2]
    })
    prediction=model.predict(input_df)
    st.success(f"Predicted Final Grade (G3): {prediction[0]:.2f}")