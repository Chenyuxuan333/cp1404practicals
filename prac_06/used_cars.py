"""CP1404/CP5632 Practical - Client code to use the Car class."""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # 1. Create limo with 100 fuel
    limo = Car("Limo", 100)
    # 2. Add 20 fuel to limo
    limo.add_fuel(20)
    # 3. Print limo's fuel
    print(f"Limo has fuel: {limo.fuel}")
    # 4. Attempt to drive 115 km
    limo.drive(115)
    # 7. Print limo to check __str__
    print(limo)


main()