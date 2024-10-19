import unittest
import json

from auto_shawarma import Bot


class TestStubCase(unittest.TestCase):
    def test_case0(self):
        with open("case0.json") as f:
            data = json.load(f)

        bot = Bot(data["bot"])
        bot.start()
