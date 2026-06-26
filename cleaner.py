import pandas as pd

def clean_dataset(input_file, output_file):
    print(f"Loading raw data from {input_file}...")
    
    # 1. Load the data
    df = pd.read_csv(input_file)
    
    # 2. Remove exact duplicate rows
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_rows - len(df)} duplicate rows.")
    
    # 3. Standardize Text (Capitalize first and last names, uppercase departments)
    df['first_name'] = df['first_name'].str.title()
    df['last_name'] = df['last_name'].str.title()
    df['department'] = df['department'].str.upper()
    
    # 4. Handle Missing Data (Nulls)
    # Fill missing ages with the median age of the dataset
    median_age = df['age'].median()
    df['age'] = df['age'].fillna(median_age)
    
    # Fill missing emails with a placeholder
    df['email'] = df['email'].fillna('NO_EMAIL_PROVIDED')
    
    # 5. Export the clean data
    df.to_csv(output_file, index=False)
    print(f"✅ Success! Cleaned data saved to {output_file}")
    
    # Display the final clean dataframe in the terminal
    print("\n--- Cleaned Dataset Preview ---")
    print(df)

if __name__ == "__main__":
    # Define our input and output files
    raw_file = 'messy_data.csv'
    clean_file = 'clean_data.csv'
    
    clean_dataset(raw_file, clean_file)