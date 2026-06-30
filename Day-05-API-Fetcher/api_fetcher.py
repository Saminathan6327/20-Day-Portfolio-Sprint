import requests
import json
from datetime import datetime

def fetch_live_rates(base_currency):
    # Public open-access API endpoint (No API key required)
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    
    print(f"Connecting to live API endpoint: {url}...")
    try:
        # Send HTTP GET request to the internet
        response = requests.get(url)
        
        # Check if connection was successful (HTTP 200 OK)
        if response.status_code == 200:
            print("🚀 Connection successful! Parsing live payload...")
            
            # Extract JSON data from the response
            data = response.json()
            
            # Parse metadata
            last_update = data.get("time_last_update_utc", "Unknown")
            rates = data.get("rates", {})
            
            # Format and isolate target currencies for display
            target_currencies = ["INR", "USD", "EUR", "GBP", "AED", "SGD"]
            
            print("\n========================================================")
            print(f" LIVE CURRENCY EXCHANGE DASHBOARD (Base: {base_currency})")
            print("========================================================")
            print(f"Data Last Updated (UTC): {last_update}")
            print(f"Timestamp Processed:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("--------------------------------------------------------")
            print(f"  Currency  |  Exchange Rate Value")
            print("--------------------------------------------------------")
            
            for currency in target_currencies:
                if currency in rates:
                    print(f"    {currency}     |  {rates[currency]:,.4f}")
            print("========================================================")
            
        else:
            print(f"❌ Failed to fetch data. Server responded with status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: Could not connect to the API server. Details: {e}")

if __name__ == "__main__":
    # Run the live analytics platform using USD as the base currency
    fetch_live_rates("USD")