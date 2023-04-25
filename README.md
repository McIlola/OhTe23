# Ohjelmistotekniikka, harjoitustyö

## Dokumentaatio
- [Vaatimusmaarittely](dokumentaatio/vaatimusmaarittely.md)
- [Työtuntikirja](dokumentaatio/tyoaika.md)
- [Changelog](dokumentaatio/changelog.md)

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
poetry run invoke test
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
