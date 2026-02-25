import pandas as pd

def calculate_variances(actuals_path="actuals.csv", budget_path="budget.csv"):
    df_actuals = pd.read_csv(actuals_path)
    df_budget = pd.read_csv(budget_path)
    
    df = pd.merge(df_actuals, df_budget, on="category")
    
    # These lines will now work because they are numeric!
    df['variance'] = df['actual_amount'] - df['budget_amount']
    df['variance_pct'] = (df['variance'] / df['budget_amount']) * 100
    
    flagged_items = df[df['variance_pct'] > 10].to_dict(orient="records")
    return flagged_items