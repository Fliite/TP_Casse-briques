class Balle:
    '''Dans cette classe, on gère la balle du jeu.
    On initialise une balle avec ses coordonnées, sa vitesse et sa couleur.
    On pourra eventuellement modifier cette classe pour ajouter des fonctionnalités comme des balles spéciales (vitesse variable, taille variable, etc.).
    '''
    def __init__(self, canvas, x, y, r=7, color="white", vitesseBalle=6):
        self.__canvas = canvas
        self.r = r
        self.__id = canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline=color)
        self.__vitesseBalle = vitesseBalle
        self.__vx = vitesseBalle * 0.7
        self.__vy = -abs(vitesseBalle * 0.7)
        self.__PosPrec = self.__canvas.coords(self.__id)
    
    def CordsBalle(self):
        ''' Renvoie les coordonnées actuelles de la balle sous la forme (x1, y1, x2, y2) '''
        return self.__canvas.coords(self.__id)

    def move(self):
        ''' Déplace la balle selon sa vitesse '''
        self.__PosPrec = self.CordsBalle()
        self.__canvas.move(self.__id, self.__vx, self.__vy)

    def Position(self, x, y):
        ''' Permet de positionner la balle aux coordonnées (x, y) 
         en déplaçant la balle de sa position actuelle à la nouvelle position
        '''
        x1, y1, x2, y2 = self.CordsBalle()
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2
        dx = x - cx
        dy = y - cy
        self.__canvas.move(self.__id, dx, dy)
        self.__PosPrec = self.CordsBalle()
    
    def RebondX(self):
        ''' Inverse la vitesse en x de la balle '''
        self.__vx = -self.__vx

    def RebondY(self):
        ''' Inverse la vitesse en y de la balle '''
        self.__vy = -self.__vy

    def VerifierVitesse(self, vx=None, vy=None):
        ''' Permet de modifier la vitesse de la balle 
        elle prend en argument la nouvelle vitesse en x et/ou y
        '''
        if vx is not None: self.vx = vx
        if vy is not None: self.vy = vy
