def rgb(r, g, b):
    """(255,0,0) -> '#ff0000' pour Tkinter."""
    return f"#{r:02x}{g:02x}{b:02x}"

class Brique:
    def __init__(self):
        """Initialise une brique avec ses caractéristiques par défaut."""
        self.__largeur = 75
        self.__hauteur = 20
        self.__couleur = (255, 0, 0)     # Rouge
        self.__position = [0, 0]         # Position (coin haut-gauche)
        self.__visible = True            # Sert à la masquer quand elle est cassée
        self.__vie = 2                   # Nombre de coups avant de disparaître
        self.__id = None                 # ID de l'objet Canvas une fois affiché

    def set_position(self, x, y):
        """Définit la position de la brique sur le Canvas."""
        self.__position = [x, y]

    def draw(self, canvas):
        """Dessine ou met à jour la brique sur le Canvas Tkinter."""
        if not self.__visible:
            # Si la brique est "cassée", on la supprime du Canvas
            if self.__id is not None:
                canvas.delete(self.__id)
                self.__id = None
            return

        # Récupère la position et la taille
        x, y = self.__position
        L, H = self.__largeur, self.__hauteur
        color = rgb(*self.__couleur)

        if self.__id is None:
            # Première fois qu'on l'affiche → on la crée
            self.__id = canvas.create_rectangle(
                x, y, x + L, y + H,
                fill=color, outline=""
            )
        else:
            # Elle existe déjà → on met juste à jour ses coordonnées
            canvas.coords(self.__id, x, y, x + L, y + H)

class Balle:
    def __init__(self):
        self.__rayon = 10
        self.__couleur = (0, 255, 0)
        self.__position = [300, 300]
        self.__vitesse = [5, -5]
    def getX(self):
        return self.__position[0]
    def getY(self):
        return self.__position[1]


class Raquette:
    def __init__(self):
        self.__largeur = 100
        self.__hauteur = 20
        self.__couleur = (0, 0, 255)
        self.__position = [250, 450]
        self.__vitesse = 10
        def getX(self):
            return self.__position[0] # la raquette se déplace en 1 dimension (x)
        def addX(self, dx):
            self.__position[0] += dx
