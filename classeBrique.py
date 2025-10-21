from foncitons import rgb

class Brique:
    def __init__(self):
        """Initialise une brique avec ses caractéristiques par défaut."""
        self.__largeur = 75
        self.__hauteur = 20
        self.__couleur = ('#FF3D17')     # Rouge
        self.__position = [0, 0]         # Position (coin haut-gauche)
        self.__visible = True            # Sert à la masquer quand elle est cassée
        self.__vie = 2                   # Nombre de coups avant de disparaître
        self.__id = None                 # ID de l'objet Canvas une fois affiché

    def set_position(self, x, y):
        """Définit la position de la brique sur le Canvas."""
        self.__position = [x, y]

    def draw(self, canvas):
        """Dessine ou met à jour la brique sur le Canvas Tkinter."""
        if not self.__visible:
            # Si la brique est "cassée", on la supprime du Canvas
            if self.__id is not None:
                canvas.delete(self.__id)
                self.__id = None
            return

        # Récupère la position et la taille
        x, y = self.__position
        L, H = self.__largeur, self.__hauteur

        if self.__id is None:
            # Première fois qu'on l'affiche → on la crée
            self.__id = canvas.create_rectangle(
                x, y, x + L, y + H,
                fill=self.__couleur, outline=""
            )
        else:
            # Elle existe déjà → on met juste à jour ses coordonnées
            canvas.coords(self.__id, x, y, x + L, y + H)
