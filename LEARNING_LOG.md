# Summary — Python/Pandas Functions and Concepts

## Week 1 — Python (syntax and idiom)

### Control flow and error handling
- `try / except ValueError as e` — catches conversion errors (e.g. `int("abc")`), lets you handle them without crashing
- `while` with validation — combine type validation and range validation in the same loop

### Functions
- `def func(param, default=0):` — optional parameter with a default value (uses `=`, never `:`)
- `*args` — receives a variable number of arguments as a **tuple**
  - `len(args)` — counts how many arguments were passed
  - Example: `def average(*args): return sum(args) / len(args)`

### Data structures
- **List** `[]` — ordered, mutable collection
- **Tuple** `()` — ordered, **immutable** collection
  - Direct unpacking in a loop: `for name, age in people:`
- **Dictionary** `{}` — key-value pairs
  - `.get(key, default)` — returns the value for a key, or a default if it doesn't exist (avoids `KeyError`)
    - Counting pattern: `dict[key] = dict.get(key, 0) + 1`
  - `.items()` — returns `(key, value)` pairs, allows unpacking: `for key, value in dict.items():`
- **Set** `{}` (no `:`) — unordered collection, no duplicates
  - `.intersection()` or `&` — elements in **both** sets
  - `.difference()` or `-` — elements in one set but **not** the other
  - `.union()` or `|` — combines two sets (no duplicates)

### Comprehensions
- List: `[expression for item in iterable if condition]`
- Dictionary: `{key: value for item in iterable if condition}`
- Nested: `[word for sentence in sentences for word in sentence.split()]`

### Strings
- **f-string** (recommended): `f"{name}, {age}"` — automatic type conversion
- `.format()`: `"{}, {}".format(name, age)` — also converts automatically
- `+` (concatenation): **requires manual conversion** — `str(age)` before concatenating
- `.split()` — splits a string into a list of words
- `.capitalize()` — returns a new string with the first letter capitalized (doesn't modify the original)
- `" ".join(iterable)` — joins elements of an iterable into a string, separated by a space

**Important rule (came up repeatedly):** methods like `.capitalize()`, `.join()`, `.fillna()`, `.dropna()`, `.sort_values()` **don't modify the original object** — they return a new value. You need to assign the result to a variable to keep it.

---

## Week 2 — Pandas

### Base structures
- **Series** — single column, 1D. `df['column']` (single square brackets)
- **DataFrame** — 2D table. `df[['column']]` (a list inside square brackets) returns a DataFrame even with 1 column

### Selection and filtering
- **Boolean filtering:** `df[df['column'] > value]`
  - Multiple conditions: `df[(condition1) & (condition2)]` — use `&`/`|`/`~`, never `and`/`or`/`not`; parentheses required around each condition (due to operator precedence)
- **`.loc[rows, columns]`** — selection by **label**; slicing **includes** the end value (`0:3` includes row 3)
- **`.iloc[rows, columns]`** — selection by **position**; slicing **excludes** the end value (`0:3` excludes position 3, like normal lists)
- Combined: `df.loc[condition, 'column']` — filters rows by condition, returns only the requested column

### Aggregation
- `df.groupby('column')['other_column'].sum()` — aggregates by group
- `.agg(['sum', 'mean', 'count'])` — multiple aggregations at once
- `df.groupby(['col1', 'col2'])` — groups by a combination of several columns (produces a **MultiIndex** in the result)

### Missing values
- `.isna()` — returns `True`/`False` per cell; **always use this to detect `NaN`**, never `== None` (comparisons with `NaN` don't behave as expected)
- `.isna().sum()` — counts missing values in a column
- `df.copy()` — creates an independent copy of a DataFrame (avoids accidentally changing the original)
- `.dropna()` — removes rows with missing values
  - No arguments: checks **all** columns
  - `subset=['column']` — checks only the specified column
- `.fillna(value)` — replaces missing values with a specific value
  - Common options: fixed value (`0`), mean (`.mean()`), median (`.median()`), forward/backward fill
  - Choice depends on context — filling with `0` isn't always appropriate (e.g. monetary values)

---

## Still to come (Week 2)
- Merge/Join between DataFrames
- Feature engineering (derived columns)
- Close-out exercise: solo pipeline (read → clean → aggregate → export)