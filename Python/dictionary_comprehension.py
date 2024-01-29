capital_temperature_c = {
    'Thailand': 35,
    'Philippines': 25,
    'China': -3,
    'USA': 12,
    'Netherlands': 14,
    'France': -5
}

capital_temperature_f = {capital: ((temp * 9/5) + 32) for (capital, temp) in capital_temperature_c.items()}
print(capital_temperature_f)
capital_hot_or_cold = {capital: print(capital,'hot') if temp >= 25 else print(capital,'cold') for capital, temp in capital_temperature_c.items()}
