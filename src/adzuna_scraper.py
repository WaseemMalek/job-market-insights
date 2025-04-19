import requests
import pandas as pd
import os
import json
from dotenv import load_dotenv

# ✅ Load .env from current script's folder
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

print("APP_ID:", APP_ID)
print("APP_KEY:", APP_KEY)


def fetch_jobs_adzuna(query="data analyst", location="London", pages=2):
    jobs = []
    for page in range(1, pages + 1):
        url = f"https://api.adzuna.com/v1/api/jobs/gb/search/{page}"
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "what": query,
            "where": location,
            "results_per_page": 20,
            "content-type": "application/json"
        }

        response = requests.get(url, params=params)

        # 🛡️ Safely try to parse the JSON
        try:
            data = response.json()
        except Exception as e:
            print("❌ Failed to parse JSON. Raw response:")
            print(response.text)
            raise e

        print(f"\n🔎 Page {page} results:")
        print(json.dumps(data, indent=2))

        for result in data.get("results", []):
            jobs.append({
                "Title": result.get("title"),
                "Company": result.get("company", {}).get("display_name"),
                "Location": result.get("location", {}).get("display_name"),
                "Salary Min": result.get("salary_min"),
                "Salary Max": result.get("salary_max"),
                "Category": result.get("category", {}).get("label"),
                "Description": result.get("description"),
                "URL": result.get("redirect_url")
            })

    return pd.DataFrame(jobs)

if __name__ == "__main__":
    df = fetch_jobs_adzuna(query="data analyst", location="London", pages=10)
    print(df.head())

    # Save to CSV
    df.to_csv("C:/Waseem/job-market-insights/data/adzuna_jobs.csv", index=False)

