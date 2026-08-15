import json #chargement du module json 
import os # chargement du module systeme pour faire des verifications sur les fichiers de l'ordi

STOCKAGE = "contacts.json"#Déclare une constante (en majuscules) contenant le nom du fichier où seront stockées tes données

def charger_contacts():#fonction de lecture du fichier JSON
    """Charge la liste des contacts depuis le fichier JSON."""
    if not os.path.exists(STOCKAGE):
        return []
    try:
        with open(STOCKAGE, "r", encoding="utf-8") as file:
            return json.load(file)#Lit le contenu du fichier JSON et le transforme directement en liste/dictionnaire Python.
    except json.JSONDecodeError:#Si le fichier JSON est vide ou mal formé, il attrape l'erreur et renvoie une liste vide [].
        return []

def sauvegarder_contacts(contacts):# fonction d'ecriture du nouveau contact si il y en a | :p |
    """Sauvegarde la liste des contacts dans le fichier JSON."""
    with open(STOCKAGE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)