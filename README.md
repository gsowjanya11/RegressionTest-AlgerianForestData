# 🔥 Algerian Forest Fire Prediction Project

## 📌 Overview
This project uses the **Algerian Forest Fire dataset** to build predictive models for fire occurrence and severity.  
We experimented with multiple regression techniques — **Linear Regression, Ridge, Lasso, and ElasticNet** — and deployed the final model using **Flask** for interactive predictions.

---

## 📂 Project Workflow

1. **Data Cleansing**
   - Handled missing values
   - Removed duplicates
   - Converted categorical variables into numerical form

2. **Exploratory Data Analysis (EDA)**
   - Visualized distributions of features (Temperature, RH, Wind Speed, Rain, FFMC, DMC, DC, ISI, BUI, FWI, Classes, Region)
   - Checked correlations and multicollinearity
   - Identified important predictors

3. **Feature Scaling**
   - Standardized numerical features using `StandardScaler`
   - Ensured all models received normalized input data

4. **Model Training**
   - **Linear Regression**: baseline model
   - **Ridge Regression**: handled multicollinearity with L2 regularization
   - **Lasso Regression**: feature selection with L1 regularization
   - **ElasticNet**: combined L1 and L2 penalties
   - Evaluated models using metrics such as RMSE, MAE, and R²

5. **Model Pickling**
   - Saved trained models using Python’s `pickle` module
   - Enabled easy loading of models without retraining

6. **Deployment with Flask**
   - Built a web interface (`index.html`) with 5+ input fields and a **Predict** button
   - Flask backend loads the pickled model and scaler
   - User inputs are transformed, scaled, and passed to the model
   - Prediction results are displayed on the webpage

