# Mitä opin tämän projektin aikana

Tähän tiedostoon on koottu keskeiset opit ja oivallukset, jotka syntyivät cookiecutter-starter-template -projektin toteutuksen aikana.

---

## 1. CI/CD-putken rakentaminen
- Opin rakentamaan GitHub Actions -workflow'n, joka synkronoi dokumentaation automaattisesti keskitettyyn dokumentaatiorepoon.
- Ymmärsin, miten ympäristömuuttujat ja GitHub-secrettien hallinta toimivat CI-ympäristössä.
- Opin, miten workflow voidaan tehdä joustavaksi tukemaan sekä pip- että Poetry-riippuvuuksien hallintaa.

## 2. Cookiecutter ja starter-templatet
- Opin, miten cookiecutter toimii ja miten sillä voi luoda nopeasti uusia projekteja yhtenäisellä rakenteella.
- Ymmärsin, miten cookiecutterin hookit (esim. post_gen_project.py) mahdollistavat automaation heti projektin luonnin yhteydessä.
- Opin, miten dotfilet (esim. .env) kannattaa käsitellä templateissa.

## 3. GitHub CLI ja automaatio
- Opin käyttämään GitHub CLI:tä (gh) automatisoidusti Python-skripteistä, mm. repositoryn luonnissa ja secretsin lisäämisessä.
- Ymmärsin, miten gh CLI:n autentikointi toimii ja miten käyttäjää kannattaa ohjeistaa interaktiivisissa vaiheissa.

## 4. Dokumentaation keskittäminen
- Opin, miten projektikohtainen dokumentaatio voidaan keskittää yhteen paikkaan CI-putken avulla.
- Ymmärsin, miksi on hyödyllistä erottaa raakasisällön synkronointi ja keskitetty buildaus (esim. MkDocs vain keskitetysti).

## 5. Yleisiä oppeja
- Hyvä dokumentaatio ja yhtenäinen rakenne nopeuttavat uusien projektien käynnistämistä ja helpottavat ylläpitoa.
- Ympäristömuuttujien ja secrettien käsittely on tärkeä osa turvallista automaatiota.
- On hyödyllistä koota opit ja ratkaisut yhteen paikkaan myöhempää käyttöä varten.

---

## Yhteys laajempiin kokonaisuuksiin

Projektin opit liittyvät suoraan DevOpsin, ohjelmistoprojektien standardoinnin, dokumentaation hallinnan, turvallisuuden ja kehittäjäkokemuksen teemoihin. Näiden osa-alueiden kehittäminen auttaa rakentamaan tehokkaampia, turvallisempia ja skaalautuvampia ohjelmistoprojekteja sekä parantaa tiedon jakamista ja yhteistyötä tiimissä.

Voit täydentää tätä tiedostoa uusilla opeilla jatkossa!
