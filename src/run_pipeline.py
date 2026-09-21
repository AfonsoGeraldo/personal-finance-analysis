import pandas as pd
import loans_pipeline as lp
import db_utils as db

def run_pipeline():

    try:
        engine = db.get_engine()
        loans = lp.get_loans()
        print(loans)

        #Clean
        cleaned_df = lp.clean_loans(loans)
        if cleaned_df is None:
            print("Df is not cleaned.")
            return False
        print("Df cleaned!")

        #Aggregate
        aggregated_df = lp.aggregate_by_risk(cleaned_df)
        if aggregated_df is None:
            print("Df is not aggregated!")
            return False
        print("Df is aggregated!")

        table_name = "RunPipelineTable"

        #Save
        saved_df = lp.save_to_sql(aggregated_df, table_name, engine)
        if saved_df is False:
            print("Data couldn't be saved!")
            return False
        
        print("Data saved!")
        return True

    except Exception as e:
        print(f"Ocorreu o seguinte erro: {e}")
        return False

if __name__ == "__main__":
    run_pipeline()