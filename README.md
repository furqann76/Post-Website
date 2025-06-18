---

# 🧠 Nerdy Posts - A Django Blog App

**Nerdy Posts** is a full-featured CRUD (Create, Read, Update, Delete) blog application built with **Django**, using **HTML**, **Bootstrap**, and **Jinja2-style templates**.
Users can create, update, and delete blog posts, manage their profiles, and access a secure REST API—all in a clean and responsive interface.

---

## 🚀 Features

* 📝 Add a new blog post
* ✏️ Edit an existing post
* ❌ Delete a post
* 📋 View all posts on the homepage
* 🔐 User authentication (signup, login, logout)
* 👤 User profile with profile picture support
* 🔄 Update user information and avatar
* 🔑 Secure REST API endpoint for posts with API key authentication
* ⚡ API throttling to limit excessive requests
* 🔁 Conditional navigation based on user login status
* 💅 Responsive frontend using Bootstrap
* 🌐 Optional CORS support for cross-origin API access

---

## 🛠 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, Bootstrap
* **Templating Engine:** Jinja2-style Django templates
* **Database:** SQLite (default)
* **API:** Django REST Framework with API key security and rate limiting

---

## 📁 Project Structure Highlights

* `blog/forms.py` — Custom forms for user registration and profile editing
* `blog/models.py` — Models for Post, Profile, and Comment
* `blog/views.py` — Views for authentication, profile, posts, and API
* `blog/serializers.py` — Serializer for Post model (API)
* `blog/permissions.py` — Custom API key permission class
* `blog/throttles.py` — Custom throttle class for API key rate limiting
* `blog/templates/blog/` — HTML templates for login, signup, home, profile, etc.
* `blog/urls.py` — URL patterns for all views and API endpoints

---

## 🔐 API Usage

### 📦 API Endpoint

`/api/posts/` — Returns all posts in JSON format.
Secured using a custom API key passed in the `X-API-KEY` header.

**Example:**

```bash
curl -H "X-API-KEY: your-secret-api-key" http://localhost:8000/api/posts/
```

### ⏱ API Throttling

To prevent abuse, API access is rate-limited (e.g., 5 requests per minute per API key).

---

## 🧪 How to Use

1. Register a new user via the signup page.
2. Log in to access your profile and create posts.
3. Edit or delete your posts from the profile or home page.
4. Access the REST API using a valid API key.
5. Use the API to display posts on other websites.

---

## 👨‍💻 Conditional Navigation

* If the user is **not authenticated**: Show **Login** and **Signup** buttons.
* If the user is **authenticated**: Show **Profile**, **Create Post**, and **Logout** options.

---

## 📍 Profile Page

Accessible at `/profile/`, this page displays:

* Username and email
* Profile picture or default avatar
* All posts created by the logged-in user

---
