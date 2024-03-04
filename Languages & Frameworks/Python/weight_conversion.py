allowed_units = ['kg', 'lb']

while True:
    try:
        weight_input = float(input("Weight: "))
    except ValueError:
        print("Please specify a valid numeric weight.")
        continue

    unit_input = input("Your unit (Kg/lb): ").lower()

    if unit_input not in allowed_units:
        print("Please only specify two units: Kg or lb")
    elif unit_input in ['kg', 'kgs']:
        converted_weight = weight_input * 2.20462
        print(f"Conversion from Kg to lb: {weight_input} Kg(s) -> {converted_weight:.2f} lb(s)")
        break
    elif unit_input in ['lb', 'lbs']:
        converted_weight = weight_input / 2.20462
        print(f"Conversion from lb to Kg: {weight_input} lb(s) -> {converted_weight:.2f} Kg(s)")
        break
    else:
        print("Please enter a valid unit (Kg or lb)")
