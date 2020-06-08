import sys
import subprocess as sp
import os
import socket
import string
from array import *

#Funkcje

def printmap(map):
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

def fire(P1,P2):
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


def setserver():
	HOST = None               # Symbolic name meaning all available interfaces
	PORT = 50007              # Arbitrary non-privileged port
	s = None
	for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
								  socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
		af, socktype, proto, canonname, sa = res
		try:
			s = socket.socket(af, socktype, proto)
		except OSError as msg:
			s = None
			continue
		try:
			s.bind(sa)
			s.listen(1)
		except OSError as msg:
			s.close()
			s = None
			continue
		break
	if s is None:
		print('could not open socket')
		sys.exit(1)
	s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
	return s

def connect():
	HOST = 'localhost'    # The remote host
	PORT = 50007              # The same port as used by the server
	s = None
	for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM,0, socket.AI_PASSIVE):
		af, socktype, proto, canonname, sa = res
		try:
			s = socket.socket(af, socktype, proto)
		except OSError as msg:
			s = None
			continue
		try:
			s.connect(sa)
		except OSError as msg:
			s.close()
			s = None
			continue
		break
	if s is None:
		print('could not open socket')
		return None
	return s

def server_confirm(s):
	print("Oczekiwanie na połączenie")
	conn, addr = s.accept()
	os.system("cls")
	with conn:
		print('Połączono z:', addr)
		while True:
			data = conn.recv(1024)
			if not data: break
			c = data.decode("utf-8")
			if c=="Ready":
				print("Klient połączony z sukcesem")
				reply="Confirm"
				conn.send(reply.encode("utf-8"))

def server_hold(s,msg):
	print(msg)
	conn, addr = s.accept()
	with conn:
		while True:
			data = conn.recv(1024)
			if not data: break
			c = data.decode("utf-8")
			os.system("cls")
			return c

def server_release(conn,reply):
	with conn:
		while True:
			data = conn.recv(1024)
			c = data.decode("utf-8")
			if c=="Ready":
				conn.send(reply.encode("utf-8"))
				break

def client_confirm(s):
	with s:
		os.system("cls")
		c="Ready"
		s.sendall(str(c).encode("utf-8"))
		data = s.recv(1024)
		repl=data.decode("utf-8")
	if repl=="Confirm":
		print("Sukces w połączeniu z serwerem")

def client_release(s,c):
	with s:
		os.system("cls")
		s.sendall(str(c).encode("utf-8"))

def client_hold(s,msg):
	with s:
		c="Ready"
		s.sendall(str(c).encode("utf-8"))
		print(msg)
		data = s.recv(1024)
		os.system("cls")
		repl=data.decode("utf-8")
	s.close()
	return repl

#Main
os.system("cls")
print("Wybierz tryb rozgrywki ")
print("1:Host")
print("2:Klient")
type=int(input())

if type==1:
	server=setserver()
	server_confirm(server)
	P1=Player()
	P2=Player()

	conn, addr = server.accept()
	print("Rozstawienie gracza")
	os.system("pause")
	os.system("cls")
	P1.setup_test()
	server_release(conn,P1.output())
	r=server_hold(server, "Oczekiwanie na rozstawienie klienta")
	P2.input(r)

	while True:
		conn, addr = server.accept()
		cor=fire(P1,P2)
		server_release(conn, cor)
		if P2.getsHP()==0:
			w=1
			break;
		printmaps(P1.mapu, P1.mapp)
		r = server_hold(server, "Tura klienta")
		getHit(P1,r)
		if P1.getsHP()==0:
			w=2
			break;
else:

	server = connect()
	client_confirm(server)
	P1=Player()
	P2=Player()

	server = connect()
	r=client_hold(server,"Oczekiwanie na rozstawienie hosta")
	P2.input(r)
	print("Rozstawienie gracza")
	os.system("pause")
	os.system("cls")
	P1.setup_test()
	server = connect()
	client_release(server,P1.output())

	while True:
		printmaps(P1.mapu, P1.mapp)
		server = connect()
		r=client_hold(server, "Tura hosta")
		getHit(P1,r)
		if P1.getsHP()==0:
			w=2
			break;
		cor=fire(P1,P2)
		server = connect()
		client_release(server, cor)
		if P2.getsHP()==0:
			w=1
			break;

if w==1:
	print("Wygrana")
else:
	print("Przegrana")


