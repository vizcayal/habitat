# Energy Market Forecasting Challenge

## Background

In electricity markets, accurate forecasting of energy prices and renewable generation is critical for market participants to optimize their operations and trading strategies. This challenge focuses on developing models to forecast the following three key variables:

1. Real-Time Locational Marginal Prices (RTLMP)
2. Day-Ahead Locational Marginal Prices (DALMP)
3. Wind Power Generation

## Challenge Description

Your task is to develop a machine learning model that can generate accurate ensemble forecasts (multiple scenarios) for these three variables based on the provided input features.

## Data Description

You are provided with two datasets:

1. `train_data.parquet`: Artifical historical data including both input features and target variables
2. `test_data.parquet`: Input features only for the test period

### Input Features (X)

The input features available in both training and test datasets are:

- `system_load_forecast`: Forecasted system-wide electricity demand (MW)
- `system_solar_forecast`: Forecasted system-wide solar generation (MW)
- `system_wind_forecast`: Forecasted system-wide wind generation (MW)
- `outage_forecast`: Forecasted transmission/generation outages (fraction of capacity)

All data is at hourly resolution with a datetime index.

### Target Variables (y)

The target variables in the training dataset are:

- `rtlmp`: Real-Time Locational Marginal Price ($/MWh)
- `dalmp`: Day-Ahead Locational Marginal Price ($/MWh)
- `wind_power_mw`: Nodal wind power generation (MW)

## Task

Your task is to:

1. Develop a model to forecast the three target variables jointly based on the provided input features
2. Generate 100 different samples/scenarios for each hour in the test dataset
3. Submit your code along with a brief explanation of your approach and how you would scale and productize your solution

## Evaluation

Your submission will be evaluated based on:

1. The quality and diversity of your ensemble forecasts
2. The ability of your model to capture market dynamics
3. Your approach to scaling and productizing the solution

## Submission Format

Please provide:

1. Your code (Python preferred) with clear documentation
2. A brief explanation of your approach (max 2 pages)
3. Your forecasted scenarios for the test period in a format of your choice

Good luck!