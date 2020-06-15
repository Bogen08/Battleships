"""Moduł obszługujący funkcjonalności związane z rozgrywką"""
import os
import string

BOARD_SIZE = 10
EMPTY_GRID_SYMBOL = 'x'
MISSED_GRID_SYMBOL = 'o'
HIT_GRID_SYMBOL = 't'


def print_map(map1):
    """ Funkcja wypisująca jedno okno mapy. """
    print()
    char = chr(92)
    print(char, end="  ")
    for char in string.ascii_lowercase[:BOARD_SIZE]:
        print(char, end=" ")
    print()
    for i, row in enumerate(map1, 1):
        print(i, end=" ")
        if i < 10:
            print(end=" ")
        for column in row:
            print(column, end=" ")
        print()
    print()


def print_maps(map1, map2):
    """ Funkcja wypisująca dwa połączone ze sobą okna map. """
    char = chr(92)
    print(char, end="  ")
    for char in string.ascii_lowercase[:BOARD_SIZE]:
        print(char, end=" ")
    print(" | ", end=" ")
    char = chr(92)
    print(char, end="  ")
    for char in string.ascii_lowercase[:BOARD_SIZE]:
        print(char, end=" ")
    print()
    for row in range(10):
        i = row + 1
        print(i, end=" ")
        if i < 10:
            print(end=" ")
        for column in map1[row]:
            print(column, end=" ")
        print(" | ", end=" ")
        print(i, end=" ")
        if i < 10:
            print(end=" ")
        for column in map2[row]:
            print(column, end=" ")
        print()
    print()


