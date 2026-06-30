from Utenti import Utente
from Prodotti import Prodotto

class Negozio:
    def __init__(self):
        self.utenti = []
        self.prodotti = []
        self.acquisti = []

    def registra_utente(self, nome, email):
        nuovo_id = len(self.utenti) + 1
        utente = Utente(nuovo_id, nome, email)
        self.utenti.append(utente)
        print(f"Utente registrato con successo! Il tuo ID è {nuovo_id}")

    def visualizza_prodotti(self):
        if len(self.prodotti) > 0:
            print("Nessun prodotto disponibile")
        else:
            for prodotto in self.prodotti:
                print(prodotto)

    def acquista_prodotto(self, id_utente, id_prodotto):
            utente_trovato = None
            for utente in self.utenti:
                if utente.id == id_utente:
                    utente_trovato = utente
            if utente_trovato is None:
                print("utente non trovato")
                return
            prodotto_trovato = None
            for prodotto in self.prodotti:
                if prodotto.id == id.prodotto:
                    prodotto_trovato = prodotto
                if prodotto_trovato is None:
                    print("prodotto non trovato")
                    return
                self.acquisti.append((id_utente, id_prodotto))
                print("Acquisto effettuato")

    def visualizza_acquisti_utente(self, id_utente):
        for id_u, id_p in self.utenti:
            if id_u == id_utente:
                for prodotto in self.prodotti:
                    if prodotto.id == id_p:
                        print(prodotto)







