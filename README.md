
## 📄 README.md — Market Data Analytics Dashboard

```markdown
# 📊 Market Data Analytics Dashboard

An interactive financial dashboard built using **Streamlit, Pandas, and Plotly** to visualize and analyze stock market data.

This project allows users to explore historical price and volume trends, compute moving averages, and export data — all via a user-friendly web interface.

---

## 🚀 Live Demo

*A live deployed demo link can go here once hosted (optional)*

---

## 💡 Features

- Fetches **historical stock price data** for multiple tickers  
- Visualizes price and volume using **Plotly charts**  
- Computes and displays moving averages for trend analysis  
- Allows **CSV export** for offline analysis  
- Interactive filtering by ticker and date ranges

---

## 🧠 Tech Stack

| Component | Technology |
|-----------|------------|
| UI / Dashboard | Streamlit |
| Data Handling | Pandas |
| Visualization | Plotly |
| Data Source | Yahoo Finance (via API) |
| Deployment | Streamlit Cloud / Localhost |

---

## 📁 Project Structure

```

market-data-dashboard/
├── app.py                  # Main Streamlit app
├── data/                   # Cached stock data
├── requirements.txt        # Python dependencies
├── utils.py                # Helper functions for data retrieval/formatting
├── assets/                 # Static assets (e.g., images, styles)
└── README.md

````

---

## 🧪 Setup & Installation

### 1️⃣ Clone the repo

```bash
git clone https://github.com/preethinihar/market-data-dashboard.git
cd market-data-dashboard
````

### 2️⃣ Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard Locally

```bash
streamlit run app.py
```

By default, the dashboard will open in your browser at:

```
http://localhost:8501
```

---

## 🖥 How It Works

1️⃣ User selects one or more stock tickers
2️⃣ Retrieves historical price & volume data
3️⃣ Displays interactive charts for selected time ranges
4️⃣ Calculates moving averages for trend analysis
5️⃣ Allows download of filtered data as CSV

*(Replace this section with actual description if your logic differs.)*

---

## 📊 Screenshots

*(Insert visuals here — helpful for portfolio viewers)*

![Price Chart](./assets/price-chart.png)
*Interactive price chart with volume and moving average*

---

## 💡 Future Enhancements

* Add technical indicators (MACD, RSI, Bollinger Bands)
* Allow comparisons between multiple stocks
* Deploy on Streamlit Cloud / Heroku / AWS
* Add login to save favorite tickers

---

## 📝 Key Learnings

* Built data-driven dashboards with Streamlit
* Mastered financial time series visualization with Plotly
* Practical experience in data manipulation with Pandas
* Exporting and filtering data for user analysis

---


