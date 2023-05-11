# Käyttöohje
## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```
Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```
Valitse aloitusnäytöstä vaikeusaste, tämän jälkeen peli alkaa. Peliä pelataan w,s näppäimillä sekä ↓,↑ nuolinäppäimillä, peli jatkuu kunnes jompikumpi pelaajista pääsee 10 pisteeseen. Tämän tapahduttua loppunäyttö tulee esille ja kertoo voittajan sekä antaa käyttäjälle mahdollisuuden aloittaa peli alusta tai sammuttaa pelin.
