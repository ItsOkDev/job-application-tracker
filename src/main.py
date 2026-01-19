import csv
import os
from datetime import datetime
from openpyxl import Workbook
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os


def init_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/jobs.csv"):
        with open("data/jobs.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Company", "Role", "Location", "Status", "Date"])


def export_to_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Job Applications"

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            ws.append(row)

    wb.save("job_applications.xlsx")
    print("✅ Jobs exported to job_applications.xlsx")

def delete_job():
    company_name = input("Enter company name to delete: ").lower()
    updated_rows = []
    found = False

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        updated_rows.append(header)

        for row in reader:
            if row[0].lower() == company_name:
                found = True
                continue  # skip this row (delete)
            updated_rows.append(row)

    if not found:
        print("❌ Company not found. No job deleted.")
        return

    confirm = input("Are you sure you want to delete this job? (yes/no): ").lower()
    if confirm != "yes":
        print("❌ Delete cancelled.")
        return

    with open("data/jobs.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    print("🗑️ Job deleted successfully!")



def send_email_reminders():
    load_dotenv()

    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        print("❌ Email credentials not found.")
        return

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = sender_email  # sending to yourself
    msg["Subject"] = "Job Application Follow-up Reminder"

    body = "Follow up on these job applications:\n\n"
    reminder_found = False

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if row[3].lower() == "applied":
                reminder_found = True
                body += f"- {row[0]} | {row[1]} | {row[2]} | Applied on {row[4]}\n"

    if not reminder_found:
        print("✅ No pending applications for reminder.")
        return

    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("📧 Reminder email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)


def edit_job():
    company_name = input("Enter company name to edit: ").lower()
    updated_rows = []
    found = False

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        updated_rows.append(header)

        for row in reader:
            if row[0].lower() == company_name:
                found = True
                print("\nCurrent Details:")
                print(f"1. Role: {row[1]}")
                print(f"2. Location: {row[2]}")
                print(f"3. Status: {row[3]}")
                print("Press Enter to keep existing value")

                new_role = input("New Role: ")
                new_location = input("New Location: ")
                new_status = input("New Status: ")

                if new_role.strip():
                    row[1] = new_role
                if new_location.strip():
                    row[2] = new_location
                if new_status.strip():
                    row[3] = new_status

            updated_rows.append(row)

    if not found:
        print("❌ Company not found. No changes made.")
        return

    with open("data/jobs.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    print("✏️ Job details updated successfully!")



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

def filter_jobs():
    print("\nFilter Jobs By:")
    print("1. Role")
    print("2. Location")

    option = input("Choose an option: ")

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header
        found = False

        if option == "1":
            role = input("Enter role to filter: ").lower()
            print("\nFiltered Results:")
            for row in reader:
                if role in row[1].lower():
                    print(
                        f"Company: {row[0]}, Role: {row[1]}, "
                        f"Location: {row[2]}, Status: {row[3]}, Date: {row[4]}"
                    )
                    found = True

        elif option == "2":
            location = input("Enter location to filter: ").lower()
            print("\nFiltered Results:")
            for row in reader:
                if location in row[2].lower():
                    print(
                        f"Company: {row[0]}, Role: {row[1]}, "
                        f"Location: {row[2]}, Status: {row[3]}, Date: {row[4]}"
                    )
                    found = True
        else:
            print("❌ Invalid filter option")
            return

        if not found:
            print("❌ No matching job applications found.")


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
        print("1. Add Job")
        print("2. View Jobs")
        print("3. Update Job Status")
        print("4. Search Jobs")
        print("5. Filter Jobs")
        print("6. Export to Excel")
        print("7. Send Email Reminder")
        print("8. Edit Job")
        print("9. Delete Job")
        print("10. Exit")



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
            filter_jobs()
        elif choice == "6":
            export_to_excel()
        elif choice == "7":
            send_email_reminders()
        elif choice == "8":
            edit_job()
        elif choice == "9":
            delete_job()
        elif choice == "10":
            print("Goodbye 👋")
            break


        else:
            print("❌ Invalid choice")