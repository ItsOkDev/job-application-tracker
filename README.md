# Job Application Tracker (Python Automation Project)

A Python-based job application tracking system designed to simulate real-world automation and RPA workflows.  
The application allows users to manage job applications efficiently using a command-line interface with secure configuration and clean Git practices.

---

## 🚀 Features
- Add, view, edit, update, and delete job applications (full CRUD)
- Search jobs by company and status
- Filter jobs by role and location
- Export job data to Excel using openpyxl
- Send automated email reminders for pending job applications
- Secure handling of credentials using environment variables (.env)
- Clean Git history with runtime data excluded via .gitignore

---

## 🛠️ Tech Stack
- Python
- CSV File Handling
- openpyxl (Excel Automation)
- SMTP (Email Automation)
- python-dotenv (Environment Variables)
- Git & GitHub
- VS Code

---

## ▶️ How to Run
python src/main.py

```bash
📁 Project Structure
job-application-tracker/
│── src/
│   └── main.py
│── data/
│   └── jobs.csv   # generated at runtime (ignored by Git)
│── .gitignore
│── README.md
```

## 💡 Use Case

This project replicates a real-world job tracking and follow-up system and is designed to be extended into:
RPA workflows (UiPath / Selenium)
Database-backed applications
Scheduled reminder automation

## 🔐 Security Practices

Sensitive credentials are stored using environment variables
.env files are excluded from version control
Runtime data is ignored to maintain clean repositories

## 📌 Future Enhancements

Follow-up reminders based on application date
Export filtered results to Excel
SQL / database integration
UI-based application

## 👤 Author
Devesh Pawar