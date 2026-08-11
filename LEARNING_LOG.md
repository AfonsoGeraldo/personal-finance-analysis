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

## 11/08/2026 — Personal Finance Analysis (Day 2)

### What I did
- Introduced Git branches for the first time: created `feature/more-categories`, added Housing, Healthcare, and Transportation expense categories (wrote the code myself, adjusted Transportation frequency/amount after a sanity check), merged into `main`, pushed, deleted the branch
- Regenerated data: 536 total transactions
- Started the exploration notebook: converted `Date` to datetime, set it as index
- Used `.resample('ME')` to get monthly totals — first for combined income+expenses, then separately for income and expenses
- Calculated monthly net savings (income - expenses), which pandas aligned automatically by date
- Used `.groupby('Category')` to see total spending by category, sorted descending

### New concepts
- `pd.to_datetime()` and setting a datetime column as index — needed for time-based operations
- `.resample('ME')` — grouping rows into time buckets (monthly)
- `.groupby('Category')` — same split-apply-combine idea as resample, but by column value instead of time
- Index alignment: subtracting two Series with matching date indexes just works, no merge needed
- Git branches end-to-end: `checkout -b`, commit, `checkout main`, `merge`, `push`, `branch -d`