# 052 — Regression Metrics: MSE, MAE, RMSE, and R²

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 052
- Transcript title: "Regression Metrics _ MSE, MAE & RMSE _ R2 Score & Adjusted R2 Score"
- Transcript file: `052 - 2021-05-13 - Regression Metrics _ MSE, MAE & RMSE _ R2 Score & Adjusted R2 Score.txt`
- Topic: evaluation metrics for continuous prediction tasks

## Learning objectives
- Define MSE, MAE, and RMSE.
- Explain how R² measures model fit.
- Compare different regression metrics.
- See how model quality is judged in practice.

## Why metrics matter
Once we train a regression model, we need a way to judge if its predictions are good.

The most common metrics are based on the difference between actual values and predicted values.

## Residuals
The residual for observation $i$ is:

$$
 e_i = y_i - \hat{y}_i
$$

where:
- $y_i$ is the true value
- $\hat{y}_i$ is the predicted value

## MSE
Mean Squared Error is:

$$
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

It penalizes large errors more strongly because each error is squared.

## MAE
Mean Absolute Error is:

$$
MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

This is easier to interpret because it is in the same units as the target.

## RMSE
Root Mean Squared Error is:

$$
RMSE = \sqrt{MSE}
$$

It keeps the same units as the target and is commonly used in practice.

## R² score
The coefficient of determination is:

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

It measures how much of the variation in the target is explained by the model.

- $R^2 = 1$: perfect fit
- $R^2 = 0$: the model is no better than predicting the mean
- negative $R^2$: worse than a mean-only model

## Python example
```python
import numpy as np

y_true = np.array([3, 5, 7, 9])
y_pred = np.array([2.5, 5.5, 6.5, 9.5])

mae = np.mean(np.abs(y_true - y_pred))
mse = np.mean((y_true - y_pred) ** 2)
rmse = np.sqrt(mse)
r2 = 1 - np.sum((y_true - y_pred) ** 2) / np.sum((y_true - y_true.mean()) ** 2)

print('MAE:', mae)
print('MSE:', mse)
print('RMSE:', rmse)
print('R2:', r2)
```

## Key takeaways
- MSE and RMSE emphasize larger errors.
- MAE is more interpretable and robust to outliers.
- $R^2$ tells us how much variance the model explains.

## Practice questions
1. What is the difference between MAE and MSE?
2. Why is RMSE often preferred over MSE for interpretation?
3. What does an $R^2$ value of 0.8 mean?
4. When might MAE be more appropriate than RMSE?

## Source reference
- Transcript title: "Regression Metrics _ MSE, MAE & RMSE _ R2 Score & Adjusted R2 Score"
- File: `052 - 2021-05-13 - Regression Metrics _ MSE, MAE & RMSE _ R2 Score & Adjusted R2 Score.txt`
