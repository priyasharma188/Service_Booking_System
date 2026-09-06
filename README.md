# 🛠️ Service Booking System

A web-based **Service Booking System** developed using **Django** that allows users to browse computer-related services, create an account, log in, book services, and track their bookings.

## 📌 Project Overview

The Service Booking System provides an easy way for customers to find and book computer-related services online.

Users can:

* Browse available services without logging in
* View service details and prices
* Create a new account
* Log in using their email and password
* Book a computer-related service
* View their booking details
* Track booking status
* View only their own bookings

An administrator can manage services and update booking statuses through the Django Admin Panel.

---

## ✨ Features

### 👤 User Features

* User Registration
* User Login
* Email-based login
* Authentication-protected booking
* Browse services
* Service booking form
* Personal booking tracker
* Booking status tracking
* User-specific booking history

### 🛠️ Booking Features

Each booking contains:

* Customer Name
* Email
* Phone Number
* Selected Service
* Booking Date
* Booking Time
* Address
* Booking Status

### 📊 Booking Status

Bookings can have the following statuses:

* **Pending**
* **Confirmed**
* **In Progress**
* **Completed**
* **Cancelled**

The booking status can be updated by the administrator from the Django Admin Panel.

---

## 🔄 Booking Flow

```text
Home Page
    ↓
Browse Services
    ↓
Click "Book Now"
    ↓
Login / Registration
    ↓
Booking Form
    ↓
Submit Booking
    ↓
Booking Success
    ↓
My Bookings
    ↓
Track Booking Status
```

---

## 💻 Services

The system can be used for computer-related services such as:

* Computer Repair
* Laptop Repair
* Windows Installation
* Virus & Malware Removal
* Data Recovery
* Network Setup
* Printer Setup & Repair
* RAM & SSD Upgrade
* Software Installation
* Computer Cleaning & Maintenance

---

## 🚀 Technologies Used

### Frontend

* HTML5
* CSS3

### Backend

* Python
* Django

### Database

* SQLite (Development)

### Tools

* VS Code
* Git
* GitHub

---

## 📁 Project Structure

```text
Service Booking System/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── services/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── static/
│   ├── booking.css
│   ├── booking_success.css
│   ├── home.css
│   ├── login.css
│   ├── tracker.css
│   └── sbs_logo.svg
│
├── templates/
│   ├── booking.html
│   ├── booking_success.html
│   ├── home.html
│   ├── login.html
│   ├── registation.html
│   └── tracker.html
│
├── manage.py
├── requirments.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Service-Booking-System.git
```

### 2. Open the Project Folder

```bash
cd Service-Booking-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirments.txt
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Create Admin User

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create the admin account.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel

The administrator can access the Django Admin Panel at:

```text
http://127.0.0.1:8000/admin/
```

From the admin panel, the administrator can:

* Add services
* Edit services
* Delete services
* View customer bookings
* Filter bookings
* Update booking status

---

## 📈 Booking Tracking

When a customer creates a booking, its initial status is:

```text
Pending
```

The administrator can then update the status:

```text
Pending
   ↓
Confirmed
   ↓
In Progress
   ↓
Completed
```

If the booking is cancelled:

```text
Cancelled
```

The customer can see the latest booking status on the **My Bookings** tracker page.

---

## 🔒 Authentication

Only authenticated users can create bookings.

Guests can browse services, but when they try to book a service, they are redirected to the login page.

After successful login, the user can continue with the booking process.

---

## 👨‍💻 Developer

** Priya **

BCA Student | Web Development Enthusiast

---

## 📄 License

This project is created for educational and learning purposes.
