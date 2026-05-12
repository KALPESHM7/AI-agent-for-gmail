# OpenClaw AI Email + WhatsApp Agent

## GitHub Repository

Repository Link:

```text
https://github.com/KALPESHM7/AI-agent-for-gmail
```

---

# What This Project Does

This project automatically:

* reads unread Gmail emails
* identifies IT-related issues
* summarizes the issue using AI
* sends email notifications
* sends WhatsApp notifications
* repeats automatically every 60 seconds

Example Issues:

* laptop slow
* WiFi issue
* login problem
* VPN problem
* system crash

---

# Technologies Used

* OpenClaw
* Python
* Ollama
* llama3 AI model
* Gmail
* WhatsApp Web

---

# IMPORTANT

Please follow ALL steps carefully.

Use:

```text
Windows PowerShell (Run as Administrator)
```

for installation commands.

---

# STEP 1 — Install VS Code

Download:

```text
https://code.visualstudio.com/
```

Install normally.

Verify Installation:

Open PowerShell and run:

```powershell
code --version
```

If version appears, installation is successful.

---

# STEP 2 — Install Git

Download:

```text
https://git-scm.com/downloads/win
```

Install normally.

IMPORTANT:

During installation make sure:

```text
Add Git to PATH
```

is enabled.

Verify Installation:

```powershell
git --version
```

---

# STEP 3 — Install Python

Download:

```text
https://www.python.org/downloads/
```

Install Python 3.11 or higher.

IMPORTANT:

During installation CHECK:

```text
Add Python to PATH
```

Verify Installation:

```powershell
python --version
```

---

# STEP 4 — Install Node.js

Download:

```text
https://nodejs.org/
```

Install LTS version.

Verify Installation:

```powershell
node -v
npm -v
```

---

# STEP 5 — Install pnpm

Open PowerShell as Administrator.

Run:

```powershell
npm install -g pnpm
```

Verify:

```powershell
pnpm -v
```

---

# STEP 6 — Install Ollama

Download:

```text
https://ollama.com/download
```

Install normally.

Verify:

```powershell
ollama list
```

---

# STEP 7 — Download AI Model

Run:

```powershell
ollama run llama3:8b
```

Wait until model downloads completely.

After it starts:

```text
Press Ctrl + C
```

The model remains installed.

---

# STEP 8 — Install OpenClaw

Open PowerShell as Administrator.

Run:

```powershell
git clone https://github.com/openclaw/openclaw.git
```

Open folder:

```powershell
cd openclaw
```

Install dependencies:

```powershell
pnpm install
```

Verify Installation:

```powershell
pnpm dev
```

If OpenClaw screen appears successfully:

```text
OpenClaw installed successfully
```

Then close terminal.

---

# STEP 9 — Download This Project

Open NEW PowerShell.

Go to Desktop:

```powershell
cd Desktop
```

Clone project:

```powershell
git clone https://github.com/KALPESHM7/AI-agent-for-gmail.git
```

Open project folder:

```powershell
cd AI-agent-for-gmail
```

Verify files exist:

```text
requirements.txt
README.md
workspace-dev/
```

---

# STEP 10 — Create Python Virtual Environment

Run:

```powershell
python -m venv venv
```

Activate environment:

```powershell
.\venv\Scripts\activate
```

If successful you will see:

```text
(venv)
```

in terminal.

---

# STEP 11 — Install Python Packages

Run:

```powershell
pip install -r requirements.txt
```

Wait until installation finishes.

---

# STEP 12 — Copy Workspace Files Into OpenClaw

Open:

```text
AI-agent-for-gmail/workspace-dev
```

You will see:

```text
agent_task.txt
email_agent.py
run_agent.py
test_whatsapp.py
```

Copy ALL these files.

Now open:

```text
openclaw/workspace-dev
```

Paste all copied files there.

Final structure should look like:

```text
openclaw/
└── workspace-dev/
    ├── agent_task.txt
    ├── email_agent.py
    ├── run_agent.py
    └── test_whatsapp.py
```

---

# STEP 13 — Gmail Setup

Open:

```text
https://myaccount.google.com/security
```

Enable:

```text
2-Step Verification
```

---

# STEP 14 — Generate Gmail App Password

Open:

```text
https://myaccount.google.com/apppasswords
```

Generate:

```text
Mail → Windows Computer
```

Copy generated password.

Example:

```text
abcd efgh ijkl mnop
```

---

# STEP 15 — Add Your Credentials

Open:

```text
openclaw/workspace-dev/email_agent.py
```

Replace:

```python
EMAIL_USER = "your_email@gmail.com"
EMAIL_PASS = "your_app_password"
```

with real Gmail credentials.

---

# STEP 16 — WhatsApp Setup

Requirements:

* Google Chrome installed
* WhatsApp account active

During first run:

Browser opens automatically.

Scan QR code using WhatsApp mobile app.

Wait until WhatsApp Web logs in successfully.

---

# STEP 17 — Start Ollama

Open NEW PowerShell.

Run:

```powershell
ollama run llama3:8b
```

Wait until:

```text
>>>
```

appears.

Then press:

```text
Ctrl + C
```

---

# STEP 18 — Run AI Agent

Open NEW PowerShell.

Go to:

```powershell
cd Desktop
cd openclaw
cd workspace-dev
```

Activate virtual environment:

```powershell
cd ../../AI-agent-for-gmail
.\venv\Scripts\activate
cd ../openclaw/workspace-dev
```

Run Agent:

```powershell
python run_agent.py
```

---

# SUCCESSFUL OUTPUT

If working correctly you will see:

```text
Checking emails...

EMAIL RECEIVED

AI SUMMARY:

Email notification sent!

WhatsApp notifications sent!
```

The system repeats automatically every 60 seconds.

---

# HOW TO TEST

Send email from another Gmail account.

Example:

Subject:

```text
Laptop Issue
```

Body:

```text
My laptop is very slow and restarting automatically.
```

Expected Result:

* AI reads email
* AI summarizes issue
* email notification sent
* WhatsApp notification sent

---

# Files Included

| File             | Purpose                        |
| ---------------- | ------------------------------ |
| email_agent.py   | Main AI email workflow         |
| run_agent.py     | Runs workflow every 60 seconds |
| test_whatsapp.py | WhatsApp testing               |
| agent_task.txt   | OpenClaw task description      |
| requirements.txt | Python package list            |

---

# Troubleshooting

## Problem: Python not recognized

Solution:

Reinstall Python and CHECK:

```text
Add Python to PATH
```

---

## Problem: Ollama not recognized

Restart system after Ollama installation.

---

## Problem: WhatsApp not sending

* Ensure WhatsApp Web logged in
* Keep internet connected
* Keep browser open during first setup

---

## Problem: Gmail login failed

Ensure:

* 2-Step Verification enabled
* App Password used
* NOT normal Gmail password

---

# Final Workflow

```text
Gmail Email
    ↓
Python Reads Email
    ↓
OpenClaw Workflow
    ↓
AI Filtering
    ↓
Ollama AI Summarization
    ↓
Email Notification
    ↓
WhatsApp Notification
    ↓
Repeats Every 60 Seconds
```

---

# Project Status

Current Features:

* Gmail Monitoring
* AI Summarization
* WhatsApp Alerts
* Email Alerts
* OpenClaw Workflow
* Local AI using Ollama
* Continuous Automation
* IT Issue Filtering

```
```
