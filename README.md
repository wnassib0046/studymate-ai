# StudyMate AI

## Presentation

StudyMate AI is a simple educational web application built with **Flask**.
It helps students ask basic questions about:

- HTML
- CSS
- Flask
- Python
- frontend and backend
- beginner web project ideas

This project does **not** use real artificial intelligence.
The chatbot works with simple programmed logic using conditions in Python.

## Main Features

- modern home page
- user registration
- user login
- chat interface
- suggested questions
- session-based chat history
- simple rule-based answers

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Jinja2

## Project Structure

```text
PROJET WEB/
|-- app.py
|-- README.md
|-- static/
|   `-- css/
|       `-- style.css
`-- templates/
    |-- base.html
    |-- index.html
    |-- login.html
    |-- register.html
    `-- chat.html
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-link>
cd "PROJET WEB"
```

### 2. Create a virtual environment

```bash
py -m venv venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

### 4. Install Flask

```bash
pip install Flask
```

## Run the Application

```bash
py app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## How to Use

1. Open the home page.
2. Click `Register` to create an account.
3. Log in with your username and password.
4. Open the chat page.
5. Ask a question or click one of the suggested prompts.
6. Read the chatbot response.
7. Use `New Chat` to clear the conversation or `Logout` to leave the session.

## Example Questions

- What is HTML?
- What is the difference between HTML and CSS?
- What does Flask do?
- How can I start learning Python?
- What is frontend?
- Give me a beginner web project idea.

## Notes

- user data is stored temporarily in a Python list
- chat history is stored temporarily in the session
- no database is used in this version
- the chatbot is rule-based, not real AI

## Possible Improvements

- add a database like SQLite
- hash passwords
- add more chatbot responses
- save chat history permanently
- add user profile features

