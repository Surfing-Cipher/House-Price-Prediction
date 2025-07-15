# 🏡 House Price Prediction API

A simple and production-ready **House Price Prediction Web App** built using:

- 🧠 XGBoost Regressor
- 🌐 Flask Web Framework
- 💄 Bootstrap Form UI
- 🐳 Docker Containerization
- 🔁 GitHub Actions for CI/CD

---

## 📌 Project Overview

This application predicts **median house prices** based on various housing and demographic features using a machine learning model trained on the California Housing Dataset.

Users can input the data via a web form and receive predicted prices directly on the webpage.

---

## 🚀 Features

- ✅ XGBoost model trained on preprocessed features
- ✅ Flask backend for web app and API
- ✅ Clean Bootstrap form UI
- ✅ Model deployed with Docker
- ✅ CI/CD pipeline using GitHub Actions
- ✅ Ready for Render/Heroku deployment

---

## 📂 Folder Structure

```bash
House_Price_Prediction/
├── house_price_api/
│   ├── main.py                # Flask app entrypoint
│   ├── form.html              # HTML form (Bootstrap)
│   ├── xgb_model.json         # Trained model (XGBoost Booster format)
│   ├── Dockerfile             # Container definition
│   ├── requirements.txt       # Python dependencies
├── .github/
│   └── workflows/
│       └── main.yml           # GitHub Actions CI/CD workflow
└── README.md
```

---

## 🛠️ Technologies Used

| Tool               | Purpose                         |
| ------------------ | ------------------------------- |
| **Python**         | Programming language            |
| **Flask**          | Lightweight backend web server  |
| **XGBoost**        | ML Model for regression         |
| **Bootstrap**      | Styling for web form UI         |
| **Docker**         | Containerization for deployment |
| **GitHub Actions** | CI/CD pipeline for automation   |

---

## 📥 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/House_Price_Prediction.git
cd House_Price_Prediction/house_price_api
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
.venv\Scripts\activate    # On Windows
# or
source .venv/bin/activate # On macOS/Linux

pip install -r requirements.txt
```

### 3. Run the Flask app

```bash
python main.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🐳 Run with Docker

### Build Docker image

```bash
docker build -t house-price-api .
```

### Run container

```bash
docker run -d -p 5000:5000 house-price-api
```

---

## 🔁 GitHub Actions CI/CD

GitHub Actions automatically:

- Installs dependencies
- Builds the Docker image
- Runs the app locally for testing

You can find the workflow under:

```
.github/workflows/main.yml
```

---

## ✨ Example Input

Try entering the following values in the form:

```
longitude: -118.30
latitude: 34.19
housing_median_age: 29.0
total_rooms: 5000
total_bedrooms: 1000
population: 1500
households: 500
median_income: 4.5
rooms_per_household: 10
bedrooms_per_room: 0.2
population_per_household: 3.0
ocean_proximity_<option>: 1 or 0 (from encoded one-hot features)
```

---

## 📦 Deployment Options

You can deploy this app using:

- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Heroku](https://heroku.com/)
- Docker on VPS or cloud providers

---

## 📜 License

This project is licensed under the MIT License.
