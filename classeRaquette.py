class Raquette:
    def __init__(self):
        self.__largeur = 100
        self.__hauteur = 20
        self.__couleur = ("#33E73F")
        self.__position = [250, 450]
        self.__vitesse = 10
        def getX(self):
            return self.__position[0] # la raquette se déplace en 1 dimension (x)
        def addX(self, dx):
            self.__position[0] += dx
        def draw(self, canvas):
            if self._id is None : 
                self._id = canvas.create_rectangle(self._largeur, self._hauteur, self._largeur + 110, self._hauteur + 16, fill=self.__couleur, outline="")
            else : 
                canvas.coords(self._id, self._largeur, self._hauteur, self._largeur + 110, self._hauteur + 16)
        def move(self, dx, W):
            """déplacement horizontal"""
            nx = self.x + dx
            nx = max(0, min(nx, W - self.w))
            dx_real = nx - self.x
            if dx_real != 0:
                self.x = nx
            return dx_real  # utile si tu veux bouger l'item Canvas avec move()