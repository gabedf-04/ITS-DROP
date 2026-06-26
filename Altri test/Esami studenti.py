class Esame:
    def __init__(self, materia, voto, data):
        self.materia = materia
        self.voto = voto
        self.data = data

    def __str__(self):
        return f"{self.materia} - {self.voto}/30 - {self.data}"

class Studente:
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.esami = []

    def __str__(self):
        return f"{self.nome} - {self.cognome} - {self.matricola}"

    def aggiungi_esame(self, esame):
        self.esami.append(esame)

studenti = []

def registra_studente():
    global studenti
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    matricola = input("Matricola: ")
    studente = Studente(nome, cognome, matricola)
    studenti.append(studente)

def visualizza_studenti():
    for s in studenti:
        print(s)

def visualizza_libretto():
    matricola = input("Inserisci Matricola: ")
    for s in studenti:
        if s.matricola == matricola:
            print(s)
            for e in s.esami:
                print(e)

def aggiungi_esame_a_studente():
    matricola = input("Inserisci Matricola: ")
    for s in studenti:
        if s.matricola == matricola:
            materia = input("Materia: ")
            voto = int(input("Voto: "))
            data = input("Data: ")
            e = Esame(materia, voto, data)
            s.aggiungi_esame(e)

def main():
    while True:
        print("\n---- MENU ----")
        print("1. REGISTRARE STUDENTE")
        print("2. AGGIUNGI ESAMI")
        print("3. VISUALIZZA STUDENTI")
        print("4. VISUALIZZA LIBRETTO")
        print("5. ESCI")

        scelta = input("Scegli: ")

        if scelta == "1":
            registra_studente()
        elif scelta == "2":
            aggiungi_esame_a_studente()
        elif scelta == "3":
            visualizza_studenti()
        elif scelta == "4":
            visualizza_libretto()
        elif scelta == "5":
            break
        else:
            print("scelta invalida!")

if __name__ == "__main__":
    main()