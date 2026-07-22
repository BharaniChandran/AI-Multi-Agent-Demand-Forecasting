# ML Integration Guide

## Overview

The ML module provides:

- Demand Forecasting
- Anomaly Detection
- Inventory Recommendation

## ML Folder Structure

```text
ml/
│
├── agents/
│   ├── forecasting_agent.py
│   ├── anomaly_agent.py
│   └── recommendation_agent.py
│
├── preprocessing/
│
├── saved_models/
│   └── random_forest.pkl
│
├── README.md
└── requirements.txt
```## Model Location

Copy the trained model:

random_forest.pkl

to

backend/models/

The backend should load the model only once during application startup.
## Forecasting Agent

File

forecasting_agent.py

Usage

```python
agent = ForecastingAgent()

prediction = agent.forecast(dataframe)
```## Anomaly Detection Agent

File

anomaly_agent.py

Usage

```python
agent = AnomalyAgent()

result = agent.detect(dataframe)
```## Recommendation Agent

File

recommendation_agent.py

Usage

```python
agent = RecommendationAgent()

recommendation = agent.generate_recommendation(
    predicted_sales,
    anomaly
)
```## Dependencies

Install using:

pip install -r requirements.txt

Required packages:

- pandas
- numpy
- scikit-learn
- joblib
## Forecast Input

```json
{
    "store_id":1,
    "product_id":101,
    "price":55000,
    "date":"2026-07-21",
    "product_name":"Laptop",
    "category":"Electronics"
}
```## Forecast Output

```json
{
    "prediction":{
        "predicted_sales":42.6
    },
    "anomaly":{
        "status":"Normal"
    },
    "recommendation":{
        "message":"Maintain current stock"
    }
}
```## Workflow

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
Anomaly Detection
      │
      ▼
Recommendation Agent
      │
      ▼
Backend Response
```