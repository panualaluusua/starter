# Projektin kuvaus

Tämä cookiecutter-template on suunniteltu nopeuttamaan uusien Python-projektien käynnistämistä ja varmistamaan, että jokaisen projektin dokumentaatio tallentuu keskitetysti samaan dokumentaatiorepoon.

## Ratkaistava ongelma

- **Hidas aloitus:** Uuden projektin perustaminen vaatii usein samoja toistuvia askeleita, kuten kansiorakenteen, riippuvuuksien ja CI-putken luomista.
- **Dokumentaation hajanaisuus:** Projektien dokumentaatio ja muistiinpanot jäävät helposti vain yksittäisen repoihin, jolloin kokonaiskuva katoaa eikä keskitettyä, helposti selattavaa dokumentaatiota synny.

## Ratkaisu

- **Yhtenäinen template:** Cookiecutter-template luo nopeasti uuden Python-projektin, jossa on valmiina hyvä kansiorakenne, riippuvuuksien hallinta (pip & Poetry) ja dokumentaatiokansio.
- **Keskitetty dokumentaatio:** Jokaisen projektin `docs/`-kansion sisältö synkronoidaan automaattisesti CI-putken avulla keskitettyyn dokumentaatiorepoon (esim. `panualaluusua/docs`), jolloin kaikki projektimuistiinpanot löytyvät yhdestä paikasta.
- **Helppo käyttöönotto:** Riittää, että generoit uuden projektin templatesta ja lisäät tarvittavan tokenin GitHub-secreteihin – CI hoitaa dokumentaation viennin puolestasi.

## Miten se toimii?

1. **Projektin generointi:**  
   Luo uusi projekti komennolla  
   ```bash
   cookiecutter c:/Users/panua/projektit/starter/cookiecutter-template
   ```
2. **Dokumentaatio:**  
   Kirjoita muistiinpanot ja dokumentaatio projektin `docs/`-kansioon.
3. **Automaattinen synkronointi:**  
   Kun pushaat projektin GitHubiin, CI-workflow siirtää `docs/`-kansion sisällön keskitettyyn dokumentaatiorepoon oikeaan polkuun.
4. **Keskitetty selailu:**  
   Kaikkien projektien dokumentaatio löytyy keskitetystä reposta yhtenäisessä muodossa.

---

**Hyödyt:**  
- Uudet projektit käynnistyvät nopeasti ja samalla tavalla.
- Dokumentaatio ei jää yksittäisiin repoihin, vaan löytyy keskitetysti yhdestä paikasta.
- Yhtenäinen rakenne helpottaa ylläpitoa ja tiedon löytymistä.

---

## Muita ominaisuuksia ja etuja

- Tukee sekä pip- että Poetry-riippuvuuksien hallintaa (molemmat valmiina templateen).
- Sisältää automaattisen GitHub Actions -workflow'n dokumentaation synkronointiin keskitettyyn repoosi.
- Ympäristömuuttujien käsittely on ohjeistettu ja turvallinen (esim. DOCS_PUSH_TOKEN secretti).
- Template on helposti laajennettavissa omiin tarpeisiin (voit lisätä hookeja, workflowja, template-tiedostoja).
- Projektin rakenne on selkeä ja yhtenäinen, mikä helpottaa ylläpitoa ja uusien kehittäjien perehdytystä.
- Soveltuu sekä henkilökohtaiseen että tiimikäyttöön.
- post_gen_project.py automatisoi mm. repo-luonnin, git remote -asetukset ja secretsin lisäämisen, jos haluat täyden automaation.

## Projektin rakenne (esimerkki)

```plaintext
projektin-nimi/
├── docs/               # Projektikohtainen dokumentaatio, synkronoidaan keskitettyyn repoosi
├── .github/
│   └── workflows/
│       └── sync-docs-to-central.yml  # Dokumentaation synkronointiworklow
├── pyproject.toml      # Poetry-konfiguraatio (valinnainen)
├── requirements.txt    # Pip-riippuvuudet (valinnainen)
├── dot-env             # Kopioituu .env:ksi
├── hooks/
│   └── post_gen_project.py  # Automaatioita projektin luonnin jälkeen
└── ...
```

## Käyttötapaukset
- Nopeuta toistuvien projektien perustamista organisaatiossa.
- Varmista, että kaikki projektit käyttävät samaa pohjaa ja dokumentaatiomallia.
- Helpota uusien kehittäjien perehdytystä ja projektien ylläpitoa.

## Laajennettavuus ja jatkokehitys
- Templatea voi helposti laajentaa lisäämällä uusia hookeja, workflowja tai muita template-tiedostoja.
- Keskitetty dokumentaatio mahdollistaa mm. automaattisen hakemiston, projektien tilan seurannan tai yhteisen changelogin rakentamisen.
- Mahdollisia jatkokehitysideoita: yhteinen changelog, automaattinen projektien listaus/dashboard, yhteiset issue- ja PR-templatet, mahdollisuus synkata myös muuta kuin dokumentaatiota.
