from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.properties import ListProperty, ObjectProperty

class RouteView(ScreenManager):
    routes = ListProperty()
    raw_route = None
    child = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()
        self.app.router.register_route_view(self)

    def on_routes(self, instance, routes):
        print(routes)
        route = routes[len(routes) - 1]
        if self.raw_route:  
            if self.raw_route.path != route.path:
                self.raw_route = route.path
                self.switch_to(
                    route.screen(),
                    direction=self.app.router.direction
                )
        elif self.raw_route == None:
            self.raw_route = route
            self.switch_to(
                route.screen(),
                direction=self.app.router.direction
            )
        if 
        self.child.routes = routes[:len(routes) - 1]

    def on_child(self, instance, child):
        child.routes = self.routes[:len(self.routes) - 1]




