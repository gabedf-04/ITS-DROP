#Dichiarazione delle variabili

studente1 = "Filippo", "Greco", "12345"
studente2 = "Gabriele", "Greco", "23456"
studente3 = "Gabriele", "De Filippi", "34567"
studente4 = "Simone", "Perlangeli", "45678"
studente5 = "Giovanni", "Mancino", "56789"

#2. Funzione per stampare un singolo studente

def stampa_studente(studente_str):
    """Riceve una stringa studente come parametro e la stampa."""
    print(f"Dati Studente: {studente_str}")

#3. Funzione per stampa tutti i 5 globali

def stampa_studenti_globali():
    """Stampa a video i 5 studenti dichiarati in una tabella formattata e colorata"""
    COLORE_TITOLO = '\033[96m'
    COLORE_INTESTAZIONE = '\033[93m'
    RESET_COLORE = '\033[0m'

#stampa del titolo colorato con cornice

#4. Funzione main




#def crea_studente(nome, cognome, matricola):
    #return {"nome": nome, "cognome": cognome, "matricola": str(matricola).zfill(5)}

#def input_e_stampa_studente():
 #   print("--- INSERIMENTO NUOVO STUDENTE ---")
  #  nome = input("Inserisci il nome: ")
   # cognome = input("Inserisci il cognome: ")
    #matricola = input("Inserisci la matricola (5 cifre): ")

    #nuovo_studente = crea_studente(nome, cognome, matricola)

    #print("\n--- DATI STUDENTE INSERITO ---")
    #print(f"Nome: {nuovo_studente['nome']}")
    #print(f"Cognome: {nuovo_studente['cognome']}")
    #print(f"Matricola: {nuovo_studente['matricola']}")

#input_e_stampa_studente()
