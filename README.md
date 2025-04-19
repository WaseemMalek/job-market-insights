# 💼 Job Market Insights Dashboard

An end-to-end data analytics project that scrapes real-time job listings from the [Adzuna API](https://developer.adzuna.com/), cleans the data, and visualizes it in an interactive Streamlit dashboard.

![Streamlit App Screenshot](https://your-app-streamlit-url/screenshot.png)

---

## 🚀 Live App

👉 [Launch the Dashboard](https://job-market-insights-pa5whg3wnmbfddcecpjhoz.streamlit.app/)  
(Hosted on Streamlit Cloud)

---

## 🧠 What This Project Covers

✅ Web scraping via API (Adzuna)  
✅ Secure handling of API keys (`.env` + Streamlit secrets)  
✅ Data cleaning and transformation with `pandas`  
✅ Interactive dashboard with filtering, search, and visuals  
✅ Git/GitHub version control  
✅ Cloud deployment with Streamlit Cloud  

---

## 📊 Features

- Filter by **location**, **company**, **salary range**, and **remote jobs**
- Full-text **search bar** for job titles & descriptions
- Bar charts for top hiring companies
- Cleaned data displayed in a table

---

## 📂 Project Structure
job-market-insights/
├── src/
│   ├── adzuna_scraper.py         # Pulls job data from Adzuna API
│   ├── clean_jobs.py             # Cleans and prepares raw job data
│   ├── dashboard.py              # Streamlit dashboard app
│   └── adzuna_jobs_clean.csv     # Cleaned static dataset used by dashboard
├── requirements.txt              # Dependencies (streamlit, pandas, etc.)
├── .gitignore                    # Tells Git to ignore .env, data/, etc.
├── README.md                     # Your project’s portfolio front page
└── (optionally: data/)   


---

## 🛠 Tech Stack

- Python
- Pandas
- Streamlit
- Requests
- Dotenv
- Git/GitHub

---

## 🔐 API Keys

This app uses the [Adzuna API](https://developer.adzuna.com/).  
You’ll need your own `APP_ID` and `APP_KEY`.

Store them in a `.env` file (for local use) or [Streamlit Secrets](https://docs.streamlit.io/streamlit-cloud/secrets-management).

```env
APP_ID=your_adzuna_app_id
APP_KEY=your_adzuna_app_key

Waseem Malek
LinkedIn: linkedin.com/in/waseemmalek
GitHub: @WaseemMalek


---

Let me know if you'd like me to personalize this further — like linking your real Streamlit URL, inserting your screenshot automatically, or writing a shorter version for LinkedIn!
