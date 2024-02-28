import matplotlib.pyplot as plt
import seaborn as sns

# Years from 2013 to 2023
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

# Example exchange rates of USD to TL (Turkish Lira) for each year
# Note: These rates are illustrative and not based on actual historical data
exchange_rates = [1.9020, 2.1881, 2.7209, 3.0223, 3.6491, 4.8115, 5.68, 7.02, 8.43, 13.88, 18.25]

# Additional data for plotting
years_additional = [2015, 2023]
exchange_rates_additional = [48, 68.5]

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Yıl', fontsize=14)
ax1.set_ylabel('Exchange rate (USD to TL)', color=color, fontsize=14)
ax1.plot(years, exchange_rates, marker='o', linestyle='-', color=color, label='Exchange rate')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:red'
ax2.set_ylabel('% Negative perception', color=color, fontsize=14)  # we already handled the x-label with ax1
ax2.plot(years_additional, exchange_rates_additional, marker='x', linestyle='--', color=color, label='% Negative Perception towards Syrians')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.legend()
plt.show()

