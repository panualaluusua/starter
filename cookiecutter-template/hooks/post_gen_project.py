#!/usr/bin/env python
"""
Tämä skripti suoritetaan automaattisesti cookiecutter-projektin luonnin jälkeen.
Se tekee seuraavat toimenpiteet:
1. Alustaa git-repon
2. Asentaa riippuvuudet
3. Luo ensimmäisen commitin
4. Asettaa etärepon (jos GitHub-tiedot on annettu)
"""
import os
import subprocess
import sys
from pathlib import Path


def run_command(command, cwd=None):
    """Suorittaa komentorivikomennon ja tulostaa tuloksen."""
    print(f"Suoritetaan: {command}")
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Virhe suoritettaessa komentoa: {command}")
        print(f"Virhekoodi: {e.returncode}")
        print(f"Virheviesti: {e.stderr}")
        return False


def initialize_git():
    """Alustaa git-repon."""
    print("Alustetaan git-repo...")
    return run_command("git init")


def install_dependencies():
    """Asentaa projektin riippuvuudet."""
    print("Asennetaan riippuvuudet...")
    
    # Tarkistetaan, onko requirements.txt olemassa
    if os.path.exists("requirements.txt"):
        print("Suoritetaan: pip install -r requirements.txt")
        result = subprocess.run(["pip", "install", "-r", "requirements.txt"], capture_output=True, text=True)
        if result.returncode != 0:
            print("Virhe suoritettaessa komentoa: pip install -r requirements.txt")
            print("Virhekoodi:", result.returncode)
            print("Virheviesti:", result.stderr)
            print("Varoitus: Python-riippuvuuksien asennus epäonnistui.")
            print("Korjausehdotus: Varmista, että käytössäsi on oikea Python-versio ja tarvittavat oikeudet asentaa paketit.")
        else:
            print(result.stdout)
    
    # Tarkistetaan, onko package.json olemassa
    if os.path.exists("package.json"):
        print("Suoritetaan: npm install")
        npm_cmd = "npm.cmd" if os.name == "nt" else "npm"
        try:
            result = subprocess.run([npm_cmd, "install"], capture_output=True, text=True)
        except FileNotFoundError:
            print(f"Virhe: {npm_cmd} komentoa ei löydy. Varmista, että Node.js on asennettu ja että npm on lisätty PATH-ympäristömuuttujaan.")
        else:
            if result.returncode != 0:
                print("Virhe suoritettaessa komentoa: npm install")
                print("Virhekoodi:", result.returncode)
                print("Virheviesti:", result.stderr)
                print("Korjausehdotus: Varmista, että Node.js on asennettu (lataa se osoitteesta https://nodejs.org/) ja että PATH on päivitetty.")
            else:
                print(result.stdout)
    
    return True


def create_first_commit():
    """Luo ensimmäisen commitin."""
    print("Luodaan ensimmäinen commit...")
    run_command("git add .")
    return run_command('git commit -m "Initial commit"')


def setup_remote_repo():
    """Asettaa etärepon, jos GitHub-tiedot on annettu."""
    github_username = "{{ cookiecutter.github_username }}"
    repo_name = "{{ cookiecutter.github_repository_name }}"
    
    if github_username and repo_name:
        print("Luodaan GitHub-repository automaattisesti...")
        # Tarkista, onko gh CLI asennettu ja autentikoitu
        auth_check = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
        if auth_check.returncode != 0:
            print("\n❌ GitHub CLI ei ole autentikoitu. Suorita 'gh auth login' ja yritä uudelleen.")
            print("Voit myös luoda repositoryn ja secretsit käsin GitHubin web-käyttöliittymästä.")
            return False
        print("Luodaan GitHub-repository automaattisesti...")
        create_repo_cmd = ["gh", "repo", "create", f"{github_username}/{repo_name}", "--public"]
        create_repo_result = subprocess.run(create_repo_cmd, capture_output=True, text=True)
        if create_repo_result.returncode != 0:
            print("Virhe suoritettaessa komentoa:", " ".join(create_repo_cmd))
            print("Virhekoodi:", create_repo_result.returncode)
            print("Virheviesti:", create_repo_result.stderr)
            print("Korjausehdotus: Tarkista, että sinulla on asennettuna GitHub CLI ja että olet kirjautunut sisään (gh auth login). Jos --confirm-lippu aiheuttaa virheen, poista se käytöstä.")
            print("Voit myös luoda repositoryn käsin GitHubissa: https://github.com/new")
            return False
        else:
            print(create_repo_result.stdout)
        
        remote_url = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.git"
        print("Asetetaan etärepo:", remote_url)
        result = subprocess.run(["git", "remote", "add", "origin", remote_url], capture_output=True, text=True)
        if result.returncode != 0:
            print("Virhe suoritettaessa komentoa: git remote add origin", remote_url)
            print("Virhekoodi:", result.returncode)
            print("Virheviesti:", result.stderr)
            print("Korjausehdotus: Tarkista, että GitHub-repon URL on oikein ja että verkko toimii.")
        else:
            print(result.stdout)
            print("Lähetetään ensimmäiset commitit etärepoon...")
            push_result = subprocess.run(["git", "push", "-u", "origin", "HEAD"], capture_output=True, text=True)
            if push_result.returncode != 0:
                print("Virhe suoritettaessa komentoa: git push -u origin HEAD")
                print("Virhekoodi:", push_result.returncode)
                print("Virheviesti:", push_result.stderr)
                print("Korjausehdotus: Tarkista, että sinulla on oikeudet puskea kyseiseen repon.")
            else:
                print(push_result.stdout)
    return True

