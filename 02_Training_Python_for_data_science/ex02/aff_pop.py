from load_csv import load
import matplotlib.pyplot as plt


try:
    dataset = load("population_total.csv")
    # print(dataset.head())

    countries = dataset['country']
    years = dataset.columns[1:]
    # print(f'Countries: {countries.size} | Years: {years.size}')

    years_until_2040 = years[:years.get_loc('2040') + 1]

    t1_projection = dataset.loc[dataset['country'] == 'France',
                                years_until_2040].iloc[0]
    t2_projection = dataset.loc[dataset['country'] == 'Belgium',
                                years_until_2040].iloc[0]

    plt.figure(figsize=(10, 8))
    plt.plot(years_until_2040, t1_projection, linestyle='-', color='b',
             label='France')
    plt.plot(years_until_2040, t2_projection, linestyle='-', color='g',
             label='Belgium')
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')

    year_ticks = years_until_2040[::40]
    plt.xticks(ticks=year_ticks, labels=year_ticks, rotation=45)

    plt.legend()
    plt.grid(False)
    plt.show()

except Exception as e:
    print(f"[ERROR]: {e}")
