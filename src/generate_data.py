import pandas as pd
import numpy as np
from datetime import date, timedelta

# Esta linha garante que os números aleatórios gerados sejam os mesmos 
# a cada execução do código, permitindo reprodutibilidade dos resultados.
np.random.seed(42)

start_date = date(2023, 1, 1)
end_date = date(2025, 12, 31)

all_dates = []
current = start_date
while current <= end_date:
    all_dates.append(current)
    current += timedelta(days=1)

print(f"Total days: {len(all_dates)}")

income_transactions = []

for current in all_dates:
    if current.day == 1:
        salary = np.random.normal(loc=2200, scale=50)
        income_transactions.append({
            'Date': current,
            'Category': 'Salary',
            'Description': 'Monthly salary',
            'Amount': round(salary, 2),
            'Type': 'Income'
        })
    
    if np.random.random() < 0.02:
        bonus = np.random.uniform(100, 800)
        income_transactions.append({
            'Date': current,
            'Category': 'Bonus',
            'Description': 'Extra income',
            'Amount': round(bonus, 2),
            'Type': 'Income'
        })

expense_transactions = []

for current in all_dates:
    if np.random.random() < 0.1:
        expense_amount = np.random.uniform(10, 200)
        expense_transactions.append({
            'Date': current,
            'Category': 'Groceries',
            'Description': 'Grocery shopping',
            'Amount': round(expense_amount, 2),
            'Type': 'Expense'
        })
    
    if np.random.random() < 0.05:
        expense_amount = np.random.uniform(20, 500)
        expense_transactions.append({
            'Date': current,
            'Category': 'Entertainment',
            'Description': 'Movies, concerts, etc.',
            'Amount': round(expense_amount, 2),
            'Type': 'Expense'
        })
    
    if np.random.random() < 0.03:
        expense_amount = np.random.uniform(50, 1000)
        expense_transactions.append({
            'Date': current,
            'Category': 'Utilities',
            'Description': 'Electricity, water, internet bills',
            'Amount': round(expense_amount, 2),
            'Type': 'Expense'
        })

    if current.day == 15:
        expense_amount = np.random.normal(loc = 500, scale = 50)
        expense_transactions.append({
            'Date': current,
            'Category': 'Housing',
            'Description': 'Monthly housing payment',
            'Amount': round(expense_amount, 2),
            'Type': 'Expense'
        })

    if np.random.random() < 0.01:
        expense_amount = np.random.uniform(100, 2000)
        expense_transactions.append({
            'Date': current,
            'Category': 'Healthcare',
            'Description': 'Medical expenses',
            'Amount': round(expense_amount, 2),
            'Type': 'Expense'
        })

    if np.random.random() < 0.25:
        expense_amount = np.random.uniform(20, 50)
        expense_transactions.append({
            'Date': current,
            'Category': 'Transportation',
            'Description': 'Fuel, public transport, etc.',
            'Amount': round(expense_amount, 2),
            'Type': 'Expense'
        })

print(f"Income transactions generated: {len(income_transactions)}")
print(f"Expense transactions generated: {len(expense_transactions)}")

# O DataFrame cria uma tabela a partir de uma lista (dicionário)
df_income = pd.DataFrame(income_transactions)
df_expense = pd.DataFrame(expense_transactions)

df_all = pd.concat([df_income, df_expense]).sort_values(by='Date').reset_index(drop=True)

print(df_all.head())
print(f"Total transactions: {len(df_all)}")

df_all.to_csv('data/transactions.csv', index=False)
print("Data saved to data/transactions.csv")