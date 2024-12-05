"""
Bonjour
"""
# Module pour déterminer si un entier est un nombre premier.

#### Fonction secondaire ####

def isprime(p):
    """
    Vérifie si un entier est un nombre premier.

    Cette fonction détermine si le nombre passé en paramètre est un
    nombre premier ou non, en renvoyant un booléen.

    Args:
        p (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est premier, False sinon.
    """
    if p <= 1:
        return False
    for i in range(2, p - 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale ####

def main():
    """
    Point d'entrée principal du programme.

    Cette fonction utilise la fonction `isprime` pour afficher tous les
    nombres premiers entre 0 et 99.
    """
    for n in range(100):
        if isprime(n):
            print(n, end=",")
    print()

if __name__ == "__main__":
    main()
