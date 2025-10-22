import tkinter as tk

class PageJeu(tk.Frame):
    def __init__(self, parent, controller):
        '''Cette page de Jeu'''
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Page des paramètres")
        label.pack(pady=20)

        canvas = tk.Canvas(self, width=200, height=100, bg="lightblue")
        canvas.pack(pady=10)


        #affiche ce que l'utilisateur a entré dans vitesse
        def afficherScore(Str):
            score = vitesse.get()
            score_label = tk.Label(self, text=f"Score: {score}", font=("Arial", 16))
            score_label.pack(pady=10, side=tk.TOP)

        vitesse = tk.Entry(self) #champ de texte pour que l'utilisateur puisse entrer la vitesse de la balle
        vitesse.pack()

        validerVitesse = tk.Button(self, text="Valider la vitesse", command = afficherScore(vitesse)) #bouton pour valider la vitesse entrée par l'utilisateur
        validerVitesse.pack()

        bouton_retour = tk.Button(self, text="Retour à l'accueil",command=lambda: controller.show_frame("PageAccueil"))
        bouton_retour.pack()