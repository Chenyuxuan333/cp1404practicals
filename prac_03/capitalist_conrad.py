import random

MIN_PRICE = 1.0
MAX_PRICE = 100.0
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
number_of_days = 0

with open("price_simulation.txt", "w") as file:
    file.write(f"Starting price: ${INITIAL_PRICE:,.2f}\n")
    print(f"Starting price: ${INITIAL_PRICE:,.2f}")

    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1
        price_change = 0
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)

        line = f"On day {number_of_days} price is: ${price:,.2f}\n"
        file.write(line)
        print(line, end="")