"""Moduł obszługujący funkcjonalności związane z rozgrywką"""
import os
import string

BOARD_SIZE = 10
EMPTY_GRID_SYMBOL = 'x'
MISSED_GRID_SYMBOL = 'o'
HIT_GRID_SYMBOL = 't'
SPACING_SYMBOL = '-'
CHOICE_BACK = 5
CHOICE_LEFT = 1
CHOICE_RIGHT = 2
CHOICE_UP = 3
CHOICE_DOWN = 4


def print_map(map1):
    """ Funkcja wypisująca jedno okno mapy. """
    print()
    print('\\', end="  ")
    for char in string.ascii_lowercase[:BOARD_SIZE]:
        print(char, end=" ")
    print()
    for i, row in enumerate(map1, 1):
        print(i, end=" ")
        if i < BOARD_SIZE:
            print(end=" ")
        for column in row:
            print(column, end=" ")
        print()
    print()


def print_maps(map1, map2):
    """ Funkcja wypisująca dwa połączone ze sobą okna map. """
    print('\\', end="  ")
    for char in string.ascii_lowercase[:BOARD_SIZE]:
        print(char, end=" ")
    print(" | ", end=" ")
    print('\\', end="  ")
    for char in string.ascii_lowercase[:BOARD_SIZE]:
        print(char, end=" ")
    print()
    for row in range(BOARD_SIZE):
        i = row + 1
        print(i, end=" ")
        if i < BOARD_SIZE:
            print(end=" ")
        for column in map1[row]:
            print(column, end=" ")
        print(" | ", end=" ")
        print(i, end=" ")
        if i < BOARD_SIZE:
            print(end=" ")
        for column in map2[row]:
            print(column, end=" ")
        print()
    print()


def set_grids(map_values, map_user, column, row, direction, length, symbol):
    if direction == 'left':
        if column < BOARD_SIZE - 1 and row > 0:
            map_values[row - 1][column + 1] = SPACING_SYMBOL
        if column < BOARD_SIZE - 1:
            map_values[row][column + 1] = SPACING_SYMBOL
        if column < BOARD_SIZE - 1 and row < BOARD_SIZE - 1:
            map_values[row + 1][column + 1] = SPACING_SYMBOL
    elif direction == 'right':
        if column > 0 and row > 0:
            map_values[row - 1][column - 1] = SPACING_SYMBOL
        if column > 0:
            map_values[row][column - 1] = SPACING_SYMBOL
        if column > 0 and row < BOARD_SIZE - 1:
            map_values[row + 1][column - 1] = SPACING_SYMBOL
    elif direction == 'up':
        if column > 0 and row < BOARD_SIZE - 1:
            map_values[row + 1][column - 1] = SPACING_SYMBOL
        if row < BOARD_SIZE - 1:
            map_values[row + 1][column] = SPACING_SYMBOL
        if column < BOARD_SIZE - 1 and row < BOARD_SIZE - 1:
            map_values[row + 1][column + 1] = SPACING_SYMBOL
    else:
        if column > 0 and row > 0:
            map_values[row - 1][column - 1] = SPACING_SYMBOL
        if row > 0:
            map_values[row - 1][column] = SPACING_SYMBOL
        if column < BOARD_SIZE - 1 and row > 0:
            map_values[row - 1][column + 1] = SPACING_SYMBOL
    for i in range(0, length):
        if direction == 'left':
            map_values[row][column - i] = symbol
            map_user[row][column - i] = symbol
            if row > 0:
                map_values[row - 1][column - i] = SPACING_SYMBOL
            if row < BOARD_SIZE - 1:
                map_values[row + 1][column - i] = SPACING_SYMBOL
        elif direction == 'right':
            map_values[row][column + i] = symbol
            map_user[row][column + i] = symbol
            if row > 0:
                map_values[row - 1][column + i] = SPACING_SYMBOL
            if row < BOARD_SIZE - 1:
                map_values[row + 1][column + i] = SPACING_SYMBOL
        elif direction == 'up':
            map_values[row - i][column] = symbol
            map_user[row - i][column] = symbol
            if column > 0:
                map_values[row - i][column - 1] = SPACING_SYMBOL
            if column < BOARD_SIZE - 1:
                map_values[row - i][column + 1] = SPACING_SYMBOL
        else:
            map_values[row + i][column] = symbol
            map_user[row + i][column] = symbol
            if column > 0:
                map_values[row + i][column - 1] = SPACING_SYMBOL
            if column < BOARD_SIZE - 1:
                map_values[row + i][column + 1] = SPACING_SYMBOL

    if direction == 'left':
        if column - length >= 0 and row > 0:
            map_values[row - 1][column - length] = SPACING_SYMBOL
        if column - length >= 0:
            map_values[row][column - length] = SPACING_SYMBOL
        if column - length >= 0 and row < BOARD_SIZE - 1:
            map_values[row + 1][column - length] = SPACING_SYMBOL
    elif direction == 'right':
        if column + length < BOARD_SIZE and row > 0:
            map_values[row - 1][column + length] = SPACING_SYMBOL
        if column + length < BOARD_SIZE:
            map_values[row][column + length] = SPACING_SYMBOL
        if column + length < BOARD_SIZE and row < BOARD_SIZE - 1:
            map_values[row + 1][column + length] = SPACING_SYMBOL
    elif direction == 'up':
        if column < BOARD_SIZE - 1 and row - length >= 0:
            map_values[row - length][column + 1] = SPACING_SYMBOL
        if row - length >= 0:
            map_values[row - length][column] = SPACING_SYMBOL
        if column > 0 and row - length >= 0:
            map_values[row - length][column - 1] = SPACING_SYMBOL
    else:
        if column < BOARD_SIZE - 1 and row + length < BOARD_SIZE:
            map_values[row + length][column + 1] = SPACING_SYMBOL
        if row + length < BOARD_SIZE:
            map_values[row + length][column] = SPACING_SYMBOL
        if column > 0 and row + length < BOARD_SIZE:
            map_values[row + length][column - 1] = SPACING_SYMBOL


