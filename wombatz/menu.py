from flask import request, url_for


class Menu:
    def __init__(self):
        self._prefix = ""
        self._root = DropDown("_Root_")
        self._stack = [self._root]
        self._home = None

    @property
    def _current(self):
        return self._stack[-1]

    def activate(self, blueprint):
        self._prefix = blueprint.name

    def clear(self):
        self._prefix = ""

    def add(self, title, home=False):
        def decorator(endpoint_function):
            name = endpoint_function.__name__
            endpoint = "{}.{}".format(self._prefix, name)
            entry = MenuEntry(title, endpoint)
            self._current.add_child(entry)
            if home:
                self._home = endpoint
            return endpoint_function
        return decorator

    def push(self, title):
        drop_down = DropDown(title)
        self._current.add_child(drop_down)
        self._stack.append(drop_down)
        return self

    def __enter__(self):
        return self

    def pop(self):
        self._stack.pop()

    def __exit__(self, *_):
        self.pop()

    def __iter__(self):
        return self._root.__iter__()

    def __str__(self):
        return str(self._root)

    def init(self, app):
        self._home = url_for(self._home)
        self._root.init(app)

    @property
    def root(self):
        return self._root

    @property
    def brand(self):
        return self._root.title

    @property
    def home(self):
        return self._home


class BaseEntry:
    def __init__(self, title):
        self._title = title

    @property
    def title(self):
        return self._title


class DropDown(BaseEntry):
    def __init__(self, title):
        super().__init__(title)
        self._children = []

    def add_child(self, entry):
        self._children.append(entry)

    def __iter__(self):
        return self._children.__iter__()

    def str(self, level=0):
        yield "{}{}".format("  " * level, self._title)
        for child in self._children:
            yield from child.str(level + 1)

    def __str__(self):
        return "\n".join(self.str())

    def init(self, app=None):
        if app is not None:
            self._title = app.name.capitalize()
        [sub.init() for sub in self._children]

    @property
    def active(self):
        return any(e.active for e in self._children)

    is_nested = True


class MenuEntry(BaseEntry):
    def __init__(self, title, endpoint):
        super().__init__(title)
        self._endpoint = endpoint
        self._url = None

        """:type: list[MenuEntry]"""

    @property
    def endpoint(self):
        return self._endpoint

    def init(self):
        self._url = url_for(self._endpoint)
        [sub.init() for sub in self]

    def str(self, level=0):
        yield "{}{}@{}".format("  " * level, self._title, self._endpoint)

    def __str__(self):
        return self.str()

    def __iter__(self):
        return ().__iter__()

    @property
    def url(self):
        return self._url

    @property
    def active(self):
        return self.endpoint == request.endpoint

    is_nested = False


menu = Menu()
