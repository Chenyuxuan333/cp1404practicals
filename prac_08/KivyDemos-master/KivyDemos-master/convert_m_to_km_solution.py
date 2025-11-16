from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Your Name'

MILES_TO_KM = 1.60934  # Conversion constant


class MilesConverterApp(App):
    # StringProperty for the output label (automatically updates UI)
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_km_converter.kv')
        return self.root

    def handle_calculate(self):
        """Calculate km from miles and update output_km."""
        miles = self.get_validated_miles()
        self.output_km = str(miles * MILES_TO_KM)

    def handle_increment(self, change):
        """Increment/decrement miles by `change` and recalculate."""
        miles = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        """Validate input miles (return 0 if invalid)."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


if __name__ == '__main__':
    MilesConverterApp().run()