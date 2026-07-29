import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Home Loan Default Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# PROFESSIONAL UI CSS
# =========================================

st.markdown("""
<style>

/* =========================
MAIN APP
========================= */

.stApp {

    background: linear-gradient(
        to right,
        #EEF2FF,
        #F8FAFC
    );

    color: #111827;
}

/* =========================
SIDEBAR
========================= */

section[data-testid="stSidebar"] {

    background: linear-gradient(
        to bottom,
        #0F172A,
        #1E3A8A
    );
}

section[data-testid="stSidebar"] * {

    color: white !important;
}

/* =========================
MAIN TITLE
========================= */

.title {

    font-size: 42px !important;

    font-weight: 800 !important;

    text-align: center !important;

    color: #1E3A8A !important;

    margin-bottom: 10px !important;

    letter-spacing: 1px !important;

    line-height: 1.2 !important;
}

/* =========================
SUBTITLE
========================= */

.subtitle {

    font-size: 24px !important;

    text-align: center !important;

    color: #475569 !important;

    margin-bottom: 35px !important;

    font-weight: 500 !important;
}

/* =========================
TEXT VISIBILITY
========================= */

h1, h2, h3, h4, h5, h6,
p, label, div {

    color: #111827 !important;
}

/* =========================
BUTTONS
========================= */

.stButton > button {

    background: linear-gradient(
        to right,
        #2563EB,
        #7C3AED
    );

    color: white !important;

    border-radius: 14px;

    height: 3.2em;

    width: 100%;

    font-size: 18px;

    font-weight: bold;

    border: none;

    transition: 0.3s;
}

.stButton > button:hover {

    background: linear-gradient(
        to right,
        #1D4ED8,
        #6D28D9
    );

    transform: scale(1.02);

    color: white !important;
}

/* =========================
INPUT BOXES
========================= */

div[data-baseweb="input"] input {

    background-color: white !important;

    color: black !important;

    border-radius: 12px;
}

/* =========================
SELECT BOX FIX
========================= */

/* =========================
SELECT BOX PROFESSIONAL FIX
========================= */

div[data-baseweb="select"] > div {

    background-color: white !important;

    color: black !important;

    border-radius: 12px !important;

    border: 1px solid #CBD5E1 !important;
}

/* Selected Value */

div[data-baseweb="select"] span {

    color: black !important;

    font-weight: 500;
}

/* Dropdown Menu */

ul {

    background-color: white !important;

    border-radius: 12px !important;
}

/* Dropdown Options */

li {

    background-color: white !important;

    color: black !important;

    font-weight: 500;
}

/* Hover */

li:hover {

    background-color: #DBEAFE !important;

    color: #1E3A8A !important;
}

div[data-baseweb="select"] span {

    color: white !important;
}

ul {

    background-color: #1F2937 !important;
}

li {

    background-color: #1F2937 !important;

    color: white !important;
}

li:hover {

    background-color: #2563EB !important;

    color: white !important;
}

/* =========================
METRIC CARDS
========================= */

div[data-testid="metric-container"] {

    background: white;

    border-radius: 20px;

    padding: 20px;

    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);

    border-left: 6px solid #2563EB;
}

div[data-testid="metric-container"] * {

    color: #111827 !important;
}

/* =========================
DATAFRAME
========================= */

[data-testid="stDataFrame"] {

    border-radius: 18px;

    overflow: hidden;

    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

/* =========================
FILE UPLOADER
========================= */

section[data-testid="stFileUploader"] {

    background: white;

    padding: 20px;

    border-radius: 18px;

    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

/* =========================
SUCCESS BOX
========================= */

div[data-testid="stSuccess"] {

    border-radius: 15px;

    background-color: #DCFCE7;
}

/* =========================
ERROR BOX
========================= */

div[data-testid="stError"] {

    border-radius: 15px;

    background-color: #FEE2E2;
}

/* =========================
REMOVE STREAMLIT BRANDING
========================= */

#MainMenu {

    visibility: hidden;
}

footer {

    visibility: hidden;
}

header {

    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOAD MODEL
# =========================================

model = joblib.load(
    'best_home_loan_model.pkl'
)

# =========================================
# LOAD FEATURE COLUMNS
# =========================================

feature_columns = joblib.load(
    'feature_columns.pkl'
)

# =========================================
# SESSION STATE
# =========================================

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = True

# =========================================
# LOGIN PAGE
# =========================================

if not st.session_state.logged_in:

    st.markdown(
        """
        <h1 class='title'>
            Home Loan Default Prediction
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h3 class='subtitle'>
            Machine Learning Based Banking Risk Assessment System
        </h3>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.subheader("Login")

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if (
                username == "admin" and
                password == "admin123"
            ):

                st.session_state.logged_in = True

                st.rerun()

            else:

                st.error(
                    "Invalid Username or Password"
                )

# =========================================
# MAIN APPLICATION
# =========================================

else:

    # =========================================
    # SIDEBAR
    # =========================================

    st.sidebar.title("Navigation")

    menu = st.sidebar.radio(
        "Select Option",
        [
            "Home",
            "Single Prediction",
            "Bulk Prediction"
        ]
    )

    st.sidebar.write("---")

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()

    # =========================================
    # HOME PAGE
    # =========================================

    if menu == "Home":

        st.markdown(
            """
            <h1 class='title'>
                Home Loan Default Prediction
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <h3 class='subtitle'>
                AI Powered Banking Risk Analysis System
            </h3>
            """,
            unsafe_allow_html=True
        )

        st.write("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Model Used",
                "XGBoost"
            )

        with col2:
            st.metric(
                "ROC AUC",
                "0.74"
            )

        with col3:
            st.metric(
                "Deployment",
                "Streamlit"
            )

        st.write("---")

        st.subheader("Features")

        st.write(
            "Single Customer Prediction"
        )

        st.write(
            "Bulk CSV Prediction"
        )

        st.write(
            "Bulk Excel Prediction"
        )

        st.write(
            "AI Risk Detection"
        )

        st.write(
            "Download Prediction File"
        )

    # =========================================
    # SINGLE PREDICTION
    # =========================================

    elif menu == "Single Prediction":

        st.markdown(
            """
            <h1 class='title'>
                Single Prediction
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.write("---")

        col1, col2 = st.columns(2)

        with col1:

            income = st.number_input(
                "Total Income",
                min_value=0.0,
                value=150000.0
            )

            credit = st.number_input(
                "Credit Amount",
                min_value=0.0,
                value=500000.0
            )

            annuity = st.number_input(
                "Annuity Amount",
                min_value=0.0,
                value=25000.0
            )

            days_birth = st.number_input(
                "Days Birth",
                value=-12000
            )

            days_employed = st.number_input(
                "Days Employed",
                value=-2000
            )

        with col2:

            children = st.number_input(
                "Children Count",
                min_value=0,
                value=0
            )

            family_members = st.number_input(
                "Family Members",
                min_value=1,
                value=2
            )

            gender = st.selectbox(
                "Gender",
                ["M", "F"]
            )

            education = st.selectbox(
                "Education Type",
                [
                    "Higher education",
                    "Secondary / secondary special",
                    "Incomplete higher"
                ]
            )

            family_status = st.selectbox(
                "Family Status",
                [
                    "Married",
                    "Single / not married",
                    "Civil marriage"
                ]
            )

            own_car = st.selectbox(
                "Own Car",
                ["Y", "N"]
            )

        # =========================================
        # CREATE INPUT DATAFRAME
        # =========================================

        input_df = pd.DataFrame({

            'AMT_INCOME_TOTAL': [income],
            'AMT_CREDIT': [credit],
            'AMT_ANNUITY': [annuity],
            'DAYS_BIRTH': [days_birth],
            'DAYS_EMPLOYED': [days_employed],
            'CNT_CHILDREN': [children],
            'CNT_FAM_MEMBERS': [family_members],
            'CODE_GENDER': [gender],
            'NAME_EDUCATION_TYPE': [education],
            'NAME_FAMILY_STATUS': [family_status],
            'FLAG_OWN_CAR': [own_car]
        })

        # =========================================
        # FEATURE ENGINEERING
        # =========================================

        input_df['INCOME_CREDIT_RATIO'] = np.where(
            input_df['AMT_CREDIT'] != 0,
            input_df['AMT_INCOME_TOTAL'] /
            input_df['AMT_CREDIT'],
            0
        )

        input_df['ANNUITY_INCOME_RATIO'] = np.where(
            input_df['AMT_INCOME_TOTAL'] != 0,
            input_df['AMT_ANNUITY'] /
            input_df['AMT_INCOME_TOTAL'],
            0
        )

        # =========================================
        # PREDICTION
        # =========================================

        if st.button("Predict Loan Default"):

            # =====================================
            # ADD MISSING COLUMNS
            # =====================================

            for col in feature_columns:

                if col not in input_df.columns:

                    input_df[col] = 0

            # =====================================
            # REORDER COLUMNS
            # =====================================

            input_df = input_df[
                feature_columns
            ]

            # =====================================
            # PREDICTION
            # =====================================

            prediction = model.predict(
                input_df
            )

            probability = model.predict_proba(
                input_df
            )[0][1]

            st.write("---")

            st.subheader(
                "Prediction Result"
            )

            st.metric(
                "Default Probability",
                f"{probability:.2%}"
            )

            if prediction[0] == 1:

                st.error(
                    "High Risk of Loan Default"
                )

            else:

                st.success(
                    "Low Risk of Loan Default"
                )

    # =========================================
    # BULK PREDICTION
    # =========================================

    else:

        st.markdown(
            """
            <h1 class='title'>
                Bulk Prediction
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.write("---")

        # =========================================
        # TEMPLATE DOWNLOAD
        # =========================================

        template_df = pd.DataFrame(
            columns=feature_columns
        )

        csv_template = template_df.to_csv(
            index=False
        )

        st.download_button(
            label="⬇ Download CSV Template",
            data=csv_template,
            file_name='bulk_prediction_template.csv',
            mime='text/csv'
        )

        uploaded_file = st.file_uploader(
            "Upload CSV or Excel File",
            type=['csv', 'xlsx']
        )

        if uploaded_file is not None:

            # READ FILE

            if uploaded_file.name.endswith('.csv'):

                bulk_df = pd.read_csv(
                    uploaded_file
                )

            else:

                bulk_df = pd.read_excel(
                    uploaded_file
                )

            st.subheader(
                "Uploaded Dataset"
            )

            st.dataframe(
                bulk_df.head()
            )

            # =====================================
            # ADD MISSING COLUMNS
            # =====================================

            for col in feature_columns:

                if col not in bulk_df.columns:

                    bulk_df[col] = 0

            # =====================================
            # REORDER COLUMNS
            # =====================================

            bulk_df = bulk_df[
                feature_columns
            ]

            # HANDLE INF VALUES

            bulk_df.replace(
                [np.inf, -np.inf],
                np.nan,
                inplace=True
            )

            # =====================================
            # PREDICTIONS
            # =====================================

            predictions = model.predict(
                bulk_df
            )

            probabilities = model.predict_proba(
                bulk_df
            )[:,1]

            bulk_df['Prediction'] = predictions

            bulk_df[
                'Default_Probability'
            ] = probabilities

            # =====================================
            # RESULTS
            # =====================================

            st.subheader(
                "Prediction Results"
            )

            st.dataframe(
                bulk_df.head()
            )

            # DOWNLOAD FILE

            csv = bulk_df.to_csv(
                index=False
            )

            st.download_button(
                label="⬇ Download Prediction File",
                data=csv,
                file_name='loan_predictions.csv',
                mime='text/csv'
            )
