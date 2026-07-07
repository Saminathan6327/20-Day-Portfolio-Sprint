import numpy as np
from sklearn.linear_model import LinearRegression

def train_and_predict():
    print("\n========================================================")
    print(" 🤖 AI PREDICTIVE MODEL: SALARY ESTIMATOR")
    print("========================================================\n")

    # 1. Historical Data (The "Experience" the AI learns from)
    # X = Years of Experience (Needs to be a 2D array for Scikit-Learn)
    # y = Salary in USD
    X_train = np.array([[1], [2], [3], [4], [5], [7], [8], [10]])
    y_train = np.array([45000, 52000, 60000, 63000, 72000, 85000, 92000, 110000])

    print("Step 1: Loading Historical Data...")
    print(f"Data points loaded: {len(X_train)} employee records.")
    
    # 2. Initialize the Machine Learning Model
    print("Step 2: Initializing Linear Regression Engine...")
    model = LinearRegression()

    # 3. Train the Model (The AI mathematically finds the line of best fit)
    print("Step 3: Training the AI on historical data...")
    model.fit(X_train, y_train)
    print("Training Complete! ✅\n")

    # 4. Make Predictions on NEW, UNSEEN Data
    # Let's ask the AI to predict salaries for 6 years, 15 years, and 20 years of experience
    X_new = np.array([[6], [15], [20]])
    print("Step 4: Making Predictions on UNSEEN Data...")
    predictions = model.predict(X_new)

    # 5. Display the Results
    for i in range(len(X_new)):
        years = X_new[i][0]
        predicted_salary = predictions[i]
        print(f"-> For {years} years of experience, AI predicts a salary of: ${predicted_salary:,.2f}")

    print("\n========================================================")
    # Exposing the AI's internal logic (y = mx + b)
    print(f"🧠 ML Insight: How did the AI calculate this?")
    print(f"   - It calculated a starting base salary of ${model.intercept_:,.2f}")
    print(f"   - It determined each year of experience is worth exactly ${model.coef_[0]:,.2f}")
    print("========================================================")

if __name__ == "__main__":
    train_and_predict()