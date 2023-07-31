from prisma import Prisma


def main():
    prisma = Prisma(auto_register=True)

    prisma.connect()

    # write your queries here
    user = prisma.user.create(
        data={
            'name': 'Robert',
            'email': 'robert@craigie.dev',
            "password": "password"
        },
    )

    prisma.disconnect()


if __name__ == '__main__':
    main()
