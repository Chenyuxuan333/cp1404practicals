import unittest
from unreliable_car import UnreliableCar
import random

class TestUnreliableCar(unittest.TestCase):
    def test_initialization(self):
        car = UnreliableCar("Test Car", 100, 50)
        self.assertEqual(car.name, "Test Car")
        self.assertEqual(car.fuel, 100)
        self.assertEqual(car.reliability, 50)

    def test_drive_when_reliable(self):
        random.seed(42)  # Fix random seed for test reproducibility
        car = UnreliableCar("Reliable Car", 200, 90)
        distance_driven = car.drive(100)
        self.assertEqual(distance_driven, 100)
        self.assertEqual(car.fuel, 100)

    def test_drive_when_unreliable(self):
        random.seed(10)  # Fix random seed for test reproducibility
        car = UnreliableCar("Unreliable Car", 200, 10)
        distance_driven = car.drive(100)
        self.assertEqual(distance_driven, 0)
        self.assertEqual(car.fuel, 200)

    def test_multiple_drive_attempts(self):
        car = UnreliableCar("Test Car", 1000, 30)
        total_distance_driven = 0
        total_attempts = 1000
        for _ in range(total_attempts):
            total_distance_driven += car.drive(10)
        # Verify total distance roughly matches 30% reliability (allow 20% error margin)
        expected_distance = 0.3 * total_attempts * 10
        self.assertAlmostEqual(total_distance_driven, expected_distance, delta=expected_distance * 0.2)

    unittest.main()