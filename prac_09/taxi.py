class Car:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def drive(self, distance):
        distance_driven = min(distance, self.fuel)
        self.fuel -= distance_driven
        self.odometer += distance_driven
        return distance_driven

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"


class Taxi(Car):
    price_per_km = 1.23
    start_fare = 4.0  # 起步价（假设）

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def start_fare(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

    def get_fare(self):
        return self.start_fare + self.current_fare_distance * self.price_per_km

    def __str__(self):
        return f"{super().__str__()}, current fare=${self.get_fare():.2f}"
