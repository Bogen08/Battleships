import sys
import socket
import os

def setserver():
	""" Tworzy socet do obsługi serwera. """
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
	""" Tworzy socet do obsługi klienta. """
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
	""" Funkcja oczekująca na uzyskanie połączenia z klientem. """
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
	""" Funkcja stopująca program do momentu uzyskania komunikatu gotowości od klienta. """
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
	""" Funkcja wysyłająca sygnał gotowości do klienta w celu zwolnienia blokady. """
	with conn:
		while True:
			data = conn.recv(1024)
			c = data.decode("utf-8")
			if c=="Ready":
				conn.send(reply.encode("utf-8"))
				break

def client_confirm(s):
	""" Funkcja oczekująca na uzyskanie połączenia z serwerem. """
	with s:
		os.system("cls")
		c="Ready"
		s.sendall(str(c).encode("utf-8"))
		data = s.recv(1024)
		repl=data.decode("utf-8")
	if repl=="Confirm":
		print("Sukces w połączeniu z serwerem")

def client_release(s,c):
	""" Funkcja wysyłająca sygnał gotowości do serwera w celu zwolnienia blokady. """
	with s:
		os.system("cls")
		s.sendall(str(c).encode("utf-8"))

def client_hold(s,msg):
	""" Funkcja stopująca program do momentu uzyskania komunikatu gotowości od serwera. """
	with s:
		c="Ready"
		s.sendall(str(c).encode("utf-8"))
		print(msg)
		data = s.recv(1024)
		os.system("cls")
		repl=data.decode("utf-8")
	s.close()
	return repl
