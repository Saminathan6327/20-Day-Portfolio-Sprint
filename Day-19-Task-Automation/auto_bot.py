import schedule
import time
from datetime import datetime
import random

def automated_job():
    """This is the task we want to run automatically."""
    # Get the exact current time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"[{now}] ⚙️ CRON TRIGGERED: Running automated background task...")
    
    # Simulate doing some "heavy" work (like scraping a site or updating a database)
    time.sleep(1)
    
    # Generate a fake metric to make our logs look like a real data pipeline
    records_synced = random.randint(100, 999)
    print(f"[{now}] ✅ SUCCESS: {records_synced} records synced to the cloud.\n")

def run_scheduler():
    print("\n========================================================")
    print(" 🤖 AUTOMATION BOT INITIALIZED")
    print("========================================================")
    print("-> The bot is now running in the background.")
    print("-> It is scheduled to run a data sync every 4 seconds.")
    print("-> Press CTRL+C to kill the bot.\n")

    # 1. Define the Schedule
    # You can easily change this to: schedule.every().day.at("10:30").do(automated_job)
    # Or: schedule.every().monday.do(automated_job)
    schedule.every(4).seconds.do(automated_job)

    # 2. Start the Infinite Loop
    # The script will live in this loop forever, checking if it's time to run a job
    try:
        while True:
            # Check if any scheduled jobs are due to run right now
            schedule.run_pending()
            
            # Sleep for 1 second so we don't max out the computer's CPU
            time.sleep(1)
            
    except KeyboardInterrupt:
        # This catches the CTRL+C command so the script exits cleanly
        print("\n🛑 SHUTDOWN SIGNAL RECEIVED. Terminating Automation Bot.")
        print("Goodbye!")

if __name__ == "__main__":
    run_scheduler()