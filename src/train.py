import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

df=pd.read_csv("data/processed_student_data.csv")

X=df[
    [
        "studytime",
        "failures",
        "absences",
        "G1",
        "G2"
    ]
]
y=df["G3"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr=LinearRegression()
lr.fit(X_train,y_train)
lr_pred=lr.predict(X_test)

print("Linear Regression")
print("MAE:",mean_absolute_error(y_test,lr_pred))
print("R2:",r2_score(y_test,lr_pred))

rf=RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
rf.fit(X_train,y_train)
rf_pred=rf.predict(X_test)

print("\nRandom Forest")
print("MAE:",mean_absolute_error(y_test,rf_pred))
print("R2:",r2_score(y_test,rf_pred))

pickle.dump(
    rf,
    open("models/student_model.pkl","wb")
)

print("\nModel Saved Successfully")