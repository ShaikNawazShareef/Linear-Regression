# 🌸 Linear Regression – Iris Dataset

## 📌 Project Overview

This project demonstrates **Simple Linear Regression** using Python and Scikit-learn.

The objective is to predict the **petal width** of an Iris flower based on its **petal length** using a Linear Regression model.

The project uses the built-in Iris dataset from Scikit-learn to train, test, and evaluate the machine learning model.

## 🎯 Objectives

- Understand Simple Linear Regression.
- Load and explore the Iris dataset.
- Split data into training and testing sets.
- Train a Linear Regression model.
- Predict petal width using petal length.
- Evaluate model performance using MSE and R² score.

## 🛠️ Technologies Used

- Python
- NumPy
- Scikit-learn
- Machine Learning
- VS Code
- Git & GitHub

## 📂 Dataset Information

**Dataset:** Iris Dataset

**Source:** Scikit-learn built-in dataset.

| Feature | Description |
|---|---|
| Input (X) | Petal Length |
| Output (y) | Petal Width |

The model uses petal length to predict petal width.

## ⚙️ Project Workflow

1. Import required Python libraries.
2. Load the Iris dataset.
3. Select petal length as the input feature.
4. Select petal width as the target variable.
5. Split the dataset into training and testing sets (80% training and 20% testing).
6. Train the Linear Regression model.
7. Generate predictions.
8. Evaluate model performance.

## 📊 Model Evaluation

The model is evaluated using the following metrics:

- **Slope:** Represents the change in predicted petal width for each 1 cm increase in petal length.
- **Intercept:** The predicted petal width when petal length is zero.
- **Mean Squared Error (MSE):** Measures the average squared prediction error. Lower values indicate better predictions.
- **R² Score:** Measures how much variation in petal width is explained by the model. A value closer to 1 indicates a better fit.

## 🔮 Prediction Example

The model predicts petal width when the petal length is **4.5 cm**.

```python
prediction = model.predict([[4.5]])
```

The predicted petal width is displayed in the output.

## 🚀 How to Run This Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd Linear-Regression
```

### 3. Install the required library

```bash
pip install scikit-learn
```

### 4. Run the Python program

```bash
python linear_regression.py
```

## 📁 Project Structure

```text
Linear-Regression/
│
├── linear_regression.py
├── README.md
└── requirements.txt
```

## 📚 Learning Outcomes

- Learned the fundamentals of Linear Regression.
- Understood training and testing data.
- Practiced model training using Scikit-learn.
- Learned prediction and model evaluation.
- Gained practical experience with machine learning.

## 👨‍💻 Author

**Nawaz Shaik**

GitHub: https://github.com/ShaikNawazShareef

---

⭐ If you find this project useful, feel free to star this repository!
