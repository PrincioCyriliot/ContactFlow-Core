import json
def lister_contacts(contacts):
    """Affiche la liste de tous les contacts."""
    if not contacts:
        print("\nAucun contact enregistré.")
        return

    print("\n--- Liste des contacts ---")
    for idx, contact in enumerate(contacts, 1):                 #enumerate(contacts, 1) : Parcourt la liste en fournissant à chaque tour l'élément
                                                                    # (contact) et son numéro d'index (idx) en commençant à 1.

        print(f"{idx}. Nom : {contact.get('nom', 'N/A')} | Tel : {contact.get('tel', 'N/A')}") # fifih rasoarisoa

def ajouter_contact(contacts):
    """Ajoute un nouveau contact à la liste."""
    nom = input("Entrez le nom du contact : ").strip()
    tel = input("Entrez le numéro de téléphone : ").strip()
    
    if nom and tel:
        contacts.append({"nom": nom, "tel": tel})
        print(f" Contact '{nom}' ajouté avec succès.")
    else:
        print(" Le nom et le téléphone ne peuvent pas être vides.")

def modifier_contact(contacts):
    """Modifie les informations d'un contact existant."""
    lister_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("\nEntrez le numéro du contact à modifier : ")) - 1
        if 0 <= index < len(contacts):
            print(f"Modification de {contacts[index]['nom']} (Laissez vide pour conserver l'actuel) :")
            nouveau_nom = input(f"Nouveau nom [{contacts[index]['nom']}] : ").strip()
            nouveau_tel = input(f"Nouveau tel [{contacts[index]['tel']}] : ").strip()

            if nouveau_nom:
                contacts[index]['nom'] = nouveau_nom
            if nouveau_tel:
                contacts[index]['tel'] = nouveau_tel

            print(" Contact mis à jour.")
        else:
            print(" Numéro invalide.")
    except ValueError:
        print(" Veuillez entrer un nombre valide.")
        print("Except value error 404")

def supprimer_contact(contacts):
    """Supprime un contact de la liste."""
    lister_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("\nEntrez le numéro du contact à supprimer : ")) - 1
        if 0 <= index < len(contacts):
            supprime = contacts.pop(index)
            print(f" Contact '{supprime['nom']}' supprimé.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print(" Veuillez entrer un nombre valide.")

def rechercher_contact(contacts):
    """Recherche un contact par son nom (partiel ou complet)."""
    recherche = input("Entrez le nom à rechercher : ").strip().lower()
    resultats = [c for c in contacts if recherche in c['nom'].lower()]
    

    if resultats:
        print(f"\n--- Résultats de recherche ({len(resultats)}) ---")
        for c in resultats:
            print(f"• Nom : {c['nom']} | Tel : {c['tel']}")
           
    else:
        print(" Aucun contact trouvé.")
        
        