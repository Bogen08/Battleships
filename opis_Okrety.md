**Okręty - Sieć**
Bogdan Ignacyk
130519
Grupa 22

# Opis zadania
* Gra prowadzona między dwójką graczy przez sieć
* Użytkownik wybiera czy chce pełnić role hosta lub klienta
* Okno z dwoma planszami 10x10 pól wyświetlane w konsoli i wyświetlonymi dostępnymi komendami.
* Na początku gracz rozmieszcza okręty (1x pięciomasztowiec (Lotniskowiec), 
1x czteromasztowiec (Niszczyciel), 2x trójmasztowiec (Kanonierka & łódź podwodna), 1x dwumasztowiec (Łódź patrolowa)).
* Po rozmieszczeniu okrętów przez hosta i zaakceptowaniu selekcji klient rozmieszcza swoje okrety.
* Okręty nie mogą się dotykać ani bokami ani rogami.
* Wybór celu przez gracza następuje przez wprowadzenie koordynatów, w razie trafienia na polu pokazuje
się symbol "x", w przeciwnym razie symbol "o" (nie można strzelić dwa razy w to samo pole).
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
8. Rozpoczęcie nowej gry po zgodzie obu graczy bez ponownego uruchomienia programu
