# Ohjelmistotekniikka, harjoitustyö
## Pong
Ohjelma on klassinen pong peli jossa kimmotetaan palloa edes takaisin.
## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.8`. Etenkin vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.
## Dokumentaatio
- [Vaatimusmaarittely](dokumentaatio/vaatimusmaarittely.md)
- [Työtuntikirja](dokumentaatio/tyoaika.md)
- [Changelog](dokumentaatio/changelog.md)
- [Release viikko 5](https://github.com/McIlola/OhTe23/releases/tag/viikko5)

## Komentorivitoiminnot
### Asennus

Asenna riippuvuudet komennolla:
```bash
poetry install
```
### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```
### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke coverage
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
