```markdown
# 🧠 Nerdy Posts - A Django Blog App

**Nerdy Posts** is a simple CRUD (Create, Read, Update, Delete) web application built with **Django**, using **HTML**, **Bootstrap**, and **Jinja2-style templates**.  
Users can create, update, and delete blog posts in a clean and user-friendly interface.

---

## 🚀 Features

- 📝 Add a new blog post  
- ✏️ Edit an existing post  
- ❌ Delete a post  
- 📋 View all posts  
- ⚡ Powered by Django’s ORM and views  
- 💅 Responsive frontend using Bootstrap  

---

## 🛠 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, Bootstrap  
- **Templating Engine:** Jinja2-style Django templates  
- **Database:** SQLite (default)

---

## 📁 Project Structure

```

nerdy\_posts/
├── manage.py
├── db.sqlite3
├── nerdy\_posts/            # Project settings
│   └── settings.py
├── posts/                  # Main app (add, edit, delete logic)
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── templates/
│       └── posts/
│           ├── index.html
│           ├── create.html
│           └── update.html
└── static/                 # Bootstrap/CSS files

````

---

## ⚙️ Installation

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/nerdy-posts.git
cd nerdy-posts
````

### 2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install required packages:

```bash
pip install -r requirements.txt
```

> Or install Django manually:

```bash
pip install django
```

### 4. Run database migrations:

```bash
python3 manage.py migrate
```

---

## 🚀 Run the Server

To start the development server, use the following command:

```bash
python3 manage.py runserver
```

Then open your browser and go to:
📍 [http://127.0.0.1:8000](http://127.0.0.1:8000)
