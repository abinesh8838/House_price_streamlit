
# !pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# -------------------------
# Page Title
# -------------------------
st.title("🏠 Ames House Price Prediction")
st.write("Choose a regression model and predict house prices.")


# -------------------------
# Load Dataset
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_excel("Ames_Housing_Subset.xlsx")
    return df

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())


# -------------------------
# Keep only numeric columns
# -------------------------
df = df.select_dtypes(include=np.number)

# Target
y = df["SalePrice"]

# Features
X = df.drop("SalePrice", axis=1)


# -------------------------
# Train-Test Split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# -------------------------
# Model Selection
# -------------------------
model_name = st.selectbox(
    "Select Regression Model",
    ["Linear Regression", "Decision Tree", "Random Forest"]
)


# -------------------------
# Train Selected Model
# -------------------------
if model_name == "Linear Regression":
    model = LinearRegression()

elif model_name == "Decision Tree":
    model = DecisionTreeRegressor(random_state=42)

else:
    model = RandomForestRegressor(n_estimators=100, random_state=42)

model.fit(X_train, y_train)


# -------------------------
# Evaluation Metrics
# -------------------------
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

st.subheader("📊 Model Evaluation")

st.write(f"**MAE:** {mae:,.2f}")
st.write(f"**RMSE:** {rmse:,.2f}")
st.write(f"**R² Score:** {r2:.3f}")


# -------------------------
# User Input Prediction
# -------------------------
st.subheader("🔮 Predict House Price")

input_data = {}

for col in X.columns:
    input_data[col] = st.number_input(
        f"Enter {col}",
        value=float(X[col].median())
    )

input_df = pd.DataFrame([input_data])

if st.button("Predict Price"):
    price = model.predict(input_df)[0]
    st.success(f"Estimated House Price: ₹ {price:,.0f}")
