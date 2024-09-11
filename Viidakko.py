import tkinter as tk
import random
import time

class ViidakkoSeikkailu:
    def __init__(self, root):
        self.root = root
        self.root.title("ernesti ja kernesti viidakossa")

        self.viidakko = [[0 for _ in range(100)] for _ in range(100)]

        self.ernesti = {"sijainti": (0,0)}
        self.kernesti = {"sijainti": (0,0)}

        self.button = tk.Button(self.root, text="Pudota Ernesti ja Kernesti", command=self.pudota)
        self.button.pack()

        self.viidakko_text = tk.Text(self.root, height=10, width=50)
        self.viidakko_text.pack()

    def pudota(self):
        self.ernesti['sijainti'] = (random.randint(0,99), random.randint(0,99))
        self.kernesti['sijainti'] = (random.randint(0,99), random.randint(0,99))

        self.update_viidakko()

        self.move()

    def update_viidakko(self):
        self.viidakko = [[0 for _ in range(100)] for _ in range(100)]

        er_sijainti = self.ernesti['sijainti']
        ker_sijainti = self.kernesti['sijainti']

        self.viidakko[er_sijainti[0]][er_sijainti[1]] = 1
        self.viidakko[ker_sijainti[0]][ker_sijainti[1]] = 2

        self.show_viidakko()
        
    def show_viidakko(self):
        self.viidakko_text.delete(1.0, tk.END)
        for row in self.viidakko[:100]:
            self.viidakko_text.insert(tk.END, ' '.join(map(str, row[:100])) + '\n')

    def move(self):

        while self.ernesti['sijainti'] != self.kernesti['sijainti']:
                
            self.ernesti['sijainti'] = self.liiku(self.ernesti['sijainti'])

            self.kernesti['sijainti'] = self.liiku(self.kernesti['sijainti'])
                
            self.update_viidakko()
                
            self.root.update()
            time.sleep(1)
        
            self.viidakko_text.insert(tk.END, "Vau, onpa mukava nähdä taas!")

    def liiku(self, sijainti):
        x, y = sijainti
        suunta = random.choice(['ylös', 'alas', 'vasemmalle', 'oikealle'])
            
        if suunta == 'ylös' and x > 0:
            x -= 1
        elif suunta == 'alas' and x < 99:
            x += 1
        elif suunta == 'vasemmalle' and y > 0:
            y -= 1
        elif suunta == 'oikealle' and y < 99:
            y += 1
            
        return (x, y)


root = tk.Tk()
peli = ViidakkoSeikkailu(root)
root.mainloop()