def set_ship(map_values, map_user, symbol, name, length):
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
                        row = BOARD_SIZE - 1
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
            if column > length - 2:
                left = True
            if column <= BOARD_SIZE - length:
                right = True
            if row > length - 2:
                upward = True
            if row <= BOARD_SIZE - length:
                down = True

            for i in range(1, length):
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
                    if left:
                        print("1:Lewo - do ", chr(66 + column - length), row + 1)
                    if right:
                        print("2:Prawo - do ", chr(64 + column + length), row + 1)
                    if upward:
                        print("3:Góra - do ", chr(65 + column), row - length + 2)
                    if down:
                        print("4:Dół - do ", chr(65 + column), row + length)
                    print("5: Wróć do wyboru pola startowego")

                    while True:
                        try:
                            choice = int(input())
                        except ValueError:
                            print("Podana wartość jest nie poprawna.")
                            continue
                        break

                    if choice == CHOICE_BACK:
                        break
                    if choice == CHOICE_LEFT:
                        if left:
                            set_grids(map_values, map_user, column, row, "left", length, symbol)
                            break
                        else:
                            print("Kierunek niedostepny, wybierz inny")
                            print()
                            continue
                    if choice == CHOICE_RIGHT:
                        if right:
                            set_grids(map_values, map_user, column, row, "right", length, symbol)
                            break
                        else:
                            print("Kierunek niedostepny, wybierz inny")
                            print()
                            continue
                    if choice == CHOICE_UP:
                        if upward:
                            set_grids(map_values, map_user, column, row, "up", length, symbol)
                            break
                        else:
                            print("Kierunek niedostepny, wybierz inny")
                            print()
                            continue
                    if choice == CHOICE_DOWN:
                        if down:
                            set_grids(map_values, map_user, column, row, "down", length, symbol)
                            break
                        else:
                            print("Kierunek niedostepny, wybierz inny")
                            print()
                            continue
                if choice == CHOICE_BACK:
                    continue
                else:
                    break
        else:
            print("Pole zajęte, podaj inne")
    return length


def alloc_map(char):
    """ Funkcja alokująca pamięć i domyślne wartości dla tablic map. """
    map_rows = []
    for i in range(BOARD_SIZE):
        map_grids = []
        map_rows.append(map_grids)
        for j in range(BOARD_SIZE):
            map_grids.append(char)
    return map_rows


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
                        row = BOARD_SIZE-1
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
        if player2.map_values[row][column] in (MISSED_GRID_SYMBOL, HIT_GRID_SYMBOL):
            print("Wspolrzedne juz ostrzelane, wpisz nowe")
            os.system("pause")
        else:
            break

    if player2.map_values[row][column] in (EMPTY_GRID_SYMBOL, SPACING_SYMBOL):
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
        for row in self.map_values:
            for grid in row:
                out = out + grid
        return out

    def input(self, inp):
        """Funkcja pobierająca string z gotowym rozstawieniem planszy"""
        self.map_values = []
        index = 0
        for i in range(BOARD_SIZE):
            maps = []
            self.map_values.append(maps)
            for j in range(BOARD_SIZE):
                maps.append(inp[index])
                if not inp[index] == EMPTY_GRID_SYMBOL and not inp[index] == "-":
                    self._ships[inp[index]] = self._ships[inp[index]] + 1
                index = index + 1
