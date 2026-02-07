# House Price Prediction (ML)

## Description
A machine learning project to predict house prices based on California Housing dataset.
This is aimed at comparing various regression models using the same data and comprehending.
why certain models outperform other models.

## Dataset
- California Housing Dataset
- Target column: `median housing value`
- features only (categorical column removed)
- Missing values dropped

## Models Used
- Linear Regression
- Ridge Regression (L2)
- Lasso Regression (L1)
- Random Forest Regressor (comparison)

## Concepts Learned
- Feature scaling using StandardScaler
- Train/Test split
- Regularization (Ridge & Lasso)
- Overfitting vs Underfitting
- Model comparison based on metrics.

## Evaluation Metrics
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## Results Summary
- Linear, Ridge and Lasso did the same.
- The highest performance was reached by Random Forest.
- The non-linear relationships were better modeled by Random Forest than by linear models.

## Project Structure
house-price-prediction-ml/
├── data/
│   └── housing.csv
├── src/
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── train_models.py
│   ├── evaluate.py
│   └── main.py
├── result/
│   └── metrics.txt
├── requirements.txt
└── README.md

## Conclusion
The project demonstrates that the choice of a model is determined by the complexity of data.
For ensembling, linear models are good baselines, although other models such as ensemble models can be used.
Random Forest are more effective where the relationships are non-linear.

