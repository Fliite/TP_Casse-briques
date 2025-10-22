class Balle:
    '''Dans cette classe, on gère la balle du jeu.
    On initialise une balle avec ses coordonnées, sa vitesse et sa couleur.
    On pourra eventuellement modifier cette classe pour ajouter des fonctionnalités comme des balles spéciales (vitesse variable, taille variable, etc.).
    '''
    def __init__(self, canvas, x, y, r=7, color="white", vitesseBalle=6):
        self.canvas = canvas
        self.r = r
        self.id = canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline=color)
        self.vitesseBalle = vitesseBalle
        self.vx = vitesseBalle * 0.7
        self.vy = -abs(vitesseBalle * 0.7)
        self._prev_bbox = self.canvas.coords(self.id)
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
            self.__id = canvas.create_oval( x-r, y - r, x + r, y + r, fill=self.__couleur, outline="")
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