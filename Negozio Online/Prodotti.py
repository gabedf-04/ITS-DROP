class Prodotto:
    def __init__(self, id_prodotto, categoria, prezzo):
        self.id_prodotto = id_prodotto
        self.categoria = categoria
        self.prezzo = prezzo

    def getid_prodotto(self):
        return self.id_prodotto
    def getid_categoria(self):
        return self.categoria
    def getid_prezzo(self):
        return self.prezzo
    def setid_prodotto(self, id_prodotto):
        self.id_prodotto = id_prodotto
    def setid_categoria(self, categoria):
        self.categoria = categoria
    def setid_prezzo(self, prezzo):
        self.prezzo = prezzo

    def __str__(self):
        return f"id: {self.id}, categoria: {self.categoria}, prezzo: {self.prezzo}"