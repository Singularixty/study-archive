class Car
  attr_accessor :name, :seats, :wheels

  def initialize(name, seats, wheels)
    @name = name
    @seats = seats
    @wheels = wheels
  end
end

car_1 = Car.new('Nissan GTR', 2, 4)
puts "#{car_1.name} has #{car_1.seats} seats and #{car_1.wheels} wheels"
