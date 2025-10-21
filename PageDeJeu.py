import tkinter as tk
from tkinter import ttk, messagebox

# PageDeJeu.py
# Page Tkinter réutilisable pour un projet multi-fenêtres.
# Attendu: le "controller" passé doit fournir une méthode show_frame(name)
# (ou équivalente) qui affiche une autre page/Frame. Adjustez les noms
# de pages appelés selon votre main.py.

#exemple de page de mesu. On peut utiliser des bouts de codes de cette fonction


class PageDeJeu(tk.Frame):
    """
    Frame principale de la page de jeu.
    Utilisation attendue depuis le fichier main:
        page = PageDeJeu(master=root, controller=self)
        page.pack(fill="both", expand=True)
    Le controller doit avoir une méthode show_frame(page_name) ou
    show_frame(PageClass) que cette page appellera pour changer de fenêtre.
    """

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.controller = controller

        # --- Menu principal en haut (sous forme de Menubar) ---
        menubar = tk.Menu(master)
        # Fichier -> Nouveau (sous-menus), Séparer par un trait, Quitter
        file_menu = tk.Menu(menubar, tearoff=0)
        new_menu = tk.Menu(file_menu, tearoff=0)
        new_menu.add_command(label="Solo", command=lambda: self._demarrer("Solo"))
        new_menu.add_command(label="Multijoueur", command=lambda: self._demarrer("Multijoueur"))
        file_menu.add_cascade(label="Nouveau", menu=new_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=master.quit)
        menubar.add_cascade(label="Fichier", menu=file_menu)

        # Affichage -> bascule de la barre latérale
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Basculer la barre latérale", command=self._toggle_sidebar)
        menubar.add_cascade(label="Affichage", menu=view_menu)

        # Aide -> A propos
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="A propos", command=self._about)
        menubar.add_cascade(label="Aide", menu=help_menu)

        # Assigne le menubar à la fenêtre principale (root)
        try:
            master.config(menu=menubar)
        except Exception:
            # Certains containers n'acceptent pas menu, ignorer
            pass

        # --- Layout: barre latérale + zone de contenu ---
        self.sidebar_visible = True
        self.sidebar = ttk.Frame(self, width=200, relief="ridge", padding=(5, 5))
        self.sidebar.pack(side="left", fill="y")

        self.content = ttk.Frame(self, padding=(10, 10))
        self.content.pack(side="left", fill="both", expand=True)

        # Boutons de navigation sur la barre latérale
        ttk.Label(self.sidebar, text="Navigation", font=("Segoe UI", 10, "bold")).pack(pady=(0, 6))

        btn_accueil = ttk.Button(self.sidebar, text="Accueil", command=lambda: self._go_to("Accueil"))
        btn_accueil.pack(fill="x", pady=2)

        btn_options = ttk.Button(self.sidebar, text="Options", command=lambda: self._go_to("Options"))
        btn_options.pack(fill="x", pady=2)

        btn_scores = ttk.Button(self.sidebar, text="Scores", command=lambda: self._go_to("Scores"))
        btn_scores.pack(fill="x", pady=2)

        # Un Menubutton sur la sidebar pour un sous-menu contextuel
        mb_frame = ttk.Frame(self.sidebar)
        mb_frame.pack(fill="x", pady=(8, 2))
        ttk.Label(mb_frame, text="Plus", font=("Segoe UI", 9)).pack(anchor="w")
        menubutton = tk.Menubutton(mb_frame, text="Actions", relief="raised")
        submenu = tk.Menu(menubutton, tearoff=0)
        submenu.add_command(label="Réinitialiser la partie", command=self._reset_game)
        submenu.add_command(label="Afficher aide rapide", command=self._show_quick_help)
        menubutton.config(menu=submenu)
        menubutton.pack(fill="x", pady=4)

        ttk.Separator(self.sidebar, orient="horizontal").pack(fill="x", pady=6)

        btn_quit = ttk.Button(self.sidebar, text="Quitter", command=master.quit)
        btn_quit.pack(side="bottom", fill="x", pady=4)

        # --- Contenu central (zone du jeu / placeholder) ---
        self.title_label = ttk.Label(self.content, text="Page de Jeu", font=("Segoe UI", 14, "bold"))
        self.title_label.pack(anchor="nw")

        self.info_text = tk.Text(self.content, height=10, wrap="word")
        self.info_text.insert("1.0", "Zone de jeu / informations.\n\nUtilisez les boutons de la gauche\nou les menus en haut pour naviguer.")
        self.info_text.config(state="disabled")
        self.info_text.pack(fill="both", expand=True, pady=(8, 0))

        # Exemple d'éléments de contrôle du jeu (placeholders)
        controls = ttk.Frame(self.content)
        controls.pack(fill="x", pady=(8, 0))
        ttk.Button(controls, text="Démarrer", command=lambda: self._demarrer("Solo")).pack(side="left", padx=2)
        ttk.Button(controls, text="Pause", command=self._pause).pack(side="left", padx=2)
        ttk.Button(controls, text="Stop", command=self._stop).pack(side="left", padx=2)

    # --- Méthodes d'interaction internes (appellent le controller si possible) ---
    def _go_to(self, page_name):
        # Tentative d'appeler la méthode show_frame du controller.
        if hasattr(self.controller, "show_frame"):
            try:
                self.controller.show_frame(page_name)
                return
            except Exception:
                pass
        # Fallback: message d'information
        messagebox.showinfo("Navigation", f"Demande de navigation vers: {page_name}")

    def _demarrer(self, mode):
        # Exemple: démarrer une partie en solo/multi
        if hasattr(self.controller, "start_game"):
            try:
                self.controller.start_game(mode)
                return
            except Exception:
                pass
        messagebox.showinfo("Démarrer", f"Démarrage mode: {mode}")

    def _reset_game(self):
        if hasattr(self.controller, "reset_game"):
            try:
                self.controller.reset_game()
                return
            except Exception:
                pass
        messagebox.showinfo("Réinitialiser", "Réinitialisation de la partie (placeholder)")

    def _show_quick_help(self):
        messagebox.showinfo("Aide rapide", "Touches:\n- Flèches: déplacer\n- Espace: tirer\n(placeholder)")

    def _pause(self):
        if hasattr(self.controller, "pause"):
            try:
                self.controller.pause()
                return
            except Exception:
                pass
        messagebox.showinfo("Pause", "Pause (placeholder)")

    def _stop(self):
        if hasattr(self.controller, "stop"):
            try:
                self.controller.stop()
                return
            except Exception:
                pass
        messagebox.showinfo("Stop", "Arrêt (placeholder)")

    def _about(self):
        messagebox.showinfo("A propos", "TP Casse-briques\nPageDeJeu - Interface de navigation (placeholder)")

    def _toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar.pack_forget()
            self.sidebar_visible = False
        else:
            self.sidebar.pack(side="left", fill="y")
            self.sidebar_visible = True


# Si ce fichier est exécuté directement, on affiche une petite fenêtre de test:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test PageDeJeu")
    # Simuler un controller minimal avec show_frame
    class FakeController:
        def show_frame(self, name):
            messagebox.showinfo("Controller", f"show_frame appelé avec: {name}")
        def start_game(self, mode):
            messagebox.showinfo("Controller", f"start_game: {mode}")

    page = PageDeJeu(root, controller=FakeController())
    page.pack(fill="both", expand=True)
    root.geometry("800x500")
    root.mainloop()