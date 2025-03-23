# 📚 Library Management System (Django + MySQL + REST API)

This project is a **Library Management System** developed using **Django**, **MySQL**, and the **Django REST Framework**. It provides two main user flows:

- ✅ **Admin** – can log in, manage (CRUD) book records
- 👨‍🎓 **Student/Guest** – can view the list of all books without logging in

---

## 🚀 Features

### 👩‍💼 Admin Features:
- **Signup** with unique email & username
- **Login** using email and password
- **JWT-based authentication** for secure access
- **Add**, **Edit**, **Delete**, and **View** books

### 👨‍🎓 Student (Guest) View:
- View list of all books without logging in (read-only)

---

## 🛠️ Tech Stack

| Tool/Library            | Description                            |
|-------------------------|----------------------------------------|
| Django (v5.x)           | Backend Framework                      |
| Django REST Framework   | RESTful API implementation             |
| MySQL                   | Relational Database                    |
| HTML + JavaScript       | Frontend (admin & student views)       |
| JWT (SimpleJWT)         | Admin authentication                   |
| CORS Headers            | For cross-origin frontend access       |

---

## 📁 Project Structure

```
library_management/
│
├── library_management/       # Main Django project
│   ├── settings.py           # Configs, MySQL DB, JWT, CORS
│   └── urls.py               # Root routes
│
├── library_app/              # Core app (books, admin auth)
│   ├── models.py             # AdminUser, Book model
│   ├── views.py              # API views (CRUD + auth)
│   ├── serializers.py        # DRF serializers
│   └── urls.py               # API routes
│
├── static/                   # Frontend files (optional hosting)
│   ├── index.html            # Role selector (Admin / Student / Signup)
│   ├── admin.html            # Admin dashboard (login + CRUD)
│   ├── student.html          # Book list view for students
│   ├── signup.html           # Admin signup page
│   └── script.js             # Common logic (login, CRUD, fetch, etc.)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone <your-repo-url>
cd library_management
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

> Or manually:
```bash
pip install django djangorestframework djangorestframework-simplejwt mysqlclient django-cors-headers
```

### 3. Configure MySQL

Create the database:

```sql
CREATE DATABASE library_db;
```

Update your `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

## 🚀 How to Use

To see the website in action:

1. **Run the Django backend**  
   Make sure your virtual environment is activated and run the development server:
   ```bash
   python manage.py runserver
   ```

2. **Open the frontend manually**  
   Since this project uses a static frontend, Django does not serve the HTML file.

   👉 Navigate to the `static/` folder and open `index.html` directly in your browser:  
   Right-click → "Open with" → select your browser.

   ❗ Do **not** open `http://localhost:8000` expecting a homepage UI — the frontend lives in the static folder.

3. **Admin Features**
   - Click "Login as Admin"
   - Use your credentials to log in
   - Perform full CRUD on books

4. **Student View**
   - Click "Continue as Student"
   - You can view the list of books only (read-only access)

5. **Admin Signup**
   - Click "Sign up as Admin" to register a new admin
   - Duplicate emails or usernames are not allowed

---
## 🧪 Testing

To run tests:

```bash
python manage.py test library_app


## 🔐 API Endpoints

### 📘 Book APIs

| Method | Endpoint                  | Auth Required | Description                |
|--------|---------------------------|---------------|----------------------------|
| GET    | `/api/books/`             | ❌ No         | List all books             |
| POST   | `/api/books/`             | ✅ Yes        | Add new book               |
| PUT    | `/api/books/<id>/`        | ✅ Yes        | Update book by ID          |
| DELETE | `/api/books/<id>/`        | ✅ Yes        | Delete book by ID          |

### 👤 Admin Auth

| Method | Endpoint                  | Description                  |
|--------|---------------------------|------------------------------|
| POST   | `/api/admin/signup/`      | Create new admin account     |
| POST   | `/api/admin/login/`       | Returns JWT access token     |

---

## 🌐 Frontend Pages

| Page           | Path              | Description                       |
|----------------|-------------------|-----------------------------------|
| Home           | `index.html`      | Role selection (admin/student)    |
| Admin Login    | `admin.html`      | Login & manage books              |
| Admin Signup   | `signup.html`     | Register new admin                |
| Student View   | `student.html`    | View books (read-only)            |

---

## 🙋 Assumptions

- No login is required for students to view books
- Only Admins can add/edit/delete books
- Email and username must be unique for admin signup

---

## 📩 Contact / Credits

Created by Shardul Pramod Manohar  
For educational/demo purposes ✨
