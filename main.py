import tkinter as tk
from PageParametres import PageParametres
from jeu import PageJeu

class Application(tk.Tk):
    def __init__(self):
        super().__init__() # le super c'est pour hériter de Tk (la classe mère)
        self.title("Application avec Frames")
        self.geometry("1280x720")

        # Dictionnaire pour stocker les différentes pages
        self.frames = {}

        # Crée les différentes pages
        for F in (PageAccueil, PageParametres):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageAccueil")

    def show_frame(self, page_name):
        '''Affiche la frame demandée'''
        frame = self.frames[page_name]
        frame.tkraise()

# Page d'accueil
class PageAccueil(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Bienvenue dans la page d'accueil")
        label.pack(pady=20)

        bouton = tk.Button(self, text="Aller aux paramètres",command=lambda: controller.show_frame("PageParametres"))
        bouton.pack()

        boutton_quitter = tk.Button(self, text="Quitter", command=self.quit)
        boutton_quitter.pack(pady=10)

        boutton_jouer = tk.Button(self, text="Jouer", command=lambda: controller.show_frame("PageJeu"))
        boutton_jouer.pack(pady=10)

        score = 0
        score_label = tk.Label(self, text=f"Score: {score}", font=("Arial", 16))
        score_label.pack(pady=10)

if __name__ == "__main__":
    app = Application()
    app.mainloop()


