__author__ = 'H.Rouhani'


class AppBuilder:
    log_path = None
    log_level = None

    def _init_app(self):
        raise NotImplementedError()

    def _build_logger(self, app):
        raise NotImplementedError()

    def _build_endpoints(self, app):
        raise NotImplementedError()

    def _build_cors(self, app):
        raise NotImplementedError()

    def construct(self):
        app = self._init_app()
        self._build_logger(app)
        self._build_endpoints(app)
        self._build_cors(app)
        return app
