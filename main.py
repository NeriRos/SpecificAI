from src.server import app
import os

env = os.environ.get('ENV', 'dev')

if __name__ == '__main__':
    app.run(port=8000, debug=env == 'dev')
