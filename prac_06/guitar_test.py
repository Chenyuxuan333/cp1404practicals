from guitar import Guitar

# Test get_age and is_vintage methods
def run_tests():
    # Test Guitar 1: Gibson L-5 CES (1922)
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(f"Gibson L-5 CES get_age() - Expected 103. Got {guitar1.get_age()}")
    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar1.is_vintage()}")

    # Test Guitar 2: Another Guitar (2013)
    guitar2 = Guitar("Another Guitar", 2013, 1000.00)
    print(f"Another Guitar get_age() - Expected 12. Got {guitar2.get_age()}")
    print(f"Another Guitar is_vintage() - Expected False. Got {guitar2.is_vintage()}")

    # Test a 50-year-old guitar
    guitar3 = Guitar("50-year old guitar", 1975, 500.00)
    print(f"50-year old guitar is_vintage() - Expected True. Got {guitar3.is_vintage()}")

run_tests()