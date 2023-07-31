import os

from prisma import Prisma
from src.server import app

env = os.environ.get('ENV', 'dev')


def main():
    db = Prisma(auto_register=True)
    db.connect()
    app.run(port=8000, debug=env == 'dev')


if __name__ == '__main__':
    main()
