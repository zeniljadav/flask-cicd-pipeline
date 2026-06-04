# Automated Flask CI Pipeline with GitHub Actions 🚀

A production-ready Continuous Integration (CI) pipeline built for a Python Flask web application. This project automates the entire code quality check and testing workflow using GitHub Actions, ensuring that only verified code moves forward.

## 🛠️ Tech Stack & Dependencies

The project strictly locks down the following production-grade versions:
- **Python:** v3.11
- **Flask (v3.0.3):** Core web application framework.
- **PyTest (v8.1.1):** Automated unit testing framework.
- **Flake8 (v7.0.0):** Static code analysis and linting gate.

---

## 📌 Features & Architecture

- **Automated Workflow Trigger:** The CI pipeline automatically spins up an ephemeral `ubuntu-latest` virtual runner on every `push` or `pull_request` to the `main` branch.
- **Continuous Quality Enforcement (Linting):** Integrates **Flake8** to scan the codebase for syntax errors, improper formatting, and unused imports, enforcing strict PEP 8 compliance.
- **Automated Unit Testing:** Executes test suites using **PyTest** to verify core application functionality and route health automatically before branch merging.
- **Delivery Protection:** Built-in fail-safe mechanism that blocks integration and notifications on failing workflows, reducing manual verification reliance to 0%.

---

## 📁 Project Structure

```text
flask-cicd-pipeline/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions Pipeline Configuration
├── app.py                  # Main Flask Web Application
├── test_app.py             # PyTest Automated Unit Tests
├── requirements.txt        # Project Dependencies (Flask, PyTest, Flake8)
└── README.md               # Project Documentation
🚀 How to Setup Locally
1. Clone the Repository
Bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/flask-cicd-pipeline.git](https://github.com/YOUR_GITHUB_USERNAME/flask-cicd-pipeline.git)
cd flask-cicd-pipeline
2. Create a Virtual Environment & Install Dependencies
Bash
# Create environment
python -m venv venv

# Activate environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install exact required packages
pip install -r requirements.txt
3. Run Quality Checks Manually
Bash
# Run Code Quality Check (Linter)
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Run Unit Tests
pytest
4. Start the Application
Bash
python app.py
Open http://127.0.0.1:5000/ in your browser to view the application.

⚙️ CI Pipeline Configuration (ci.yml)
The automation workflow is structured into sequential stages:

Environment Provisioning: Sets up a clean Ubuntu runner and installs Python 3.11.

Dependency Management: Caches and installs packages (Flask==3.0.3, pytest==8.1.1, flake8==7.0.0) from requirements.txt.

Linting Gate: Runs flake8 to catch programmatic and syntax bugs.

Test Execution Gate: Runs pytest to ensure all functionality is working as expected.

A green checkmark (✅) on GitHub indicates that all pipeline quality gates have successfully passed.
