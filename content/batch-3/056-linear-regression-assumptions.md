# 056 — Linear Regression Assumptions

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 056
- Transcript title: "What are the main Assumptions of Linear Regression_ _ Top 5 Assumptions of Linear Regression"
- Transcript file: `056 - 2022-06-20 - What are the main Assumptions of Linear Regression_ _ Top 5 Assumptions of Linear Regression.txt`
- Topic: core assumptions behind ordinary least squares regression

## Learning objectives
- List the main assumptions of linear regression.
- Explain why these assumptions matter for valid inference and prediction.
- Understand how a violation can affect model quality.
- Connect assumptions to model diagnostics.

## The five key assumptions
1. Linearity
   - The relationship between predictors and target is linear.
2. Independence of errors
   - Residuals should not be correlated with each other.
3. Homoscedasticity
   - The variance of errors should be constant across all levels of the predictors.
4. Normality of residuals
   - Residuals are approximately normally distributed when used for inference.
5. No multicollinearity
   - Predictor variables should not be perfectly or very highly correlated.

## Why they matter
If assumptions are violated, the model may still make predictions, but the estimates, conclusions, and uncertainty may be unreliable.

## Example checks
- linearly: scatter plots and residual plots
- independence: time-order checks in time-series data
- heteroscedasticity: residual spread that grows over the range
- normality: Q-Q plots or residual histograms
- multicollinearity: large variance inflation factors or high pairwise correlations

## Mathematical note
The ordinary least squares estimator is optimal under these assumptions, especially when the errors are independent and homoscedastic.

## Common mistakes
- assuming linear regression is valid for every pattern simply because it fits numerically
- ignoring residual diagnostics
- using highly correlated features without checking for multicollinearity

## Key takeaways
- Linear regression is simple and useful, but it relies on assumptions.
- Assumption checks are part of responsible modeling.
- Violations do not always invalidate the model, but they affect interpretation and reliability.

## Practice questions
1. Why is linearity important?
2. What does homoscedasticity mean?
3. Why is multicollinearity a problem?
4. How do you diagnose whether a regression model is violating assumptions?

## Source reference
- Transcript title: "What are the main Assumptions of Linear Regression_ _ Top 5 Assumptions of Linear Regression"
- File: `056 - 2022-06-20 - What are the main Assumptions of Linear Regression_ _ Top 5 Assumptions of Linear Regression.txt`
