**Okręty - Sieć**
Bogdan Ignacyk
130519
Grupa 22

# Opis zadania
* Gra prowadzona między dwójką graczy przez sieć
* Użytkownik wybiera czy chce pełnić role hosta lub klienta
* Okno z dwoma planszami 10x10 pól (np. siatki przycisków) oraz
przyciskiem rozpoczęcia gry i przyciskiem reset.
* Na początku gracz rozmieszcza okręty (1x pięciomasztowiec, 1x czteromasztowiec, 2x trójmasztowiec, 1x dwumasztowiec).
* Po rozmieszczeniu okrętów przez klienta i zaakceptowaniu seleckji host rozmieszcza swoje okrety.
* Okręty nie mogą się dotykać ani bokami ani rogami.
* Po rozmieszczeniu okrętów przez obu graczy jeden z nich wykonuje pierwszy ruch
(decydowane losowo).
* Wybór celu przez gracza następuje przez kliknięcie pola, w razie trafienia przycisk
staje się czerwony, w przeciwnym razie niebieski (nie można strzelić dwa razy w to
samo pole).
* Gra kończy się gdy któryś gracz straci ostatni okręt, wyświetlane jest okno
z informacją o zwycięzcy (np. “Wygrana!”, “Przegrana!”).

Testy
1. Próba niepoprawnego ustawienia okrętu (stykanie się bokami lub
rogami). Oczekiwana informacja o błędzie
2. Poprawne rozmieszczenie wszystkich okrętów przez gracza i wciśnięcie
przycisku rozpoczęcia gry.
3. Strzelenie w puste pole.
4. Trafienie w okręt przeciwnika.
6. Próba ponownego strzelenia w puste pole - oczekiwane niepowodzenie.
7. Próba ponownego strzelenia w okręt przeciwnika - oczekiwane niepowodzenie.
8. Rozmieszczenie części okrętów, wciśnięcie przycisku reset - oczekiwany
reset plansz.
9. Poprawne rozmieszczenie wszystkich okrętów, oddanie kilku strzałów, rozpoczęcie
nowej gry, ponowne poprawne rozmieszczenie okrętów, oddanie strzałów w te same
pola.
10. Rozpoczęcie nowej gry po zgodzie obu graczy bez ponownego uruchomienia programu

