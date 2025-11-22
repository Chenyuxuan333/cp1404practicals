import unittest
from silver_service_taxi import SilverServiceTaxi

class TestSilverServiceTaxi(unittest.TestCase):
    """Test cases for the SilverServiceTaxi class."""

    def test_initialization(self):
        """Test that the SilverServiceTaxi is initialized correctly."""
        taxi = SilverServiceTaxi("Hummer", 200, 2)
        self.assertEqual(taxi.name, "Hummer")
        self.assertEqual(taxi.fuel, 200)
        self.assertEqual(taxi.fanciness, 2)
        self.assertEqual(taxi.price_per_km, 2 * 1.23)  # Assuming base price is $1.23/km
        self.assertEqual(taxi.flagfall, 4.50)

    def test_calculate_fare(self):
        """Test that the fare is calculated correctly with flagfall and fanciness."""
        # Test case from the problem: 18km trip with fanciness of 2
        taxi = SilverServiceTaxi("Test Taxi", 100, 2)
        taxi.drive(18)
        # Expected fare: 4.50 (flagfall) + (18 * 1.23 * 2) = 4.50 + 44.28 = 48.78
        self.assertEqual(taxi.get_fare(), 48.78)

    def test_str_representation(self):
        """Test the string representation includes the flagfall."""
        taxi = SilverServiceTaxi("Limo", 150, 3)
        self.assertEqual(
            str(taxi),
            "Limo, fuel=150, odo=0, 0km on current fare, $3.69/km plus flagfall of $4.50"
        )

    def test_drive_and_fare_reset(self):
        """Test that driving resets the current fare distance correctly."""
        taxi = SilverServiceTaxi("Test", 50, 1.5)
        taxi.drive(10)
        self.assertEqual(taxi.get_fare(), 4.50 + (10 * 1.23 * 1.5))  # 4.50 + 18.45 = 22.95
        taxi.start_fare()  # Reset the fare
        self.assertEqual(taxi.get_fare(), 4.50)  # Only flagfall initially

if __name__ == '__main__':
    unittest.main()