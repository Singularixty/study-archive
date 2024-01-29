class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} - ${self.price}")


class CarShowroom:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_inventory(self):
        print(f"\n{self.name} Inventory:")
        for car in self.cars:
            car.display_info()

    def find_car_by_make(self, make):
        matching_cars = [car for car in self.cars if car.make.lower() == make.lower()]
        if matching_cars:
            print(f"\nCars with make '{make}':")
            for car in matching_cars:
                car.display_info()
        else:
            print(f"No cars found with make '{make}' in {self.name} inventory.")


car1 = Car("Toyota", "Camry", 2022, 25000)
car2 = Car("Honda", "Civic", 2023, 22000)
car3 = Car("Ford", "Mustang", 2021, 40000)

showroom = CarShowroom("Singularixty Showroom")

showroom.add_car(car1)
showroom.add_car(car2)
showroom.add_car(car3)


showroom.show_inventory()


showroom.find_car_by_make("Toyota")
