import tkinter as tk

class PageParametres(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Page des paramètres")
        label.pack(pady=20)

        canvas = tk.Canvas(self, width=200, height=100, bg="lightblue")
        canvas.pack(pady=10)

        bouton_retour = tk.Button(self, text="Retour à l'accueil",command=lambda: controller.show_frame("PageAccueil"))
        bouton_retour.pack()