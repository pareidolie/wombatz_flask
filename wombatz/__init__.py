from flask import Flask


def create_app(config):
    app = Flask("wombatz")

    app.config.from_object(config)

    from .views import views

    for view in views:
        app.register_blueprint(view)

    from .menu import menu

    menu.init(app)
    app.jinja_env.globals["menu"] = menu
    return app
