import os

def printmap(map):
	""" Funkcja wypisująca jedno okno mapy. """
	print()
	ch = chr(92)
	print(ch, end="  ")
	for i in range(10):
		ch = chr(65 + i)
		print(ch, end=" ")
	print()
	i = 1
	for c in map:
		print(i, end=" ")
		if i < 10:
			print(end=" ")
		i = i + 1
		for r in c:
			print(r, end=" ")
		print()
	print()

def printmaps(map1,map2):
	""" Funkcja wypisująca dwa połączone ze sobą okna map. """
	ch = chr(92)
	print(ch, end="  ")
	for i in range(10):
		ch = chr(65 + i)
		print(ch, end=" ")
	print(" | ", end=" ")
	ch = chr(92)
	print(ch, end="  ")
	for i in range(10):
		ch = chr(65 + i)
		print(ch, end=" ")
	print()
	i = 1
	for c in range(10):
		print(i, end=" ")
		if i < 10:
			print(end=" ")
		for r in map1[c]:
			print(r, end=" ")
		print(" | ", end=" ")
		print(i, end=" ")
		if i < 10:
			print(end=" ")
		i = i + 1
		for r in map2[c]:
			print(r, end=" ")
		print()
	print()

def set_ship(map_values,map_user,s,name,dl):
	""" Funkcja ustawiająca dany statek dla danego gracza. """
	os.system("cls")
	printmap(map_user)
	print(name)
	while True:
		while True:
			incord = input("Podaj wspolrzedne: ")
			if len(incord) != 2 and len(incord) != 3:
				print("Podaj poprawna wartośc")
				continue
			try:
				column = int(ord(incord[0])) - 65
			except TypeError:
				print("Podana wartość jest nie poprawna.")
				continue
			try:
				row = int(incord[1]) - 1
				if len(incord) == 3:
					if row == 0 and incord[2] == "0":
						row = 9
					else:
						row = 10
			except ValueError:
				print("Podana wartość jest nie poprawna.")
				continue
			if column > 10:
				column = column - 32
			if column < 0 or column > 9 or row < 0 or row > 9:
				print("Podaj poprawne wartości")
				continue
			else:
				break
		if map_values[row][column] == "x":
			left = 1
			right = 1
			up = 1
			down = 1
			if column > dl-2:
				left = 0
			if column < 11-dl:
				right = 0
			if row > dl-2:
				up = 0
			if row < 11-dl:
				down = 0

			for i in range(1, dl):
				if left != 0 or map_values[row][column - i] != "x":
					left = 1
				if right != 0 or map_values[row][column + i] != "x":
					right = 1
				if up != 0 or map_values[row - i][column] != "x":
					up = 1
				if down != 0 or map_values[row + i][column] != "x":
					down = 1
			if left + right + up + down == 4:
				print("Brak możliwych ustawień, podaj inne pole")
				continue
			else:
				while True:
					print("Wybierz dostępny kierunek ustawienia")
					if left == 0:
						print("1:Lewo - do ", chr(66 + column -dl), row+1)
					if right == 0:
						print("2:Prawo - do ", chr(64 + column +dl), row+1)
					if up == 0:
						print("3:Góra - do ", chr(65 + column), row - dl +2)
					if down == 0:
						print("4:Dół - do ", chr(65 + column), row + dl)
					print("5: Wróć do wyboru pola startowego")
					choice = int(input())

					if choice == 5:
						break
					if choice==1:
						if left==0:
							if column<9 and row>0:
								map_values[row-1][column+1]="-"
							if column<9:
								map_values[row][column+1]="-"
							if column<9 and row<9:
								map_values[row+1][column+1]="-"
							for i in range(0,dl):
								map_values[row][column-i]=s
								map_user[row][column-i]=s
								if row>0:
									map_values[row - 1][column-i] = "-"
								if row<9:
									map_values[row +1 ][column-i] = "-"
							if column-dl>=0 and row>0:
								map_values[row-1][column-dl]="-"
							if column-dl>=0:
								map_values[row][column-dl]="-"
							if column-dl>=0 and row<9:
								map_values[row+1][column-dl]="-"

							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue
					if choice==2:
						if right==0:
							if column>0 and row>0:
								map_values[row-1][column-1]="-"
							if column>0:
								map_values[row][column-1]="-"
							if column>0 and row<9:
								map_values[row+1][column-1]="-"
							for i in range(0,dl):
								map_values[row][column+i]=s
								map_user[row][column + i] = s
								if row > 0:
									map_values[row - 1][column + i] = "-"
								if row < 9:
									map_values[row + 1][column + i] = "-"
							if column + dl <= 9 and row > 0:
								map_values[row - 1][column + dl] = "-"
							if column + dl <= 9:
								map_values[row][column + dl] = "-"
							if column + dl <= 9 and row < 9:
								map_values[row + 1][column + dl] = "-"
							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue
					if choice==3:
						if up==0:
							if column>0 and row<9:
								map_values[row+1][column-1]="-"
							if row<9:
								map_values[row+1][column]="-"
							if column<9 and row<9:
								map_values[row+1][column+1]="-"
							for i in range(0,dl):
								map_values[row-i][column]=s
								map_user[row - i][column] = s
								if column > 0:
									map_values[row-i][column -1] = "-"
								if column < 9:
									map_values[row-i][column + 1] = "-"
							if column < 9 and row - dl >= 0:
								map_values[row - dl][column + 1] = "-"
							if row - dl >= 0:
								map_values[row - dl][column] = "-"
							if column > 0 and row - dl >= 0:
								map_values[row - dl][column - 1] = "-"
							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue
					if choice==4:
						if down==0:
							if column>0 and row>0:
								map_values[row-1][column-1]="-"
							if row>0:
								map_values[row-1][column]="-"
							if column<9 and row>0:
								map_values[row-1][column+1]="-"
							for i in range(0,dl):
								map_values[row+i][column]=s
								map_user[row + i][column] = s
								if column > 0:
									map_values[row + i][column - 1] = "-"
								if column < 9:
									map_values[row + i][column + 1] = "-"
							if column < 9 and row + dl <= 9:
								map_values[row + dl][column + 1] = "-"
							if row + dl <= 9:
								map_values[row + dl][column] = "-"
							if column > 0 and row + dl <= 9:
								map_values[row + dl][column - 1] = "-"
							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue

				if choice==5:
					continue
				else:
					break
		else:
			print("Pole zajęte, podaj inne")
	return dl

