# 📈 Bank Marketing Optimization Analysis

This project analyzes a direct marketing campaign dataset from a Portuguese bank to understand customer behavior and optimize marketing strategies. It explores patterns, performs statistical testing, and builds machine learning models for predicting term deposit subscription.

---

## 📂 Dataset

**Source**: `data/bank-full.csv`  
**Separator**: `;`

---

## 🔍 Objective

- Identify key factors influencing client subscription.
- Apply A/B Testing on contact methods.
- Perform data preprocessing, feature engineering, and build predictive models.
- Optimize marketing campaign efficiency using data-driven strategies.

---

## 🧮 Key Techniques Used

- 📊 Exploratory Data Analysis (EDA)
- 📐 A/B Testing (Z-Test)
- 🧼 Data Preprocessing & One-Hot Encoding
- 🔢 Feature Engineering
- 🤖 Logistic Regression
- 📉 Evaluation using Accuracy, Precision, Recall

---

## 📊 Exploratory Data Analysis

- Visualized distributions of all categorical features (e.g., job, marital status, education, contact).
- Plotted conversion rate (`y=1`) across each category in categorical features to observe impact on campaign success.
- Found that **cellular** contact mode had the **highest conversion rate** among all contact types.

---

## 🧪 Statistical Insight

- A two-proportion **Z-test** was conducted to compare conversion rates of different contact methods.
- **Chi-square test** was used to check independence between categorical features and target variable.

---

## ⚙️ Model Performance Highlight

Using logistic regression with `class_weight='balanced'`, the recall score significantly improved:

- **Recall Before**: 0.35  
- **Recall After**: **0.81**  

This helped address the class imbalance and ensured better identification of potential subscribers.

---

## 📈 Key Findings / Results

- **Recall improved from 0.35 to 0.81** by using `class_weight='balanced'` in logistic regression, making the model much more effective at identifying potential responders in an imbalanced dataset.
- **Contact mode via 'cellular'** is statistically significant in increasing conversion rates. This was supported by a Chi-squared test (p-value = 0.0321), indicating that mode of contact affects outcome.

---

## 🛠️ Folder Structure

```
.
├── data/
│   └── bank-full.csv
├── images/
│   └── *.png (All visualizations)
├── models/
│   ├── model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── 01_data_analysis.ipynb
├── scripts/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   └── modeling.py
├── main.py
├── README.md
└── requirements.txt
```

---

## 📌 Dependencies

Install via:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

```bash
python main.py
```

---

## ✍️ Author

**Bikram Singh**  
_Data Analyst | ML Enthusiast_

---

## 📚 License

MIT License.