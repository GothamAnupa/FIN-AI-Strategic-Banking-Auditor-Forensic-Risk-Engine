import pandas as pd

# 1. Actual Spend (What happened)
actuals_data = {
    "category": ["Marketing", "Cloud Infrastructure", "Salaries", "Office Rent", "Travel"],
    "actual_amount": [55000, 12000, 200000, 15000, 8500],
    "transaction_count": [142, 1, 50, 1, 12]
}

# 2. Budget (What was planned)
budget_data = {
    "category": ["Marketing", "Cloud Infrastructure", "Salaries", "Office Rent", "Travel"],
    "budget_amount": [40000, 8000, 200000, 15000, 5000]
}

def generate_csvs():
    pd.DataFrame(actuals_data).to_csv("actuals.csv", index=False)
    pd.DataFrame(budget_data).to_csv("budget.csv", index=False)
    print("✅ Financial data files (actuals.csv, budget.csv) created.")

if __name__ == "__main__":
    generate_csvs()