def set_ship(map_values, map_user, symbol, name, lenght):
    """ Funkcja ustawiająca dany statek dla danego gracza. """

    os.system("cls")
    print_map(map_user)
    print(name)
    while True:
        while True:
            incord = input("Podaj wspolrzedne: ")
            if len(incord) != 2 and len(incord) != 3:
                print("Podaj poprawna wartośc")
                continue
            try:
                column = int(ord(incord[0])) - ord('A')
            except TypeError:
                print("Podana wartość jest nie poprawna.")
                continue
            try:
                row = int(incord[1]) - 1
                if len(incord) == 3:
                    if row == 0 and incord[2] == "0":
                        row = 9
                    else:
                        row = -1
            except ValueError:
                print("Podana wartość jest nie poprawna.")
                continue
            if column > BOARD_SIZE:
                column = column - 32
            if not 0 <= column < BOARD_SIZE or not 0 <= row < BOARD_SIZE:
                print("Podaj poprawne wartości")
                continue
            else:
                break
        if map_values[row][column] == EMPTY_GRID_SYMBOL:
            left = False
            right = False
            upward = False
            down = False
            if column > lenght - 2:
                left = True
            if column <= BOARD_SIZE - lenght:
                right = True
            if row > lenght - 2:
                upward = True
            if row <= BOARD_SIZE - lenght:
                down = True

            for i in range(1, lenght):
                if map_values[row][column - i] != EMPTY_GRID_SYMBOL:
                    left = False
                if map_values[row][column + i] != EMPTY_GRID_SYMBOL:
                    right = False
                if map_values[row - i][column] != EMPTY_GRID_SYMBOL:
                    upward = False
                if map_values[row + i][column] != EMPTY_GRID_SYMBOL:
                    down = False
            if left + right + upward + down == 0:
                print("Brak możliwych ustawień, podaj inne pole")
                continue
            else:
                while True:
                    print("Wybierz dostępny kierunek ustawienia")
                    if left is True:
                        print("1:Lewo - do ", chr(66 + column - lenght), row + 1)
                    if right is True:
                        print("2:Prawo - do ", chr(64 + column + lenght), row + 1)
                    if upward is True:
                        print("3:Góra - do ", chr(65 + column), row - lenght + 2)
                    if down is True:
                        print("4:Dół - do ", chr(65 + column), row + lenght)
                    print("5: Wróć do wyboru pola startowego")

                    while True:
                        try:
                            choice = int(input())
                        except ValueError:
                            print("Podana wartość jest nie poprawna.")
                            continue
                        break

                    if choice == 5:
                        break
                    if choice == 1:
                        if left is True:
                            if column < BOARD_SIZE - 1 and row > 0:
                                map_values[row - 1][column + 1] = "-"
                            if column < BOARD_SIZE - 1:
                                map_values[row][column + 1] = "-"
                            if column < BOARD_SIZE - 1 and row < BOARD_SIZE - 1:
                                map_values[row + 1][column + 1] = "-"
                            for i in range(0, lenght):
                                map_values[row][column - i] = symbol
                                map_user[row][column - i] = symbol
                                if row > 0:
                                    map_values[row - 1][column - i] = "-"
                                if row < BOARD_SIZE - 1:
                                    map_values[row + 1][column - i] = "-"
                            if column - lenght >= 0 and row > 0:
                                map_values[row - 1][column - lenght] = "-"
                            if column - lenght >= 0:
                                map_values[row][column - lenght] = "-"
                            if column - lenght >= 0 and row < BOARD_SIZE - 1:
                                map_values[row + 1][column - lenght] = "-"

                            break
                        else:
                            print("Kierunek niedostepny, wybierz inny")
                            print()
                            continue
                    if choice == 2:
                        if right is True:
                            if column > 0 and row > 0:
                                map_values[row - 1][column - 1] = "-"
                            if column > 0:
                                map_values[row][column - 1] = "-"
                            if column > 0 and row < BOARD_SIZE - 1:
                                map_values[row + 1][column - 1] = "-"
                            for i in range(0, lenght):
                                map_values[row][column + i] = symbol
                                map_user[row][column + i] = symbol
                                if row > 0:
                                    map_values[row - 1][column + i] = "-"
                                if row < BOARD_SIZE - 1:
                                    map_values[row + 1][column + i] = "-"
                            if column + lenght < BOARD_SIZE and row > 0:
                                map_values[row - 1][column + lenght] = "-"
                            if column + lenght < BOARD_SIZE:
                                map_values[row][column + lenght] = "-"
                            if column + lenght < BOARD_SIZE and row < BOARD_SIZE - 1:
                                map_values[row + 1][column + lenght] = "-"
                            break
                        else:
                            print("Kierunek niedostepny, wybierz inny")
                            print()
                            continue
                    if choice == 3:
                        if upward is True:
                            if column > 0 and row < BOARD_SIZE - 1:
                                map_values[row + 1][column - 1] = "-"
                            if row < BOARD_SIZE - 1:
                                map_values[row + 1][column] = "-"
                            if column < BOARD_SIZE - 1 and row < BOARD_SIZE - 1:
                                map_values[row + 1][column + 1] = "-"
                            for i in range(0, lenght):
                                map_values[row - i][column] = symbol
                                map_user[row - i][column] = symbol
                                if column > 0:
                                    map_values[row - i][column - 1] = "-"
                                if column < BOARD_SIZE - 1:
                                    map_values[row - i][column + 1] = "-"
                            if column < BOARD_SIZE - 1 and row - lenght >= 0:
                                map_values[row - lenght][column + 1] = "-"
                            if row - lenght >= 0:
                                map_values[row - lenght][column] = "-"
                            if column > 0 and row - lenght >= 0:
                                map_values[row - lenght][column - 1] = "-"
                            break
                        else:
                            print("Kierunek niedostepny, wybierz inny")
                            print()
                            continue
                    if choice == 4:
                        if down is True:
                            if column > 0 and row > 0:
                                map_values[row - 1][column - 1] = "-"
                            if row > 0:
                                map_values[row - 1][column] = "-"
                            if column < BOARD_SIZE - 1 and row > 0:
                                map_values[row - 1][column + 1] = "-"
                            for i in range(0, lenght):
                                map_values[row + i][column] = symbol
                                map_user[row + i][column] = symbol
                                if column > 0:
                                    map_values[row + i][column - 1] = "-"
                                if column < BOARD_SIZE - 1:
                                    map_values[row + i][column + 1] = "-"
                            if column < BOARD_SIZE - 1 and row + lenght < BOARD_SIZE:
                                map_values[row + lenght][column + 1] = "-"
                            if row + lenght < BOARD_SIZE:
                                map_values[row + lenght][column] = "-"
                            if column > 0 and row + lenght < BOARD_SIZE:
                                map_values[row + lenght][column - 1] = "-"
                            break
                        else:
                            print("Kierunek niedostepny, wybierz inny")
                            print()
                            continue

                if choice == 5:
                    continue
                else:
                    break
        else:
            print("Pole zajęte, podaj inne")
    return lenght


def alloc_map(char):
    """ Funkcja alokująca pamięć i domyślne wartości dla tablic map. """
    map_a = []
    for i in range(10):
        maps = []
        map_a.append(maps)
        for j in range(10):
            maps.append(char)
    return map_a


