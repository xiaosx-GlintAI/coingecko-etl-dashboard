# README.md
 📈 CoinGecko Crypto ETL Dashboard

An end-to-end data pipeline that fetches cryptocurrency data from the [CoinGecko API](https://www.coingecko.com/en/api), stores historical prices into PostgreSQL using Airflow, and visualizes trends in a Streamlit dashboard.

---

## 🚀 Features

- ⛏️ Daily ETL pipeline using Airflow
- 📬 Fetches real-time crypto prices (top 10)
- 🗃️ Stores historical data in PostgreSQL
- 📊 Interactive Streamlit dashboard with:
  - Price trends over time
  - Market cap, volume metrics
  - Top 10 comparison

---

## 🧱 Stack

| Layer       | Tech                      |
|-------------|---------------------------|
| Data Source | CoinGecko API             |
| ETL         | Python, Airflow           |
| Storage     | PostgreSQL                |
| Dashboard   | Streamlit + Plotly        |
| Orchestration | Docker (optional)       |

---

## 📁 Project Structure

coingecko-crypto-etl-dashboard/
├── dags/
│   └── crypto_etl_dag.py                # Airflow DAG
├── etl/
│   ├── extract.py                       # API call logic
│   ├── transform.py                     # Data cleaning
│   └── load.py                          # PostgreSQL load (historical)
├── streamlit_app/
│   └── app.py                           # Interactive dashboard
├── sql/
│   └── create_crypto_tables.sql         # Schema for crypto_history
├── config/
│   └── settings.py                      # DB creds, constants
├── docker-compose.yml                   # Optional: Airflow + PostgreSQL stack
├── requirements.txt
├── README.md
└── .env.example                         # For DB config
