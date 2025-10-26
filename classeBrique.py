class Brique:
    '''Dans cette classe, on gère les briques du jeu.
    On initialise une brique avec ses coordonnées, sa couleur et le nombre de coups nécessaires pour la détruire.
    On pourra eventuellement modifier cette classe pour ajouter des fonctionnalités comme des briques spéciales (indestructibles, qui donnent des bonus, etc.).
    '''
    def __init__(self, canvas, x1, y1, x2, y2, color="orange", PVBrique=1):
        ''' Initialise une brique aux coordonnées (x1, y1, x2, y2) avec une couleur et des points de vie '''
        self.canvas = canvas
        self.hits = PVBrique #nombre de points de vie de la brique.
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def DetruireBrique(self):
        ''' Détruit la brique en la supprimant du canevas '''
        try:
            self.canvas.delete(self.id)
        except Exception:
            pass