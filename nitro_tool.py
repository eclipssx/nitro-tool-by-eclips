import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

banner = r"""
 _   _ ___ _____ ____   ___    _____ ___  ___ _     
| \ | |_ _|_   _|  _ \ / _ \  |_   _/ _ \|  _| |    
|  \| || |  | | | |_) | | | |   | || | | | | | |    
| |\  || |  | | |  _ <| |_| |   | || |_| | |_| |___ 
|_| \_|___| |_| |_| \_\\___/    |_| \___/|____|_____|
                                                    
               V 1.0 - Console Menu
"""

def main():
    clear()
    print(banner)
    print("\n[1] Lancer")
    print("[2] Quitter")
    choix = input("\n> Entrez votre choix : ")

    if choix == "1":
        clear()
        print("===================================")
        print("       COMMANDE LANCÉE             ")
        print("===================================")
        print("\nExécution en cours...")
        time.sleep(3)
        input("\nAppuyez sur Entrée pour revenir au menu...")
        main()
    elif choix == "2":
        print("Fermeture du programme...")
        time.sleep(1)
        exit()
    else:
        print("Choix invalide.")
        time.sleep(1)
        main()

if __name__ == "__main__":
    main()
