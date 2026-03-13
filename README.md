# BMW Price Prediction Web App

This project predicts the **price category of BMW vehicles** using machine learning.

## Features

* Data analysis using Pandas and Seaborn
* Multiple ML models (Logistic Regression, Decision Tree, Random Forest)
* Hyperparameter tuning with GridSearchCV
* Feature importance visualization
* Interactive web app built with Streamlit

## Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* Matplotlib
* Seaborn

## Project Structure

```
bmw-price-prediction-ml
│
├── data/                # dataset
├── notebook/            # ML analysis notebook
├── app.py               # Streamlit web app
├── bmw_model.pkl        # trained ML model
└── requirements.txt     # dependencies
```

## Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the web app:

```
python -m streamlit run app.py
```

## Example Input

* Year: 2019
* Mileage: 25000
* Engine Size: 2.0
* Fuel Type: Petrol

The model predicts the **price category** of the car.

## Author

Satakshi Srivastava
