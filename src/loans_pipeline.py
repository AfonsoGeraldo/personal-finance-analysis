import pandas as pd
import db_utils as db

def get_loans():
    query = 'Select * from dbo.loans'
    engine = db.get_engine()
    try:
        loans = pd.read_sql(query, engine)
        return loans
    except Exception as e:
        print(f"There's an error: {e}")
    
def clean_loans(df):
    try:
        df = df[df['OutstandingBalance'] != 0]
        return df
    except Exception as e:
        print(f"It's not possible to clean the dataframe: {e}")
        return

def aggregate_by_risk (df):
    try:
        if df is not None:
            df_groupped = df.groupby('RiskCategory')[['OutstandingBalance']].mean().reset_index()
            return df_groupped
        else:
            print("Failed while cleaning")
            return
    except Exception as e:
        print(f"It's not possible to aggregate by risk: {e}")
        return

def save_to_sql(df, table_name, engine):
    try:
        if df is not None:
            df.to_sql(table_name, engine, if_exists='append', index=False)
            return True
        else:
            print("The df is empty. Please insert a new one.")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False