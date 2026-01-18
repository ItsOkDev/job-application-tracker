import csv
from datetime import datetime

def add_job(company, role, location, status):       # function expects 4, got 4
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


def update_job_status():
    company_name = input("Enter company name to update: ")
    updated_rows = []
    found = False

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        updated_rows.append(header)

        for row in reader:
            if row[0].lower() == company_name.lower():
                new_status = input("Enter new status (Applied / Interview / Rejected): ")
                row[3] = new_status
                found = True
            updated_rows.append(row)

    if not found:
        print("❌ Company not found.")
        return

    with open("data/jobs.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    print("✅ Job status updated successfully!")


if __name__ == "__main__":
    while True:
        print("\n--- Job Application Tracker ---")
        print("1. Add Job")
        print("2. View Jobs")
        print("3. Update Job Status")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            company = input("Company Name: ")
            role = input("Role: ")
            location = input("Location: ")
            status = input("Status (Applied / Interview / Rejected): ")
            add_job(company, role, location, status)

        elif choice == "2":
            view_jobs()

        elif choice == "3":
            update_job_status()

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid option. Try again.")
