from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialized version of a Taxi with additional features and a higher fare structure."""

    # Flagfall is a class variable representing the initial hire fee
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialize a SilverServiceTaxi instance.

        Args:
            name (str): The name of the taxi.
            fuel (float): The initial fuel amount.
            fanciness (float): A multiplier for the price per kilometer.
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Adjust the price per km based on the fanciness level
        self.price_per_km *= fanciness

    def get_fare(self):
        """Calculate the total fare including the flagfall and distance traveled."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
