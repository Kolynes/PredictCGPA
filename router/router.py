from typing import List
from kivy.event import EventDispatcher
from .route_view import RouteView
from .route import Route
from router import route_view
from kivy.properties import ListProperty

from router import route

class Router(EventDispatcher):
    routes: list
    root_route_view = None
    route_view_cursor = None
    history = []
    base = "/"
    direction = "left"

    def __init__(self, routes=[], base="/"):
        self.routes = routes
        self.base = base
        self.direction = "left"

    def register_route_view(self, route_view: RouteView):
        if self.root_route_view == None:
            self.root_route_view = route_view
            self.push(self.base)
        else:
            self.route_view_cursor = self.root_route_view
            while self.route_view_cursor.child != None:
                self.route_view_cursor = self.route_view_cursor.child
            self.route_view_cursor.child = route_view

    def get_route(self, path: str, routes: list):
        required_routes = []
        for route in routes:
            if path.startswith(route.path) and len(route.children) > 0:
                temp = self.get_route(path, route.children)
                if len(temp) > 0:
                    required_routes.extend(temp)
                    required_routes.append(route)
                    break
            elif route.path == path:
                required_routes.append(route)
                break
        return required_routes

    def push(self, path: str, args={}):
        self.direction = "left"
        print(self.get_route(path, self.routes))
        self.root_route_view.routes = self.get_route(path, self.routes)
        self.history.append(path)

    def pop(self):
        path = self.history[len(self.history) - 2]
        self.direction = "right"
        self.required_routes = self.get_route(path, self.routes)
        if self.required_routes == []:
            return
        self.root_route_view.switch_to(
            self.required_routes.pop().screen(),
            direction=self.direction
        )
        self.history.pop()