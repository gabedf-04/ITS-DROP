from Negozio import Negozio
from Prodotti import Prodotto
negozio = Negozio()
negozio.prodotti.append(Prodotto(1,"Scarpe", 49.99))
negozio.prodotti.append(Prodotto(2, "Zaino", 29.99))
negozio.prodotti.append(Prodotto(3, "Giacca", 89.99))

while True:
    print("1. Registra Utente")
    print("2. Visualizza Prodotto")
    print("3. Acquista Prodotto")
    print("4. Visualizza acquisti utente")
    print("5. Esci")

    scelta = input("Scegli un'opzione")

    if scelta == "1":
        print("Registra Utente")
        nome = input("Utente: ")
        email = input("Email: ")
        negozio.registra_utente(nome, email)
    elif  scelta == "2":
        negozio.visualizza_prodotto()
    elif scelta == "3":
        id_utente = int(input("Utente: "))
        id_prodotto = int(input("Prodotto: "))
        negozio.acquista_prodotto(id_utente, id_prodotto)
    elif scelta == "4":
        id_utente = int(input("Utente: "))
        negozio.visualizza_prodotto(id_utente, id_prodotto)
    elif scelta == "5":
        break

