import tkinter as tk

class PageJeu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Page du jeu")
        label.pack(pady=20)

        canvas = tk.Canvas(self, width=1280, height=720, bg="black")
        canvas.pack(pady=10)

        boutonRetour = tk.Button(self, text="Retour à l'accueil",command=lambda: controller.show_frame("PageAccueil"))
        boutonRetour.pack()
        


