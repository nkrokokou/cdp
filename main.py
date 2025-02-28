# main.pyimport subprocess

# Définir le message du commit
import subprocess
import subprocess
import sys

try:
    # Définir le message du commit
    commit_message = "Mise à jour automatique"

    # Ajouter tous les fichiers au commit
    subprocess.run(["git", "add", "."], check=True)

    # Effectuer le commit avec le message spécifié
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    print("Commit effectué avec succès !")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors du commit : {e}")
    sys.exit(1)

commit_message = "Mise à jour automatique"

# Ajouter tous les fichiers au commit
subprocess.run(["git", "add", "."], check=True)

# Effectuer le commit avec le message spécifié
subprocess.run(["git", "commit", "-m", commit_message], check=True)

print("Commit effectué!")

