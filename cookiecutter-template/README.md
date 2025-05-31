# Cookiecutter Starter Template

Tämä on cookiecutter-template uusien Python-projektien aloittamiseen. Template tukee sekä pip- että Poetry-riippuvuuksien hallintaa ja keskitettyä dokumentaation synkronointia.

## Käyttö

Voit käyttää tätä templatea kahdella tavalla:

### 1. Paikallisesti

```bash
# Asenna cookiecutter, jos sitä ei ole vielä asennettu
pip install cookiecutter

# Käytä templatea paikallisesta hakemistosta
cookiecutter c:/Users/panua/projektit/starter/cookiecutter-template
```

---

## 2. Riippuvuuksien hallinta: pip ja Poetry

Projektissa voi käyttää kumpaa tahansa tapaa:

### Pip (requirements.txt)
```bash
pip install -r requirements.txt
```

### Poetry (pyproject.toml)
```bash
pip install poetry
poetry install
```

---

## 3. Dokumentaation synkronointi keskitettyyn dokumentaatiorepoon

Projektin `docs/`-kansion sisältö synkronoidaan automaattisesti keskitettyyn dokumentaatiorepoon (esim. `panualaluusua/docs`) GitHub Actions -workflow'n avulla. Dokumentaatio löytyy keskitetystä reposta polusta `docs/<projektin-nimi>/`.

### DOCS_PUSH_TOKEN-secretti

Jotta synkronointi toimii, lisää projektisi GitHub-repositorion asetuksiin **Actions secretti** nimellä `DOCS_PUSH_TOKEN`, jonka arvona on Personal Access Token, jolla on kirjoitusoikeudet keskitettyyn dokumentaatiorepoon.

1. Luo token GitHubista (Settings → Developer settings → Personal access tokens).
2. Lisää token projektisi repoasetuksiin: Settings → Secrets and variables → Actions → New repository secret → Nimeksi `DOCS_PUSH_TOKEN`.

---

## 4. .env-tiedoston ja ympäristömuuttujien käsittely

Koska cookiecutter ei kopioi dotfileja suoraan, template sisältää tiedoston nimeltä `dot-env`, joka nimetään uudessa projektissa `.env`:ksi. Voit käyttää cookiecutter-muuttujia .env-tiedostossa.

**Huom!** Jos tarvitset ympäristömuuttujia automaatiossa (esim. post_gen_project.py), aseta ne ennen projektin generointia komentorivillä:

```bash
set DOCS_PUSH_TOKEN=ghp_xxx  # Windows
export DOCS_PUSH_TOKEN=ghp_xxx  # Unix
cookiecutter ...
```

---

## 5. Vanhojen projektien migraatio keskitettyyn dokumentaatiomalliin

Voit ottaa keskitetyn dokumentaatiomallin käyttöön myös vanhoissa projekteissa:

1. Kopioi .github/workflows/sync-docs-to-central.yml tähän projektiin.
2. Lisää `DOCS_PUSH_TOKEN`-secretti projektin GitHub Actions -secreteihin.
3. Varmista, että projektin dokumentaatio on `docs/`-kansiossa.
4. (Valinnainen) Lisää pyproject.toml, jos haluat käyttää Poetrya.

---

## 6. Yleisiä huomioita

- Dokumentaation buildaus tapahtuu vain keskitetyn dokumentaatiorepon CI:ssä. Yksittäiset projektit synkkaavat vain raakasisällön.
- Voit käyttää sekä pipiä että Poetrya, workflow tunnistaa molemmat automaattisesti.
- .env-tiedosto EI ole käytettävissä post_gen_project hookissa, joten ympäristömuuttujat tulee asettaa ennen generointia, jos niitä tarvitaan automaatiossa.

---

## 7. Ongelmatilanteet

- Jos dokumentaatio ei päivity keskitettyyn repoosi, tarkista että DOCS_PUSH_TOKEN on oikein ja workflow on käynnistynyt.
- Jos saat virheen `Could not open requirements.txt`, voit käyttää Poetrya tai lisätä tyhjän requirements.txt-tiedoston.
- Jos tarvitset lisää ohjeita, katso projektin workflow-tiedostoa ja tätä README:tä.

---


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

## .env-tiedoston lisääminen projektiin

Jos haluat, että uusi projekti sisältää valmiin `.env`-tiedoston, lisää templateen tiedosto nimellä `dot-env` (ei pisteellä alkavaa nimeä). Cookiecutter muuntaa tämän automaattisesti `.env`-tiedostoksi uuden projektin juureen.

**Esimerkki:**

```bash
# Template-tiedosto: {{ cookiecutter.project_slug }}/dot-env
SECRET_KEY={{ cookiecutter.project_slug }}_secret
```

Uudessa projektissa tämä näkyy tiedostona `.env`.

Voit käyttää tiedoston sisällä cookiecutter-muuttujia kuten `{{ cookiecutter.project_slug }}`.

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
