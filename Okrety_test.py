import unittest
import okrety
import os
from Modules import Networking, ShipElements


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = ShipElements.Player()
        test_input = "lllll-xxxx------xxxxdddd-xxxxx-----xxxxxsss-" \
                     "xxxxxx----xxxxxxggg-xxxxxx----xxxxxxp-xxxxxxxxp-xxxxxxxx"
        self.player.input(test_input)

    def test_ships(self):
        self.assertIsNotNone(self.player._ships)

    def test_map_values(self):
        self.assertIsNotNone(self.player.map_values)

    def test_map_user(self):
        self.assertIsNotNone(self.player.map_user)

    def test_map_targets(self):
        self.assertIsNotNone(self.player.map_targets)


if __name__ == '__main__':
    unittest.main()
