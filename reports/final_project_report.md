Project FORESIGHT: Final Executive Closure Report
To: Head of Operations, NorthBay Living

From: Sumit Yadav, Data Scientist

Date: October 2, 2026

Subject: Demand Forecasting Model Final Results & Business Impact

1. Executive Summary
Project FORESIGHT was initiated to optimize inventory management and reduce stockouts through data-driven demand forecasting. Over the course of the engagement, we successfully built an automated data pipeline, engineered predictive features, and trained a Machine Learning model. The final Random Forest model significantly outperformed historical baseline metrics, providing a robust tool for future inventory planning.

2. Methodology & Feature Engineering
To enable accurate forecasting, the raw data (sales, inventory, SKU master, and calendar) was unified into a single analytical pipeline. The following features were engineered to help the Machine Learning algorithm recognize hidden demand patterns:

Temporal Features: Extracted day of the week, month, and weekend indicators to capture weekly seasonality.

Lag Features: Engineered 1-day, 2-day, and 3-day sales lags to account for immediate short-term demand momentum.

Rolling Averages: Calculated a 7-day rolling mean for each SKU to smooth out daily volatility and identify longer-term sales trajectories.

3. Results & Business Impact
The core objective was to minimize the Weighted Absolute Percentage Error (WAPE) when predicting unit sales. We evaluated our model against a "Seasonal-Naive" baseline (assuming sales match the exact same day from the previous week).

Baseline Error (Naive 7-Day Lag): 28.83%

Machine Learning Error (Random Forest): 17.85%

Performance Improvement: The model reduced forecasting error by nearly 11 absolute percentage points (an approximate 38% relative improvement in accuracy).

Business Value: By predicting daily SKU demand with an average error rate of only 17.85%, NorthBay Living can optimize warehouse capital allocation. This tightened accuracy directly translates to lower holding costs for slow-moving inventory (Dead Stock) and a reduction in lost revenue from stockouts of high-velocity items (Top Movers).

4. Deployment & Next Steps
The final Random Forest model has been serialized and saved as rf_demand_model.pkl. This allows the IT and Operations teams to instantly generate daily forecasts on new incoming data without needing to retrain the algorithm from scratch. Future iterations of this project could explore incorporating external data sources, such as broader economic indicators or localized weather patterns, to drive the WAPE score down even further.