def fire(player1, player2):
    """ Funkcja obsługująca wybranie pola do ostrzału przez gracza oraz jego efekt.
     Zwraca ostrzelane koordynaty oraz efekt trafienia"""
    print()
    print("Ostrzal")
    print()
    print_maps(player1.map_user, player1.map_targets)
    while True:
        while True:
            incord = input("Podaj wspolrzedne: ")
            if len(incord) != 2 and len(incord) != 3:
                print("Podaj poprawna wartośc")
                continue
            try:
                column = int(ord(incord[0])) - ord('A')
            except TypeError:
                print("Podana wartość jest nie poprawna.")
                continue
            try:
                row = int(incord[1]) - 1
                if len(incord) == 3:
                    if row == 0 and incord[2] == "0":
                        row = 9
                    else:
                        row = -1
            except ValueError:
                print("Podana wartość jest nie poprawna.")
                continue
            if column > 10:
                column = column - 32
            if not 0 <= column < BOARD_SIZE or not 0 <= row < BOARD_SIZE:
                print("Podaj poprawne wartości")
                continue
            else:
                break
        if player2.map_values[row][column] == MISSED_GRID_SYMBOL or player2.map_values[row][column] == HIT_GRID_SYMBOL:
            print("Wspolrzedne juz ostrzelane, wpisz nowe")
            os.system("pause")
        else:
            break

    if player2.map_values[row][column] == EMPTY_GRID_SYMBOL or player2.map_values[row][column] == "-":
        print("Pudlo")
        player2.map_values[row][column] = MISSED_GRID_SYMBOL
        player1.map_targets[row][column] = MISSED_GRID_SYMBOL
        effect = 0
    else:
        print("trafienie")
        target = player2.map_values[row][column]
        player2.hit(target)
        effect = 1
        if player2.get_hull_points(target) == 0:
            print("Zatopienie")
            effect = 2
        player2.map_values[row][column] = HIT_GRID_SYMBOL
        player1.map_targets[row][column] = EMPTY_GRID_SYMBOL

    os.system("pause")
    os.system("cls")

    return str(row) + str(column) + str(effect)


def get_hit(player, msg):
    """ Funkcja obsługująca wartość zwrotną funkcji fire dla strony ostrzeliwanej"""
    print()
    row = int(msg[0])
    column = int(msg[1])
    effect = int(msg[2])
    if effect == 0:
        player.map_values[row][column] = MISSED_GRID_SYMBOL
        player.map_user[row][column] = MISSED_GRID_SYMBOL
    else:
        player.hit(player.map_values[row][column])
        player.map_values[row][column] = HIT_GRID_SYMBOL
        player.map_user[row][column] = HIT_GRID_SYMBOL
        print("Statek otrzymal trafienie")
        if effect == 2:
            print("Stracono okret")
    print()


class Player:
    """ Klasa przechowująca mapy oraz stany okrętów. """

    def __init__(self):
        """Funkcja inicjalizująca obiekt gracza"""
        self.map_values = alloc_map(EMPTY_GRID_SYMBOL)
        self.map_targets = alloc_map(" ")
        self.map_user = alloc_map(" ")
        self._ships = {'l': 0, 'd': 0, 's': 0, 'g': 0, 'p': 0, }

    def setup(self):
        """Funkcja kontrolująca rozstawianie okrętów gracza"""
        self._ships['l'] = set_ship(self.map_values, self.map_user, "l", "Lotniskowiec", 5)
        self._ships['d'] = set_ship(self.map_values, self.map_user, "d", "Niszczyciel", 4)
        self._ships['s'] = set_ship(self.map_values, self.map_user, "s", "Łódź podwodna", 3)
        self._ships['g'] = set_ship(self.map_values, self.map_user, "g", "Kanonierka", 3)
        self._ships['p'] = set_ship(self.map_values, self.map_user, "p", "Łódka patrolowa", 2)

    def get_hull_points(self, char):
        """Funkcja zwracająca wartość wytrzymałości okrętu ( Hull point - punkty wytrzymałości kadłuba okrętu)"""
        return self._ships[char]

    def get_sum_hull_points(self):
        """Funkcja zwracająca sumę wartości wytrzymałości okrętów gracza"""
        return self._ships['l'] + self._ships['d'] + self._ships['s'] + self._ships['g'] + self._ships['p']

    def hit(self, char):
        """Funkcja zmniejszająca wartość wytrzymałości okrętu"""
        self._ships[char] -= 1

    def output(self):
        """Funkcja zwracająca ustawienie planszy jako string"""
        out = ""
        for i in self.map_values:
            for j in i:
                out = out + j
        return out

    def input(self, inp):
        """Funkcja pobierająca string z gotowym rozstawieniem planszy"""
        self.map_values = []
        index = 0
        for i in range(10):
            maps = []
            self.map_values.append(maps)
            for j in range(10):
                maps.append(inp[index])
                if not inp[index] == EMPTY_GRID_SYMBOL and not inp[index] == "-":
                    self._ships[inp[index]] = self._ships[inp[index]] + 1
                index = index + 1
