
import os
from Modules import Networking, ShipElements

#Main
os.system("cls")
print("Wybierz tryb rozgrywki ")
print("1:Host")
print("2:Klient")
type=int(input())

if type==1:
	server= Networking.setserver()
	Networking.server_confirm(server)
	P1= ShipElements.Player()
	P2= ShipElements.Player()

	conn, addr = server.accept()
	print("Rozstawienie gracza")
	os.system("pause")
	os.system("cls")
	P1.setup_test()
	Networking.server_release(conn, P1.output())
	r= Networking.server_hold(server, "Oczekiwanie na rozstawienie klienta")
	P2.input(r)

	while True:
		conn, addr = server.accept()
		cor= ShipElements.fire(P1, P2)
		Networking.server_release(conn, cor)
		if P2.getsHP()==0:
			w=1
			break;
		ShipElements.printmaps(P1.mapu, P1.mapp)
		r = Networking.server_hold(server, "Tura klienta")
		ShipElements.getHit(P1, r)
		if P1.getsHP()==0:
			w=2
			break;
else:

	server = Networking.connect()
	Networking.client_confirm(server)
	P1= ShipElements.Player()
	P2= ShipElements.Player()

	server = Networking.connect()
	r= Networking.client_hold(server, "Oczekiwanie na rozstawienie hosta")
	P2.input(r)
	print("Rozstawienie gracza")
	os.system("pause")
	os.system("cls")
	P1.setup_test()
	server = Networking.connect()
	Networking.client_release(server, P1.output())

	while True:
		ShipElements.printmaps(P1.mapu, P1.mapp)
		server = Networking.connect()
		r= Networking.client_hold(server, "Tura hosta")
		ShipElements.getHit(P1, r)
		if P1.getsHP()==0:
			w=2
			break;
		cor= ShipElements.fire(P1, P2)
		server = Networking.connect()
		Networking.client_release(server, cor)
		if P2.getsHP()==0:
			w=1
			break;

if w==1:
	print("Wygrana")
else:
	print("Przegrana")


