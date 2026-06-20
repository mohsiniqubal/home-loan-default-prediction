# 🏦 Home Loan Default Risk Prediction System

A Machine Learning-based Banking Risk Assessment System developed using XGBoost and Streamlit to predict the probability of home loan default. This application helps financial institutions assess loan applicants and identify high-risk borrowers before loan approval.

## 📌 Features

- User Authentication (Login System)
- Single Applicant Loan Default Prediction
- Bulk Prediction using CSV Upload
- Default Probability Score
- High Risk / Low Risk Classification
- Interactive Streamlit Dashboard
- Download Prediction Results
- Machine Learning Model using XGBoost

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Imbalanced-Learn (SMOTE)
- Joblib

## 📊 Input Features

The model uses applicant information such as:

- Total Income
- Credit Amount
- Annuity Amount
- Days Birth
- Days Employed
- Gender
- Education Type
- Family Status
- Number of Children
- Family Members
- Own Car Status

## 🚀 How to Run Locally

### Clone Repository

```bash
git clone https://github.com/mohsiniqubal/home-loan-default-prediction.git
cd home-loan-default-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

## 📂 Project Structure

```text
home-loan-default-prediction/
│
├── app.py
├── best_home_loan_model.pkl
├── feature_columns.pkl
├── requirements.txt
├── sample_bulk_prediction.csv
└── README.md
```

## 📈 Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Feature Engineering
4. Handling Class Imbalance using SMOTE
5. Model Training using XGBoost
6. Model Evaluation
7. Streamlit Deployment

## 🎯 Prediction Output

The system provides:

- Default Probability (%)
- Risk Category
  - Low Risk
  - High Risk
- Bulk Prediction Results

## 📷 Application Screens

- Login Page
- Single Prediction Module
- Prediction Result Dashboard
- Bulk Prediction Module

## 👨‍💻 Author

**Mohsin Iqubal**

- MCA, Tezpur University


LinkedIn:
https://www.linkedin.com/in/mohsin-iqubal-805145129/

GitHub:
https://github.com/mohsiniqubal

## 📄 License

This project is developed for academic and educational purposes.
