# 📊 Trader Behavior & Sentiment Analysis

## 📌 Overview
This project analyzes trader performance and behavior based on market sentiment (Fear vs Greed). The goal is to understand how sentiment impacts profitability, trading activity, and risk-taking patterns.

The project also includes a simple predictive model, clustering of traders into behavioral groups, and an interactive dashboard for visualization.

---

## 🚀 Live Dashboard
🔗 https://data-science-intern-project.onrender.com/

---

## 📂 Project Structure
Data Science Intern  Project/
│
├── Trader_Behavior_Analysis.ipynb # Main analysis notebook
├── dashboard.py # Streamlit dashboard
├── daily_metrics.csv # Processed dataset
├── requirements.txt # Dependencies



---

## ⚙️ Features

### 📊 Data Analysis
- Cleaned and merged historical trader data with sentiment data
- Created daily metrics such as:
  - PnL (Profit & Loss)
  - Win Rate
  - Trade Count
  - Average Trade Size
  - Long/Short Ratio

---

### 📈 Key Analysis

#### 1. Performance vs Sentiment
- Compared trader profitability and win rates across Fear, Greed, and Neutral conditions

#### 2. Behavioral Analysis
- Analyzed how traders change:
  - Trading frequency
  - Position sizes
  - Market bias (long/short)

#### 3. Segmentation
- Grouped traders into:
  - High vs Low activity
  - Consistent vs inconsistent traders

---

### 🤖 Bonus Work

#### Predictive Model
- Built a Logistic Regression model to predict trader profitability
- Used behavioral features such as:
  - Trade count
  - Position size
  - Directional bias

#### Clustering
- Applied K-Means clustering to identify behavioral archetypes:
  - High-frequency traders
  - Large position traders
  - Balanced traders

---

### 📊 Dashboard
- Built using Streamlit
- Features:
  - Sentiment filter
  - Key metrics (PnL, win rate, trade count)
  - Performance and behavior visualizations
  - Cluster-based insights

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Altair / Matplotlib

---

## 📌 Key Insights

- Traders tend to achieve higher profitability during Fear periods despite slightly lower win rates
- Trading activity and risk-taking increase during Fear conditions
- High-frequency traders often show lower profitability, indicating possible overtrading effects
- Different trader archetypes exist based on behavior and risk exposure

---

# Clone the repository
https://github.com/AnuvratSharma9/Data-Science-Intern-Project

# Navigate into the project folder
cd Data Science Intern _Project

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run dashboard.py
