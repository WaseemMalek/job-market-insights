import streamlit as st
import pandas as pd

# Load cleaned data
df = pd.read_csv("src/adzuna_jobs_clean.csv")

st.set_page_config(page_title="Job Market Insights", layout="wide")
st.title("Job Market Insights Dashboard")

# Filters
# Add "All" to the location dropdown
location_options = ["All"] + sorted(df["Location"].unique().tolist())
selected_location = st.selectbox("Select Location", options=location_options)

# Filter based on selection
if selected_location == "All":
    filtered_df = df.copy()
else:
    filtered_df = df[df["Location"] == selected_location]

remote_only = st.checkbox("Show Remote Jobs Only")

# --- COMPANY Filter ---
company_options = ["All"] + sorted(filtered_df["Company"].unique().tolist())
selected_company = st.selectbox("Select Company", options=company_options)

# Apply company filter
if selected_company != "All":
    filtered_df = filtered_df[filtered_df["Company"] == selected_company]

# --- SALARY SLIDER ---
salary_range = None  # 👈 create a default value

if not filtered_df.empty and filtered_df["Salary Avg"].notna().sum() > 0:
    min_salary = int(filtered_df["Salary Avg"].min())
    max_salary = int(filtered_df["Salary Avg"].max())

    if min_salary < max_salary:
        salary_range = st.slider("Select Salary Range (£)",
                                 min_value=min_salary,
                                 max_value=max_salary,
                                 value=(min_salary, max_salary),
                                 step=1000)
        filtered_df = filtered_df[
            (filtered_df["Salary Avg"] >= salary_range[0]) &
            (filtered_df["Salary Avg"] <= salary_range[1])
        ]
    else:
        st.info(f"Only one salary value available: £{min_salary}")

# ✅ Don't apply salary_range filter again if it was already applied above!
# (No need to apply again later)


# --- SEARCH BAR ---
search_term = st.text_input("🔍 Search for a keyword in job titles or descriptions")

if search_term:
    filtered_df = filtered_df[
        filtered_df["Title"].str.contains(search_term, case=False, na=False) |
        filtered_df["Description"].str.contains(search_term, case=False, na=False)
    ]

if remote_only:
    filtered_df = filtered_df[filtered_df["Is Remote"] == True]

# Show summary stats
st.subheader("Summary Stats")
st.write(f"Number of Jobs: {len(filtered_df)}")
st.write(f"Average Salary: £{filtered_df['Salary Avg'].mean():,.0f}")

# Top companies bar chart
st.subheader("Top Hiring Companies")
top_companies = filtered_df["Company"].value_counts().head(10)
st.bar_chart(top_companies)

# Show table
st.subheader("Job Listings")
st.dataframe(filtered_df[["Title", "Company", "Location", "Salary Avg", "Is Remote", "URL"]])
