overworld_x = None
overworld_y = None
overworld_z = None
nether_x = None
nether_y = None
nether_z = None

action = input("Are you looking for Nether/Overworld (N/O): ").lower()

if action in ['n', 'nether', 'o', 'overworld']:
    x_coord, y_coord, z_coord = input("X Coordinate: "), input("Y Coordinate: "), input("Z Coordinate: ")

    if x_coord.isdigit() and y_coord.isdigit() and z_coord.isdigit():
        x, y, z = int(x_coord), int(y_coord), int(z_coord)
        if action in ['n', 'nether']:
            nether_x, nether_y, nether_z = x // 8, y, z // 8
            print(f"Your Coordinate (Overworld): {x},{y},{z}")
            print(f"Nether Coordinate: {nether_x},{nether_y},{nether_z}")
        else:
            overworld_x, overworld_y, overworld_z = x * 8, y, z * 8
            print(f"Your Coordinate (Nether): {x},{y},{z}")
            print(f"Overworld Coordinate: {overworld_x},{overworld_y},{overworld_z}")
    else:
        print("Please enter only numbers for X, Y, and Z coordinates.")
else:
    print("Invalid input. Please enter 'N' for Nether or 'O' for Overworld.")