def set_github_pages_branch():
    """Asettaa GitHub Pages -julkaisulähteen automaattisesti gh-pages-haaraan (root)."""
    github_username = "{{ cookiecutter.github_username }}"
    repo_name = "{{ cookiecutter.github_repository_name }}"
    if github_username and repo_name:
        print("Yritetään asettaa GitHub Pages -julkaisulähde gh-pages-haaraan...")
        cmd = [
            "gh", "api",
            "-X", "PATCH",
            "-H", "Accept: application/vnd.github+json",
            f"/repos/{github_username}/{repo_name}/pages",
            "-f", "source.branch=gh-pages",
            "-f", "source.path=/"
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ GitHub Pages -julkaisulähde asetettu onnistuneesti gh-pages-haaraan.")
            else:
                print("⚠️  GitHub Pages -asetuksen automaatio epäonnistui.")
                print("Virhekoodi:", result.returncode)
                print("Virheviesti:", result.stderr)
                print("Aseta tarvittaessa Pages-julkaisulähde käsin repositoryn asetuksista.")
        except Exception as e:
            print("⚠️  Poikkeus GitHub Pages -asetuksen automaatiossa:", e)
            print("Aseta tarvittaessa Pages-julkaisulähde käsin repositoryn asetuksista.")
    else:
        print("GitHub-tietoja ei annettu, ohitetaan Pages-haaran asetus.")
    return True


def add_docs_push_token_secret():
    """Lukee DOCS_PUSH_TOKEN-arvon .env-tiedostosta tai ympäristömuuttujasta ja lisää sen uuden projektin GitHub-repoon gh CLI:llä."""
    from dotenv import load_dotenv
    load_dotenv()
    github_username = "{{ cookiecutter.github_username }}"
    repo_name = "{{ cookiecutter.github_repository_name }}"
    token = os.environ.get("DOCS_PUSH_TOKEN")
    if not token:
        print("Syötä DOCS_PUSH_TOKEN (PAT-token, jolla on oikeudet docs-repoon):")
        token = input().strip()
    if github_username and repo_name and token:
        # Tarkista gh CLI -autentikointi ennen secretsin lisäystä
        auth_check = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
        if auth_check.returncode != 0:
            print("\n❌ GitHub CLI ei ole autentikoitu. Suorita 'gh auth login' ja yritä uudelleen.")
            print("Voit myös lisätä DOCS_PUSH_TOKEN-secretsin käsin GitHubin web-käyttöliittymässä:")
            print(f"https://github.com/{github_username}/{repo_name}/settings/secrets/actions")
            return False
        print("Lisätään DOCS_PUSH_TOKEN secret uuteen projektiin...")
        cmd = [
            "gh", "secret", "set", "DOCS_PUSH_TOKEN",
            "--repo", f"{github_username}/{repo_name}",
            "--body", token
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ DOCS_PUSH_TOKEN lisätty onnistuneesti!")
        else:
            print("⚠️  Salaisuuden lisääminen epäonnistui:")
            print(result.stderr)
            print("Voit lisätä salaisuuden myös käsin GitHubissa:")
            print(f"https://github.com/{github_username}/{repo_name}/settings/secrets/actions")
    else:
        print("Tarvittavat tiedot puuttuvat, salaisuutta ei lisätty.")


def main():
    """Pääfunktio, joka suorittaa kaikki toimenpiteet."""
    print("Aloitetaan projektin automaattinen alustus...")
    
    # Suoritetaan toimenpiteet järjestyksessä
    steps = [
        initialize_git,
        install_dependencies,
        create_first_commit,
        setup_remote_repo,
        set_github_pages_branch,
        add_docs_push_token_secret
    ]
    
    for step in steps:
        if not step():
            print(f"Varoitus: Vaihe {step.__name__} epäonnistui. Jatketaan seuraavaan vaiheeseen.")
    
    print("\nProjektin alustus valmis!")
    print("Voit nyt jatkaa kehitystä. Onnea matkaan!")


if __name__ == "__main__":
    main()
