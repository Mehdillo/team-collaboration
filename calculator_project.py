
def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b

# Fonction de division
def division(a, b):
    if b == 0:
        return "Erreur! Division par zéro."
    else:
        return a / b

# Fonction principale
def calculatrice():
    print("Sélectionnez l'opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choix = input("Entrez votre choix (1/2/3/4): ")

        if choix in ('1', '2', '3', '4'):
            num1 = float(input("Entrez le premier nombre: "))
            num2 = float(input("Entrez le deuxième nombre: "))

            if choix == '1':
                print(f"{num1} + {num2} = {addition(num1, num2)}")
            elif choix == '2':
                print(f"{num1} - {num2} = {soustraction(num1, num2)}")
            elif choix == '3':
                print(f"{num1} * {num2} = {multiplication(num1, num2)}")
            elif choix == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")
            
            # Demande à l'utilisateur s'il veut effectuer un autre calcul
            prochain_calcul = input("Voulez-vous effectuer un autre calcul? (oui/non): ")
            if prochain_calcul.lower() != 'oui':
                break
        else:
            print("Choix invalide, veuillez réessayer.")

# Exécution de la fonction principale
if __name__ == "__main__":
    calculatrice()

