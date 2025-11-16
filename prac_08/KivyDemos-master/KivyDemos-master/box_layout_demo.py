from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greet button press: update label with greeting"""
        input_name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {input_name}"

    def handle_clear(self):
        """Handle clear button press: reset input and label"""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"  # Reset to original label text


BoxLayoutDemo().run()
