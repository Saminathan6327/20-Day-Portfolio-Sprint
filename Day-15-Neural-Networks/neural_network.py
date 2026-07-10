import numpy as np
from sklearn.neural_network import MLPClassifier
import warnings

# Suppress minor warnings for a clean terminal
warnings.filterwarnings("ignore")

def run_neural_network():
    print("\n========================================================")
    print(" 🧠 AI DEEP LEARNING: NEURAL NETWORK (MLP)")
    print("========================================================\n")

    # 1. Complex Non-Linear Data (Transaction Fraud Detection)
    # Features: [Transaction Amount (0=Small, 1=Large), Distance from Home (0=Local, 1=International)]
    # Target: 0 = Legit, 1 = FRAUD
    # The logic: Small local is fine. Large international is fine (traveling business).
    # BUT large local? Suspicious. Small international? Suspicious (stolen card testing).
    
    X_train = np.array([
        [0, 0],  # Small amount, local -> Legit (0)
        [1, 1],  # Large amount, international -> Legit (0)
        [1, 0],  # Large amount, local -> FRAUD (1)
        [0, 1]   # Small amount, international -> FRAUD (1)
    ])
    y_train = np.array([0, 0, 1, 1])

    print("Step 1: Loading complex transaction data (Non-linear pattern)...")
    
    # 2. Build the "Brain"
    print("Step 2: Constructing the Neural Network architecture...")
    # We give the AI a "Hidden Layer" of 4 artificial neurons.
    # max_iter=2000 means the brain gets up to 2,000 attempts to adjust its weights and learn.
    ai_brain = MLPClassifier(hidden_layer_sizes=(4,), activation='relu', max_iter=2000, random_state=42)

    # 3. Train the Brain
    print("Step 3: Training the Neural Network (Adjusting synaptic weights)...")
    ai_brain.fit(X_train, y_train)
    # n_iter_ tells us exactly how many cycles it took for the brain to figure out the puzzle
    print(f"Training Complete! The AI learned the pattern in {ai_brain.n_iter_} epochs/cycles. ✅\n")

    # 4. Test the AI's Logic
    print("Step 4: Testing the Artificial Brain's Predictions...")
    print("--------------------------------------------------------")
    
    scenarios = [
        ([0, 0], "Small transaction, local"),
        ([1, 1], "Large transaction, international"),
        ([1, 0], "Large transaction, local"),
        ([0, 1], "Small transaction, international")
    ]

    for data, desc in scenarios:
        # Ask the AI for its prediction and how confident it is
        prediction = ai_brain.predict([data])[0]
        confidence = np.max(ai_brain.predict_proba([data])) * 100
        
        result = "🔴 FRAUD DETECTED" if prediction == 1 else "🟢 LEGITIMATE"
        print(f"Scenario: {desc}")
        print(f"-> Prediction: {result} (Confidence: {confidence:.1f}%)")
        print("--------------------------------------------------------")

if __name__ == "__main__":
    run_neural_network()