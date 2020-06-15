"""Moduł zawierający testy funkcji programu"""
import unittest

from Modules import ship_elements


class PlayerTest(unittest.TestCase):
    """Klasa testowania funkcji rozgrywki"""
    def setUp(self):
        """Funkcja inicjalizująca zmienne klasu"""
        self.player1 = ship_elements.Player()
        self.player2 = ship_elements.Player()

    def test_input_output(self):
        """Funkcja testująca funkcje inputu i outputu ustawienia planszy gracza"""
        test_input = "lllll-xxxx------xxxxdddd-xxxxx-----xxxxxsss-" \
                     "xxxxxx----xxxxxxggg-xxxxxx----xxxxxxp-xxxxxxxxp-xxxxxxxx"
        self.player1.input(test_input)
        self.assertEqual(self.player1.output(), test_input)

    def test_hit(self):
        """Funkcja testująca reakcje planszy gracza na trafienie"""
        test_in = "lllll-xxxx------xxxxdddd-xxxxx-----xxxxxsss-" \
                  "xxxxxx----xxxxxxggg-xxxxxx----xxxxxxp-xxxxxxxxp-xxxxxxxx"
        self.player1.input(test_in)
        test_input_hit = "tllll-xxxx------xxxxdddd-xxxxx-----xxxxxsss-" \
                         "xxxxxx----xxxxxxggg-xxxxxx----xxxxxxp-xxxxxxxxp-xxxxxxxx"
        ship_elements.get_hit(self.player1, "001")
        self.assertEqual(self.player1.output(), test_input_hit)

    def test_miss(self):
        """Funkcja testująca reakcje planszy gracza na spudłowanie"""
        test_in = "lllll-xxxx------xxxxdddd-xxxxx-----xxxxxsss-" \
                  "xxxxxx----xxxxxxggg-xxxxxx----xxxxxxp-xxxxxxxxp-xxxxxxxx"
        self.player1.input(test_in)
        test_in_miss = "lllll-xxxx------xxxxdddd-xxxxx-----xxxxxsss-" \
                       "xxxxxx----xxxxxxggg-xxxxxx----xxxxxxp-xxxxxxxxp-xxxxxxxo"
        ship_elements.get_hit(self.player1, "990")
        self.assertEqual(self.player1.output(), test_in_miss)

    def test_hp(self):
        """Funkcja testująca funkcje zwracające wytrzymałość okrętów gracza"""
        test_in = "lllll-xxxx------xxxxdddd-xxxxx-----xxxxxsss-" \
                  "xxxxxx----xxxxxxggg-xxxxxx----xxxxxxp-xxxxxxxxp-xxxxxxxx"
        self.player1.input(test_in)
        self.assertEqual(self.player1.get_hp("l"), 5)
        self.assertEqual(self.player1.get_shp(), 17)
        self.player1.hit("l")
        self.assertEqual(self.player1.get_hp("l"), 4)
        self.assertEqual(self.player1.get_shp(), 16)

    def test_fire(self):
        """Funkcja testująca funkcje ostrzeliwania planszy"""
        test_in = "lllll-xxxx------xxxxdddd-xxxxx-----xxxxxsss-" \
                  "xxxxxx----xxxxxxggg-xxxxxx----xxxxxxp-xxxxxxxxp-xxxxxxxx"
        self.player1.input(test_in)
        ship_elements.fire(self.player2, self.player1)
        self.assertNotEqual(self.player1.output(), test_in)

    def test_map_values(self):
        """Funkcja sprawdzająca inicjalizacje zmiennych planszy"""
        self.assertIsNotNone(self.player1.map_values)

    def test_map_user(self):
        """Funkcja sprawdzająca inicjalizacje zmiennych planszy"""
        self.assertIsNotNone(self.player1.map_user)

    def test_map_targets(self):
        """Funkcja sprawdzająca inicjalizacje zmiennych planszy"""
        self.assertIsNotNone(self.player1.map_targets)

    def test_alloc(self):
        """Funkcja sprawdzająca alokacje pamięci dla zmiennej przechowującej plansze"""
        test_map = ship_elements.alloc_map("x")
        self.assertEqual(test_map[0][0], "x")
        self.assertEqual(len(test_map), 10)


if __name__ == '__main__':
    unittest.main()
