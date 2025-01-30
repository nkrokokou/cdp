# main.pyimport subprocess

# Définir le message du commit
import subprocess


commit_message = "Mise à jour automatique"

# Ajouter tous les fichiers au commit
subprocess.run(["git", "add", "."], check=True)

# Effectuer le commit avec le message spécifié
subprocess.run(["git", "commit", "-m", commit_message], check=True)

print("Commit effectué avec succès !")

