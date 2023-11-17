### Wirtualny Ogród Botaniczny

Projekt wykonany w ramach zajęć : **[Analiza i projektowanie obiektowe](https://github.com/glowform/projektowanie_obiektowe_UEK)** \
Wykonany przez : ***Kamila Kapinos***, ***Justyna Gargula***, ***Szymon Hawryluk (221399)***.

**Opis projektu**:
Wirtualny Ogród Botaniczny to aplikacja, która pozwala użytkownikom na stworzenie i pielęgnację swojego wirtualnego ogrodu. Użytkownicy mogą wybierać różne gatunki roślin, dowiedzieć się więcej o ich właściwościach i wymaganiach pielęgnacyjnych, a następnie dbać o nie w swoim wirtualnym środowisku.

**Główne funkcje**:
- Wybór roślin z bazy danych. 
- Pielęgnacja roślin (podlewanie, przycinanie itp.).
- Uczenie się o botanice i różnych gatunkach roślin.
- Zdobywanie osiągnięć za odpowiednią pielęgnację roślin.
- Możliwość udostępniania swojego ogrodu innym użytkownikom.

**Struktura klas**:
1. **Klasa bazowa: Roślina**
    * **Atrybuty**:
        - nazwa_naukowa
        - rodzaj
        - wymagania_pielęgnacyjne (np. ilość wody, nasłonecznienie)
        - stan_rośliny (np. zdrowa, wymaga wody, przycięcia)
    * **Metody**:
        - podlej()
        - przesadź()
        - przycinaj()
        - aktualizuj_stan()

2. **Klasy pochodne**:

    a) **Drzewo** (dziedziczy po klasie Roślina)
        * Dodatkowe atrybuty: wysokość, typ owoców
        * Dodatkowe metody: zbierz_owoce()

    b) **Krzew** (dziedziczy po klasie Roślina)
        * Dodatkowe atrybuty: kolor kwiatów, okres kwitnienia
        * Dodatkowe metody: zbierz_kwiaty()

    c) **Kwiat** (dziedziczy po klasie Roślina)
        * Dodatkowe atrybuty: zapach, typ korzeni (np. bulwa)
        * Dodatkowe metody: zapyl()

3. **Klasa: Ogród**
    * **Atrybuty**:
        - lista_roślin (zawiera obiekty klasy Roślina i jej pochodnych)
        - właściciel
        - rozmiar
        - typ_gleby
    * **Metody**:
        - dodaj_roślinę()
        - usuń_roślinę()
        - podlej_wszystkie()
        - przycinaj_wszystkie()
        - informacje_o_ogrodzie()

**Rozszerzenia i dodatkowe funkcje**:
1. Symulacje różnych warunków pogodowych i ich wpływ na rośliny.
2. Wirtualny sklep z roślinami i narzędziami ogrodniczymi.
3. Interaktywne wyzwania i zadania dla użytkowników (np. "Utrzymaj zdrowy ogród przez 30 dni").
4. Możliwość tworzenia wirtualnych spacerów po ogrodach innych użytkowników.
5. Integracja z rzeczywistością rozszerzoną, aby "przenosić" wirtualne rośliny do rzeczywistego świata.