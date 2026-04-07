# Ames House Price Prediction App
## Project Overview

This project is a Machine Learning web application built using Streamlit that predicts house prices based on various features from the Ames Housing dataset.

## Users can:

- Select different regression models
- View dataset preview
- Evaluate model performance
- Input custom values to predict house prices

## Features

- Interactive web app using Streamlit
- Multiple ML models:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
- Model evaluation metrics:
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² Score
- Real-time house price prediction based on user inputs

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
  
## Dataset

The dataset used is Ames Housing Dataset (subset) containing various numerical features related to houses such as:

- Area
- Number of rooms
- Year built

Target variable:

- SalePrice

## Machine Learning Workflow
- Data loading and preprocessing
- Selecting only numerical features
- Train-test split (80/20)
- Model selection by user
- Model training
- Performance evaluation
- Prediction using user inputs
  
## Installation & Setup

1. Clone the repository
   
git clone [https://github.com/abinesh8838/House_price_streamlit]

cd your-repo-name

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run app.py

## App Preview

(https://github.com/abinesh8838/House_price_streamlit/blob/main/App%20Preview.png)

## Example Output

- Displays dataset preview
- Shows model performance metrics
- Predicts house price instantly

## Future Improvements

- Add feature selection options
- Include non-numeric feature handling
- Hyperparameter tuning
- Deploy on Streamlit Cloud
  
## Acknowledgements

- Ames Housing Dataset
- Scikit-learn documentation
- Streamlit
