# House Price Prediction (ML)

## Description
A Machine learning project to predict house prices using California Housing data.

**YouTube Video:**
[[House Price Prediction | Machine Learning Project 2](https://youtu.be/FO-MNmWJQxs?si=tBWcTD7qq273bzp3)]

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
- Random Forest performed better on this dataset.
- The non-linear relationships were better modeled by Random Forest than by linear models.

## Project Structure
```
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
```

---
   ```bash
   git clone https://github.com/Sabirhusseinbalal/house-price-prediction-ml.git
   ```
---

## Machine Learning (Basics)
---
-  [***simple-regression-lab***](https://github.com/sabirhusseinbalal/simple-regression-lab)
- 👉 **house-price-prediction-ml**
- [***same-data-different-models***](https://github.com/sabirhusseinbalal/same-data-different-models)
- [***regression-error-analysis***](https://github.com/sabirhusseinbalal/regression-error-analysis)

**Watch Full YouTube Playlist:**
[[Machine Learning (Beginner → Advanced)](https://youtube.com/playlist?list=PLBslpEV463BcknHrcoF_OJDyutuE1DneY&si=7PfeO4OSQCqh1wEI)]
