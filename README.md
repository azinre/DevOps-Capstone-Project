# DevOps Capstone Project  

Capstone project for the **IBM DevOps & Software Engineering Program**.  

This project implements a **Customer Accounts microservice** using **Flask**, following **Test-Driven Development (TDD)** and deployed with a **CI/CD pipeline**. Builds a Customer Accounts microservice with Flask using TDD, CI/CD (GitHub Actions, Tekton), Docker, Kubernetes/OpenShift, PostgreSQL, and security best practices. Demonstrates Agile planning, automation, and cloud-native deployment. 

---
# CI/CD Tools and Practices Final Project Template

This repository contains the template to be used for the Final Project for the Coursera course **CI/CD Tools and Practices**.

---

## 📖 Project Overview  

- **Microservice Architecture**: Flask-based RESTful API for customer accounts  
- **Development Approach**: Test-Driven Development (TDD)  
- **CI/CD**: GitHub Actions, Tekton pipelines  
- **Containerization & Orchestration**: Docker, Kubernetes, OpenShift  
- **Database**: PostgreSQL  
- **DevOps Practices**: Automation, Agile workflow, linting, code coverage, and security best practices  

This repository demonstrates the full DevOps lifecycle — from code, build, and test, to containerization, deployment, and monitoring.  

---

## 🚀 Getting Started  

### Prerequisites  

Ensure you have the following installed:  

- [Python 3.9+](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/) / [virtualenv](https://virtualenv.pypa.io/en/stable/)  
- [Docker](https://docs.docker.com/get-docker/)  
- [PostgreSQL](https://www.postgresql.org/download/)  
- [GitHub Account](https://github.com/)  

### Clone the Repository  

```bash
git clone https://github.com/azinre/DevOps-Capstone-Project.git
cd DevOps-Capstone-Project

## Setup

After entering the lab environment you will need to run the `setup.sh` script in the `./bin` folder to install the prerequisite software.

```bash
bash bin/setup.sh
```

Then you must exit the shell and start a new one for the Python virtual environment to be activated.

```bash
exit
```
## Setup Environment

Install dependencies:

make install


Activate virtual environment (if not already active):

source venv/bin/activate

Run the Application
flask run


The service will be available at:
👉 http://127.0.0.1:5000/

✅ Testing & Code Quality
Run Unit Tests with Coverage
nosetests --with-coverage --cover-package=service

Run Linting
flake8 service

## ⚙️ CI/CD Pipeline

A GitHub Actions workflow (.github/workflows/ci.yml) is included. It:

Runs on every push and pull request to the main branch

Installs dependencies and sets up the Python environment

Runs unit tests with nosetests

Generates test coverage reports

Runs flake8 linting for code quality

This ensures code quality and functionality are validated on every commit.

## 📦 Docker
Build Docker Image
docker build -t customer-accounts-service .

Run Container
docker run -p 8080:8080 customer-accounts-service


The service will be available at:
👉 http://localhost:8080/

## ☸️ Kubernetes Deployment

Deployment manifests will be added for Kubernetes / OpenShift in later sprints.
Expected workflow:

Build container image

Push to container registry (e.g., DockerHub)

Apply Kubernetes manifests (deployment.yaml, service.yaml)

Expose service via Ingress / Route

 ## 📅 Agile Sprint Breakdown

Sprint 1:

Build Flask microservice

Write unit tests (TDD)

Add Dockerfile for containerization

Sprint 2:

Configure CI with GitHub Actions

Add flake8 linting

Add nosetests with code coverage

Sprint 3:

Implement CD with Tekton pipelines

Deploy to Kubernetes / OpenShift

Integrate PostgreSQL database

Sprint 4:

Add security hardening

Implement monitoring & logging

Final polish and documentation

📂 Repository Structure
DevOps-Capstone-Project/
│
├── service/               # Flask microservice source code
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── tests/             # Unit tests
│
├── Dockerfile             # Container build file
├── requirements.txt       # Python dependencies
├── Makefile               # Automation commands
├── setup.cfg              # Test and linting config
├── .flake8                # Flake8 linting rules
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions CI pipeline
│
└── README.md              # Project documentation

## License

Licensed under the Apache License. See [LICENSE](/LICENSE)

## 👩‍💻 Author

Azin Rezaeian https://www.linkedin.com/in/azinre/