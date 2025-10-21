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