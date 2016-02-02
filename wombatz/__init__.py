from flask import Flask


def create_app(config):
    app = Flask("wombatz")

    app.config.from_object(config)

    from .views import views

    for view in views:
        app.register_blueprint(view)

    from .menu import menu

    with app.app_context():
        menu.init(app)
    print(menu)
    app.jinja_env.globals["menu"] = menu

    return app
