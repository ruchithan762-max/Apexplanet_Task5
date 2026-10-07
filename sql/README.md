# ApexPlanet Data Analytics Internship

This project contains my work for the 30-Day Data Analytics Internship at ApexPlanet Software Pvt. Ltd.

## Tasks

- Task 1: Foundational Setup & Exploratory Data Analysis
- Task 2: SQL for Data Extraction
- Task 3: Data Visualization & Dashboarding
- Task 4: Advanced Analytics
- Task 5: Final Report & Automation

## Project Overview

This project analyzes the Sample Superstore dataset and provides data cleaning,
SQL analysis, visualization, advanced analytics, and an automated data pipeline.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- SQL
- Excel
- GitHub

## Project Structure

- `data/` - Raw and processed datasets
- `notebooks/` - Analysis notebooks
- `dashboards/` - Dashboard files
- `reports/` - Final report, dashboard screenshot, and PDF report
- `scripts/` - Automation scripts
- `sql/` - SQL queries
- `requirements.txt` - Python dependencies

## Automation Pipeline

The automation script is located at:

`scripts/automation.py`

The pipeline:

1. Loads the raw Superstore CSV data
2. Cleans the dataset
3. Calculates business KPIs
4. Creates category, region, and monthly summaries
5. Saves cleaned data
6. Exports KPI results to Excel

### Run the Automation

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the automation script:

```bash
python scripts/automation.py
```