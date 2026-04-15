"""
email_client.py

Handles connection to the email server (Gmail via IMAP) and retrieval of messages.

Responsibilities:
- Authenticate using credentials from environment variables
- Fetch unread emails from the inbox
- Parse and return structured email data (subject, body, sender, etc.)

Acts as the interface between the program and the email service.
"""