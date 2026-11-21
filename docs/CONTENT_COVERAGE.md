# Content Coverage Plan

## 1. Coverage classification

The final ML Atlas must explicitly separate course material into the following categories.

### A. Original CampusX course material

This is the core body of the course and should be preserved in order.

Coverage includes:

- ML foundations and learning types
- data gathering and preprocessing
- EDA and feature engineering
- PCA and linear models
- classification theory and metrics
- Naive Bayes, KNN, SVM
- decision trees and ensembles

### B. Additional foundational explanations

These are needed to make the original course educationally complete.

Examples:

- linear algebra basics for PCA and SVM
- probability essentials for Bayes and logistic regression
- derivative and optimization fundamentals for gradient descent
- bias-variance reasoning in plain language plus math
- matrix/vector notation with practical examples

### C. Advanced supplementary ML topics

These topics are beyond the original transcript set and should be clearly labeled as supplementary.

Examples:

- deep learning basics
- neural networks and backpropagation
- ML deployment and monitoring
- time series and forecasting
- NLP and recommender systems
- clustering beyond K-means
- active learning, anomaly detection, causal ML

### D. Interview preparation

This should be built as a companion layer to the course material.

Examples:

- common conceptual interview questions
- model selection justifications
- underfitting vs overfitting
- evaluation trade-offs
- feature importance interpretation
- model debugging questions

### E. Practical projects

These are practical tasks that turn course theory into real ML workflows.

Examples:

- classification pipeline project
- regression benchmarking project
- feature engineering notebook
- hyperparameter tuning project
- model comparison project
- end-to-end deployment notes

## 2. High-priority topics requiring more educational depth

The original course is already strong in many areas, but these topics need deeper mathematical and visual treatment in ML Atlas.

### High priority math-heavy topics

- PCA and variance maximization
- linear regression objective function and least squares
- gradient descent derivation and update rule
- logistic regression loss and cross-entropy
- Bayes theorem and conditional probability
- SVM margin and optimization
- decision tree entropy / Gini impurity
- AdaBoost weighting and error minimization

### High priority diagram topics

- ML pipeline from data to deployment
- train/test split and validation flow
- linear regression line fitting
- gradient descent contour plots
- PCA projection and explained variance
- SVM margin and support vectors
- decision tree splitting decisions
- bias-variance trade-off curves

### High priority Python topics

- feature scaling and encoding pipelines
- missing value imputation strategies
- PCA implementation and explained variance plots
- linear regression from scratch
- logistic regression from scratch
- Naive Bayes implementation with probability calculations
- decision tree and random forest examples
- AdaBoost and bagging implementation

### High priority exercise topics

- derivation practice for loss functions
- small datasets for feature engineering
- model comparison tasks
- confusion-matrix interpretation
- feature importance reasoning
- performance trade-off questions

## 3. Lesson clusters by learning objective

| Learning objective | Lessons | Comments |
| --- | --- | --- |
| ML foundations and problem framing | 1-14 | Strong conceptual base |
| Data collection and EDA | 15-22 | Need clean notebooks and examples |
| Feature engineering | 23-46 | Highest practical value |
| Dimensionality reduction | 47-49 | Requires geometry and algebra |
| Regression and optimization | 50-66 | Core mathematical depth |
| Logistic regression and metrics | 67-81 | Must include derivations and metrics |
| Bayes, KNN, SVM | 82-96 | Probability and geometry heavy |
| Decision trees and ensembles | 97-119 | Key interview and model-comparison topics |

## 4. Recommended coverage balance for the final guide

The final ML Atlas should target roughly this balance:

- 45% original CampusX material
- 25% mathematical and conceptual expansion
- 15% code and practical implementation
- 10% interview prep
- 5% advanced supplementary topics

This keeps the site grounded in the transcript source while adding educational value beyond a simple transcript mirror.

## 5. Important constraint

The final ML Atlas should never claim a lesson is covered if a transcript is unavailable. The no-caption lessons 87 and 89 must remain explicitly marked as unavailable and not reconstructed.

## 6. Batch 1 completion snapshot

### Completed in this batch

- 001 — What is Machine Learning?
- 002 — AI vs ML vs DL for Beginners
- 003 — Types of Machine Learning
- 004 — Batch / Offline vs Online Learning
- 005 — Online Machine Learning
- 006 — Instance-Based vs Model-Based Learning
- 007 — Challenges in Machine Learning
- 008 — Applications of Machine Learning

### Audit status

Batch 1 has passed a detailed educational-quality audit. Key issues found and fixed included:

- improved beginner clarity for lessons 001–003
- strengthened technical vocabulary explanations across all lessons
- added deeper mathematical intuition where needed, especially in lesson 006
- fixed overlapping conceptual repetition between lessons 004 and 005 by separating the broad training-mode distinction from streaming production mechanics
- expanded real-world examples, misconceptions, and interview-relevant practice questions
- confirmed source references and transcript alignment for all lessons in the batch

### Validation notes

