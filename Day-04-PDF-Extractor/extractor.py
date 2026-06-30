import re

def extract_structured_data(file_path):
    print(f"Opening and parsing text stream from {file_path}...\n")
    
    with open(file_path, 'r') as file:
        text_content = file.read()
        
    # Define Regular Expression patterns for targeted data points
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    id_pattern = r'\b[A-Z]{3}-\d{4}-\d{4}\b|\b[A-Z]{3}-\d{6}-[A-Z]\b'

    # Execute text scanning matching operations
    found_emails = re.findall(email_pattern, text_content)
    found_dates = re.findall(date_pattern, text_content)
    found_ids = re.findall(id_pattern, text_content)

    # Output extracted findings structured cleanly
    print("========================================================")
    print("EXTRACTED STRUCTURED PROFILE DATA")
    print("========================================================")
    
    print("\n[+] Identified Email Addresses:")
    for email in found_emails:
        print(f" -> {email}")
        
    print("\n[+] Identified Timestamps & Dates:")
    for date in found_dates:
        print(f" -> {date}")
        
    print("\n[+] Identified System Reference IDs:")
    for system_id in found_ids:
        print(f" -> {system_id}")
    print("========================================================")

if __name__ == "__main__":
    target_document = "raw_report.txt"
    extract_structured_data(target_document)