* Project Overview
This project implements a CI/CD pipeline for an MLOps Inference Service using Jenkins, Docker, and GitHub. It automates the build, test, and deployment phases of a machine learning model-serving application with modular folder structures and Kubernetes integration planned.

*Project Structure
mlops-inference-service/
│
├── app/                    # FastAPI inference service code
│   ├── main.py
│   └── requirements.txt
│
├── model/                  # ML model files
│   └── model.pkl
│
├── notebooks/              # Jupyter Notebooks for model training/testing
│   └── train_model.ipynb
│
├── k8s/                    # Kubernetes deployment files (to be added)
│
├── monitoring/             # Monitoring setup (Prometheus, Grafana - planned)
│
├── grafana/                # Grafana dashboards and provisioning (planned)
│
│
├── Dockerfile              # Dockerfile to build the inference service
├── jenkinsfile             # Jenkins CI/CD pipeline script
└── README.md               # Project documentation (you are reading it)


Steps Completed
✅ Step 1: Project Initialization
Created modular directory structure:

app, model, notebooks, k8s, monitoring, grafana, .github/workflows

Initialized GitHub repository: VamshiAdep/Mlops_DevOps

Pushed basic skeleton structure

✅ Step 2: FastAPI Inference App
Added FastAPI server under app/main.py

Model loads from model/model.pkl

Installed required packages via app/requirements.txt

Locally tested the API using:

bash
Copy
Edit
uvicorn app.main:app --reload
✅ Step 3: Dockerization
Created Dockerfile at project root:

dockerfile
Copy
Edit
FROM python:3.10-slim
WORKDIR /app
COPY ./app /app
COPY ./model /model
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
Docker Build & Run:

bash
Copy
Edit
docker build -t vamshiadep/mlops-inference-service:latest .
docker run -p 8000:8000 vamshiadep/mlops-inference-service:latest
DockerHub Image:
https://hub.docker.com/repository/docker/vamshiadep/mlops-inference-service

✅ Step 4: Jenkins Pipeline Setup
Installed Jenkins on EC2 / Localhost

Installed required plugins:

Docker Pipeline

GitHub Integration

Connected GitHub repo to Jenkins

Step 5: Final Cleanup and Security Review
Jenkins build runs successfully and pushes Docker image to DockerHub.

Received security warning: Credentials transmitted in plain text from Quality Gates Plugin — acknowledged; no fix available yet.

All images pushed and Jenkins pipeline verified.

Next Steps (Not yet implemented)
Kubernetes YAMLs in k8s/ folder

Monitoring setup in monitoring/

Grafana dashboards in grafana/
