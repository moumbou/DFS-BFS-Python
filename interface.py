import tkinter
import tkinter.messagebox
import customtkinter
from recherche import Recherche

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("projet M1 DFS BFS ##BY MOUMBOU##")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ creation de deux sections ============

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(8, weight=1)
        self.frame_left.grid_rowconfigure(5, weight=1)
        self.frame_left.grid_rowconfigure(4, weight=1)

        self.MethodLabel = customtkinter.CTkLabel(master=self.frame_left,
                                                  anchor="w",
                                                  text="Choisir la method de recherche :",
                                                  font=("Roboto Medium", -14))
        self.MethodLabel.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        self.methodChoisi = tkinter.IntVar(value=0)

        self.dfs = customtkinter.CTkRadioButton(master=self.frame_left,
                                                variable=self.methodChoisi,
                                                text='DFS',
                                                value=0)
        self.dfs.grid(row=2, column=0, pady=5, padx=20, sticky="swn")

        self.bfs = customtkinter.CTkRadioButton(master=self.frame_left,
                                                variable=self.methodChoisi,
                                                text='BFS',
                                                value=1)
        self.bfs.grid(row=3, column=0, pady=5, padx=20, sticky="swn")

        self.A = customtkinter.CTkRadioButton(master=self.frame_left,
                                                variable=self.methodChoisi,
                                                text='A*',
                                                value=2)
        self.A.grid(row=4, column=0, pady=5, padx=20, sticky="swn")

        # START AND END NODE SECTION INPUT

        self.startNodeLabel = customtkinter.CTkLabel(master=self.frame_left,
                                                     anchor="w",
                                                     text="Choisir le noeud du debut :",
                                                     font=("Roboto Medium", -14))
        self.startNodeLabel.grid(row=4, column=0, pady=5, padx=10, sticky="we")

        self.StartNode = customtkinter.CTkEntry(master=self.frame_left,
                                                placeholder_text="noeud de debut",
                                                width=25,
                                                height=25,
                                                border_width=2,
                                                corner_radius=2)
        self.StartNode.grid(column=0, row=5, sticky="nwe", padx=50, pady=0)

        self.endNodeLabel = customtkinter.CTkLabel(master=self.frame_left,
                                                   anchor="w",
                                                   text="Choisir le noeud de fin :",
                                                   font=("Roboto Medium", -14))
        self.endNodeLabel.grid(row=6, column=0, pady=5, padx=10, sticky="we")

        self.EndNode = customtkinter.CTkEntry(master=self.frame_left,
                                              placeholder_text="noeud de debut",
                                              width=25,
                                              height=25,
                                              border_width=2,
                                              corner_radius=2)
        self.EndNode.grid(column=0, row=7, sticky="nwe", padx=50, pady=0)

        self.confirmeButton = customtkinter.CTkButton(master=self.frame_left,
                                                      text="Confirmer",
                                                      command=self.button_event)
        self.confirmeButton.grid(
            row=11, column=0, pady=10, padx=5, sticky="we")

        # ============ frame_right ============

        self.frame_right.columnconfigure((0, 1), weight=1)

        # ============ champ pour entrer le graph ============

        self.GraphLabel = customtkinter.CTkLabel(master=self.frame_right,
                                                 anchor="w",
                                                 text="Entrez le graph ici :",
                                                 font=("Roboto Medium", -14))
        self.GraphLabel.grid(row=0, column=0, pady=5, padx=10, sticky="w")

        self.GraphInput = customtkinter.CTkTextbox(master=self.frame_right,
                                                   border_width=1,
                                                   height=400,
                                                   )
        self.GraphInput.grid(column=0, row=2, columnspan=2,
                             sticky="nswe", padx=10, pady=10)


    def button_event(self):
        methode = self.methodChoisi.get()
        start = self.StartNode.get()
        end = self.EndNode.get()
        if start.isnumeric():
            start = int(start)
            end = int(end)
        text = self.GraphInput.get('0.0', 'end')
        try:
            text = eval(text)
        except:
            return print('Error')
        
        Recherche(methode, text, start, end).search()

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
