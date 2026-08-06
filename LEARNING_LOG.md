## 06/08/2026 — Personal Finance Analysis (Day 1)

### What I did
- Set up `personal-finance-analysis` project (structure, venv, Git init)
- Built `src/generate_data.py`: generated 3 years of synthetic daily data (2023-2025)
- Income: monthly salary (normal distribution) + random occasional bonuses
- Expenses: Groceries, Entertainment, Utilities — daily probability check per category, amounts via uniform distribution (wrote this part myself)
- Combined income + expenses into one DataFrame, sorted by date, saved to `data/transactions.csv`

### New concepts
- `np.random.uniform()` vs `np.random.normal()` — flat range vs. bell-curve distribution
- `np.random.seed()` — reproducibility of "random" generation
- `pd.DataFrame(list_of_dicts)` — building a DataFrame from a list of dictionaries
- `pd.concat()` with `ignore_index=True`, `.reset_index(drop=True)`
- `.to_csv(path, index=False)` — exporting a DataFrame, and why `index=False` matters