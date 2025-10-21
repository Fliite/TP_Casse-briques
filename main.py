import tkinter as tk
from PageParametres import PageParametres
from PageDeJeu import PageJeu
from classeBalle import Balle
from classeRaquette import Raquette
from classeBrique import Brique

class Application(tk.Tk):
    '''La classe principale qui gère les différentes pages (frames).
    Les pages parametres, jeu, accueil sont des frames qui héritent de tk.Frame.
    Ce sont des onglets que l'on peut afficher ou cacher.
    '''
    def __init__(self):
        super().__init__() # le super c'est pour hériter de Tk (la classe mère)
        self.title("Application avec Frames")
        self.geometry("1920x1080")

        # Dictionnaire pour stocker les différentes pages
        self.frames = {}

        # Crée les différentes pages
        for F in (PageAccueil, PageParametres, PageJeu):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew") # nsew pour que la frame prenne toute la place

        self.show_frame("PageAccueil")

    def show_frame(self, page_name):
        '''Affiche la frame demandée'''
        frame = self.frames[page_name]
        frame.tkraise()

#permet de lancer l'application de manière autonome, utile pour les tests
if __name__ == "__main__":
    app = Application()
    app.mainloop()