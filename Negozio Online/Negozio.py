from Utente import *
from Prodotti import *

class Negozio:
    def __init__(self):
        self.prodotti = []
        self.utenti = []
        self.acquisti = [[]]

    def add_prodotto(self, prodotto):
        self.prodotti.append(prodotto)


    def add_utente(self, email, password, nome):
        for u in self.utenti:
            if u.get_email() == email:
                print("Utente già esistente")
                return
            else:
                self.utenti.append(Utente(email, password, nome))

    def mostra_prodotto(self, prodotto):
        for prodotti in self.prodotti:
            print(prodotti)

    def mostra_acquisti_utente(self, email):
        for i in self.acquisti[i]:
            for j in self.acquisti:
             if self.acquisti [i][j] == self.email:
                print(self.acquisti [i])

    def acquisti_utente(self, email, id):
        self.acquisti.append((email, id))
