def costo_taxi(chilometri, tariffa_notturna):
     costo_base = chilometri * 2

     if tariffa_notturna == True:
         costo_finale = costo_base + 5
     else:
         costo_finale = costo_base

     print(f"Il prezzo finale della corsa è di [{costo_finale}]")

if __name__ == "__main__":

    print(" Corsa Diurna ")
    costo_taxi(chilometri=10, tariffa_notturna=False)

    print(" Corsa Notturna ")
    costo_taxi(chilometri=10, tariffa_notturna=True)



