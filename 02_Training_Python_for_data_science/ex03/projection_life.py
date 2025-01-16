import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load

try:
    income_path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_path = "life_expectancy_years.csv"
    income_data = load(income_path)
    life_data = load(life_path)
    if income_data is None or life_data is None:
        raise Exception("Data not found\n")
except Exception as e:
    print(f"[FILE_ERROR]: {e}")

try:
    if '1900' not in income_data.columns or '1900' not in life_data.columns:
        raise Exception("Year 1900 not found in one or both datasets\n")
    income_data = income_data[['country', '1900']]
    life_data = life_data[['country', '1900']]
    merged_data = pd.merge(income_data, life_data, on="country",
                           suffixes=('_income', '_life'))
    merged_data.columns = ['country', 'income', 'life']
    merged_data['income'] = pd.to_numeric(merged_data['income'],
                                          errors='coerce')
    merged_data['life'] = pd.to_numeric(merged_data['life'], errors='coerce')
    merged_data.dropna(inplace=True)
    if merged_data.empty:
        raise Exception("No data to plot\n")
except Exception as e:
    print(f"[DATA_ERROR]: {e}")

try:
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_data['income'], merged_data['life'], alpha=1)
    plt.title("1900")
    plt.xlabel("Gross Domestic Product (GDP)")
    plt.ylabel("Life Expectancy")
    plt.xscale('log')
    plt.grid(False)
    ticks = [300, 1000, 10000]
    tick_labels = ['300', '1k', '10k']
    plt.xticks(ticks, tick_labels)
    plt.show()
except Exception as e:
    print(f"[PROJECTION_ERROR]: {e}")
