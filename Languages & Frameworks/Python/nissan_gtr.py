class Car():
    def __init__(self, Name, Type, Color, Wheels):
        self.Name = Name
        self.Type = Type
        self.Color = Color
        self.Wheels = Wheels

if __name__ == '__main__':
    nissan_GTR = Car(Name='Nissan GTR', Type='Luxury Car', Color='Yellow',Wheels=4)
    print(nissan_GTR.Name)