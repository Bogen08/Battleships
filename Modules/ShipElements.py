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

def set_ship(map,mapu,s,name,dl):
	""" Funkcja ustawiająca dany statek dla danego gracza. """
	os.system("cls")
	printmap(map)
	print(name)
	while True:
		k = int(ord(input("Podaj kolumne: ")) - 65)
		if k > 10:
			k = k - 32
		#print(k)
		w = int(input("Podaj wiersz: ")) - 1
		if map[w][k] == "x":
			l = 1
			r = 1
			u = 1
			d = 1
			if k > dl-2:
				l = 0
			if k < 11-dl:
				r = 0
			if w > dl+2:
				u = 0
			if w < 11-dl:
				d = 0

			for i in range(1, dl):
				if l != 0 or map[w][k - i] != "x":
					l = 1
				if r != 0 or map[w][k + i] != "x":
					r = 1
				if u != 0 or map[w - i][k] != "x":
					u = 1
				if d != 0 or map[w + i][k] != "x":
					d = 1
			if l + r + u + d == 4:
				print("Brak możliwych ustawień, podaj inne pole")
				continue
			else:
				while True:
					print("Wybierz dostępny kierunek ustawienia")
					if l == 0:
						print("1:Lewo - do ", chr(66 + k -dl), w+1)
					if r == 0:
						print("2:Prawo - do ", chr(64 + k +dl), w+1)
					if u == 0:
						print("3:Góra - do ", chr(65 + k), w - dl +2)
					if d == 0:
						print("4:Dół - do ", chr(65 + k), w + dl)
					print("5: Wróć do wyboru pola startowego")
					wy = int(input())

					if wy == 5:
						break
					if wy==1:
						if l==0:
							for i in range(0,dl):
								map[w][k-i]=s
								mapu[w][k-i]=s
							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue
					if wy==2:
						if r==0:
							for i in range(0,dl):
								map[w][k+i]=s
								mapu[w][k + i] = s
							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue
					if wy==3:
						if u==0:
							for i in range(0,dl):
								map[w-i][k]=s
								mapu[w - i][k] = s
							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue
					if wy==4:
						if d==0:
							for i in range(0,dl):
								map[w+i][k]=s
								mapu[w + i][k] = s
							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue

				if wy==5:
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
	printmaps(P1.mapu, P1.mapp)
	while True:
		k = int(ord(input("Podaj kolumne: ")) - 65)
		if k > 10:
			k = k - 32
		w = int(input("Podaj wiersz: ")) - 1
		if P2.map[w][k] == "o" or P2.map[w][k] == "t":
			print("Wspolrzedne juz ostrzelane, wpisz nowe")
			os.system("pause")
		else:
			break

	if P2.map[w][k] == "x" or P2.map[w][k] == "-":
		print("Pudlo")
		P2.map[w][k] = "o"
		P1.mapp[w][k] = "o"
		ef=0
	else:
		print("trafienie")
		c = P2.map[w][k]
		P2.hit(c)
		ef = 1
		if P2.getHP(c) == 0:
			print("Zatopienie")
			ef = 2
		P2.map[w][k] = "t"
		P1.mapp[w][k] = "x"

	os.system("pause")
	os.system("cls")

	return (str(w)+str(k)+str(ef))

def getHit(P1,msg):
	""" Funkcja obsługująca wartość zwrotną funkcji fire dla strony ostrzeliwanej"""
	print()
	w=int(msg[0])
	k = int(msg[1])
	ef = int(msg[2])
	if ef==0:
		P1.map[w][k]="o"
		P1.mapu[w][k] = "o"
	else:
		P1.hit(P1.map[w][k])
		P1.map[w][k] = "t"
		P1.mapu[w][k] = "t"
		print("Statek otrzymal trafienie")
		if ef==2:
			print("Stracono okret")
	print()


class Player:
	""" Klasa przechowująca mapy oraz stany okrętów. """
	def __init__(self):
		self.map = alloc_map("x")
		self.mapp = alloc_map(" ")
		self.mapu = alloc_map(" ")
		self._ships = {'l':0, 'd':0, 's':0, 'g':0, 'p':0,}

	def setup(self):
		self._ships['l'] = set_ship(self.map, self.mapu, "l", "Lotniskowiec", 5)
		self._ships['d'] = set_ship(self.map, self.mapu, "d", "Niszczyciel", 4)
		self._ships['s'] = set_ship(self.map, self.mapu, "s", "Łódź podwodna", 3)
		self._ships['g'] = set_ship(self.map, self.mapu, "g", "Kanonierka", 3)
		self._ships['p'] = set_ship(self.map, self.mapu, "p", "Łódka patrolowa", 2)

	def setup_test(self):
		self._ships['p'] = set_ship(self.map, self.mapu, "p", "Łódka patrolowa", 2)
		self._ships['g'] = set_ship(self.map, self.mapu, "g", "Kanonierka", 3)

	def getsHP(self):
		return self._ships['l']+self._ships['d']+self._ships['s']+self._ships['g']+self._ships['p']

	def getHP(self,char):
		return self._ships[char]

	def hit(self,char):
		self._ships[char]-=1

	def output(self):
		out=""
		for i in self.map:
			for j in i:
				out=out+j
		return out

	def input(self,inp):
		self.map = []
		id=0
		for i in range(10):
			maps = []
			self.map.append(maps)
			for j in range(10):
				maps.append(inp[id])
				if not inp[id]=="x":
					self._ships[inp[id]]=self._ships[inp[id]]+1
				id=id+1
