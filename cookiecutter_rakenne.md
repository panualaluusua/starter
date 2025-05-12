# Cookiecutter-rakenne: Projekti + Docusaurus-dokumentaatio

## Hakemistorakenne

> **TODO:** Selvitä Windsurf-kehityksen ja koodauskäytäntöjen parhaat käytännöt ja dokumentoi ne projektin sääntöihin.

```
{{ cookiecutter.project_slug }}/
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt            # Python-riippuvuudet (jos käytössä)
├── pyproject.toml / package.json (riippuen teknologiasta)
├── data/                      # Data-aineistot, esimerkkidatat ym.
├── src/
│   └── __init__.py / index.js
├── tests/
│   └── test_sample.py / test_sample.js
├── docs/
│   ├── index.md
│   ├── vision.md                # Projektin visio
│   ├── video_demo_material.md   # Videodemon käsikirjoitus ja materiaalit
│   ├── roadmap.md               # Kehityksen tiekartta
│   ├── changelog.md             # Muutosloki
│   ├── architecture.md          # Arkkitehtuurikuvaus
│   └── {{ cookiecutter.project_slug }}/
│       ├── intro.md
│       ├── käyttö.md
│       └── api.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── sidebars.js                # Sivupalkin rakenne Docusaurus-osuudelle
├── POST_SETUP_COMMANDS.md      # Komennot, jotka tulee ajaa heti templaten ajamisen jälkeen
└── README_DOCS.md             # Ohjeet dokumentaation ylläpitoon
```

## Tiedostojen ja hakemistojen perustelut

- **POST_SETUP_COMMANDS.md**: Tähän tiedostoon kerätään kaikki tärkeät komennot, jotka tulee ajaa heti uuden projektin luomisen jälkeen (esim. git init, riippuvuuksien asennus, alustavat skriptit). Helpottaa projektin käynnistystä ja varmistaa, ettei mitään vaihetta unohdu.


- **requirements.txt**: Listaa Python-projektin riippuvuudet, nopea tapa asentaa vaaditut paketit (käytetään usein pyproject.toml:n rinnalla tai vaihtoehtona).
- **data/**: Kansio data-aineistoille, esimerkkidatalle, testidatalle tai muille projektiin liittyville tiedostoille.


- **docs/roadmap.md**: Kehityksen tiekartta, tulevat ominaisuudet ja suunnitellut parannukset.
- **docs/changelog.md**: Muutosloki, jossa seurataan projektin kehityksen vaiheita ja julkaisuja.
- **docs/architecture.md**: Projektin arkkitehtuurin ja teknisten ratkaisujen kuvaus.


- **docs/vision.md**: Dokumentoi projektin tarkoituksen, vision ja pitkän tähtäimen tavoitteet. Antaa kehitykselle suunnan ja auttaa tiimiä pysymään tavoitteissa.
- **docs/video_demo_material.md**: Paikka videodemon käsikirjoitukselle, storyboardille ja materiaalille, jota voi kerätä kehityksen aikana ja hyödyntää videon tuotannossa.


- docs/{{ cookiecutter.project_slug }}/intro.md: Projektin esittely ja aloitussivu.
- docs/{{ cookiecutter.project_slug }}/käyttö.md: Käyttöohjeet tai asennusohjeet.
- docs/{{ cookiecutter.project_slug }}/api.md: API- tai tekninen dokumentaatio.
- sidebars.js: Sivupalkin rakenne juuri tämän projektin dokumentaatiolle (voidaan importata pää-Docusaurusin konfiguraatioon).
- README.md: Ohjeet, miten tätä dokumentaatiokansiota ylläpidetään ja miten se liitetään pää-Docusaurukseen.
