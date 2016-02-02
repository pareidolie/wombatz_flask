from wombatz import create_app
from wombatz.config import Local


if __name__ == '__main__':
    app = create_app(Local)
    app.run(debug=True, port=80)
