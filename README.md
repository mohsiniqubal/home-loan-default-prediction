# Home Loan Default Risk Prediction System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## Live Demo

https://home-loan-default-prediction-bysv2vz6iaqz9sjrrtyryn.streamlit.app/

---

## About the Project

Home Loan Default Risk Prediction System is a Machine Learning-based banking risk assessment application designed to predict the probability of a borrower defaulting on a home loan.

The project helps financial institutions identify high-risk applicants before loan approval, enabling better risk management and more informed lending decisions.

The application provides both individual customer prediction and bulk prediction through CSV file uploads.

---

## How it Works

* Applicant information is collected through an interactive web interface
* Data is preprocessed and transformed into a machine-learning-ready format
* The trained XGBoost model evaluates the applicant profile
* Default probability is calculated
* The system classifies the applicant as Low Risk or High Risk
* Results are displayed instantly through the Streamlit dashboard

---

## 📊 Features Used

* Total Income
* Credit Amount
* Annuity Amount
* Days Birth
* Days Employed
* Gender
* Education Type
* Family Status
* Number of Children
* Family Members
* Car Ownership Status

---

## Model Details

The final model used is **XGBoost Classifier**.

Several machine learning models were trained and compared, including:

* Logistic Regression
* Decision Tree
* Random Forest
* Naive Bayes
* Artificial Neural Network (ANN)
* XGBoost

Based on ROC-AUC score and overall performance, XGBoost was selected as the final model.

---

## Evaluation Metrics

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

ROC-AUC was used as the primary evaluation metric because the dataset contains class imbalance and requires effective risk discrimination.

---

## Application Features

### Secure Login System

* User authentication before accessing prediction modules

### Single Prediction

* Predict default probability for an individual applicant

### Bulk Prediction

* Upload CSV files
* Predict multiple applicants at once
* Download prediction results

### Risk Assessment Dashboard

* Default Probability (%)
* High Risk / Low Risk Classification
* Real-time Results

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Imbalanced-Learn (SMOTE)
* Joblib
* Streamlit

---

## Run Locally

```bash
git clone https://github.com/mohsiniqubal/home-loan-default-prediction.git

cd home-loan-default-prediction

pip install -r requirements.txt

streamlit run app.py
```

---

## Deployment

The application is deployed using **Streamlit Community Cloud** and can be accessed through any web browser without local installation.

---

## Project Highlights

* End-to-End Machine Learning Pipeline
* Banking Risk Assessment System
* Single and Bulk Prediction Modules
* User Authentication
* Interactive Streamlit Dashboard
* Real-Time Default Risk Prediction
* Industry-Oriented Financial Analytics Project

---

## Project Structure

```text
home-loan-default-prediction
│
├── app.py
├── best_home_loan_model.pkl
├── feature_columns.pkl
├── requirements.txt
├── sample_bulk_prediction.csv
└── README.md
```

---

## Academic Information

**Degree:** Master of Computer Applications (MCA)

**University:** Tezpur University


---

## Disclaimer

This system provides predictions based on historical data and machine learning algorithms. The results should be used as a decision-support tool and not as the sole basis for financial decisions.

---

## 👨‍💻 Author

### Mohsin Iqubal

🔗 LinkedIn: https://www.linkedin.com/in/mohsin-iqubal-805145129/

🔗 GitHub: https://github.com/mohsiniqubal

---

⭐ If you found this project useful, consider giving the repository a star.
