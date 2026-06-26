class Prodotti:
    def __init__(self, id, nome, prezzo):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo
    def __str__(self):
        return f"ID: {self.id}, nome: {self.nome}, prezzo: {self.prezzo}"