- All eight lessons were mapped to the original CampusX transcript titles and filenames.
- Each lesson file contains original-source explanation, supplementary teaching notes, and a small Python example.
- The batch stays within the requested scope and does not generate final HTML.
- Lessons 87 and 89 remain explicitly marked as unavailable because they have no captions recorded in the source inventory.
- A dedicated quality review is recorded in `docs/BATCH_01_AUDIT.md`.

## 7. Batch 2 completion snapshot

### Completed in this batch

- 009 — Machine Learning Development Life Cycle
- 010 — Data Engineer vs Data Analyst vs Data Scientist vs ML Engineer
- 011 — What are Tensors?
- 012 — Installing Anaconda, Jupyter Notebook, and Google Colab
- 013 — End-to-End Toy Project
- 014 — How to Frame a Machine Learning Problem
- 015 — Working with CSV Files
- 016 — Working with JSON and SQL

### Validation notes

- Batch 2 continues the original CampusX sequence after lesson 008.
- The lesson order remains source-aligned and traceable.
- Practical Python examples and conceptual explanations were expanded for the project workflow, setup, and data ingestion topics.
- The project keeps the same educational quality bar established in Batch 1.
- The next lesson to process is 017: Fetching Data From an API.

## 8. Batch 3 continuation snapshot

### Completed in this batch

- 017 — Fetching Data From an API
- 018 — Fetching Data Using Web Scraping
- 019 — Understanding Your Data
- 020 — EDA Using Univariate Analysis
- 021 — EDA Using Bivariate and Multivariate Analysis

### Validation notes

- The continuation maintains the original transcript sequence and does not reconstruct unavailable lessons.
- The content stays transcript-first while adding beginner intuition, technical explanation, and practical Python examples.
- Setup-heavy material has been trimmed so the project remains focused on ML learning rather than installation-only detail.
- The next target in sequence is lesson 022: Pandas Profiling.

## 9. Continuation batch 4-7 snapshot

### Completed in this phase

- 061-080 — Polynomial regression, regularization, classification metrics, and softmax foundations
- 081-100 — Naive Bayes, KNN, SVM, kernels, and decision tree basics
- 101-120 — Ensemble learning, voting, bagging, random forests, and boosting
- 121-134 — Gradient boosting, XGBoost, clustering, class imbalance, and Optuna tuning

### Validation notes

- The continuation remains in original CampusX order and keeps missing/no-caption lessons explicit.
- The files are numbered consistently and stored under `content/batch-4`, `content/batch-5`, `content/batch-6`, and `content/batch-7` to match the transcript sequence.
- Lessons 087 and 089 stay intentionally marked as unavailable and are not reconstructed.
- The remaining content-generation portion is complete for every available transcript lesson in this archive.

## 10. Complete source inventory audit (2026-10-30)

### Evidence summary

The original CampusX archive and the extracted transcript directory were audited directly before continuing from lesson 022.

| Metric | Value |
| --- | --- |
| Total archive entries | 134 |
| Transcript files in archive | 132 |
| Additional archive files | 2 |
| Extracted transcript files | 132 |
| Missing lesson numbers | 87, 89 |
| Unavailable / no-caption lessons | 87, 89 |
| Duplicate transcript files | 0 |
| Empty or unreadable transcript files | 0 |
| Original sequence preserved | Yes |

### What this audit confirms

- The archive and extracted folder are in parity.
- There are no missing transcript files beyond the intentionally unavailable lessons 87 and 89.
- The archive contains exactly two non-transcript files: `manifest.json` and `manifest.csv`.
- The extracted transcript set is readable and can be used as the source-of-truth backbone.
- The audit does not claim that every transcript has been content-analyzed; it distinguishes between discovered, read, analyzed, drafted, and validated states.

### Status categories used in the audit

- File discovered: all transcript files exist in the archive and extracted directory
- File successfully read: all extracted transcripts can be opened and decoded
- Content analyzed: only the lessons with corresponding ML Atlas lesson content have been conceptually reviewed
- Lesson drafted: all available lessons 001-134 excluding 087 and 089 have now been drafted in sequence with source traceability
- Lesson validated: previously drafted lessons were checked for source traceability and coverage consistency

### Current lesson pipeline status

- Processed and drafted: 001-134, excluding 087 and 089
- Current backlog: none for available transcript lessons
- Explicitly unavailable lessons: 87 and 89 remain marked as unavailable and are not reconstructed

## 11. Final assembly status (2026-10-31)

- Final standalone output assembled at `dist/ML-Atlas.html`
- Included lesson count: 132 available transcript lessons
- Unavailable lessons preserved: 087 and 089 (no captions)
- Navigation, lesson order, search/filter behavior, and lesson-link integrity were validated against the assembled HTML

## 12. Final coverage thesis

The transcript archive is strong enough to form a complete course backbone. The main improvement work is to convert it into a deeper, more structured educational experience with better explanations, mathematical notation, diagrams, Python exercises, and source-aware organization.
