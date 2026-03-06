# ============================================================
# FILE: JOB APPLICATION TRACKER (PYTHON CLI PROJECT)
# Topic: File Handling, Automation, and Job Tracking System
# WHY: Job seekers apply to many companies and lose track of
# application status. This tool stores applications, allows
# searching/filtering, exports reports, and sends reminders.
# ============================================================

# ============================================================
# EXAMPLE 1 — Real World Story
# Story: Suppose you applied to:
#
# Amazon – Data Analyst
# Google – ML Engineer
# Flipkart – Data Scientist
#
# After a week you forget:
# - Which company you applied to
# - Which role
# - When you applied
# - When to follow up
#
# This Job Tracker solves that problem.
# ============================================================


# ============================================================
# IMPORT REQUIRED LIBRARIES
# ============================================================

import csv
import os
from datetime import datetime
from openpyxl import Workbook
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


# ============================================================
# FUNCTION 1 — Initialize Storage
# WHY: Ensure the data folder and CSV file exist before using
# the system.
# ============================================================

def init_file():

    # Create data folder if it does not exist
    os.makedirs("data", exist_ok=True)

    # Create CSV file if missing
    if not os.path.exists("data/jobs.csv"):

        with open("data/jobs.csv", "w", newline="") as file:
            writer = csv.writer(file)

            # CSV Header
            writer.writerow(["Company", "Role", "Location", "Status", "Date"])


# ============================================================
# FUNCTION 2 — Add Job Application
# Story: User applied to Amazon for Data Analyst role
# ============================================================

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


# ============================================================
# FUNCTION 3 — View All Jobs
# ============================================================

def view_jobs():

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        print("\nYour Job Applications:")

        for row in reader:
            print(
                f"Company: {row[0]}, "
                f"Role: {row[1]}, "
                f"Location: {row[2]}, "
                f"Status: {row[3]}, "
                f"Date: {row[4]}"
            )


# ============================================================
# FUNCTION 4 — Update Job Status
# Story: Amazon changed status from Applied → Interview
# ============================================================

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


# ============================================================
# FUNCTION 5 — Search Job
# ============================================================

def search_job():

    print("\nSearch Job By:")
    print("1. Company Name")
    print("2. Status")

    choice = input("Choose option: ")
    with open("data/jobs.csv", "r") as file:

        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if choice == "1":
                company_name = input("Enter company name: ")
                if row[0].lower() == company_name.lower():
                    print(row)

            elif choice == "2":
                status = input("Enter status: ")
                if row[3].lower() == status.lower():
                    print(row)


# ============================================================
# FUNCTION 6 — Filter Jobs
# ============================================================

def filter_jobs():

    print("\nFilter Jobs By:")
    print("1. Role")
    print("2. Location")

    option = input("Choose option: ")

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        found = False

        if option == "1":
            role = input("Enter role: ").lower()

            for row in reader:
                if role in row[1].lower():
                    print(row)
                    found = True

        elif option == "2":
            location = input("Enter location: ").lower()

            for row in reader:
                if location in row[2].lower():
                    print(row)
                    found = True
        if not found:
            print("❌ No matching jobs found")


# ============================================================
# FUNCTION 7 — Export Data to Excel
# ============================================================

def export_to_excel():

    wb = Workbook()
    ws = wb.active
    ws.title = "Job Applications"
    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            ws.append(row)
    wb.save("job_applications.xlsx")
    print("✅ Exported to Excel")


# ============================================================
# FUNCTION 8 — Email Reminder
# ============================================================

def send_email_reminders():
    load_dotenv()
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        print("❌ Email credentials missing")
        return

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = sender_email
    msg["Subject"] = "Job Application Reminder"
    body = "Follow up on these jobs:\n\n"

    with open("data/jobs.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if row[3].lower() == "applied":
                body += f"{row[0]} | {row[1]} | {row[2]}\n"

    msg.set_content(body)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)
    print("📧 Reminder email sent")


# ============================================================
# MAIN PROGRAM — CLI MENU
# ============================================================

if __name__ == "__main__":

    init_file()

    while True:

        print("\n=== Job Application Tracker ===")

        print("1 Add Job")
        print("2 View Jobs")
        print("3 Update Status")
        print("4 Search Job")
        print("5 Filter Jobs")
        print("6 Export Excel")
        print("7 Send Reminder")
        print("8 Exit")

        choice = input("Choose option: ")

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
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice")


# ============================================================
# TIME COMPLEXITY SUMMARY
# ============================================================

# Add Job → O(1)
# View Jobs → O(n)
# Update Status → O(n)
# Search Job → O(n)
# Filter Job → O(n)
# Export Excel → O(n)

# n = number of job applications


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Demonstrates Python file handling using CSV
# 2. Implements CRUD operations (Create, Read, Update, Delete)
# 3. Automates job tracking
# 4. Exports reports to Excel
# 5. Sends automated email reminders
# 6. Real-world CLI productivity tool