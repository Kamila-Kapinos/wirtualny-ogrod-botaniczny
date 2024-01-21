# Wirtualny Ogród Botaniczny

Projekt wykonany w ramach zajęć : **Analiza i projektowanie obiektowe** \
Wykonany przez : ***Kamila Kapinos***, ***Justyna Gargula***, ***Szymon Hawryluk***.

## Opis projektu:
Wirtualny Ogród Botaniczny to aplikacja, która pozwala użytkownikom na stworzenie i pielęgnację swojego wirtualnego ogrodu. Użytkownicy mogą wybierać różne gatunki roślin, a następnie dbać o nie w swoim wirtualnym środowisku.

## Technologie
Projekt został napisany w języku Python.

## Wersje rozszerzeń
Python 3.10.4
pip 22.0.4 

## Uruchomienie
Aplikację należy obsługiwać przez uruchomienie pliku **main.py**. Testowane środowiska to PyCharm (niezalecane korzystanie z wbudowanego terminala) i VisualStudioCode. Rekomendowane narzędzia do otwierania programu (szczególnie z zapisanego pliku) to: PowerShell lub Terminal (w MacOS).\
Istnieje możliwość otworzenia wcześniej zapisanego ogrodu z poziomu terminala poprzez dodanie parametru "--seed=nazwa_pliku".\
Przykładowe polecenia do uruchomienia aplikacji z zapisanym wcześniej ogrodem: 
```bash
py main.py --seed=nazwa_pliku.pkl
```

## Zakres funkcjonalności
**Główne funkcje**:
- Wybór rodzaju rośliny i nadanie jej nazwy. 
- Pielęgnacja roślin (podlewanie, dbanie o nasłonecznienie).
- Zbieranie owoców (wyrastają one po osiągnięciu odpowiedniego poziomu wzrostu rośliny)
- Możliwość zapisania swojego ogrodu.

**Rozszerzenia i dodatkowe funkcje możliwe do zaimplementowania w przyszłości**:
1. Symulacje różnych warunków pogodowych i ich wpływ na rośliny.
2. Wirtualny sklep z roślinami i narzędziami ogrodniczymi.
3. Interaktywne wyzwania i zadania dla użytkowników (np. "Utrzymaj zdrowy ogród przez 30 dni").
4. Możliwość tworzenia wirtualnych spacerów po ogrodach innych użytkowników.
5. Integracja z rzeczywistością rozszerzoną, aby "przenosić" wirtualne rośliny do rzeczywistego świata.
