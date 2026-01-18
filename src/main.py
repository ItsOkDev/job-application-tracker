import csv
from datetime import datetime

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



def view_jobs():
    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        print("\n--- Job Applications ---")
        for row in reader:
            print(f"Company: {row[0]}, Role: {row[1]}, Location: {row[2]}, Status: {row[3]}, Date: {row[4]}")


if __name__ == "__main__":
    print("1. Add Job")
    print("2. View Jobs")

    choice = input("Choose an option: ")

    if choice == "1":
        company = input("Company Name: ")
        role = input("Role: ")
        location = input("Location: ")
        status = input("Status (Applied / Interview / Rejected): ")
        add_job(company, role, location, status)
        print("✅ Job added successfully!")

    elif choice == "2":
        view_jobs()
