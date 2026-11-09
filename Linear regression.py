from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the Iris dataset
iris = load_iris()

# Use petal length to predict petal width
X = iris.data[:, [2]]  # Petal length
y = iris.data[:, 3]    # Petal width

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions and evaluate
y_pred = model.predict(X_test)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Mean squared error:", mean_squared_error(y_test, y_pred))
print("R-squared score:", r2_score(y_test, y_pred))

# Predict petal width for a petal length of 4.5 cm
prediction = model.predict([[4.5]])
print("Predicted petal width:", prediction[0])