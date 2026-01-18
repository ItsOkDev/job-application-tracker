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

#Day 2: View Jobs Functionality
def view_jobs():
    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        print("Your Job Applications:")
        for row in reader:
            print(f"Company: {row[0]}, Role: {row[1]}, Location: {row[2]}, Status: {row[3]}, Date Applied: {row[4]}")


#Day 1: Main Loop
if __name__ == "__main__":
    while True:
        print("Job Application Tracker")
        print("1. Add Job")
        print("2. View Jobs")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            company = input("Company: ")
            role = input("Role: ")
            location = input("Location: ")
            status = input("Status (e.g., Applied, Interviewing, Offered): ")
            add_job(company, role, location, status)
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


        