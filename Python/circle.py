import math

while True:
    try:
        radius = float(input("Radius: "))
    except ValueError:
        print("Please specify only numeric value for radius")
        continue;

    area = math.pi * radius ** 2
    print(f"The area of the circle is {area:,.2f}")
    break;