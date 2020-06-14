"""Plik główny programu"""
import os
from Modules import Networking, ShipElements

def main():
    """Funkcja główna programu"""
    os.system("cls")
    print("Wybierz tryb rozgrywki ")
    print("1:Host")
    print("2:Klient")
    mode = int(input())

    if mode == 1:
        server = Networking.setserver()
        Networking.server_confirm(server)
        player1 = ShipElements.Player()
        player2 = ShipElements.Player()

        conn = server.accept()
        print("Rozstawienie gracza")
        os.system("pause")
        os.system("cls")
        player1.setup()
        Networking.server_release(conn, player1.output())
        os.system("cls")
        ShipElements.printmap(player1.map_user)
        reply = Networking.server_hold(server, "Oczekiwanie na rozstawienie klienta")
        player2.input(reply)

        while True:
            conn = server.accept()
            cor = ShipElements.fire(player1, player2)
            Networking.server_release(conn, cor)
            if player2.getsHP() == 0:
                win = 1
                break
            ShipElements.printmaps(player1.map_user, player1.map_targets)
            reply = Networking.server_hold(server, "Tura klienta")
            ShipElements.getHit(player1, reply)
            if player1.getsHP() == 0:
                win = 2
                break
    else:
        host_adress = input("Podaj adress hosta: ")
        timeout = 0
        while True:
            server = Networking.connect(host_adress)
            timeout += 1
            if server is not None or timeout == 15:
                break
        Networking.client_confirm(server)
        player1 = ShipElements.Player()
        player2 = ShipElements.Player()

        server = Networking.connect(host_adress)
        reply = Networking.client_hold(server, "Oczekiwanie na rozstawienie hosta")
        player2.input(reply)
        print("Rozstawienie gracza")
        os.system("pause")
        os.system("cls")
        player1.setup()
        server = Networking.connect(host_adress)
        Networking.client_release(server, player1.output())

        while True:
            ShipElements.printmaps(player1.map_user, player1.map_targets)
            server = Networking.connect(host_adress)
            reply = Networking.client_hold(server, "Tura hosta")
            ShipElements.getHit(player1, reply)
            if player1.getsHP() == 0:
                win = 2
                break
            cor = ShipElements.fire(player1, player2)
            server = Networking.connect(host_adress)
            Networking.client_release(server, cor)
            if player2.getsHP() == 0:
                win = 1
                break

    ShipElements.printmaps(player1.map_user, player1.map_targets)
    print()
    if win == 1:
        print("Wygrana")
    else:
        print("Przegrana")


if __name__ == '__main__':
    main()
