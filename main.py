import json
from auto_shawarma import Bot


def main():
    with open("conf.json") as f:
        Bot(json.load(f))


if __name__ == '__main__':
    main()
