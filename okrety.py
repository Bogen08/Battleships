"""Plik główny programu"""
import os
from Modules import networking
from Modules import ship_elements


def servermode():
    """Funkcja obsługująca rozgrywkę jako server"""
    server = networking.setserver()
    networking.server_confirm(server)
    player1 = ship_elements.Player()
    player2 = ship_elements.Player()

    conn = server.accept()
    print("Rozstawienie gracza")
    os.system("pause")
    os.system("cls")
    player1.setup()
    networking.server_release(conn[0], player1.output())
    os.system("cls")
    ship_elements.print_map(player1.map_user)
    reply = networking.server_hold(server, "Oczekiwanie na rozstawienie klienta")
    player2.input(reply)

    while True:
        conn = server.accept()
        cor = ship_elements.fire(player1, player2)
        networking.server_release(conn[0], cor)
        if player2.get_sum_hull_points() == 0:
            ship_elements.print_maps(player1.map_user, player1.map_targets)
            print()
            return True
        ship_elements.print_maps(player1.map_user, player1.map_targets)
        reply = networking.server_hold(server, "Tura klienta")
        ship_elements.get_hit(player1, reply)
        if player1.get_sum_hull_points() == 0:
            ship_elements.print_maps(player1.map_user, player1.map_targets)
            print()
            return False


def clientmode():
    """Funkcja obsługująca rozgrywkę jako klient"""
    host_adress = input("Podaj adress hosta: ")
    timeout = 0
    while True:
        server = networking.connect(host_adress)
        timeout += 1
        if server is not None or timeout == 15:
            break
    networking.client_confirm(server)
    player1 = ship_elements.Player()
    player2 = ship_elements.Player()

    server = networking.connect(host_adress)
    reply = networking.client_hold(server, "Oczekiwanie na rozstawienie hosta")
    player2.input(reply)
    print("Rozstawienie gracza")
    os.system("pause")
    os.system("cls")
    player1.setup()
    server = networking.connect(host_adress)
    networking.client_release(server, player1.output())

    while True:
        ship_elements.print_maps(player1.map_user, player1.map_targets)
        server = networking.connect(host_adress)
        reply = networking.client_hold(server, "Tura hosta")
        ship_elements.get_hit(player1, reply)
        if player1.get_sum_hull_points() == 0:
            ship_elements.print_maps(player1.map_user, player1.map_targets)
            print()
            return False
        cor = ship_elements.fire(player1, player2)
        server = networking.connect(host_adress)
        networking.client_release(server, cor)
        if player2.get_sum_hull_points() == 0:
            ship_elements.print_maps(player1.map_user, player1.map_targets)
            print()
            return True


def main():
    """Funkcja główna programu"""
    os.system("cls")
    print("Wybierz tryb rozgrywki ")
    print("1:Host")
    print("2:Klient")
    mode = int(input())

    if mode == 1:
        win = servermode()
    else:
        win = clientmode()

    if win is True:
        print("Wygrana")
    else:
        print("Przegrana")


if __name__ == '__main__':
    main()
