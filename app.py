"""
Email Prioritization System (Flask Backend)

Purpose:
This application processes batches of student emails, uses AI to:
- classify each email into categories (deadlines, requests, issues, etc.)
- assign priority levels (1–5)
- generate concise summaries
- group emails by category
- generate professional reply drafts for counselors

Designed to help school counselors manage high email volume efficiently.
"""

# Flask web framework for routing and rendering HTML templates
from flask import Flask, render_template, request

# OpenAI client for LLM-based classification and reply generation
from openai import OpenAI

import json
from collections import defaultdict

# Initialize Flask app
app = Flask(__name__)

# OpenAI API client initialization
# NOTE: Replace with environment variable in production for security
client = OpenAI(api_key="INSERT_API_KEY")


# ----------------------------
# PARSE EMAILS
# ----------------------------
# Converts raw pasted email text into structured email dictionaries
# Expected format:
# From: ...
# Subject: ...
# Body: ...
# ---
def parse_emails(raw_text):
    emails = []
    blocks = raw_text.strip().split('---')  # Each email separated by ---

    for block in blocks:
        lines = block.strip().split('\n')

        # Default structure for each email
        email = {"sender": "", "subject": "", "body": ""}

        for line in lines:
            # Extract sender field
            if line.startswith("From:"):
                email["sender"] = line.replace("From:", "").strip()

            # Extract subject field
            elif line.startswith("Subject:"):
                email["subject"] = line.replace("Subject:", "").strip()

            # Extract body field
            elif line.startswith("Body:"):
                email["body"] = line.replace("Body:", "").strip()

        # Only add valid emails (must have body content)
        if email["body"]:
            emails.append(email)

    return emails


# ----------------------------
# CLASSIFY EMAIL
# ----------------------------
# Uses OpenAI to classify email into category + priority + summary
def classify_email(email):
    prompt = f"""
Return ONLY valid JSON.

Analyze this student email and return:
- category (Deadlines, Schedule Changes, Course Requests, Administrative Issues, General Questions, Other)
- priority (1-5)
- summary (1 short sentence)

Email:
Subject: {email['subject']}
Body: {email['body']}
"""

    # Call OpenAI model for classification
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    # Try parsing model output as JSON
    try:
        return json.loads(response.choices[0].message.content)
    except:
        # Fallback in case model output is invalid JSON
        return {"category": "Other", "priority": 3, "summary": "Parsing error"}


# ----------------------------
# GENERATE REPLY
# ----------------------------
# Generates a professional response email based on grouped summaries
def generate_reply(category, summaries):
    combined = "\n".join(summaries)

    prompt = f"""
Write a professional, concise email reply.

Category: {category}
Questions:
{combined}
"""

    # Call OpenAI model for response generation
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content


# ----------------------------
# MAIN ROUTE
# ----------------------------
# Handles both GET (load page) and POST (process emails)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Get raw email input from frontend form
        raw_text = request.form["emails"]

        # Step 1: Parse raw text into structured emails
        emails = parse_emails(raw_text)

        processed = []

        # Step 2: Classify each email using AI
        for email in emails:
            analysis = classify_email(email)
            processed.append({
                "email": email,
                "analysis": analysis
            })

        # Step 3: Sort emails by priority (highest first)
        processed.sort(key=lambda x: x["analysis"]["priority"], reverse=True)

        # Step 4: Group emails by category for easier management
        groups = defaultdict(list)
        for item in processed:
            groups[item["analysis"]["category"]].append(item)

        # Step 5: Generate one AI reply per category
        replies = {}
        for category, items in groups.items():
            summaries = [i["analysis"]["summary"] for i in items]
            replies[category] = generate_reply(category, summaries[:5])

        # Render results in UI
        return render_template("index.html",
                               processed=processed,
                               groups=groups,
                               replies=replies)

    # GET request → show empty page
    return render_template("index.html", processed=None)


# ----------------------------
# RUN APP
# ----------------------------
if __name__ == "__main__":
    # Enable debug mode for development (auto-reload + error logs)
    app.run(debug=True)
