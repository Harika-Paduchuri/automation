# OrangeHRM Playwright Automation Framework (Python + Pytest)

## Allure Report Integration

This repository is configured to generate Allure results during pytest execution and automatically produce an Allure HTML report after the test run.

This is a UI automation framework built using Playwright with Python and Pytest.
It follows Page Object Model (POM) design pattern for maintainability and scalability.

# Pre-requisites
- Python
- Playwright
- Pytest
- Pytest-HTML (Reporting)
- Python-dotenv

## Installation

### 1. Clone repo
git clone <repo-url>
cd orangehrm-playwright

### 2. Create virtual environment
python -m venv venv

### 3. Activate environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 4. Install dependencies
pip install -r requirements.txt

### 5. Install browsers
playwright install


## Environment Variables

Create a `.env` file:

BASE_URL=https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
USERNAME=Admin
PASSWORD=admin123


## Run Tests

Run all tests:
pytest

Run with verbose:
pytest -v -s

Run specific test:
pytest tests/test_login.py

Generate HTML report:
pytest --html=report.html