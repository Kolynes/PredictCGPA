from router import Router, RouteView, Route
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from views import *

class PredictCGPAApp(MDApp):
    router = Router(
        routes=[
            Route("/", lambda: HomeScreen(), children=[
                Route("/", lambda: ScreenOneScreen()),
                Route("/two", lambda: ScreenTwoScreen()),
            ]),
            Route("/settings", lambda: SettingsScreen())
        ]
    )
    
    def build(self):
        return Builder.load_file("./PredictCGPA.kv")