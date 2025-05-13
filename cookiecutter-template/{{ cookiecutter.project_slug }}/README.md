# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

**Tekijä:** {{ cookiecutter.author_name }}

**GitHub:** https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}

## Projektin rakenne

Tämä projekti käyttää seuraavaa kansiorakennetta:

```
{{ cookiecutter.project_slug }}/
├── .github/                # GitHub Actions ja muut GitHub-asetukset
├── config/                 # Konfiguraatiotiedostot
│   ├── .env.example        # Ympäristömuuttujien esimerkki
├── docs/                   # Dokumentaatio
│   ├── architecture.md     # Arkkitehtuuridokumentaatio
│   ├── changelog.md        # Muutosloki
│   ├── index.md            # Dokumentaation etusivu
│   ├── roadmap.md          # Tiekartta
│   └── vision.md           # Visio
├── src/                    # Lähdekoodi
│   ├── css/                # CSS-tiedostot
│   └── __init__.py         # Python-moduulin alustus
├── tests/                  # Testit
├── .gitignore              # Git-ignore-tiedosto
├── package.json            # Node.js-riippuvuudet
├── pyproject.toml          # Python-projektin konfiguraatio
├── README.md               # Tämä tiedosto
└── requirements.txt        # Python-riippuvuudet
```

## Käyttöönotto

Seuraa näitä ohjeita projektin käyttöönottamiseksi:

1. Kloonaa repositorio:
   ```bash
   git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.git
   cd {{ cookiecutter.project_slug }}
   ```

2. Asenna riippuvuudet:
   ```bash
   pip install -r requirements.txt
   npm install
   ```

3. Kopioi ympäristömuuttujat:
   ```bash
   cp config/.env.example .env
   ```
   Muokkaa .env-tiedostoa tarvittaessa.

4. Käynnistä kehitysympäristö:
   ```bash
   # Lisää tähän projektikohtaiset komennot
   ```

## Dokumentaatio

Projektin dokumentaatio löytyy `docs/`-kansiosta. Voit rakentaa dokumentaation Docusauruksella:

```bash
npm run build
```

Tai käynnistää kehityspalvelimen:

```bash
npm run start
```

## Testaus

Suorita testit komennolla:

```bash
# Lisää tähän projektikohtaiset testauskomennot
```

## Lisenssi

Tämä projekti on lisensoitu [MIT-lisenssillä](LICENSE).
