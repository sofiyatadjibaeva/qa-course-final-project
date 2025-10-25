# Automated Testing of the Skillbox Online Store

## 1. Project Name
**Automated Testing of the Skillbox Online Store**  

---

## 2. Project Description
This project is an automated testing system for the Skillbox online store web application.
Its main goal is to verify the correct operation of key user scenarios, including product selection, order placement, user registration, and promo code usage.

**Key Objectives:**
- Automate main user flows of the online store.
- Ensure stability of the interface’s core features.
- Accelerate regression testing.
- Generate clear and informative test execution reports.

**Stack used**
- **Python + Pytest** — for writing and running tests.
- **Selenium WebDriver** — for browser automation.
- **Allure Report** — for visualizing test results.
- **flake8** — for code style and quality checking.
- **logging** — for detailed test activity logs.
- **Chrome DevTools** — for page performance analysis.

---

## 3. Installation and Setup

### Requirements
- Python 3.10+
- Google Chrome / Chromium
- Matching version of ChromeDriver
- Dependencies from `requirements.txt`

### Installation
```bash
git clone https://github.com/sofiyatadjibaeva/qa-course-final-project.git
cd qa-course-final-project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Running Tests
```pytest -v --alluredir=reports/allure-results```

### Viewing the Allure Report
```allure serve reports/allure-results```

---

## 4. How to Use the Project

### Test Functionality

The tests cover the main user scenarios of the Skillbox online store:

- Placing an order from the main page.
- Interacting with the product slider (hover, add to cart, view details).
- Working with the cart — changing quantity, deleting, refreshing, proceeding to checkout.
- Registering a new user during checkout.
- Applying promo codes.
- Registering in the loyalty program.
- Verifying order confirmation data accuracy.

### Architecture

The project follows the Page Object Model (POM) pattern.

It separates the logic of page interactions from the test cases themselves,

ensuring modularity, readability, and easy maintenance.

### Logging

Log format:
[%(levelname)s][%(asctime)s][%(name)s] %(message)s

INFO — output to console

DEBUG — written to log.log

### Project Structure
final_project/  
├── src/  
│   ├── actions  
│   ├── fixtures  
│   ├── utils  
│   └── _init_  
├── tests/  
│   ├── cart_page  
│   ├── checkout_page  
│   ├── loyalty_program_page  
│   ├── main_page  
│   ├── menu_page  
│   ├── product_page  
│   ├── registration_form  
│   └── log  
├── .flake8  
├── .gitignore  
├── .gitkeep  
├── README.md  
├── conftest.py  
├── log.txt  
├── logging.ini  
├── pytest.ini  
└── requirements.txt   

---

## 5. Author

Author: Sofiya Tadjibaeva  
GitHub: https://github.com/sofiyatadjibaeva  
Email: sofiatadjibaeva@gmail.com  
Telegram: @stridersan

---

## 6. License

This project is distributed under the GPL v3.0 (General Public License).
You are free to use, modify, and distribute this code as long as the original author is credited.
