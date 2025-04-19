import pandas as pd
import os

def clean_job_data(input_path="C:/Waseem/job-market-insights/data/adzuna_jobs.csv", output_path="C:/Waseem/job-market-insights/data/adzuna_jobs_clean.csv"):
    # Load the raw data
    df = pd.read_csv(input_path)

    # Drop rows with no title or description
    df = df.dropna(subset=["Title", "Description"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing company/location with "Unknown"
    df["Company"] = df["Company"].fillna("Unknown")
    df["Location"] = df["Location"].fillna("Unknown")

    # Create a new column: average salary (if min/max exist)
    df["Salary Avg"] = df[["Salary Min", "Salary Max"]].mean(axis=1)

    # Flag remote jobs
    df["Is Remote"] = df["Description"].str.contains("remote", case=False, na=False)

    # Clean description text (optional starter)
    df["Description"] = df["Description"].str.replace(r'\s+', ' ', regex=True).str.strip()

    # Save cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")
    print(df.head())

if __name__ == "__main__":
    clean_job_data()
