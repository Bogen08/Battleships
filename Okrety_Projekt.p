import sys
import subprocess as sp
import os
import string
tmp = sp.call('cls',shell=True)
from array import *

#Funkcje
def printmap(map):
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

def setup_test(map):
	# Rozstawienie okretow - WIP
	map[2][1] = "l"
	map[2][2] = "l"
	map[2][3] = "l"
	map[2][4] = "l"
	map[2][5] = "l"

	map[1][7] = "g"
	map[2][7] = "g"
	map[3][7] = "g"

	map[7][3] = "p"
	map[7][4] = "p"

def set_ship(map,s,name,dl):
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
							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue
					if wy==2:
						if r==0:
							for i in range(0,dl):
								map[w][k+i]=s
							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue
					if wy==3:
						if u==0:
							for i in range(0,dl):
								map[w-i][k]=s
							break
						else:
							print("Kierunek niedostepny, wybierz inny")
							print()
							continue
					if wy==4:
						if d==0:
							for i in range(0,dl):
								map[w+i][k]=s
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

def setup_map(map):
	set_ship(map,"l","Lotniskowiec",5)
	set_ship(map, "d", "Niszczyciel", 4)
	set_ship(map,"s","Łódź podwodna",3)
	set_ship(map, "g", "Kanonierka", 3)
	set_ship(map, "p", "Łódka patrolowa", 2)
	os.system("cls")

def alloc_map(char):
	map=[]
	for i in range(10):
		maps = []
		map.append(maps)
		for j in range(10):
			maps.append(char)
	return map


class Player:
	def __init__(self):
		self.map = alloc_map("x")
		self.mapp = alloc_map(" ")
		self._lhp = set_ship(self.map,"l","Lotniskowiec",5)
		self._dhp = set_ship(self.map, "d", "Niszczyciel", 4)
		self._shp = set_ship(self.map,"s","Łódź podwodna",3)
		self._ghp = set_ship(self.map, "g", "Kanonierka", 3)
		self._php = set_ship(self.map, "p", "Łódka patrolowa", 2)

	def getHP(self,char):
		"""
		name=('%s%s'%(char,'hp'))
		return self._name
		"""
		if char=='l':
			return self._lhp

#Main

P1=Player()
printmap(P1.map)
print(P1.getHP('l'))

#Rozgrywka
"""
while lhp>0 or dhp>0 or ghp>0 or shp>0 or php>0:
	#Rysowanie planszy
	printmap(map)
	printmap(mapp)
	while True:
		k=int(ord(input("Podaj kolumne: "))-65)
		if k>10:
			k=k-32
		w=int(input("Podaj wiersz: "))-1
		if map[w][k] == "o" or map[w][k]=="t":
			print("Wspolrzedne juz ostrzelane, wpisz nowe")
			os.system("pause")
		else:
			break
	if map[w][k]=="l":
		print("trafienie")
		if lhp==1:
			print("Zatopienie")
			lhp=0
		else:
			lhp=lhp-1
		map[w][k]="t"
		mapp[w][k] = "x"
	elif map[w][k]=="d":
		print("trafienie")
		if dhp==1:
			print("Zatopienie")
			dhp=0
		else:
			dhp=dhp-1
		map[w][k]="t"
		mapp[w][k] = "x"
	elif map[w][k]=="g":
		print("trafienie")
		if ghp==1:
			print("Zatopienie")
			ghp=0
		else:
			ghp=ghp-1
		map[w][k]="t"
		mapp[w][k] = "x"
	elif map[w][k]=="s":
		print("trafienie")
		if shp==1:
			print("Zatopienie")
			shp=0
		else:
			shp=shp-1
		map[w][k]="t"
		mapp[w][k] = "x"
	elif map[w][k]=="p":
		print("trafienie")
		if php==1:
			print("Zatopienie")
			php=0
		else:
			php=php-1
		map[w][k]="t"
		mapp[w][k] = "x"
	else:
		print("Pudlo")
		map[w][k]="o"
		mapp[w][k] = "o"

	os.system("pause")
	os.system("cls")

print("Wygrana")"""