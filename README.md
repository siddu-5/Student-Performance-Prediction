# 🎓 Student Performance Prediction

A Machine Learning project that predicts a student's final grade (G3) based on academic and behavioral factors such as study time, past failures, absences, and previous grades.
The project follows a complete ML workflow including data preprocessing, feature engineering, model training, evaluation, deployment, and real-time prediction through a Streamlit web application.

🌐 Live Demo: https://siddu-5-student-performance-prediction-app-ishw2l.streamlit.app/

---
# 🚀 Technologies Used
* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Matplotlib
* Git & GitHub
---
# ✨ Features
### 📊 Data Preprocessing
* Cleaned and prepared the dataset
* Encoded categorical variables
* Selected relevant features

### 🤖 Machine Learning
* Trained Linear Regression model
* Trained Random Forest Regressor
* Compared model performance

### 📈 Model Evaluation
* Mean Absolute Error (MAE)
* R² Score

### 🌐 Interactive Web Application
* User-friendly Streamlit interface
* Real-time grade prediction
* Instant prediction results
---
# 🏗️ Project Architecture
User Input
↓
Streamlit Interface
↓
Random Forest Model
↓
Prediction Engine
↓
Display Final Grade

---

# 📁 Project Structure
Student-Performance-Prediction/
├── data/
├── models/
├── src/
├── app.py
├── requirements.txt
├── README.md
└── screenshots/

---

# 🎯 Input Features
The model predicts the final grade (G3) using:
* Study Time
* Past Failures
* Absences
* G1 Grade
* G2 Grade

Target Variable:
* G3 (Final Grade)
---
# 📸 Screenshots
### Home Page
<img width="1917" height="1028" alt="image" src="https://github.com/user-attachments/assets/a9a10a11-7440-464e-b853-7e872d2dba80" />

### Prediction Result
<img width="1085" height="858" alt="image" src="https://github.com/user-attachments/assets/3a324807-a568-4756-ade1-b2847543e622" />


---
# 🧠 Machine Learning Workflow
### Step 1: Dataset Collection
Downloaded Student Performance dataset and analyzed available features.
### Step 2: Data Preprocessing
Converted categorical values into numerical representations and prepared the dataset for model training.
### Step 3: Feature Selection
Selected important academic indicators such as study time, failures, absences, G1 and G2 grades.
### Step 4: Model Training
Trained:
* Linear Regression
* Random Forest Regressor
### Step 5: Model Evaluation
Evaluated models using:
* MAE
* R² Score
### Step 6: Deployment
Built a Streamlit web application and deployed it online.

---
# 🎓 What I Learned
Through this project I learned:
* Data preprocessing techniques
* Feature engineering
* Machine Learning model training
* Model evaluation metrics
* Model serialization using Pickle
* Building ML web applications using Streamlit
* Deployment of machine learning applications
* Version control using Git and GitHub
---
# 🔥 Challenges Faced
### Dataset Formatting Issues
Handled CSV parsing and preprocessing challenges while working with the dataset.
### Feature Mismatch During Prediction
Resolved prediction errors by ensuring the same features were used during both training and inference.
### Deployment Issues
Fixed dependency conflicts in requirements.txt and successfully deployed the application using Streamlit Cloud.

---
# 🚀 Future Improvements
* Store prediction history in a database
* Add user authentication
* Support multiple ML models
* Improve UI/UX
* Add advanced analytics dashboard
* Deploy with custom domain
---
# 💻 Installation
Clone the repository:
git clone https://github.com/siddu-5/Student-Performance-Prediction.git
Navigate into the project:
cd Student-Performance-Prediction
Install dependencies:
pip install -r requirements.txt
Run the application:
streamlit run app.py

---


⭐ If you found this project useful, consider giving it a star.
