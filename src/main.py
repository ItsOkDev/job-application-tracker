import csv
import os
from datetime import datetime


def init_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/jobs.csv"):
        with open("data/jobs.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Company", "Role", "Location", "Status", "Date"])


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

def search_job():
    print("\n search job by company name")
    print("1. company name")
    print("2. status")

    choice = input("Choose an option: ")

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        print("\nYour Job Applications:")
        for row in reader:
            if choice == "1":
                company_name = input("Enter company name: ")
                if row[0].lower() == company_name.lower():
                    print(
                        f"Company: {row[0]}, Role: {row[1]}, "
                        f"Location: {row[2]}, Status: {row[3]}, Date: {row[4]}"
                    )
            elif choice == "2":
                status = input("Enter status: ")
                if row[3].lower() == status.lower():
                    print(
                        f"Company: {row[0]}, Role: {row[1]}, "
                        f"Location: {row[2]}, Status: {row[3]}, Date: {row[4]}"
                    )
                else:
                    print("No jobs found matching the criteria.")

def view_jobs():
    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        print("\nYour Job Applications:")
        for row in reader:
            print(
                f"Company: {row[0]}, Role: {row[1]}, "
                f"Location: {row[2]}, Status: {row[3]}, Date: {row[4]}"
            )


def update_job_status():
    company_name = input("Enter company name: ")
    updated_rows = []
    found = False

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        updated_rows.append(header)

        for row in reader:
            if row[0].lower() == company_name.lower():
                row[3] = input("Enter new status: ")
                found = True
            updated_rows.append(row)

    if not found:
        print("❌ Company not found")
        return

    with open("data/jobs.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    print("✅ Status updated successfully")


if __name__ == "__main__":
    init_file()

    while True:
        print("\nJob Application Tracker")
        print("1. Add Job")
        print("2. View Jobs")
        print("3. Update Job Status")
        print("4. Search Job")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_job(
                input("Company: "),
                input("Role: "),
                input("Location: "),
                input("Status: ")
            )
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            update_job_status()
        
        elif choice == "4":
            search_job()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice")