import pandas as pd
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv("data/student-por.csv")
le=LabelEncoder()
for col in df.columns:
    if df[col].dtype=="object":
        df[col]=le.fit_transform(df[col])
df.to_csv("data/processed_student_data.csv",index=False)
print(df.columns.tolist())
print(df.shape)