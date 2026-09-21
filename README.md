# Personal Finance Analysis

A learning project exploring synthetic personal finance data using Python, pandas, and SQL Server integration.

## Overview

This project simulates personal financial transactions (income and expenses) and analyzes them using pandas, then extends into a full SQL Server pipeline: extracting data from a database, transforming it with pandas, and writing results back.

## Project Structure

```
personal-finance-analysis/
├── data/
│   ├── transactions.csv       # Synthetic transaction data
│   └── week2.csv               # Exported aggregation from Week 2 close-out
├── notebooks/
│   ├── 01_exploration.ipynb    # Initial data exploration
│   ├── analysis.ipynb          # Core pandas practice: filtering, groupby, missing values, merge, feature engineering
│   ├── week2_finalExercise.ipynb   # Week 2 close-out pipeline (CSV-based)
│   └── 03_sql_integration.ipynb    # Week 3: SQL Server connection, read/write, error handling
├── src/
│   ├── generate_data.py        # Generates synthetic transaction data
│   ├── db_utils.py             # SQL Server connection (get_engine)
│   ├── loans_pipeline.py       # Loans data functions: get_loans, clean_loans, aggregate_by_risk, save_to_sql
│   └── run_pipeline.py         # End-to-end pipeline entry point
└── README.md
```

## Setup

1. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install dependencies:
   ```
   pip install pandas pyodbc sqlalchemy
   ```
3. Ensure a local SQL Server instance is running, with the `Testes` database and a `Loans` table (see `src/loans_pipeline.py` for expected schema).

## Usage

### Generate synthetic transaction data
```
python src/generate_data.py
```

### Run the full Loans pipeline (extract → clean → aggregate → save)
```
python src/run_pipeline.py
```
This connects to SQL Server, reads the `Loans` table, removes fully-paid loans (`OutstandingBalance == 0`), aggregates average outstanding balance by `RiskCategory`, and saves the result to a new table (`RunPipelineTable`).

## Key Concepts Practiced

- **pandas**: Series vs. DataFrame, boolean filtering, `.loc`/`.iloc`, `groupby`/`.agg()`, missing values (`.isna()`, `.dropna()`, `.fillna()`), merge/join, feature engineering (date parts, derived columns)
- **SQL Server integration**: `SQLAlchemy` connections, `pd.read_sql()`, `.to_sql()`, raw SQL execution, error handling
- **Software structure**: separating logic into reusable modules (`db_utils.py`, `loans_pipeline.py`), consistent function return contracts (`True`/`False`/`None`), `if __name__ == "__main__":` entry point pattern
- **Git**: feature branches, incremental commits, pushing to a remote repository

## Notes

- SQL Server connection uses `TrustServerCertificate=yes` for local development (not recommended for production).
- Functions follow a consistent pattern: return `None` (or `False`) on failure, with an error message printed, rather than letting exceptions propagate uncaught.
