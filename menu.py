from contacts import (
    lister_contacts,
    ajouter_contact,
    modifier_contact,
    supprimer_contact,
    rechercher_contact
)
from storage import sauvegarder_contacts

def afficher_menu():
    print("\n" + "="*30)
    print("      GESTION DES CONTACTS")
    print("="*30)
    print("1 - Lister les contacts")
    print("2 - Ajouter un contact")
    print("3 - Modifier un contact")
    print("4 - Supprimer un contact")
    print("5 - Rechercher un contact")
    print("6 - Sauvegarder et Quitter")

def executer_menu(contacts):
    while True:
        afficher_menu()
        choix = input("\nChoisissez une option (1-6) : ").strip()

        if choix == "1":
            lister_contacts(contacts)
        elif choix == "2":
            ajouter_contact(contacts)
        elif choix == "3":
            modifier_contact(contacts)
        elif choix == "4":
            supprimer_contact(contacts)
        elif choix == "5":
            rechercher_contact(contacts)
        elif choix == "6":
            sauvegarder_contacts(contacts)
            print(" Données sauvegardées dans 'contacts.json'. Au revoir !")
            break
        else:
            print(" Option invalide, veuillez choisir entre 1 et 6.")