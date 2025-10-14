class Brique:
    def __init__(self):
        self.__largeur = 75
        self.__hauteur = 20
        self.__couleur = (255, 0, 0)
        self.__position = [0, 0]
        self.__visible = True
        self.__vie = 2
    def Brique_casse(self):
        self.__vie -= 1
        if self.__vie <= 0:
            self.__visible = False
    def draw(self, canvas):
        if not self._visible:
            return
        x, y = self.__position
        L, H = self._largeur, self.__hauteur
        if self._id is None:
            self._id = canvas.create_rectangle(x, y, x+L, y+H, fill="green")
        else :
            canvas.coords(self._id, x, , x+L, y+H)

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
