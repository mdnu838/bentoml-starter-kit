# BentoML Starter Kit 🚀

![Python](https://img.shields.io/badge/Python-3.11-blue)
![BentoML](https://img.shields.io/badge/BentoML-1.0.25-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

```markdown
# BentoML Starter Kit 🚀

Deploy and serve a scikit-learn model using [BentoML](https://bentoml.com/) — a flexible framework for machine learning model serving, packaging, and deployment.

This project demonstrates how to train an Iris classifier, package it with BentoML, and expose it as a REST API.

---
```
## 📦 Project Structure
```markdown
├── bentofile.yaml         # BentoML build config
├── requirements.txt       # Python dependencies
├── service.py             # BentoML service definition
├── train.py               # Model training and saving
├── test.py                # Optional: API test script
```

---

## 🔧 Setup

### 1. Clone the Repo

```bash
git clone https://github.com/mdnu838/bentoml-starter-kit.git
cd bentoml-starter-kit
````

### 2. Create a Virtual Environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Train and Save the Model

```bash
python train.py
```

This will train a simple classifier on the Iris dataset and save it to BentoML's model store.

---

## 🔨 Build the Bento

Make sure `bentofile.yaml` is correct, then:

```bash
bentoml build
```

---

## 🚀 Serve the Model Locally

```bash
bentoml serve bentoml-starter-kit:latest
```

The API will be available at:
**[http://localhost:3000/classify](http://localhost:3000/classify)**

---

## 📬 Sample Request

You can test the endpoint using `curl` or Python:

```bash
curl -X POST http://localhost:3000/classify \
  -H "Content-Type: application/json" \
  -d '[[5.1, 3.5, 1.4, 0.2]]'
```

Expected response:

```json
[0]
```

---

## 🧪 Optional: Run Test Script

```bash
python test.py
```

Make sure the server is running before executing this script.

---

## 🐳 Docker Deployment

BentoML makes it easy to containerize your service and run it anywhere with Docker.

### ✅ 1. Build the Bento

```bash
bentoml build
```
### ✅ 2. Containerize the Service
Create a Docker image from the Bento using:
```bash
bentoml containerize bentoml-starter-kit:latest
```
This will create a Docker image named:
```makefile
bentoml-starter-kit:latest
```
### ✅ 3. Run the Docker Container
Start the container and expose it on port 3000:
```bash
docker run -it --rm -p 3000:3000 bentoml-starter-kit:latest
```
The BentoML API will now be accessible at:
```bash
http://localhost:3000/classify
```
### ✅ 4. Test the API (Inside Docker)
You can test it using `curl`:
```bash
curl -X POST http://localhost:3000/classify \
  -H "Content-Type: application/json" \
  -d '[[5.1, 3.5, 1.4, 0.2]]'
```
Expected response:
```json
[0]
```
---
## 📚 Resources

* [BentoML Documentation](https://docs.bentoml.com/)
* [scikit-learn](https://scikit-learn.org/)
* [FastAPI](https://fastapi.tiangolo.com/)

---

## 🧑‍💻 Author

[MD. Nizamuddin](https://github.com/mdnu838)

---

## 📄 License

MIT License

