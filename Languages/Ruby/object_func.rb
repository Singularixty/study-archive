class Vehicle
  attr_accessor :name, :seats, :wheels

  def initialize(name, seats, wheels)
    @name = name
    @seats = seats
    @wheels = wheels
  end

  def Type_Declare
        if @wheels == 2
          return "Motorcycle"
        else
          return "Car"
        end
  end
end

Vehicle_1 = Vehicle.new('Nissan GTR', 2, 4)
puts "#{Vehicle_1.name} has #{Vehicle_1.seats} seats and #{Vehicle_1.wheels} wheels"
puts Vehicle_1.Type_Declare
Vehicle_2 = Vehicle.new('Yamaha', 2, 2)
puts "#{Vehicle_2.name} has #{Vehicle_2.seats} seats and #{Vehicle_2.wheels} wheels"
puts Vehicle_2.Type_Declare
