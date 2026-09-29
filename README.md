## Monte Carlo Stock Price Simulation 

This project implements a **Monte Carlo Simulation** in Python to forecast potential stock price trajectories over a 1-year horizon (252 trading days) using **Geometric Brownian Motion (GBM)** and **Itô's Lemma**.

## Features
- Historical Data Retrieval: Automatically fetches stock data using 'yfinance'.
- Mathematical Rigor: Incorporates Itô's correction to handle volatility drag.
- Large-Scale Simulation : Simulates 10,000 price paths using NumPy operations.
- Risk Analysis: Evaluates mean, median, worst-case (5th percentile), and best-case (95th percentile) scenarios.
- Data Visualization: Generates path charts and probability distribution histograms with Matplotlib.

## Tech Stack
- Python
- NumPy - Matrix calculations & random generation
- Pandas - Financial data manipulation
- Matplotlib - Data visualization
- yfinance - Yahoo Finance 

## How to Run
1. Clone this repository:
   ```bash
   git clone [https://github.com/yamzahri-gif/onte_carlo_stock_simulation.git](https://github.com/yamzahri-gif/onte_carlo_stock_simulation.git)
