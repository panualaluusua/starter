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
        if not run_command("pip install -r requirements.txt"):
            print("Varoitus: Python-riippuvuuksien asennus epäonnistui.")
    
    # Tarkistetaan, onko package.json olemassa
    if os.path.exists("package.json"):
        if not run_command("npm install"):
            print("Varoitus: Node.js-riippuvuuksien asennus epäonnistui.")
    
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
        print(f"Asetetaan etärepo: github.com/{github_username}/{repo_name}")
        return run_command(f"git remote add origin https://github.com/{github_username}/{repo_name}.git")
    return True


def main():
    """Pääfunktio, joka suorittaa kaikki toimenpiteet."""
    print("Aloitetaan projektin automaattinen alustus...")
    
    # Suoritetaan toimenpiteet järjestyksessä
    steps = [
        initialize_git,
        install_dependencies,
        create_first_commit,
        setup_remote_repo
    ]
    
    for step in steps:
        if not step():
            print(f"Varoitus: Vaihe {step.__name__} epäonnistui. Jatketaan seuraavaan vaiheeseen.")
    
    print("\nProjektin alustus valmis!")
    print("Voit nyt jatkaa kehitystä. Onnea matkaan!")


if __name__ == "__main__":
    main()
