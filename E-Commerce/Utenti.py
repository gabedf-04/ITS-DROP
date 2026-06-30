class Utente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email


    def __str__(self):
         return f'id: {self.id}, nome: {self.nome}, email: {self.email}'
