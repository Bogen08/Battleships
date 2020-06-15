"""Moduł obsługujący interfejs sieciowy"""
import sys
import socket
import os
BUFF_SIZE = 1024

def setserver():
    """ Tworzy socet do obsługi serwera. """
    host = None  # Symbolic name meaning all available interfaces
    port = 50007  # Arbitrary non-privileged port
    sock = None
    for res in socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM):
        af, socktype, proto, _, sa = res
        try:
            sock = socket.socket(af, socktype, proto)
        except OSError:
            sock = None
            continue
        try:
            sock.bind(sa)
            sock.listen(1)
        except OSError:
            sock.close()
            sock = None
            continue
        break
    if sock is None:
        print('could not open socket')
        sys.exit(1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return sock


def connect(host):
    """ Tworzy socet do obsługi klienta. """
    port = 50007  # The same port as used by the server
    sock = None
    for res in socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM):
        af, socktype, proto, _, sa = res
        try:
            sock = socket.socket(af, socktype, proto)
        except OSError:
            sock = None
            continue
        try:
            sock.connect(sa)
        except OSError:
            sock.close()
            sock = None
            continue
        break
    if sock is None:
        print('Nie mozna polaczyc sie z serwerem')
        return None
    return sock


def server_confirm(sock):
    """ Funkcja oczekująca na uzyskanie połączenia z klientem. """
    print("Oczekiwanie na połączenie")
    conn = sock.accept()
    os.system("cls")
    with conn[0]:
        print('Połączono z:', conn[1])
        while True:
            data = conn[0].recv(BUFF_SIZE)
            if not data:
                break
            message = data.decode("utf-8")
            if message == "Ready":
                print("Klient połączony z sukcesem")
                reply = "Confirm"
                conn[0].send(reply.encode("utf-8"))


def server_hold(sock, message):
    """ Funkcja stopująca program do momentu uzyskania komunikatu gotowości od klienta. """
    print(message)
    conn = sock.accept()
    with conn[0]:
        while True:
            data = conn[0].recv(BUFF_SIZE)
            if not data:
                break
            message = data.decode("utf-8")
            os.system("cls")
            return message


def server_release(conn, reply):
    """ Funkcja wysyłająca sygnał gotowości do klienta w celu zwolnienia blokady. """
    with conn:
        while True:
            data = conn.recv(BUFF_SIZE)
            message = data.decode("utf-8")
            if message == "Ready":
                conn.send(reply.encode("utf-8"))
                break


def client_confirm(sock):
    """ Funkcja oczekująca na uzyskanie połączenia z serwerem. """
    with sock:
        os.system("cls")
        message = "Ready"
        sock.sendall(str(message).encode("utf-8"))
        data = sock.recv(BUFF_SIZE)
        reply = data.decode("utf-8")
    if reply == "Confirm":
        print("Sukces w połączeniu z serwerem")


def client_release(sock, message):
    """ Funkcja wysyłająca sygnał gotowości do serwera w celu zwolnienia blokady. """
    with sock:
        os.system("cls")
        sock.sendall(str(message).encode("utf-8"))


def client_hold(sock, message):
    """ Funkcja stopująca program do momentu uzyskania komunikatu gotowości od serwera. """
    with sock:
        message = "Ready"
        sock.sendall(str(message).encode("utf-8"))
        data = sock.recv(BUFF_SIZE)
        os.system("cls")
        reply = data.decode("utf-8")
    sock.close()
    return reply
