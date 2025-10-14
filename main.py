import tkinter as tk
from PageParametres import PageParametres
from PageDeJeu import PageJeu

class Application(tk.Tk):
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

# Page d'accueil
class PageAccueil(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="lightgreen")

        label = tk.Label(self, text="Bienvenue dans la page d'accueil")
        label.pack(pady=20)

        bouton_parametres = tk.Button(self, text="Aller aux paramètres",command=lambda: controller.show_frame("PageParametres"))
        bouton_parametres.pack()

        boutton_quitter = tk.Button(self, text="Quitter", command=self.quit)
        boutton_quitter.pack(pady=10, side=tk.TOP)

        boutton_jouer = tk.Button(self, text="Jouer", command=lambda: controller.show_frame("PageJeu"))
        boutton_jouer.pack(pady=10, side=tk.TOP)

        score = 0
        score_label = tk.Label(self, text=f"Score: {score}", font=("Arial", 16))
        score_label.pack(pady=10, side=tk.TOP)

if __name__ == "__main__":
    app = Application()
    app.mainloop()


