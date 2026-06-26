class Veicolo:
    """
    Classe Base (o Classe Madre).
    Contiene le caratteristiche comuni a TUTTI i veicoli (targa e colore).
    """

    def __init__(self, targa, colore):
        # Il costruttore inizializza le variabili fondamentali del veicolo
        self.targa = targa
        self.colore = colore

    def __str__(self):
        # Metodo speciale richiamato automaticamente quando si usa print() sull'oggetto.
        # Deve SEMPRE restituire (return) una stringa di testo.
        return f"Targa: {self.targa}\nColore: {self.colore}"


class Auto(Veicolo):
    """
    Classe Figlia che eredita da Veicolo.
    Aggiunge caratteristiche specifiche per le automobili (ruote e modello).
    """

    def __init__(self, numero_di_ruote, modello, targa, colore):
        # super().__init__ invia targa e colore alla classe madre Veicolo
        # per evitare di riscrivere il codice di inizializzazione
        super().__init__(targa, colore)
        # Inizializzazione degli attributi specifici di Auto
        self.numero_di_ruote = numero_di_ruote
        self.modello = modello

    def __str__(self):
        # Sovrascrive il metodo della classe madre per mostrare TUTTI i dati dell'auto
        return f"Auto: {self.numero_di_ruote} ruote - {self.modello}, {self.targa}, {self.colore}"

    # --- METODI GETTER (Per leggere i dati internamente) ---
    def getnumero_di_ruote(self):
        return self.numero_di_ruote

    def getmodello(self):
        return self.modello

    # --- METODI SETTER (Per modificare i dati internamente) ---
    def setnumero_di_ruote(self, numero_di_ruote):
        self.numero_di_ruote = numero_di_ruote

    def setmodello(self, modello):
        self.modello = modello


class Moto(Veicolo):
    """
    Classe Figlia che eredita da Veicolo.
    Gestisce le motociclette con la stessa logica di Auto.
    """

    def __init__(self, numero_di_ruote, modello, targa, colore):
        # Invia i parametri comuni a Veicolo
        super().__init__(targa, colore)
        # Inizializza le proprietà specifiche di Moto
        self.numero_di_ruote = numero_di_ruote
        self.modello = modello

    def __str__(self):
        # Mostra a schermo i dettagli specifici formattati per la Moto
        return f"Moto: {self.numero_di_ruote} ruote - {self.modello}, {self.targa}, {self.colore}"

    # --- METODI GETTER E SETTER ---
    def getnumero_di_ruote(self):
        return self.numero_di_ruote

    def getmodello(self):
        return self.modello

    def setnumero_di_ruote(self, numero_di_ruote):
        self.numero_di_ruote = numero_di_ruote

    def setmodello(self, modello):
        self.modello = modello


# ==============================================================================
# FUNZIONI DI INTERFACCIA E LOGICA DI CONTROLLO
# ==============================================================================

def menù():
    """
    Stampa a schermo le opzioni disponibili per l'utente.
    """
    print("\n--- MENÙ ---")
    print("1, Auto o Moto (Inserisci un nuovo veicolo)")
    print("2, Stampa tutti i veicoli")
    print("3, Esci")


def main():
    """
    Funzione principale che esegue il programma e coordina il flusso logico.
    """
    # Creiamo una lista vuota in memoria per salvare tutti gli oggetti (veicoli) creati
    lista_veicoli = []

    # [TEST STATICO] Inseriamo un'auto predefinita per verificare subito il funzionamento
    a1 = Auto("4", "Ferrari", "XXX", "Rosso")
    lista_veicoli.append(a1)  # Aggiunge la Ferrari alla nostra lista dei veicoli
    print(f"Test statico main eseguito (Ferrari aggiunta automaticamente).")

    # Avviamo un ciclo infinito. Il programma continuerà a mostrare il menù
    # finché l'utente non deciderà esplicitamente di uscire premendo 3.
    while True:
        menù()  # Mostra le opzioni testuali
        scelta = input("Scegli un'opzione: ").strip()

        # ----------------------------------------------------------------------
        # OPZIONE 1: INSERIMENTO NUOVO VEICOLO
        # ----------------------------------------------------------------------
        if scelta == "1":
            tipo = input("Vuoi inserire un'Auto o una Moto? ").strip().lower()

            # Chiediamo all'utente tutti i dati necessari (comuni e specifici)
            targa = input("Targa: ")
            colore = input("Colore: ")
            modello = input("Modello: ")
            numero_di_ruote = input("Numero di Ruote: ")

            # Verifichiamo cosa l'utente vuole creare e istanziamo la classe corretta
            if tipo == "auto":
                nuovo_veicolo = Auto(numero_di_ruote, modello, targa, colore)
                lista_veicoli.append(nuovo_veicolo)  # Salva l'oggetto auto nella lista
                print("Auto inserita con successo!")

            elif tipo == "moto":
                nuovo_veicolo = Moto(numero_di_ruote, modello, targa, colore)
                lista_veicoli.append(nuovo_veicolo)  # Salva l'oggetto moto nella lista
                print("Moto inserita con successo!")

            else:
                # Gestione dell'errore nel caso l'utente scriva una parola non riconosciuta
                print("Scelta non valida! Devi digitare 'auto' o 'moto'.")

        # ----------------------------------------------------------------------
        # OPZIONE 2: STAMPA DI TUTTI I VEICOLI REGISTRATI
        # ----------------------------------------------------------------------
        elif scelta == "2":
            # Controllo di sicurezza: se la lista è vuota avvisa l'utente
            if not lista_veicoli:
                print("Nessun veicolo presente in memoria.")
            else:
                print("\n--- ELENCO TUTTI I VEICOLI ---")
                # Ciclo FOR: scorre la lista elemento per elemento
                for v in lista_veicoli:
                    # Python richiama in automatico il metodo __str__ specifico dell'oggetto (Auto o Moto)
                    print(v)

        # ----------------------------------------------------------------------
        # OPZIONE 3: CHIUSURA DEL PROGRAMMA
        # ----------------------------------------------------------------------
        elif scelta == "3":
            print("Uscita dal programma in corso...")
            break  # Interrompe bruscamente il ciclo 'while True', terminando il main

        # Gestione errore se l'utente inserisce caratteri o numeri non presenti nel menù
        else:
            print("Opzione non valida. Riprova.")


# Questo blocco assicura che il programma parta eseguendo la funzione main()
# solo se il file viene lanciato direttamente (non importato come modulo esterno)
if __name__ == "__main__":
    main()