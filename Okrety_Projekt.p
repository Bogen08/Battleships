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
		if char=='d':
			return self._dhp
		if char=='s':
			return self._shp
		if char=='g':
			return self._ghp
		if char=='p':
			return self._php

	def hit(self,char):
		"""
		name=('%s%s'%(char,'hp'))
		self._name=-1
		"""
		if char=='l':
			self._lhp-=1
		if char=='d':
			self._dhp-=1
		if char=='s':
			self._shp-=1
		if char=='g':
			self._ghp-=1
		if char=='p':
			self._php-=1
#Main

P1=Player()
#Rozgrywka

while P1.getHP("l")>0 or P1.getHP("d")>0 or P1.getHP("g")>0 or P1.getHP("s")>0 or P1.getHP("p")>0:
	#Rysowanie planszy
	"""
	print(P1.getHP('l'))
	print(P1.getHP('d'))
	print(P1.getHP('g'))
	print(P1.getHP('s'))
	print(P1.getHP('p'))
	"""
	printmap(P1.map)
	printmap(P1.mapp)
	while True:
		k=int(ord(input("Podaj kolumne: "))-65)
		if k>10:
			k=k-32
		w=int(input("Podaj wiersz: "))-1
		if P1.map[w][k] == "o" or P1.map[w][k]=="t":
			print("Wspolrzedne juz ostrzelane, wpisz nowe")
			os.system("pause")
		else:
			break
	if P1.map[w][k]=="l":
		print("trafienie")
		P1.hit('l')
		if P1.getHP("l")==0:
			print("Zatopienie")
		P1.map[w][k]="t"
		P1.mapp[w][k] = "x"
	elif P1.map[w][k]=="d":
		print("trafienie")
		P1.hit('d')
		if P1.getHP("d")==0:
			print("Zatopienie")
		P1.map[w][k]="t"
		P1.mapp[w][k] = "x"
	elif P1.map[w][k]=="g":
		print("trafienie")
		P1.hit('g')
		if P1.getHP("g")==0:
			print("Zatopienie")
		P1.map[w][k]="t"
		P1.mapp[w][k] = "x"
	elif P1.map[w][k]=="s":
		print("trafienie")
		P1.hit('s')
		if P1.getHP("s")==0:
			print("Zatopienie")
		P1.map[w][k]="t"
		P1.mapp[w][k] = "x"
	elif P1.map[w][k]=="p":
		print("trafienie")
		P1.hit('p')
		if P1.getHP("p")==0:
			print("Zatopienie")
		P1.map[w][k]="t"
		P1.mapp[w][k] = "x"
	else:
		print("Pudlo")
		P1.map[w][k]="o"
		P1.mapp[w][k] = "o"

	os.system("pause")
	os.system("cls")

print("Wygrana")
