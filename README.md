# ❤️ Heart Disease Prediction using Machine Learning

An end-to-end Machine Learning project that predicts whether a patient is at risk of heart disease using clinical and demographic information. This project demonstrates the complete Data Science workflow—from data preprocessing and exploratory data analysis (EDA) to model training, evaluation, and deployment using **Streamlit**.

---

# 🌐 Live Demo

🚀 **Web Application**  
https://heart-disease-predictionkk.streamlit.app/

💻 **GitHub Repository**  
https://github.com/Kapil80-Khotani/heart-disease-prediction-ml

---

# 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can assist healthcare professionals in making timely decisions and improve patient outcomes.

This project implements a supervised Machine Learning pipeline to classify whether a patient is at risk of heart disease based on various clinical features. Multiple classification algorithms were trained, tuned, and evaluated before selecting the best-performing model for deployment.

---

# ✨ Features

- 📊 Comprehensive Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Preprocessing
- 📌 Missing Value Analysis
- 📈 Outlier Detection
- ⚙️ Feature Engineering
- 🎯 Feature Selection
- 📏 Feature Scaling
- 🤖 Training Multiple Machine Learning Models
- 🔧 Hyperparameter Tuning using GridSearchCV
- 📊 Model Evaluation & Comparison
- 🌐 Interactive Streamlit Web Application
- ⚡ Real-time Heart Disease Prediction

---

# 📊 Dataset

The dataset contains patient medical information, including:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting Electrocardiographic Results
- Maximum Heart Rate Achieved
- Exercise-Induced Angina
- Oldpeak (ST Depression)
- ST Slope
- Number of Major Vessels
- Thalassemia
- Target (Heart Disease)

---

# 🛠️ Tech Stack

### Programming Language

- Python

### Libraries

- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Pickle
- Streamlit

---

# 🤖 Machine Learning Algorithms

The following classification algorithms were trained and evaluated:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest

---

# 🏆 Best Performing Model

After evaluating multiple Machine Learning algorithms, **Support Vector Machine (SVM)** was selected as the final model because of its excellent ability to detect heart disease cases.

## 📈 Model Performance (Test Dataset)

| Metric | Class 0 | Class 1 (Heart Disease) |
|---------|---------|-------------------------|
| Precision | 0.94 | 0.73 |
| Recall | 0.57 | **0.97** |
| F1-Score | 0.71 | 0.83 |

### Overall Performance

- **Accuracy:** **79%**
- **Weighted Precision:** **83%**
- **Weighted Recall:** **79%**
- **Weighted F1-Score:** **78%**

### 🎯 Key Highlight

The **Support Vector Machine (SVM)** achieved a **97% Recall for the Heart Disease class**, meaning it correctly identified **97% of patients with heart disease**. This makes the model particularly useful for medical screening applications where minimizing false negatives is more important than maximizing overall accuracy.

---

# 📈 Machine Learning Workflow

1. Data Collection
2. Data Inspection
3. Exploratory Data Analysis (EDA)
4. Data Cleaning
5. Missing Value Treatment
6. Outlier Detection
7. Feature Engineering
8. Feature Scaling
9. Train-Test Split
10. Model Training
11. Hyperparameter Tuning
12. Model Evaluation
13. Model Comparison
14. Final Model Selection
15. Model Serialization using Pickle
16. Deployment using Streamlit

---

# 📊 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report

---

# 📂 Project Structure

```text
heart-disease-prediction-ml/
│
├── data/
│   └── heart.csv
│
├── models/
│   └── trained_model.sav
│
├── notebook/
│   └── heart-disease-prediction.ipynb
│
├── src/
│   └── heart_disease_prediction.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Kapil80-Khotani/heart-disease-prediction-ml.git
```

### Navigate to the project directory

```bash
cd heart-disease-prediction-ml
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run src/heart_disease_prediction.py
```

---

# 📚 Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering
- Feature Selection
- Machine Learning
- Classification Algorithms
- Hyperparameter Tuning
- Model Evaluation
- Predictive Analytics
- Model Deployment
- Streamlit
- Git & GitHub

---

# 🚀 Future Improvements

- Develop a REST API using Flask or FastAPI
- Dockerize the application
- Deploy on AWS, Azure, or Google Cloud Platform
- Implement CI/CD using GitHub Actions
- Add user authentication
- Integrate a database for storing patient records
- Implement model monitoring and automated retraining

---

# 👨‍💻 Author

**Kapil**

GitHub: https://github.com/Kapil80-Khotani

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Your support motivates me to build more Machine Learning and AI projects.

---

# 📄 Disclaimer

This application is developed for **educational and demonstration purposes only**. It should **not** be used as a substitute for professional medical advice, diagnosis, or treatment.

---

# 📜 License

This project is licensed under the **MIT License**.
