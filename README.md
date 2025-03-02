# SensorNet: ML-Powered Sensory Monitoring Platform

A production-grade microservices platform for processing and analyzing sensory data in real-time, built with DevOps best practices.

## Project Overview

SensorNet demonstrates modern DevOps practices through a practical application that processes environmental sensory data. This project serves as both a learning experience and a portfolio showcase of DevOps skills including containerization, orchestration, CI/CD, and infrastructure as code.

The system collects environmental data (sound, light, movement) from sensors, processes it through ML pipelines, and provides real-time insights and recommendations through an API.

## Technology Stack

- **Container Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus & Grafana
- **Infrastructure as Code**: Terraform
- **Backend Services**: Python FastAPI
- **ML Pipeline**: MLflow

## Features

- **Microservices Architecture**: Scalable, resilient services with clear separation of concerns
- **Automated CI/CD Pipeline**: Continuous integration and deployment with GitHub Actions
- **Infrastructure as Code**: Reproducible infrastructure with Terraform
- **Observability**: Comprehensive monitoring with Prometheus and Grafana
- **ML Integration**: Real-time data analysis with machine learning

## Getting Started

### Prerequisites

- Docker Desktop with Kubernetes enabled
- kubectl
- Minikube (for local development)
- Terraform (optional, for infrastructure deployment)

### Quick Start

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/sensornet.git
   cd sensornet
   ```

2. Start a local Kubernetes cluster
   ```bash
   minikube start
   ```

3. Deploy the data collector service
   ```bash
   kubectl apply -f kubernetes/datacollector-pod.yaml
   kubectl apply -f kubernetes/datacollector-service.yaml
   ```

4. Access the API
   ```bash
   kubectl port-forward service/datacollector-service 8080:8080
   ```
   Then visit http://localhost:8080/health

### Development Workflow

This project follows a GitOps workflow:

1. Make changes in a feature branch
2. Open a pull request to trigger CI checks
3. Upon approval and merge, CD pipeline deploys to the target environment

## Project Structure

```
sensornet/
├── .github/workflows/    # CI/CD pipeline definitions
├── kubernetes/           # Kubernetes manifests
├── services/             # Microservice source code
│   ├── data-collector/   # Sensor data collection service
│   └── ml-predictor/     # ML prediction service
├── terraform/            # Infrastructure as code
└── monitoring/           # Monitoring configurations
```

## Learning Path

This project was built incrementally, following a learn-by-doing approach:

1. **Containerization**: Starting with Dockerizing a simple FastAPI service
2. **Kubernetes Basics**: Deploying single pods, understanding YAML configuration
3. **Service Networking**: Exposing and connecting services
4. **Deployment Strategies**: Moving to Deployments for scalability
5. **Observability**: Adding monitoring and logging
6. **Infrastructure as Code**: Managing infrastructure with Terraform
7. **CI/CD**: Implementing automated pipelines

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built as a portfolio project to demonstrate DevOps practices
- Inspired by real-world sensory monitoring systems
- Thanks to the open-source community for the amazing tools that make this possible. 
