import numpy as np

def saisir_matrice():
    n = int(input("Entrez la taille de la matrice carrée (n x n) : "))
    matrice = []
    print("Entrez les coefficients de la matrice ligne par ligne :")
    for i in range(n):
        ligne = list(map(float, input().split()))
        if len(ligne) != n:
            print("Erreur : Veuillez entrer exactement", n, "valeurs par ligne.")
            return None
        matrice.append(ligne)
    return np.array(matrice)

def inverser_matrice(matrice):
    try:
        inverse = np.linalg.inv(matrice)
        return inverse
    except np.linalg.LinAlgError:
        print("La matrice n'est pas inversible.")
        return None

def main():
    matrice = saisir_matrice()
    if matrice is not None:
        print("Matrice saisie :\n", matrice)
        inverse = inverser_matrice(matrice)
        if inverse is not None:
            print("Matrice inverse :\n", inverse)

if __name__ == "__main__":
    main()