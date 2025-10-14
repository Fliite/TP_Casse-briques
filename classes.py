class Brique:
    def __init__(self):
        # Attributs "privés" (name mangling), garde EXACTEMENT ces noms
        self.__largeur = 75
        self.__hauteur = 20
        self.__couleur = (255, 0, 0)    # -> sera converti avec rgb()
        self.__position = [0, 0]
        self.__visible = True
        self.__vie = 2
        self.__id = None                # id Canvas une fois dessiné

    def set_position(self, x, y):
        """Positionne la brique (coin haut-gauche)."""
        self.__position = [x, y]

    def brique_casse(self):
        """Renvoie visible à False quand la vie tombe à 0."""
        self.__vie -= 1
        if self.__vie <= 0:
            self.__visible = False

    def draw(self, canvas):
        """Dessine ou met à jour la brique sur le Canvas."""
        if not self.__visible:
            # Si elle n'est plus visible, supprime-la du canvas si besoin
            if self.__id is not None:
                canvas.delete(self.__id)
                self.__id = None
            return

        x, y = self.__position
        L, H = self.__largeur, self.__hauteur

        if self.__id is None:
            # Première fois : on crée le rectangle
            self.__id = canvas.create_rectangle( x, y, x + L, y + H, fill=rgb(*self.__couleur), outline="")
        else:
            # Déjà créé : on met juste à jour ses coordonnées
            canvas.coords(self.__id, x, y, x + L, y + H)

class Balle:
    def __init__(self):
        self.__rayon = 10
        self.__couleur = (0, 255, 0)
        self.__position = [300, 300]
        self.__vitesse = [5, -5]

class Raquette:
    def __init__(self):
        self.__largeur = 100
        self.__hauteur = 20
        self.__couleur = (0, 0, 255)
        self.__position = [250, 450]
        self.__vitesse = 10
