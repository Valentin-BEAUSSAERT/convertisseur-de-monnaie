from forex_python.converter import * 
import datetime

def convertir_devise(montant, devise_from, devise_to):
    c = CurrencyRates()
    try:
        montant_converti = c.convert(devise_from, devise_to, montant)
        return montant_converti
    except RatesNotAvailableError:
        return None

def convertir_devise(montant, devise_from, devise_to):
    c = CurrencyRates()
    try:
        montant_converti = c.convert(devise_from, devise_to, montant)
        return montant_converti
    except RatesNotAvailableError:
        return None
    
def enregistrer_historique(montant, devise_from, devise_to, montant_converti):
    with open("historique_conversions.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = f"{timestamp} - {montant} {devise_from} -> {montant_converti} {devise_to}\n"
        file.write(ligne)

def main():
    montant = float(input("Entrez le montant à convertir: "))
    devise_from = input("Entrez la devise d'origine (ex: EUR, USD): ").upper()
    devise_to = input("Entrez la devise cible (ex: EUR, USD): ").upper()

    montant_converti = convertir_devise(montant, devise_from, devise_to)
    if montant_converti is not None:
        print(f"{montant} {devise_from} équivaut à {montant_converti} {devise_to}")
        enregistrer_historique(montant, devise_from, devise_to, montant_converti)
    else:
        print("La conversion demandée est impossible.")

if __name__ == "__main__":
    main()
