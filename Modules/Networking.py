import sys
import socket
import os

def setserver():
	""" Tworzy socet do obsługi serwera. """
	HOST = None               # Symbolic name meaning all available interfaces
	PORT = 50007              # Arbitrary non-privileged port
	s = None
	for res in socket.getaddrinfo(HOST, PORT, socket.AF_INET, socket.SOCK_STREAM):
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

def connect(HOST):
	""" Tworzy socet do obsługi klienta. """
	#HOST = "127.0.0.1"   # The remote host
	PORT = 50007              # The same port as used by the server
	s = None
	for res in socket.getaddrinfo(HOST, PORT, socket.AF_INET, socket.SOCK_STREAM):
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
		print('Nie mozna polaczyc sie z serwerem')
		return None
	return s

def server_confirm(s):
	""" Funkcja oczekująca na uzyskanie połączenia z klientem. """
	print("Oczekiwanie na połączenie")
	conn, addr = s.accept()
	os.system("cls")
	with conn:
		print('Połączono z:', addr)
		while True:
			data = conn.recv(1024)
			if not data: break
			message = data.decode("utf-8")
			if message=="Ready":
				print("Klient połączony z sukcesem")
				reply="Confirm"
				conn.send(reply.encode("utf-8"))

def server_hold(s,msg):
	""" Funkcja stopująca program do momentu uzyskania komunikatu gotowości od klienta. """
	print(msg)
	conn, addr = s.accept()
	with conn:
		while True:
			data = conn.recv(1024)
			if not data: break
			message = data.decode("utf-8")
			os.system("cls")
			return message

def server_release(conn,reply):
	""" Funkcja wysyłająca sygnał gotowości do klienta w celu zwolnienia blokady. """
	with conn:
		while True:
			data = conn.recv(1024)
			message = data.decode("utf-8")
			if message=="Ready":
				conn.send(reply.encode("utf-8"))
				break

def client_confirm(s):
	""" Funkcja oczekująca na uzyskanie połączenia z serwerem. """
	with s:
		os.system("cls")
		message="Ready"
		s.sendall(str(message).encode("utf-8"))
		data = s.recv(1024)
		reply=data.decode("utf-8")
	if reply=="Confirm":
		print("Sukces w połączeniu z serwerem")

def client_release(s, message):
	""" Funkcja wysyłająca sygnał gotowości do serwera w celu zwolnienia blokady. """
	with s:
		os.system("cls")
		s.sendall(str(message).encode("utf-8"))

def client_hold(s,msg):
	""" Funkcja stopująca program do momentu uzyskania komunikatu gotowości od serwera. """
	with s:
		message="Ready"
		s.sendall(str(message).encode("utf-8"))
		print(msg)
		data = s.recv(1024)
		os.system("cls")
		reply=data.decode("utf-8")
	s.close()
	return reply
