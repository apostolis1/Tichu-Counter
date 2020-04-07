import tkinter as tk

class PlayerFrame(tk.Frame):
    def __init__(self, parent, playername,  *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg=self.parent["background"])
        self.playerLabel = tk.Label(self, text = str(playername), bg=self.parent["background"])
        self.scoreLabel = tk.Label(self, text = "Current Points", bg=self.parent["background"])
        self.score = tk.Label(self, text=0, bg=self.parent["background"])
        self.playerLabel.grid(row=0, column=0, columnspan=2)
        self.scoreLabel.grid(row=1, column=0)
        self.score.grid(row=1, column=1)
        self.scoreSlider = tk.Scale(self, from_=-25, to=125, orient=tk.HORIZONTAL, resolution=5, bg=self.parent["background"])
        self.scoreSlider.grid(row=2, columnspan=2)

        self.addBtn = tk.Button(self, text="Add", command=lambda : self.updateScore(), bg=self.parent["background"])
        self.addBtn.grid(row=3, columnspan=2)

    def updateScore(self):
        self.score['text'] = int(self.score.cget("text")) + self.scoreSlider.get()
        self.scoreSlider.set(0)
        return
    def makeZero(self):
        self.score['text'] = 0
        self.scoreSlider.set(0)
        return

class MainApplication(tk.Frame):
    def newGame(self):
        self.player1.makeZero()
        self.player2.makeZero()
        self.player3.makeZero()
        self.player4.makeZero()
        return

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Tichu Counter")
        self.parent.resizable(False, False)
        self.player1 = PlayerFrame(self, "You")
        self.player2 = PlayerFrame(self, "Teammate")
        self.player3 = PlayerFrame(self, "Oponnent 1")
        self.player4 = PlayerFrame(self, "Oponnent 2")
        self.player1.grid(row=2, column=1, sticky="nsew")
        self.player2.grid(row=0, column=1, sticky="nsew")
        self.player3.grid(row=1, column=0, sticky="nsew")
        self.player4.grid(row=1, column=3, sticky="nsew")
        self.newGameBtn = tk.Button(self, command = lambda : self.newGame(), text="NEW GAME")
        self.newGameBtn.grid(row=1, column=1)

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=1)

    root.mainloop()
