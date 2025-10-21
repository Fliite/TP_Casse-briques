from foncitons import rgb

class Brique:
    def __init__(self):
        """Initialise une brique avec ses caractéristiques par défaut."""
        self.__largeur = 75
        self.__hauteur = 20
        self.__couleur = (['#FF3D17', ])     # Rouge
        self.__position = [0, 0]         # Position (coin haut-gauche)
        self.__visible = True            # Sert à la masquer quand elle est cassée
        self.__vie = 2                   # Nombre de coups avant de disparaître
        self.__id = None                 # ID de l'objet Canvas une fois affiché

    def set_position(self, x, y):
        """Définit la position de la brique sur le Canvas."""
        self.__position = [x, y]