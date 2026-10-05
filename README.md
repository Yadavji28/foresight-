# Project FORESIGHT: Demand & Inventory Intelligence

**A Data Science Internship Project at Zidio Development**  
**Client:** NorthBay Living  
**Author:** Sumit Yadav  

---

## Project Overview
**Project FORESIGHT** is an end-to-end Machine Learning pipeline designed to optimize supply chain and inventory management for NorthBay Living. By accurately predicting future product demand, this project helps reduce overstocking, minimize stockouts, and improve overall operational efficiency.

The core of this project involves extensive data cleaning, complex feature engineering, and the deployment of a robust predictive model to forecast demand trends across various products and timeframes.

##  Key Objectives
- Merge and analyze complex datasets (Sales, Inventory, Calendar).
- Perform exploratory data analysis (EDA) to uncover demand trends and seasonality.
- Engineer time-series features such as rolling averages and time-based lags.
- Train and evaluate a Machine Learning model to forecast demand with high accuracy.
- Maintain a clean, modular, and version-controlled project structure.

## Machine Learning Model & Performance
The primary forecasting algorithm utilized in this project is the **Random Forest Regressor**. 

By applying advanced feature engineering and hyperparameter tuning, the model achieved significant improvements over the baseline metrics:
- **Baseline WAPE (Weighted Absolute Percentage Error):** 28.83%
- **Final Model WAPE:** **17.85%** 🚀

*This 11% improvement in WAPE translates directly to better inventory precision and reduced holding costs for the business.*

##  Project Structure
The repository is organized into standard data science directories for modularity and ease of use:

```text
├── data/               # Contains raw and processed CSV datasets
├── notebooks/          # Jupyter notebooks for EDA and model training
├── models/             # Serialized Machine Learning models (.pkl)
├── src/                # Modular Python scripts for pipeline execution
├── reports/            # Final project documentation and analysis reports
├── .gitignore          # Git ignore rules for large files and caches
├── requirements.txt    # Python dependencies for the project
└── README.md           # Project documentation
