import csv
from datetime import datetime


#Day 1: Add Job Functionality
def add_job(company, role, location, status):
    with open("data/jobs.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            company,
            role,
            location,
            status,
            datetime.now().strftime("%Y-%m-%d")
        ])
    print("✅ Job added successfully")

#Day 1: Main Loop
if __name__ == "__main__":
    while True:
        print("Job Application Tracker")
        print("1. Add Job")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            company = input("Company: ")
            role = input("Role: ")
            location = input("Location: ")
            status = input("Status (e.g., Applied, Interviewing, Offered): ")
            add_job(company, role, location, status)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")