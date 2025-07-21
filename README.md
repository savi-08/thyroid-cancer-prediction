# 🧠 Thyroid Cancer Reoccurrence Prediction

This project predicts whether a **Thyroid Cancer survivor's cancer will recur** using patient data like age, medical history, diagnosis, and response to treatment.

---

## 📊 Dataset

- 383 patient records
- Features: 16 medical and demographic columns
- Target: `Recurred` (Yes/No)

---

## 🧪 Model Workflow

1. Data Cleaning & Preprocessing  
2. Exploratory Data Analysis  
3. Label Encoding  
4. Model Training (Logistic Regression & Random Forest)  
5. Model Evaluation  
6. CLI-based Prediction System

---

## 🧠 Best Model: Random Forest

| Metric      | Score |
|-------------|-------|
| Accuracy    | 94.8% |
| Precision   | 95%   |
| F1-Score    | 90%   |

---

## 📁 Project Structure

thyroid_cancer_prediction/
├── data/ ← Raw dataset (.csv)
├── models/ ← Trained model (.joblib)
├── notebooks/ ← Jupyter Notebook (EDA + training)
├── main.py ← CLI prediction script
├── requirements.txt ← Python dependencies
└── README.md ← Project overview

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/thyroid-cancer-prediction.git
   cd thyroid-cancer-prediction
   ```
### Install dependencies:
```bash
pip install -r requirements.txt
```
### Run prediction script:
```bash
python main.py
```
## 🔮 Sample CLI Output
```python
Choose input method:
1. Manual input
2. Random sample from dataset
```
## 🎯 Prediction Result:
✅ Cancer WILL NOT Recur

### 📌 Author
Shravani Bande
GitHub