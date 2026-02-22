# 📧 Google OAuth Based Email Management System

A Python-based Gmail Automation System that integrates with the Gmail
API using Google OAuth 2.0 for secure authentication and automated email
operations.

This project enables users to securely authenticate with Gmail, fetch
recent emails, categorize them, detect attachments, send emails, and
delete emails (individually or in bulk) through a structured
command-line interface.

------------------------------------------------------------------------

## 🚀 Features

-   Secure authentication using Google OAuth 2.0
-   Fetch top 5 latest emails
-   Rule-based email categorization
-   Attachment detection with MIME type identification
-   Send emails programmatically
-   Delete individual emails
-   Bulk delete emails by category
-   Modular and scalable architecture
-   Interactive CLI-based interface

------------------------------------------------------------------------

## 🏗️ Project Structure

    Google-OAuth-Based-Email-Management/
    │
    ├── main.py
    ├── auth.py
    ├── fetch.py
    ├── categorize.py
    ├── actions.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

## 🔐 Authentication (Google OAuth 2.0)

The system uses Google OAuth 2.0 to securely access Gmail services.

### Scopes Used

``` python
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]
```

-   gmail.modify → Required for deleting emails
-   gmail.send → Required for sending emails

### Authentication Flow

1.  Checks if token.json exists
2.  Reuses stored credentials if valid
3.  Opens browser login if missing or expired
4.  Saves credentials locally

------------------------------------------------------------------------

## 📥 Email Fetching

Retrieves the latest 5 emails and extracts:

-   Sender
-   Subject
-   Attachment presence
-   Attachment MIME types

------------------------------------------------------------------------

## 🏷️ Email Categorization

  Keywords            Category
  ------------------- -------------
  OTP, Verification   Security
  Invoice, Payment    Finance
  Offer, Sale         Promotional
  Others              General

------------------------------------------------------------------------

## 📤 Sending Emails

1.  Create message using MIMEText
2.  Encode using Base64
3.  Send via Gmail API

------------------------------------------------------------------------

## 🗑️ Email Deletion

### Single Delete

Select email number and confirm deletion.

### Bulk Delete

Delete all emails from selected category.

------------------------------------------------------------------------

## 📦 Requirements

-   Python 3.8+
-   Internet connection
-   Google account

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ⚙️ Setup

1.  Enable Gmail API in Google Cloud Console
2.  Create OAuth Client ID (Desktop App)
3.  Download credentials
4.  Rename file to:

```{=html}
<!-- -->
```
    client_secret.json

5.  Place it in project root directory

------------------------------------------------------------------------

## ▶️ Usage

Run:

``` bash
python main.py
```

On first run, browser authentication will be required.\
token.json will be generated automatically.

------------------------------------------------------------------------

## 🛡️ Security Notes

Do NOT share:

    client_secret.json
    token.json

------------------------------------------------------------------------

## 👨‍💻 Tech Stack

-   Python
-   Google OAuth 2.0
-   Gmail API
-   REST API Integration

------------------------------------------------------------------------

## 📄 License

Educational and research purposes only.
