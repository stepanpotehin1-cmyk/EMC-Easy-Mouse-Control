# Upravleniye myshkoy s klaviatury

Prostaya programma dlya upravleniya kursorom myshi s pomoshch'yu strelokek na klaviature.

## Ustanovka

1. Ubedites', chto u vas ustanovlen Python 3.7+
2. Ustanovite zavisimosti:
```bash
pip install pynput
```

## Zapusk

```bash
python mouse_control.py
```

Ili zapustite gotovyy EXE-fayl:
```
dist/MouseControl.exe
```

## Upravleniye

| Klavisha | Deystviye |
|----------|-----------|
| Strelki (strelochki) | Dvizheniye kursora |
| Enter | Klik levoy knopkoy myshi |
| Ctrl + Enter | Klik pravoy knopkoy myshi |
| + ili = | Uvelichit' skorost' (+2) |
| - | Umen'shit' skorost' (-2) |
| Esc | Vykhod iz programmy |

## Nastroyka skorosti

Skorost' mozhno men'hat vo vremya raboty programmy:
- Nazhmite `+` ili `=` chtoby uvelichit' skorost'
- Nazhmite `-` chtoby umen'shit' skorost'

Diapazon skorosti: ot 1 do 50 pikseley za shag.

## Osobennosti

- Kursor dvizhetsya plavno pri uderzhanii strelki
- Mozhno dvigat'sya po diagonali, uderzhivaya dve strelki odnovremenno
- Rabotayet vo vsekh prilozheniyakh
- **Praviy klik** — uderzhivayte Ctrl i nazhmite Enter
- **Izmeneniye skorosti** — v realnom vremeni klavishami +/-

## Sozdaniye EXE

```bash
pyinstaller --onefile --name "MouseControl" mouse_control.py
```
