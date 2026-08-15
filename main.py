from storage import charger_contacts
from menu import executer_menu

def main():

    # Chargement initial des contacts depuis contacts.json
    contacts = charger_contacts()
    
    # Lancement de l'interface menu
    executer_menu(contacts)

if __name__ == "__main__":
    main()