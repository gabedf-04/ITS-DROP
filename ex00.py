
#classe padre: contiene gli attributi e metodi comuni a tutti i veicoli
class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca ##attributo marca, modello e auto
        self.modello = modello
        self.anno = anno

##metodo base, verrà sottoscritto nelle classi figlie
    def avvia(self):
        print("il veicolo si avvia...")

##rappresentazione testuale dell'oggetto
    def __str__(self):
        return f"marca: {self.marca}, modello: {self.modello}, anno: {self.anno}"

##classe figlia auto: eredita da veicolo e aggiunge numero_porte
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

##override del metodo avvia()
    def avvia(self):
        print("l'auto avvia il motore: vroom!")

##riusa __str__ del padre e aggiunge il campo specifico
    def __str__(self):
        return super().__str__() + f", porte: {self.numero_porte}"

##classe figlia moto: eredita da veicolo e aggiunge il tipo
class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno) ##richiama il costruttore del padre
        self.tipo = tipo ##attributo specifico di moto

#override del metodo avvia
    def avvia(self):
        print("la moto avvia il motore: brum brum")

##riusa __str__ del padre e aggiunge il campo specifico
    def __str__(self):
        return super().__str__() + f", tipo: {self.tipo}"


##---MAIN---

##chiede all'utente che tipo di veicolo vuole inserire
scelta = input("vuoi inserire un auto o una moto? (A/M): ").upper()

##raccoglie i dati per creare un oggetto auto
if scelta == "A":
    marca = input("marca: ")
    modello = input("modello: ")
    anno = int(input("anno: "))
    porte = int(input("porte: "))
    veicolo = Auto(marca, modello, anno, porte) ##crea l'oggetto auto

#raccoglie i dati per creare un oggetto moto
elif scelta == "M":
    marca = input("marca: ")
    modello = input("modello: ")
    anno = int(input("anno: "))
    tipo= input("tipo: (sportiva, custom, naked):")
    veicolo = Moto(marca, modello, anno, tipo) ##crea l'effetto moto

else:
    print("scelta non valida!")
    exit()

print(veicolo) ##chiama __str__
veicolo.avvia() ##chiama avvia() dalla classe corretta