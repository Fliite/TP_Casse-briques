class brique:
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
