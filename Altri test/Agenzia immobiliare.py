import os
from casa import Casa
class AgenziaImmobiliare:
    def __init__(self, ):

class Casa:
    def __init__(self, codice, prezzo, vani, mq, ha_garage, ha_ascensore, in_condominio, indirizzo, proprietario):
        self.codice = codice
        self.prezzo = prezzo
        self.vani = vani
        self.mq = mq
        self.ha_garage = ha_garage
        self.ha_ascensore = ha_ascensore
        self.in_condominio = in_condominio
        self.indirizzo = indirizzo
        self.proprietario = proprietario

class Indirizzo:
    def __init__(self, via_numero="", cap=""):
        self.via_numero = via_numero
        self.cap = cap

class Proprietario:
    def __init__(self, nome="", cognome="", numero="", ):
        self.nome = nome
        self.cognome = cognome
        self.numero = numero


