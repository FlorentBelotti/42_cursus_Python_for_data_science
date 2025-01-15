from load_csv import load
import matplotlib.pyplot as plt


def convert_to_int(value):
    if isinstance(value, str):
        if 'k' in value:
            return int(float(value.replace('k', '')) * 1_000)
        elif 'M' in value:
            return int(float(value.replace('M', '')) * 1_000_000)
    return int(value)


try:
    dataset = load("population_total.csv")

    countries = dataset['country']
    years = dataset.columns[1:].astype(int)
    t1 = dataset[dataset['country']
                 == 'France'].iloc[0, 1:].apply(convert_to_int)
    t2 = dataset[dataset['country']
                 == 'Belgium'].iloc[0, 1:].apply(convert_to_int)

    plt.figure(figsize=(10, 9))
    plt.plot(years, t1, linestyle='-', color='g', label='France')
    plt.plot(years, t2, linestyle='-', color='b', label='Belgium')
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()

    year_ticks = range(1800, 2051, 40)
    plt.xticks(ticks=year_ticks, labels=year_ticks, rotation=45)

    plt.grid(False)
    plt.show()

except Exception as e:
    print(f"[ERROR]: {e}")
