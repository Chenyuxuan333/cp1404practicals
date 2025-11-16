from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        # Define a list of names
        names = ["Alice", "Bob", "Charlie", "Diana"]
        # Dynamically create a Label for each name
        for name in names:
            self.root.ids.main.add_widget(Label(text=name))
        return self.root

if __name__ == '__main__':
    DynamicLabelsApp().run()