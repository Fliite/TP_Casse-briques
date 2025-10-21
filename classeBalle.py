class Balle:
    def __init__(self):
        self.__rayon = 10
        self.__couleur = ("#F7FF17")
        self.__position = [300, 300]
        self.__vitesse = [5, -5]
        self.__id = None
    def getX(self):
        return self.__position[0]
    def getY(self):
        return self.__position[1]
    def getR(self):
        return self.__rayon
    def draw_b(self, canvas):
        """ Crée et met à jour la balle """
        x, y = self.__position
        r = self.__rayon
        if self.__id is None:
            self.__id = canvas.create_oval( x-r, y - r, x + r, y + r, fill=rgb(*self.__couleur), outline="")
        else : 
            canvas.coords(self.__id, x-r, y - r, x + r, y + r )
    def rebond(self, canvas, ):
        """ Permet de créer la physique de la balle"""
        x, y = self.__position
        vx, vy = self.__vitesse
        r = self.__rayon

        #Déplacement 
        x += vx
        y += vy

        #Rebond mur gauche/droit
        if x-r <= 0 or x+r <= 720:
            vx = -vx
        #Rebond mur plafond
        if y-r <= 0 :
            vy = -vy

        self.__position = [x, y]
        self.__vitesse = [vx, vy]
        self.draw(canvas)