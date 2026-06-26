from negozio import Negozio
from prodotti import Prodotti

negozio = Negozio()

negozio.prodotti.append(Prodotti(1,"scarpe", 49.99))
negozio.prodotti.append(Prodotti(2,"zaino", 29.99))
negozio.prodotti.append(Prodotti(3,"giacca", 89.99))

while True:
    print("1. registra utente")
    print("2. visualizza prodotto")
    print("3. acquista prodotto")
    print("4. visualizza acquisti utente")
    print("5. esci")

    scelta = input("scegli un opzione: ")

    if scelta == "1":
        nome = input("nome: ")
        email = input("email: ")
        negozio.registra_utente(nome,email)
    elif scelta == "2":
        negozio.visualizza_prodotti()
    elif scelta == "3":
        id_utente = int(input("id utente: "))
        id_prodotto = int(input("id prodotto: "))
        negozio.acquista_prodotto(id_utente, id_prodotto)
    elif scelta == "4":
        id_utente = int(input("id utente: "))
        negozio.visualizza_acquisti_utente(id_utente)
    elif scelta == "5":
        break
    else:
        print("opzione non valida")
