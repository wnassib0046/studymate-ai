from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "studymate_secret_key"

users = []
SUGGESTED_PROMPTS = [
    "What is HTML?",
    "What is the difference between HTML and CSS?",
    "What does Flask do?",
    "How can I start learning Python?",
    "What is the difference between frontend and backend?",
    "Give me a beginner web project idea."
]


def get_bot_reply(message):
    user_message = message.lower().strip()

    if not user_message:
        return "Please type a question, and I will try to help you."

    if any(word in user_message for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Hello! I can help with HTML, CSS, Flask, Python, frontend, backend, and beginner project ideas."

    if any(word in user_message for word in ["thanks", "thank you"]):
        return "You're welcome. Ask me another question any time."

    if any(word in user_message for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Keep practicing and come back when you want to revise more."

    if "what can you do" in user_message or "help" in user_message:
        return (
            "I can answer simple study questions about HTML, CSS, Flask, Python, "
            "frontend, backend, responsive design, databases, and beginner project ideas."
        )

    if "difference" in user_message and "html" in user_message and "css" in user_message:
        return "HTML gives a web page its structure, while CSS controls the design, colors, spacing, and layout."

    if "difference" in user_message and "frontend" in user_message and "backend" in user_message:
        return "Frontend is what users see and interact with, while backend handles logic, server work, and data."

    if "html" in user_message and "tag" in user_message:
        return "An HTML tag defines an element on a web page, such as a heading, paragraph, image, link, or form."

    if "html" in user_message:
        return "HTML is used to structure web pages using elements like headings, paragraphs, images, links, and forms."

    if "css" in user_message and "selector" in user_message:
        return "A CSS selector chooses which HTML element you want to style, such as a class, id, or tag name."

    if "css" in user_message or "style" in user_message:
        return "CSS is used to style web pages. It controls colors, spacing, fonts, positioning, and responsive layouts."

    if "flask" in user_message and "route" in user_message:
        return "In Flask, a route connects a URL like /login or /chat to a Python function."

    if "flask" in user_message:
        return "Flask is a Python framework used to build web applications with routes, templates, forms, and sessions."

    if "python" in user_message and any(word in user_message for word in ["learn", "start", "beginner"]):
        return "Start Python with variables, conditions, loops, functions, and lists, then practice by building small projects."

    if "python" in user_message:
        return "Python is a programming language used for backend development, automation, data work, and many other tasks."

    if "frontend" in user_message:
        return "Frontend development focuses on the visible part of a website using HTML, CSS, and sometimes JavaScript."

    if "backend" in user_message:
        return "Backend development handles application logic, authentication, server code, and database operations."

    if "responsive" in user_message:
        return "Responsive design means making a website look good on phones, tablets, and desktop screens."

    if "database" in user_message or "sql" in user_message:
        return "A database stores application data, and SQL is often used to create, read, update, and delete that data."

    if "api" in user_message:
        return "An API allows different applications or parts of a system to communicate and exchange data."

    if "project" in user_message or "idea" in user_message:
        return "A good beginner project is a to-do app, quiz app, student dashboard, weather page, or simple blog built with Flask."

    if "roadmap" in user_message or "learn web" in user_message:
        return "A simple roadmap is: learn HTML first, then CSS, then Python basics, then Flask, and then build small projects."

    return (
        "I am not fully sure about that yet. Try asking about HTML, CSS, Flask, Python, frontend, backend, "
        "responsive design, databases, or beginner project ideas."
    )


def get_chat_history():
    return session.setdefault("chat_history", [])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password']

        if not username or not email or not password:
            flash("Please fill in all fields.", "error")
            return redirect(url_for('register'))

        for user in users:
            if user['username'] == username:
                flash("That username already exists. Try another one.", "error")
                return redirect(url_for('register'))

        users.append({
            'username': username,
            'email': email,
            'password': password
        })

        flash("Account created successfully. You can log in now.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                session['chat_history'] = []
                return redirect(url_for('chat'))

        flash("Invalid username or password.", "error")
        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))

    history = get_chat_history()

    if request.method == 'POST':
        user_message = request.form['message'].strip()

        if user_message:
            bot_reply = get_bot_reply(user_message)
            history.append({'sender': 'user', 'text': user_message})
            history.append({'sender': 'bot', 'text': bot_reply})
            session['chat_history'] = history[-12:]
            session.modified = True

    return render_template(
        'chat.html',
        username=session['username'],
        chat_history=session.get('chat_history', []),
        suggested_prompts=SUGGESTED_PROMPTS
    )


@app.route('/clear-chat')
def clear_chat():
    session['chat_history'] = []
    return redirect(url_for('chat'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('chat_history', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
