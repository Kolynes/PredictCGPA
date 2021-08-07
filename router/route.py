from router.route_view import RouteView
from kivy.uix.screenmanager import Screen

class Route:
    path: str
    screen: Screen
    children: list

    def __init__(self, path: str, screen: Screen, children: list=[]):
        self.path = path
        self.screen = screen
        self.children = children

    def __str__(self): 
        return self.path