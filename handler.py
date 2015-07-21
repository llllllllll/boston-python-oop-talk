from flask.views import MethodView


class TrivialEndpoint(MethodView):
    """An endpoint handler that returns
    the method name.
    """
    def get(self):
        return 'hello from my new webserver'
