import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the required VADER AI lexicon (runs automatically in the background)
nltk.download('vader_lexicon', quiet=True)

def analyze_sentiments(data_stream):
    # Initialize the AI Analyzer
    sia = SentimentIntensityAnalyzer()
    
    print("\n========================================================")
    print(" 🧠 AI SENTIMENT ANALYSIS REPORT")
    print("========================================================")
    
    for i, text in enumerate(data_stream, 1):
        # The AI calculates scores for Negative, Neutral, Positive, and a Compound (overall) score
        scores = sia.polarity_scores(text)
        overall_score = scores['compound']
        
        # Categorize based on the compound score
        if overall_score >= 0.05:
            sentiment = "🟢 POSITIVE"
        elif overall_score <= -0.05:
            sentiment = "🔴 NEGATIVE"
        else:
            sentiment = "🟡 NEUTRAL"
            
        print(f"Customer Review {i}:")
        print(f"\"{text}\"")
        print(f"-> AI Classification: {sentiment} (Confidence Score: {overall_score:.2f})")
        print("--------------------------------------------------------")

if __name__ == "__main__":
    # Simulated stream of incoming customer feedback
    customer_reviews = [
        "This laptop is absolutely amazing! Lightning fast and great battery life.",
        "Terrible customer service. My screen broke after 2 days and they won't fix it.",
        "The product is okay. It does the job, but nothing special for the price.",
        "I LOVE this new phone! The camera quality is out of this world!!!",
        "Shipping was delayed by three weeks. Completely unacceptable."
    ]
    
    print("Initializing NLP Engine...")
    analyze_sentiments(customer_reviews)