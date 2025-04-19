import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_indeed_jobs(query="data analyst", location="London", max_pages=3):
    base_url = "https://uk.indeed.com/jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    jobs = []
    


    for page in range(0, max_pages * 10, 10):  # Indeed shows 10 results per page
        params = {
            "q": query,
            "l": location,
            "start": page
        }
        print(f"Scraping page {page//10 + 1}...")
        response = requests.get(base_url, headers=headers, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Page title:", soup.title.text)
        job_cards = soup.find_all('div', class_='job_seen_beacon')
        


        for card in job_cards:
            title = card.find('h2', class_='jobTitle')
            company = card.find('span', class_='companyName')
            location = card.find('div', class_='companyLocation')
            salary = card.find('div', class_='salary-snippet')
            summary = card.find('div', class_='job-snippet')

            jobs.append({
                "Title": title.text.strip() if title else None,
                "Company": company.text.strip() if company else None,
                "Location": location.text.strip() if location else None,
                "Salary": salary.text.strip() if salary else "Not listed",
                "Summary": summary.text.strip() if summary else None
            })

        time.sleep(1)  # Be polite to the server

    return pd.DataFrame(jobs)

if __name__ == "__main__":
    df = scrape_indeed_jobs(query="data analyst", location="London", max_pages=2)
    print(df.head())
    df.to_csv("C:/Waseem/job-market-insights/data/job_postings_raw.csv", index=False)
