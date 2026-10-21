# Project Name: Dealership Management & Review Application

## Repository Name: `xrwvm-fullstack_developer_capstone`
**GitHub Repository:** [xrwvm-fullstack_developer_capstone](https://github.com/omg1707afk/xrwvm-fullstack_developer_capstone)  
**Repository Owner:** `omg1707afk`  
**Branch:** `main`  
**Public README URL:** `https://github.com/omg1707afk/xrwvm-fullstack_developer_capstone/blob/main/README.md`

---

## Project Overview

The **Dealership Management & Review Application** is a full-stack web application developed using Django, React, and RESTful web services. The application allows users to explore nationwide car dealership locations across all 50 US states, filter dealerships by state (e.g. Kansas), view dealership details and customer reviews, inspect automobile models and makes, evaluate customer review sentiment using automated NLP microservices, and register or authenticate accounts.

---

## Main Features

1. **User Authentication & Authorization**
   - User Registration (`/djangoapp/registration` and `/register/`) with 5 required input fields: Username, First Name, Last Name, Email, and Password.
   - User Login (`/djangoapp/login`) using Django authentication session management returning `{"userName": "...", "status": "Authenticated"}`.
   - User Logout (`/djangoapp/logout`) with clean session invalidation returning `{"userName": ""}`.

2. **Dealership Services & Directory**
   - View all registered dealerships across states (`/fetchDealers` and `/djangoapp/get_dealers`).
   - Query individual dealership by identifier (`/fetchDealer/<id>`).
   - State-level dealership filtering (`/fetchDealers/<state>`).

3. **Customer Reviews & Community Feedback**
   - Retrieve customer reviews for any selected dealership (`/fetchReviews/dealer/<id>`).
   - Interactive review posting system (`/dealers/<id>/post-review/`).

4. **Car Inventory & Model Catalog**
   - Fetch automobile manufacturers and associated vehicle models (`/djangoapp/get_cars`).

5. **Automated Sentiment Analysis**
   - Real-time review sentiment classification (`/analyze/<text>`) providing instant evaluation (`{"sentiment": "positive"}`) for customer sentiment analysis.

6. **Responsive Frontend Interfaces**
   - Dedicated **About Us** page (`server/frontend/static/About.html`) featuring team bios, roles, and photography.
   - Dedicated **Contact Us** page (`server/frontend/static/Contact.html`) with interactive inquiry form validation and office contact details.
   - React **Register** component (`server/frontend/src/components/Register/Register.jsx`) with live validation and error handling.

---

## Technologies Used

- **Backend:** Python 3.14, Django 6.1, WSGI Architecture
- **Database:** SQLite3 / Django ORM, MongoDB / JSON Datasets
- **Frontend:** React, HTML5, CSS3, JavaScript (ES6+)
- **API Architecture:** RESTful JSON APIs, cURL
- **Version Control & CI/CD:** Git, GitHub Actions, Code Engine / Cognitive Class Proxy

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/omg1707afk/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

### 2. Install Dependencies
```bash
pip install django
```

### 3. Run Migrations & Start Server
```bash
cd server
python manage.py migrate
python manage.py runserver 8000
```

The server will be accessible at `http://127.0.0.1:8000/`.

---

## Submission & Verification Links

- **README:** `https://github.com/omg1707afk/xrwvm-fullstack_developer_capstone/blob/main/README.md`
- **About Us Page:** `https://github.com/omg1707afk/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/About.html`
- **Contact Us Page:** `https://github.com/omg1707afk/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/Contact.html`
- **Registration Component:** `https://github.com/omg1707afk/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/src/components/Register/Register.jsx`
