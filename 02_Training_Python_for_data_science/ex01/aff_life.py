from load_csv import load
import matplotlib.pyplot as plt


try:
    dataset = load("life_expectancy_years.csv")
    # print(dataset.head())

    countries = dataset['country']
    years = dataset.columns[1:]
    # print(f'Countries: {countries.size} | Years: {years.size}')
    target = 'France'
    projections = dataset[dataset['country'] == target].iloc[0, 1:]

    plt.figure(figsize=(10, 8))
    plt.plot(years, projections, linestyle='-', color='b')
    plt.title(f'{target} Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')

    year_ticks = years[::40]
    plt.xticks(ticks=year_ticks, labels=year_ticks, rotation=45)

    plt.grid(False)
    plt.show()

except Exception as e:
    print(f"[ERROR]: {e}")
