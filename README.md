# Web Automation API (FastAPI + Playwright + Docker)

This project automates a website task — for example, logging in and searching for a specific product — using **Python, FastAPI**, and **Playwright**.  
It’s packaged as a web API so anyone can trigger the automation remotely via HTTP.

---

## Features
- Automates real browser interactions (login, search, extract data)
- REST API access via FastAPI
- Supports headless
- Dockerized for easy deployment anywhere
- Ready for cloud deployment via Render or Google Cloud Run

---


## ⚙️ Requirements
- Python 3.9+
- Playwright
- FastAPI
- Docker (for containerized deployment)

---


## Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/MuddyHope/playscraper.git
   cd playscraper
   ```

2. **Install dependencies**
    ```bash 
   pip install -r requirements.txt
   playwright install
    ```
3. **Run the python main.py file**
   ```commandline
   python main.py --product "shirt"
   ```

## Local Setup with FastAPI

1. **Clone the repository**
   ```bash
   git clone https://github.com/MuddyHope/playscraper.git
   cd playscraper
   ```

2. **Install dependencies**
    ```bash 
   pip install -r requirements.txt
   playwright install
    ```

3. **Run the FastApi server**
    ```bash
   uvicorn api_service:app --reload
    ```
   
4. **Access the API**
    ```bash
    http://127.0.0.1:8000/docs 
   ```



## Docker Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/MuddyHope/playscraper.git
   cd playscraper
   ```

2. **Build and Run the image**
    ```bash
   
   docker build -t playscraper .
   docker run -p 8000:8000 playscraper
    ```
   
3. **Access the API**
    ```bash
   http://127.0.0.1:8000/docs
    ```


## Deployed Service

### URL: https://playscraper.onrender.com/docs


## Example API Request

Endpoint: POST /run-task
Test data (use this exact JSON in Swagger / curl / Postman):
```bash
{
  "url": "https://www.saucedemo.com/",
  "username": "standard_user",
  "password": "secret_sauce",
  "product": "bike",
}
```