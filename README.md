# 🧠 Nerdy Posts - Django Blog & RAG API Project

A full-featured blog platform built with **Django** and **Django REST Framework**, featuring user authentication, profile management, CRUD for posts and comments, REST API with API key security, rate limiting, and a FastAPI-based Retrieval-Augmented Generation (RAG) PDF QA microservice.

---

## 🚀 Features

- 📝 Create, edit, and delete blog posts
- 💬 Comment on posts (with text-to-speech for comments)
- 🔐 User authentication (register, login, logout)
- 👤 User profile with profile picture and editable info
- 📋 View all posts, search posts, and filter by user
- 🗝️ Secure REST API for posts with API key authentication and throttling
- ⚡ API rate limiting for anonymous, user, and API key requests
- 🌐 Responsive frontend using Bootstrap 4
- 🔁 Conditional navigation based on authentication status
- 📄 RAG PDF QA API using FastAPI (ask questions about PDFs)
- 🖼️ Media uploads (profile pictures)
- 🗃️ SQLite database (default)

---

## 🛠 Tech Stack

- **Backend:** Django 5, Django REST Framework, FastAPI
- **Frontend:** HTML, Bootstrap 4, Django templates
- **Database:** SQLite
- **API:** REST (DRF), FastAPI (RAG)
- **Other:** PyMuPDF, Sentence Transformers, FAISS, gTTS

---

## 📁 Project Structure

📁 Django-Project/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .env
├── README.md
├── siddique\_family.pdf
├── django.pdf
│
├── blog/
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── form.py
│   ├── models.py
│   ├── permissions.py
│   ├── rag.py                  # FastAPI RAG PDF QA microservice
│   ├── serializers.py
│   ├── signals.py
│   ├── tests.py
│   ├── throttles.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── management/
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── post\_detail.html
│   │       └── ...
│   └── media/
│       └── profile\_pics/
│
├── myapp/
│   ├── **init**.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── api/
│
└── media/
└── profile\_pics/


---

## 🔑 API Usage

- **Posts API:**  
  Endpoint: `/api/posts/`  
  - Requires API key in the header: `Authorization: Api-Key <your-key>`
  - Throttled by user, anon, and API key (see `myapp/settings.py`)
  - Serializer: [`PostSerializer`](blog/serializers.py)
  - Permission: [`HasAPIKey`](blog/permissions.py)
  - Throttle: [`APIKeyRateThrottle`](blog/throttles.py)

- **RAG PDF QA API:**  
  - Run with:  
    ```
    uvicorn blog.rag.rag:app --reload
    ```
  - Ask questions about PDFs in the project root (`django.pdf`).

---

## 🧪 How to Run

1. **Install dependencies:**
    ```sh
    pip install -r requirement.txt
    ```

2. **Apply migrations:**
    ```sh
    python [manage.py](http://_vscodecontentref_/19) migrate
    ```

3. **Create a superuser (optional):**
    ```sh
    python [manage.py](http://_vscodecontentref_/20) createsuperuser
    ```

4. **Run the Django server:**
    ```sh
    python [manage.py](http://_vscodecontentref_/21) runserver
    ```

5. **Run the FastAPI RAG server (for PDF QA):**
    ```sh
    uvicorn blog.rag.rag:app --reload
    ```

---

## 👨‍💻 Main Django App Highlights

- **Forms:** [`blog/form.py`](blog/form.py) — User registration, profile edit, post/comment forms
- **Models:** [`blog/models.py`](blog/models.py) — `Post`, `Profile`, `Comment`
- **Views:** [`blog/views.py`](blog/views.py) — CRUD, profile, API, TTS for comments
- **Serializers:** [`blog/serializers.py`](blog/serializers.py) — DRF serializers
- **Permissions:** [`blog/permissions.py`](blog/permissions.py) — API key permission
- **Throttles:** [`blog/throttles.py`](blog/throttles.py) — Custom API key throttling
- **Templates:** [`blog/templates/blog/`](blog/templates/blog/) — HTML templates
- **URLs:** [`blog/urls.py`](blog/urls.py), [`myapp/urls.py`](myapp/urls.py)
- **Settings:** [`myapp/settings.py`](myapp/settings.py) — All configuration

---

## 📍 Profile Page

Accessible at `/profile/`, this page displays:

- Username and email
- Profile picture or default avatar
- All posts created by the logged-in user

---

## 📄 RAG PDF QA API

- **Location:** [`blog/rag.py`](blog/rag.py)
- **Purpose:** Ask questions about the PDFs in the project root using LLMs and vector search.
- **Run:**  

- **Dependencies:** See `requirement.txt` for `fastapi`, `faiss-cpu`, `sentence-transformers`, `PyMuPDF`, etc.

---

## 📦 Requirements

See [`requirement.txt`](requirement.txt) for all dependencies.

---

## 📝 License

This project is for educational/demo purposes.

---
