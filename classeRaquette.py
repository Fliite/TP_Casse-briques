class Raquette:
    '''La classe Raquette représente la raquette contrôlée par le joueur.
    On initialise une raquette avec sa position centrale, sa largeur, sa hauteur, sa couleur et sa vitesse de déplacement.
    On gère le déplacement de la raquette, sa position et son centrage.
    '''
    def __init__(self, canvas, x, y, largeur=100, hauteur=12, color="lightblue", vitesse=9):
        ''' Initialise une raquette aux coordonnées (x, y) avec une largeur, une hauteur, une couleur et une vitesse '''
        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur
        self.id = canvas.create_rectangle(x - largeur/2, y - hauteur/2, x + largeur/2, y + hauteur/2, fill=color, outline=color)
        self.vitesse = vitesse
        self.vx = 0

    def deplacement(self):
        '''Déplace la raquette selon sa vitesse. Gère les limites du canevas.'''
        self.canvas.move(self.id, self.vx, 0)
        # clamp to canvas
        x1, y1, x2, y2 = self.coordonnees()
        W = int(self.canvas['width'])
        if x1 < 0:
            self.canvas.move(self.id, -x1, 0)
        elif x2 > W:
            self.canvas.move(self.id, W - x2, 0)

    def coordonnees(self):
        ''' Renvoie les coordonnées actuelles de la raquette sous la forme (x1, y1, x2, y2) '''
        return self.canvas.coords(self.id)

    def centre(self):
        ''' Renvoie les coordonnées du centre de la raquette sous la forme (cx, cy) '''
        x1, y1, x2, y2 = self.coordonnees()
        return ((x1 + x2) / 2, (y1 + y2) / 2) # centre de la raquette

    def centrer(self, x):
        ''' Permet de centrer la raquette en x '''
        x1, y1, x2, y2 = self.coordonnees()
        cx = (x1 + x2) / 2
        dx = x - cx
        self.canvas.move(self.id, dx, 0)

    def GoRaquette(self, vx):
        ''' Permet de modifier la vitesse de la raquette '''
        self.vx = vx