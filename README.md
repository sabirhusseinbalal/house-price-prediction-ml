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

---
   ```bash
   git clone https://github.com/Sabirhusseinbalal/house-price-prediction-ml.git
   ```
---

## Machine Learning Roadmap (Beginner → Advanced)

---

### Stage 1: Regression Foundations
-  ***[simple-regression-lab]***(https://github.com/sabirhusseinbalal/simple-regression-lab)
- 👉 **house-price-prediction-ml**
- ***same-data-different-models***

---

### Stage 2: Regression Deep Dive
- regression-error-analysis
- feature-engineering-regression
- regression-from-scratch

---

### Stage 3: Classification Core
- binary-classification-basics
- credit-risk-classification
- threshold-tuning-classification

---

### Stage 4: Classification Depth
- class-imbalance-handling
- logistic-regression-from-scratch
- model-interpretability

---

### Stage 5: Unsupervised Learning
- customer-segmentation-clustering
- dimensionality-reduction
- clustering-comparison

---

### Stage 6: Association & Anomaly Detection
- market-basket-analysis
- anomaly-detection-dbscan
- anomaly-detection-isolation-forest

---

### Stage 7: Ensemble & Optimization
- ensemble-learning-ml
- hyperparameter-tuning

---

### Stage 8: Real-World ML Projects
- churn-prediction-system
- fraud-detection-system
- sales-forecasting-system

---

### Stage 9: Advanced ML Engineering
- end-to-end-ml-system
- ml-pipeline-project
- model-monitoring-simulation





