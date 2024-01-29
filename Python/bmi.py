try:
    weight = float(input("Enter your weight in kilograms: "))
    height_cm = float(input("Enter your height in centimeters: "))
except ValueError:
    print("Please enter valid numeric values for weight and height.")
    exit()

# Convert height to meters
height_m = height_cm / 100

bmi = weight / ((height_cm/100) ** 2)

if bmi < 18.5:
    bmi_type = "Underweight"
elif 18.5 <= bmi < 25:
    bmi_type = "Normal weight"
elif 25 <= bmi < 30:
    bmi_type = "Overweight"
else:
    bmi_type = "Obese"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are {bmi_type}")
