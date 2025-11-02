# 🚀 Python Backend Training

This repository documents a step-by-step backend training process using **Python** with modern best practices.  
Each step should be developed in a dedicated **git branch** (use SSH).

---

## 📌 Steps

### 1. FastAPI App
- Develop a **FastAPI** application consuming endpoints from the **UNSPLASH Images Public API**.
- Requirements:
  - Pre-commits
  - `pyenv` (Python 3.14)
  - Poetry /uv
  - Virtual environments
  - Ruff, Bandit
  - `build.sh` script for local build
  - OpenAPI documentation
  - Document chosen **design patterns**
  - Use advanced Python features:
    - Decorators
    - Generators /Corutines
    - List comprehensions
    - Context managers
    - Memory optimizations (cache, generators, replacing loops with O(1) solutions where possible)

---

### 2. Testing & CI
- Add **unit and system tests**.
- Use **Wiremock** for mocking external APIs.
---

### 3. Dockerization
- Dockerize with **2 stages**: build and run.
- Automate builds with **GitHub Actions**.
- Docker compose

---

### 4. Databases
- Save API data into:
  - PostgreSQL
  - SQLite
  - MongoDB
  - Key-value DBs
- Use **public containers** (popular images).
- Database migrations with **Alembic**.
- Dockerize with **Docker Compose**.

---

### 5. Reverse Proxy
- Introduce **Nginx** and **Apache** before Uvicorn.
- Perform **stress tests** and document **metrics**.

---

### 6. Visualization
- Add a visual **HTTPS panel** to display API results.

---

### 7. Authentication
- Add **OpenID Connect authentication**.
- Support 3rd party providers: **Facebook, Google, GitHub**.

---

### 8. Cloud Integration
- Introduce **SaaS** in:
  - AWS
  - Azure
  - Google Cloud
- Use services:
  - AWS: S3, SQS, SNS, DynamoDB, Cognito, Lambda
  - Azure & GCP: equivalent services

---

### 9. Deployment
- Deploy the application with cloud-native practices.
- CI
- gitlab
- Jenkins
- github Actions
---

### 10. Kubernetes
- Introduce **Kubernetes (K8s)** for orchestration.

---

### 11. Microservices
- Split into microservices per cloud provider.

---

### 12. Data & AI
- Introduce a new microservice using:
  - **Pandas**
  - **LLM libraries** (e.g., PyTorch)

---

## ⚙️ Setup Instructions

```bash
# Install Poetry
pip install poetry

# Install pyenv
pip install pyenv

# Install Python 3.13
pyenv install 3.13
pyenv versions
pyenv global 3.13.1

# Setup Poetry environment
poetry env use python3.13
poetry shell

# Link Poetry virtualenv
# ln -s /PATH_TO/Caches/pypoetry/virtualenvs/VIRTUAL_ENV_NAME venv
# source venv/bin/activate
# buildin locally
# ./build.sh
# poetry show (after .poetry lock is created)

###
Building  & running with with docker
docker compose up --build
docker compose up  # just to run
#####

python server.py
# in browser go to
http://127.0.0.1:8000/documentation
http://127.0.0.1:8000/maps/image/3


curl "https://api.unsplash.com/photos/random?query=mountain&client_id=<ACCESS_KEY>"
