# Wirtualny Ogród Botaniczny

Projekt wykonany w ramach zajęć : **Analiza i projektowanie obiektowe** \
Wykonany przez : ***Kamila Kapinos***, ***Justyna Gargula***, ***Szymon Hawryluk***.

## Opis projektu:
Wirtualny Ogród Botaniczny to aplikacja, która pozwala użytkownikom na stworzenie i pielęgnację swojego wirtualnego ogrodu. Użytkownicy mogą wybierać różne gatunki roślin, a następnie dbać o nie w swoim wirtualnym środowisku.

<table>
  <tr>
    <td>Przykładowy ogród:</td>
    <td>Przykładowe statystyki o roślinach:</td>
  </tr>
    <tr>
    <td> 
      <img src=https://github.com/Kamila-Kapinos/wirtualny-ogrod-botaniczny/assets/92400632/b1318153-d73d-4d65-b211-dc76621a1711 > 
    </td>
    <td>
      <img src=https://github.com/Kamila-Kapinos/wirtualny-ogrod-botaniczny/assets/92400632/00c505d3-99e6-416f-a8a8-bda606b05ffc>
    </td>
  </tr>
</table>

## Technologie
Projekt został napisany w języku Python w wersji 3.10. Użyto wbudowanych bibliotek m.in. `pickle`, `random` i `argparse`.

## Uruchomienie
Aplikację należy obsługiwać przez uruchomienie pliku **main.py**. Testowane środowiska to PyCharm (niezalecane korzystanie z wbudowanego terminala) i VisualStudioCode. Rekomendowane narzędzia do otwierania programu (szczególnie z zapisanego pliku) to: PowerShell lub Terminal (w MacOS).\
Istnieje możliwość otworzenia wcześniej zapisanego ogrodu z poziomu terminala poprzez dodanie parametru `--seed=nazwa_pliku`.\
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
