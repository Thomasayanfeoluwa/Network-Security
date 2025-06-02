# Network Security Project for Phishing Data

This project is focused on building and deploying a machine learning solution for detecting phishing attempts using network security data. It leverages FastAPI for the API, Docker for containerization, and GitHub Actions for CI/CD with AWS ECR/ECS deployment.

---

## Project Structure

```
NETWORK SECURITY/
├── app.py
├── Dockerfile
├── requirements.txt
├── networksecurity/
│   └── ... (your Python modules)
├── .github/
│   └── workflows/
│       └── main.yml
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- Docker
- AWS account (for deployment)
- GitHub repository with Actions enabled

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/network-security.git
    cd network-security
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the FastAPI app locally:
    ```sh
    uvicorn app:app --reload
    ```

---

## Docker Usage

To build and run the Docker container locally:

```sh
docker build -t networksecurity-app .
docker run -p 8000:8000 networksecurity-app
```

---

## Deployment

This project uses GitHub Actions for CI/CD.  
On every push to the `main` branch, the workflow in `.github/workflows/main.yml` will:

- Run linting and unit tests
- Build and push a Docker image to AWS ECR
- Deploy the image to your AWS ECS/ECR environment

**Required GitHub Secrets:**

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `ECR_REPOSITORY_NAME`
- `AWS_ECR_LOGIN_URI`

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Author

- [Your Name](https://github.com/your-username)