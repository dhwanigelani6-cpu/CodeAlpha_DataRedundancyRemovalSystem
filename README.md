
# CodeAlpha Data Redundancy Removal System

## Project Overview
The Data Redundancy Removal System is a Python-based web
application that validates incoming records and prevents duplicate
data from being stored in a database.

## Objectives
- Validate user input before saving records.
- Identify duplicate email addresses.
- Classify possible duplicate names as potential false positives.
- Store unique and verified records.
- Improve data accuracy and database consistency.

## Technologies Used
- Python
- Flask
- SQLite
- HTML
- CSS
- GitHub

## Features
- User-friendly web interface.
- Name, email and phone validation.
- Case-insensitive email duplicate detection.
- Possible false-positive classification.
- SQLite database storage.
- Record listing and duplicate rejection.

## Project Structure
- app.py: Main Flask application.
- database.py: Database connection and queries.
- validator.py: Validation and classification logic.
- templates/index.html: Web interface.
- static/style.css: Interface styling.
- requirements.txt: Python dependency.
- .gitignore: Excluded local files.

## Requirements
- Python 3.10 or newer.
- pip.

## Installation and Execution

1. Clone this repository:
   git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project directory:
   cd CodeAlpha_DataRedundancyRemovalSystem

3. Create a virtual environment:
   python -m venv .venv

4. Activate the environment.

   Windows:
   .venv\Scripts\activate

   macOS/Linux:
   source .venv/bin/activate

5. Install dependencies:
   pip install -r requirements.txt

6. Start the application:
   python app.py

7. Open this address in your browser:
   http://127.0.0.1:5000

## Testing
1. Add a new name and email.
2. Submit the same email again using different letter case.
3. Confirm that the duplicate is rejected.
4. Submit a different email with the same name.
5. Confirm that the possible false positive is identified.
6. Check that the saved records are displayed.

## Database Integrity
Email addresses are normalized to lowercase before insertion.
SQLite also enforces a UNIQUE constraint on the email column.

## Limitations
This is a local demonstration application. It does not include
cloud hosting, user authentication, or production-grade security.

## Future Improvements
- Deploy to a cloud platform.
- Add user authentication and authorization.
- Add automated tests and monitoring.
- Use managed cloud database storage.

## Internship
CodeAlpha Cloud Computing Internship - Task 1
# CodeAlpha_DataRedundancyRemovalSystem
Python-based Data Redundancy Removal System that validates incoming records and prevents duplicate entries using SQLite.
