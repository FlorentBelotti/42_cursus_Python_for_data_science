import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load

income_path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
le_path = "life_expectancy_years.csv"

year = 1900

income_data = load(income_path)
le_data = load(le_path)

if income_data is None or le_data is None:
    print("Error loading datasets.")
else:
    year_str = str(year)
    if year_str not in income_data.columns or year_str not in le_data.columns:
        print(f"Error: Year {year} not found in one or both datasets.")
    else:

        income_data = income_data[['country', year_str]]
        le_data = le_data[['country', year_str]]
        merged_data = pd.merge(income_data, le_data, on="country",
                               suffixes=('_income', '_life'))
        merged_data.columns = ['country', 'income', 'le']
        merged_data.dropna(inplace=True)
        merged_data['income'] = pd.to_numeric(merged_data['income'],
                                              errors='coerce')
        merged_data['le'] = pd.to_numeric(merged_data['le'],
                                          errors='coerce')

        merged_data.dropna(inplace=True)

        if merged_data.empty:
            print("Error: No data to plot.")
        else:
            plt.figure(figsize=(10, 6))
            plt.scatter(merged_data['income'], merged_data['le'], alpha=1)
            plt.title(f"{year}")
            plt.xlabel("Gross Domestic Product (GDP)")
            plt.ylabel("Life Expectancy")
            plt.xscale('log')
            plt.grid(False)

            ticks = [300, 1000, 10000]
            tick_labels = ['300', '1k', '10k']
            plt.xticks(ticks, tick_labels)

            plt.show()