def alloc_map(char):
	""" Funkcja alokująca pamięć i domyślne wartości dla tablic map. """
	map=[]
	for i in range(10):
		maps = []
		map.append(maps)
		for j in range(10):
			maps.append(char)
	return map

def fire(P1,P2):
	""" Funkcja obsługująca wybranie pola do ostrzału przez gracza oraz jego efekt.
	 Zwraca ostrzelane koordynaty oraz efekt trafienia"""
	print()
	print("Ostrzal")
	print()
	printmaps(P1.map_user, P1.map_targets)
	while True:
		while True:
			incord = input("Podaj wspolrzedne: ")
			if len(incord) != 2 or len(incord) != 3:
				print("Podaj poprawna wartośc")
				continue
			try:
				column = int(ord(incord[0])) - 65
			except TypeError:
				print("Podana wartość jest nie poprawna.")
				continue
			try:
				row = int(incord[1]) - 1
				if len(incord)==3:
					if row==0 and incord[2] == "0":
						row = 9
					else:
						row = 10
			except ValueError:
				print("Podana wartość jest nie poprawna.")
				continue
			if column > 10:
				column = column - 32
			if column < 0 or column > 9 or row < 0 or row > 9:
				print("Podaj poprawne wartości")
				continue
			else:
				break
		if P2.map_values[row][column] == "o" or P2.map_values[row][column] == "t":
			print("Wspolrzedne juz ostrzelane, wpisz nowe")
			os.system("pause")
		else:
			break

	if P2.map_values[row][column] == "x" or P2.map_values[row][column] == "-":
		print("Pudlo")
		P2.map_values[row][column] = "o"
		P1.map_targets[row][column] = "o"
		effect=0
	else:
		print("trafienie")
		target = P2.map_values[row][column]
		P2.hit(target)
		effect = 1
		if P2.getHP(target) == 0:
			print("Zatopienie")
			effect = 2
		P2.map_values[row][column] = "t"
		P1.map_targets[row][column] = "x"

	os.system("pause")
	os.system("cls")

	return (str(row)+str(column)+str(effect))

def getHit(P1,msg):
	""" Funkcja obsługująca wartość zwrotną funkcji fire dla strony ostrzeliwanej"""
	print()
	row=int(msg[0])
	column = int(msg[1])
	effect = int(msg[2])
	if effect==0:
		P1.map_values[row][column]="o"
		P1.map_user[row][column] = "o"
	else:
		P1.hit(P1.map_values[row][column])
		P1.map_values[row][column] = "t"
		P1.map_user[row][column] = "t"
		print("Statek otrzymal trafienie")
		if effect==2:
			print("Stracono okret")
	print()


class Player:
	""" Klasa przechowująca mapy oraz stany okrętów. """
	def __init__(self):
		self.map_values = alloc_map("x")
		self.map_targets = alloc_map(" ")
		self.map_user = alloc_map(" ")
		self._ships = {'l':0, 'd':0, 's':0, 'g':0, 'p':0,}

	def setup(self):
		self._ships['l'] = set_ship(self.map_values, self.map_user, "l", "Lotniskowiec", 5)
		self._ships['d'] = set_ship(self.map_values, self.map_user, "d", "Niszczyciel", 4)
		self._ships['s'] = set_ship(self.map_values, self.map_user, "s", "Łódź podwodna", 3)
		self._ships['g'] = set_ship(self.map_values, self.map_user, "g", "Kanonierka", 3)
		self._ships['p'] = set_ship(self.map_values, self.map_user, "p", "Łódka patrolowa", 2)

	def setup_test(self):
		self._ships['p'] = set_ship(self.map_values, self.map_user, "p", "Łódka patrolowa", 2)
		self._ships['g'] = set_ship(self.map_values, self.map_user, "g", "Kanonierka", 3)

	def getsHP(self):
		return self._ships['l']+self._ships['d']+self._ships['s']+self._ships['g']+self._ships['p']

	def getHP(self,char):
		return self._ships[char]

	def hit(self,char):
		self._ships[char]-=1

	def output(self):
		out=""
		for i in self.map_values:
			for j in i:
				out=out+j
		return out

	def input(self,inp):
		self.map_values = []
		id=0
		for i in range(10):
			maps = []
			self.map_values.append(maps)
			for j in range(10):
				maps.append(inp[id])
				if not inp[id]=="x" and not inp[id]=="-":
					self._ships[inp[id]]=self._ships[inp[id]]+1
				id=id+1
