from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from arsd.ars_core import ARSKernel

class MainLayout(BoxLayout):
    output_text = StringProperty("Welcome to PolyOS ARS Kernel")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kernel = ARSKernel()

    def run_kernel(self):
        results = self.kernel.run_steps(10)
        self.output_text = "Kernel outputs:\n" + ", ".join(str(x) for x in results)

class PolyOSApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    PolyOSApp().run()