# Cookiecutter Starter Template

Tämä on cookiecutter-template uusien projektien aloittamiseen. Tämä ohje selittää, miten käytät tätä templatea.

## Käyttö

Voit käyttää tätä templatea kahdella tavalla:

### 1. Paikallisesti

```bash
# Asenna cookiecutter, jos sitä ei ole vielä asennettu
pip install cookiecutter

# Käytä templatea paikallisesta hakemistosta
cookiecutter c:/Users/panua/projektit/starter/cookiecutter-template
```

### 2. Suoraan GitHubista (jos template on GitHubissa)

```bash
# Asenna cookiecutter, jos sitä ei ole vielä asennettu
pip install cookiecutter

# Käytä templatea suoraan GitHubista
cookiecutter gh:panualaluusua/starter
```

## Mitä tapahtuu?

Kun suoritat cookiecutter-komennon, sinulta kysytään seuraavat tiedot:

- `project_name`: Projektin nimi (esim. "Uusi Projektini")
- `project_slug`: Projektin slug, käytetään kansioiden ja tiedostojen nimissä (esim. "uusi-projektini")
- `author_name`: Tekijän nimi (esim. "Panu Alaluusua")
- `description`: Lyhyt kuvaus projektista
- `github_username`: GitHub-käyttäjänimesi
- `github_repository_name`: GitHub-repositorion nimi

Cookiecutter luo uuden kansion `project_slug`-arvolla ja kopioi kaikki tiedostot templaten sisältä siihen, korvaten kaikki `{{ cookiecutter.xxx }}`-muuttujat antamillasi arvoilla.

## Automaattiset toiminnot

Projektin luonnin jälkeen suoritetaan automaattisesti seuraavat toimenpiteet (hooks/post_gen_project.py):

1. Git-repositorion alustus (`git init`)
2. Riippuvuuksien asennus (`pip install -r requirements.txt` ja `npm install`)
3. Ensimmäisen commitin luonti
4. Etärepon asetus (jos GitHub-tiedot on annettu)

## Templaten muokkaaminen

Jos haluat muokata templatea:

1. Tee muutokset `{{ cookiecutter.project_slug }}`-kansioon
2. Käytä `{{ cookiecutter.xxx }}`-muuttujia dynaamisiin osiin
3. Muokkaa `cookiecutter.json`-tiedostoa, jos haluat lisätä uusia muuttujia
4. Päivitä hooks-skriptejä tarpeen mukaan

## Templaten rakenne

```
cookiecutter-template/
├── cookiecutter.json        # Määrittelee muuttujat ja oletusarvot
├── hooks/                   # Hooks-skriptit
│   └── post_gen_project.py  # Suoritetaan projektin luonnin jälkeen
└── {{ cookiecutter.project_slug }}/ # Templaten sisältö
    ├── .github/             # GitHub Actions ja muut GitHub-asetukset
    ├── config/              # Konfiguraatiotiedostot
    ├── docs/                # Dokumentaatio
    ├── src/                 # Lähdekoodi
    ├── tests/               # Testit
    └── ...                  # Muut tiedostot ja kansiot
```
