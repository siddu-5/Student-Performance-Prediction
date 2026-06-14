import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/processed_student_data.csv")

plt.figure(figsize=(8,5))
plt.hist(df["G3"], bins=10)
plt.title("Final Grade Distribution")
plt.xlabel("G3")
plt.ylabel("Number of Students")
plt.savefig("grade_distribution.png")
plt.show()