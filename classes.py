def rgb(r, g, b):
    """(255,0,0) -> '#ff0000' pour Tkinter."""
    return f"#{r:02x}{g:02x}{b:02x}"

class Brique:
    def __init__(self):
        # attributs "privés" (double underscore) -> accessible UNIQUEMENT dans la classe
        self.__largeur = 75
        self.__hauteur = 20
        self.__couleur = (255, 0, 0)  # on convertira au draw()
        self.__position = [0, 0]
        self.__visible = True
        self.__vie = 2
        self.__id = None  # id de l'objet Canvas une fois créé

    def set_position(self, x, y):
        """Permet de positionner depuis l'extérieur sans toucher à __position directement."""
        self.__position = [x, y]

    def draw(self, canvas):
        """Dessine ou met à jour la brique sur le Canvas."""
        if not self.__visible:
            if self.__id is not None:
                canvas.delete(self.__id)
                self.__id = None
            return

        x, y = self.__position
        L, H = self.__largeur, self.__hauteur
        color = rgb(*self.__couleur)

        if self.__id is None:
            # première création
            self.__id = canvas.create_rectangle(
                x, y, x + L, y + H,
                fill=color, outline=""
            )
        else:
            # juste mise à jour de la position/taille
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
        def getX(self):
            return self.__position[0] # la raquette se déplace en 1 dimension (x)
        def addX(self, dx):
            self.__position[0] += dx
