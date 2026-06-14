import pandas as pd
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv("data/student-por.csv",sep=";")
le=LabelEncoder()
for column in df.columns:
    if df[column].dtype=="object":
        df[column]=le.fit_transform(df[column])
df.to_csv("data/processed_student_data.csv",index=False)
print("Processing completed")
print(df.head())