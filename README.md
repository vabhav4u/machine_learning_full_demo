# 📊 Machine Learning Full Demo

This repository contains a **complete end-to-end machine learning project** that demonstrates how to build an ML pipeline step-by-step — from data generation to training and inference — using Python.  
It’s lightweight (≤2000 rows), GitHub-friendly, and designed for learning or small projects. :contentReference[oaicite:1]{index=1}

---

## 🚀 Overview

This project demonstrates:

✔ Data ingestion  
✔ Data cleaning & validation  
✔ Feature engineering & feature store  
✔ Model training  
✔ Evaluation & metrics  
✔ CLI-based inference  
✔ Git-ready structured code (no notebooks) :contentReference[oaicite:2]{index=2}

---

## 🗂️ Project Structure


---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
``` :contentReference[oaicite:4]{index=4}

---

## 🧠 How to Run

### 1️⃣ Generate the dataset

```bash
python src/data_ingestion.py
``` :contentReference[oaicite:5]{index=5}

### 2️⃣ Clean the data

```bash
python src/data_cleaning.py
``` :contentReference[oaicite:6]{index=6}

### 3️⃣ Create feature store

```bash
python src/feature_engineering.py
``` :contentReference[oaicite:7]{index=7}

### 4️⃣ Train the ML model

```bash
python src/train.py
``` :contentReference[oaicite:8]{index=8}

### 5️⃣ Evaluate model

```bash
python src/evaluate.py
``` :contentReference[oaicite:9]{index=9}

### 6️⃣ Run Inference

```bash
python src/inference.py \
  --age 45 \
  --tenure 10 \
  --monthly_spend 6000 \
  --support_calls 2 \
  --usage_score 0.5 \
  --contract_type yearly
``` :contentReference[oaicite:10]{index=10}

---

## 📌 What This Project Demonstrates

- 🧪 **Data Generation & Ingestion**  
- 🧹 **Cleaning & Preparation**  
- 📊 **Feature Engineering & Store**  
- 🤖 **ML Model Training**  
- 📈 **Evaluation Metrics**  
- ⚙ CLI-based **Inference**  
- 🗃️ **Git-friendly Code Structure** :contentReference[oaicite:11]{index=11}

---

## 📌 Notes

- The `src/` folder contains all executable scripts.  
- No Jupyter notebooks — this is pure Python scripts for easy automation and CI/CD.  
- The dataset is small, so it runs fast and is suitable for learning or demo purposes. :contentReference[oaicite:12]{index=12}

---

## 💡 Optional Improvements

You can extend this project with:

- Docker containerization  
- GitHub Actions CI/CD  
- Logging & debug modes  
- MLflow or DVC tracking  
- Deployment (FastAPI / Flask) :contentReference[oaicite:13]{index=13}

---

## 📄 License

This project is open source — feel free to use and modify! 📦

