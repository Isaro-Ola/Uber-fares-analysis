
**NAMES**: ISARO MUHIRWA Ola 

**ID**: 26878  

# Uber Fares Big Data Analysis

This project involves performing exploratory data analysis (EDA) on an Uber Fares dataset using Python and visualizing the insights using Power BI.

---

##  Dataset Description
This dataset has information about Uber rides like the pickup and drop-off locations, how much the fare was, how many passengers were in the car, and the date and time. I used Python to clean and analyze the data, and then I created visuals in Power BI to better understand the trends.

##  Data Cleaning Steps
- I removed rows where some important values like coordinates were missing.
- I got rid of fare amounts or distances that didn’t make sense.
- I calculated the distance between where a ride started and ended.
- I also took the hour out of the datetime to use it for time-based analysis.

##  Key Visualizations
1. How fare amounts are spread (distribution)
2. Average fare during each hour of the day
3. Number of rides for different passenger counts
4. Average fare compared to distance
5. Number of rides per hour
6. Total fare grouped by passenger count

## 💡 Insights & Outcomes
- Most Uber rides happen in the morning and evening rush hours (7AM–9AM and 5PM–8PM).
- The farther the ride, the more expensive the fare.
- A lot of rides only have 1 or 2 passengers.
- I also found and removed some weird outliers in the fare values that were messing up the graphs.

## 🔧 Tools Used
- Python (with Pandas)
- Power BI Desktop
- GitHub for version control and submission

## 📁 Files Included
- `analysis.py`: My Python script where I cleaned and explored the data.
- `26878 Uber Dashboard.pbix`: Power BI dashboard with the visuals.
- `uber_cleaned.zip`: This is the cleaned CSV file. I zipped it because the original `.csv` was too big (over 25MB) for GitHub to allow.
- `screenshots/`: This folder has all the screenshots showing the steps I took and the outputs I got.
