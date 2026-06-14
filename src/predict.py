import pickle
import pandas as pd

model=pickle.load(open("models/student_model.pkl","rb"))

print("Enter Student Details")
studytime=int(input("Study Time (1-4): "))
failures=int(input("Past Failures: "))
absences=int(input("Absences: "))
g1=int(input("G1 Grade: "))
g2=int(input("G2 Grade: "))

input_df=pd.DataFrame({
    "studytime":[studytime],
    "failures":[failures],
    "absences":[absences],
    "G1":[g1],
    "G2":[g2]
})

prediction=model.predict(input_df)
print(f"\nPredicted Final Grade (G3): {prediction[0]:.2f}")