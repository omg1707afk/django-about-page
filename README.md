# Dealership Management & Review Application

**GitHub Repository:** [django-about-page](https://github.com/omg1707afk/django-about-page)  
**Repository Owner:** `omg1707afk`  
**Branch:** `main`  
**Public README URL:** `https://github.com/omg1707afk/django-about-page/blob/main/README.md`

---

## Project Overview

The **Dealership Management & Review Application** is a full-stack web application developed using Django, React, and RESTful web services. The application allows users to explore nationwide car dealership locations, filter dealerships by state, read dealer reviews with automated sentiment analysis, explore vehicle makes and models, and register or authenticate accounts to submit verified reviews.

---

## Main Features

1. **User Authentication & Authorization**
   - User Registration (`/register/` and `/signup/`) supporting Username, First Name, Last Name, Email, and Password with field validation.
   - User Login (`/login/`) using Django authentication session management.
   - User Logout (`/logout/`) with clean session invalidation.

2. **Dealership Services & Directory**
   - View all registered dealerships across states (`/dealers/` and `/get_dealers/`).
   - Query individual dealership by identifier (`/dealers/<id>/`).
   - State-level dealership filtering (`/dealers/by-state/?state=<StateName>`).

3. **Customer Reviews & Community Feedback**
   - Retrieve customer reviews for any selected dealership (`/dealers/<id>/reviews/`).
   - Interactive review posting system (`/dealers/<id>/post-review/`).

4. **Car Inventory & Model Catalog**
   - Fetch all supported automobile manufacturers and associated vehicle models (`/car-makes/`).

5. **Automated Sentiment Analysis**
   - Real-time review sentiment classification (`/analyze-review/`) providing instant evaluation (Positive, Neutral, Negative) for customer sentiment analysis.

6. **Responsive Frontend Interfaces**
   - Unified navigation and modern aesthetics.
   - Dedicated **About Us** page (`server/frontend/static/About.html`) featuring team bios, roles, and photography.
   - Dedicated **Contact Us** page (`server/frontend/static/Contact.html`) with interactive inquiry form validation and office contact details.
   - React **Register** component (`server/frontend/src/components/Register/Register.jsx`) with live validation and error handling.

---

## Technologies Used

- **Backend:** Python 3.14, Django 6.1, WSGI Architecture
- **Database:** SQLite3 / Django ORM
- **Frontend:** React, HTML5, CSS3, JavaScript (ES6+)
- **API Architecture:** RESTful JSON APIs, cURL
- **Version Control:** Git, GitHub

---

## Project Structure

```text
├── README.md
├── cookies.txt
├── login_body.json
├── submission_evidence/
│   ├── django_server
│   ├── loginuser
│   ├── logoutuser
│   ├── getdealerreviews
│   ├── getalldealers
│   ├── getdealerbyid
│   ├── getdealersbyState
│   ├── getallcarmakes
│   └── analyzereview
└── server/
    ├── manage.py
    ├── db.sqlite3
    ├── config/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── dealers.py
    │   ├── dealers_by_state.py
    │   ├── dealer_by_id.py
    │   ├── dealer_reviews.py
    │   ├── login_view.py
    │   ├── car_makes.py
    │   ├── analyze_review.py
    │   ├── home.py
    │   └── post_review.py
    ├── frontend/
    │   ├── src/
    │   │   └── components/
    │   │       └── Register/
    │   │           ├── Register.jsx
    │   │           └── Register.css
    │   └── static/
    │       ├── About.html
    │       ├── Contact.html
    │       └── style.css
    └── templates/
        ├── home.html
        └── post_review.html
```

---

## Installation and Setup

### 1. Prerequisites
- Python 3.10+ (tested on Python 3.14)
- Git

### 2. Clone the Repository
```bash
git clone https://github.com/omg1707afk/django-about-page.git
cd django-about-page
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Run Database Migrations
```bash
cd server
python manage.py migrate
```

### 5. Start the Django Application
```bash
python manage.py runserver 8000
```

The server will be accessible at `http://127.0.0.1:8000/`.

---

## API Endpoints Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Home Dealership Portal |
| `POST` | `/login/` | Authenticate user credentials |
| `POST` | `/logout/` | End user session |
| `POST` | `/register/` | Register new user account |
| `GET` | `/dealers/` | Retrieve all dealerships |
| `GET` | `/dealers/<id>/` | Retrieve dealership details by ID |
| `GET` | `/dealers/by-state/?state=<name>` | Filter dealerships by state |
| `GET` | `/dealers/<id>/reviews/` | Retrieve reviews for specified dealer |
| `GET` | `/car-makes/` | Retrieve vehicle manufacturers and models |
| `POST` | `/analyze-review/` | Classify sentiment of submitted text |

---

## Submission & Verification Links

- **README:** `https://github.com/omg1707afk/django-about-page/blob/main/README.md`
- **About Us Page:** `https://github.com/omg1707afk/django-about-page/blob/main/server/frontend/static/About.html`
- **Contact Us Page:** `https://github.com/omg1707afk/django-about-page/blob/main/server/frontend/static/Contact.html`
- **Registration Component:** `https://github.com/omg1707afk/django-about-page/blob/main/server/frontend/src/components/Register/Register.jsx`
