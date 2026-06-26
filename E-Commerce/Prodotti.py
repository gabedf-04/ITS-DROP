class Prodotto:
    def __init__(self, id, nome, prezzo):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo

    def __str__(self):
        return f'id: {self.id}, nome: {self.nome}, prezzo: {self.prezzo}'

