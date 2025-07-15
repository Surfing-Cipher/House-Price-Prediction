from flask import Flask, request, render_template
import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the XGBoost model from .json
model = xgb.Booster()
model.load_model("xgb_model.json")

# Columns expected by the model after preprocessing (adjust if needed)
feature_columns = [
    'longitude', 'latitude', 'housing_median_age', 'total_rooms',
    'total_bedrooms', 'population', 'households', 'median_income',
    'ocean_proximity_INLAND', 'ocean_proximity_ISLAND',
    'ocean_proximity_NEAR_BAY', 'ocean_proximity_NEAR_OCEAN',
    'rooms_per_household', 'bedrooms_per_room', 'population_per_household'
]

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None

    if request.method == "POST":
        # Get user input
        data = {
            'longitude': float(request.form['longitude']),
            'latitude': float(request.form['latitude']),
            'housing_median_age': float(request.form['housing_median_age']),
            'total_rooms': float(request.form['total_rooms']),
            'total_bedrooms': float(request.form['total_bedrooms']),
            'population': float(request.form['population']),
            'households': float(request.form['households']),
            'median_income': float(request.form['median_income']),
            'ocean_proximity': request.form['ocean_proximity']
        }

        # Derived features
        data['rooms_per_household'] = data['total_rooms'] / data['households']
        data['bedrooms_per_room'] = data['total_bedrooms'] / data['total_rooms']
        data['population_per_household'] = data['population'] / data['households']

        # One-hot encode ocean_proximity manually
        for cat in ['INLAND', 'ISLAND', 'NEAR_BAY', 'NEAR_OCEAN']:
            data[f'ocean_proximity_{cat}'] = 1 if data['ocean_proximity'] == cat else 0
        del data['ocean_proximity']

        # Convert to DataFrame
        input_df = pd.DataFrame([data])

        # Ensure correct order of columns
        input_df = input_df[feature_columns]

        # Scale numeric features (you should reuse the scaler used during training if possible)
        scaler = StandardScaler()
        input_scaled = scaler.fit_transform(input_df)  # For production: load and use the same scaler

        dmatrix = xgb.DMatrix(input_scaled, feature_names=feature_columns)
        prediction = model.predict(dmatrix)[0]
        prediction = round(prediction, 2)

    return render_template("form.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
