# 🛒 E-Commerce QA Automation Framework  
### (Selenium + Pytest | Page Object Model)

---

## 📌 Project Overview

This project is a scalable and modular Web Test Automation Framework developed using **Selenium WebDriver with Python** and **Pytest**, following the **Page Object Model (POM)** design pattern.

The framework automates core user workflows of an e-commerce web application including Login and Add to Cart functionality. It is structured to support future enhancements such as Checkout flow automation, Data-Driven Testing, Reporting, and CI/CD integration.

Application Tested: SauceDemo (Demo E-Commerce Platform)

---

## 🚀 Key Features

- ✅ Login Automation
- ✅ Add to Cart Automation
- ✅ Page Object Model (POM) Architecture
- ✅ Modular & Scalable Folder Structure
- ✅ Pytest Integration
- ✅ Assertion-Based Validations
- ✅ Virtual Environment Configuration
- ✅ Git Version Control Ready
- ✅ HTML Reporting Support

---

## 🧱 Framework Architecture

The project follows the **Page Object Model (POM)** design pattern to ensure:

- Better code reusability
- Clear separation of test logic and page elements
- Easy maintenance
- Scalable structure for large test suites

---

## 📂 Project Structure

ECOMMERCE-QA-AUTOMATION
│
├── tests/
│   ├── __init__.py
│   └── test_login.py
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   └── inventory_page.py
│
├── utilities/
│   ├── __init__.py
│   └── driver_setup.py
│
├── reports/
│
├── README.md
├── requirements.txt
├── .gitignore
└── venv/


---

## 🛠 Tech Stack

- **Programming Language:** Python 3.12  
- **Automation Tool:** Selenium WebDriver  
- **Test Framework:** Pytest  
- **Design Pattern:** Page Object Model (POM)  
- **IDE:** VS Code  
- **Version Control:** Git & GitHub  

---

## 🔍 Automated Test Scenarios

### 🔐 Login Test
- Launch application
- Enter valid credentials
- Click login button
- Verify successful redirection

### 🛒 Add to Cart Test
- Login to application
- Add product to cart
- Validate cart badge count
- Confirm successful product addition

---


## ▶️ How to Execute the Project

### 1️⃣ Navigate to Project Directory

- cd Ecommerce-QA-Automation

### 2️⃣ Create Virtual Environment
- python -m venv venv

### 3️⃣ Activate Virtual Environment (Windows)
- venv\Scripts\activate

### 4️⃣ Install Dependencies
- pip install -r requirements.txt

### 5️⃣ Execute Tests
- pytest -v