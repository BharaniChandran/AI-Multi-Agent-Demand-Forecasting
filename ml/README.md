# AI Multi-Agent Product Demand Forecasting - ML Module

This module contains the Machine Learning components for the AI Multi-Agent Product Demand Forecasting System.

It includes:

- Data preprocessing
- Feature engineering
- Model training
- Forecasting agent
- Anomaly detection agent
- Recommendation agent

## Project Structure

```text
ml/
│
├── agents/
│   ├── forecasting_agent.py
│   ├── anomaly_agent.py
│   └── recommendation_agent.py
│
├── preprocessing/
│   ├── clean_data.py
│   ├── feature_engineering.py
│   └── split_dataset.py
│
├── models/
│   ├── train_model.py
│   ├── evaluate.py
│   └── predict.py
│
├── saved_models/
│   └── random_forest.pkl
│
├── data/
│   ├── raw/
│   └── processed/
│
└── requirements.txt
```

## Forecasting Model

Model Name:
Random Forest Demand Forecasting Model

Algorithm:
RandomForestRegressor

Framework:
scikit-learn

Saved Model:
random_forest.pkl

## Model Input Features

The forecasting model requires the following features:

| Feature | Type |
|----------|------|
| Store_ID | Integer |
| Product_ID | Integer |
| Price | Float |
| Year | Integer |
| Month | Integer |
| Day | Integer |
| DayOfWeek | Integer |
| Quarter | Integer |
| IsWeekend | Integer |
| Product_Name_* | One-Hot Encoded |
| Category_* | One-Hot Encoded |

## Feature Engineering

The preprocessing pipeline performs:

- Convert Date to datetime
- Extract Year
- Extract Month
- Extract Day
- Extract DayOfWeek
- Extract Quarter
- Generate IsWeekend feature
- One-hot encode Product_Name
- One-hot encode Category
- Remove Date column

## Load Model

```python
import joblib

model = joblib.load("random_forest.pkl")
```

## Forecasting Agent

File:

forecasting_agent.py

Usage:

```python
from ml.agents.forecasting_agent import ForecastingAgent

agent = ForecastingAgent()

prediction = agent.forecast(dataframe)
```

## Anomaly Detection Agent

File:

anomaly_agent.py

Usage:

```python
agent = AnomalyAgent()

result = agent.detect(dataframe)
```

The agent uses Isolation Forest to detect abnormal sales values.

## Recommendation Agent

File:

recommendation_agent.py

Usage:

```python
agent = RecommendationAgent()

recommendation = agent.generate_recommendation(
    predicted_sales,
    anomaly
)
```

## Dependencies

Install using:

pip install -r requirements.txt

Required packages:

- pandas
- numpy
- scikit-learn
- joblib

## Sample Input

```json
{
  "store_id": 1,
  "product_id": 101,
  "price": 55000,
  "date": "2026-07-21",
  "product_name": "Laptop",
  "category": "Electronics"
}
```

## Sample Output

```json
{
  "predicted_sales": 42.6
}
```

## Multi-Agent Workflow

```text
Sales Data
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Forecasting Agent
      │
      ▼
Prediction
      │
      ▼
Anomaly Detection Agent
      │
      ▼
Recommendation Agent
      │
      ▼
Final Recommendation
```

## Backend Integration Notes

- Use the same preprocessing steps before prediction.
- Ensure the feature columns match the training dataset.
- Load the model once when the backend starts.
- Reuse the loaded model for all prediction requests.
- Do not change the order of input features.