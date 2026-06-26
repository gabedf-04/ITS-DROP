def conta_vocali(frase):
    contatore = 0
    vocali = "aeiouAEIOU"

    for carattere in frase:
        if carattere in vocali:
            contatore += 1

    print(f"Nella frase ci sono in totale {contatore} vocali.")



if __name__ == "__main__":
    frase_utente = input("Inserisci una frase a tua scelta: ")
    conta_vocali(frase_utente)