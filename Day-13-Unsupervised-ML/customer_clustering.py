import numpy as np
from sklearn.cluster import KMeans
import warnings

# Suppress minor warnings for a cleaner terminal output
warnings.filterwarnings("ignore")

def discover_customer_segments():
    print("\n========================================================")
    print(" 🤖 AI UNSUPERVISED MODEL: CUSTOMER SEGMENTATION")
    print("========================================================\n")

    # 1. Raw Data (No labels, no categories—just raw numbers)
    # Format: [Annual Income (in $1,000s), Spending Score (1 to 100)]
    customer_data = np.array([
        [15, 20], [16, 25], [18, 15], [20, 22],  # Group A?
        [80, 90], [85, 85], [90, 95], [100, 90], # Group B?
        [50, 50], [55, 45], [60, 55], [65, 50]   # Group C?
    ])

    print("Step 1: Loading raw customer financial data...")
    print(f"Loaded {len(customer_data)} uncategorized customer profiles.\n")

    # 2. Initialize the AI (We ask it to find 3 distinct groups)
    print("Step 2: Initializing K-Means Clustering Algorithm...")
    # We tell the AI to look for 3 clusters, but we DON'T tell it what they mean
    ai_model = KMeans(n_clusters=3, random_state=42, n_init=10)

    # 3. Train the AI to find patterns
    print("Step 3: AI is scanning data for hidden mathematical clusters...")
    clusters = ai_model.fit_predict(customer_data)
    print("Clustering Complete! ✅\n")

    # 4. Display the AI's Discoveries
    print("Step 4: Analyzing the AI's groupings...")
    print("--------------------------------------------------------")
    
    # We will loop through the data and show which cluster the AI assigned to each customer
    for i in range(len(customer_data)):
        income = customer_data[i][0]
        spend_score = customer_data[i][1]
        assigned_group = clusters[i]
        
        # Adding some human-readable context to the AI's mathematical groups
        if assigned_group == 0:
            profile = "🟢 Middle Income / Average Spenders"
        elif assigned_group == 1:
            profile = "🔴 Low Income / Low Spenders"
        else:
            profile = "⭐ HIGH INCOME / VIP SPENDERS"
            
        print(f"Customer {i+1} [Income: ${income}k, Spend Score: {spend_score}/100] -> {profile}")

    print("\n========================================================")
    # Exposing the AI's internal logic (The Cluster Centers)
    print("🧠 ML Insight: What are the mathematical centers of these groups?")
    centers = ai_model.cluster_centers_
    for idx, center in enumerate(centers):
        print(f"   - Group {idx} Center: ~${center[0]:.0f}k Income, ~{center[1]:.0f} Spend Score")
    print("========================================================")

if __name__ == "__main__":
    discover_customer_segments()