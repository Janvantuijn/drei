import argparse
import random
import subprocess

class BingoGenerator:

    def __init__(self, names=["Voornaam Achternaam"]):
        self.names = names
        self.cards = []

        self.excuses = []
        with open("afmeldingen.txt") as f:
            self.excuses = [line.strip() for line in f]

    def run(self):
        
        excuses_left = len(self.excuses) 
        random.shuffle(self.excuses)

        for name in self.names:

            # Create new LaTeX file 
            new_card = ""
            with open("template.tex") as f:
                new_card = f.read()

            # Add name to .tex file
            new_card = new_card.replace("NAME", name)
            name = name.replace(" ", "_")

            # Add excuses to .tex file
            for x in range(6):
                new_card = new_card.replace("EXCUSE" + str(x), self.excuses[excuses_left - x - 1])
            excuses_left = excuses_left - 6

            with open("kaart_" + name + ".tex", "w+") as f:
                f.write(new_card)

            # Shuffle excuses if all are used
            if(excuses_left < 6):
                random.shuffle(self.excuses)
                excuses_left = len(self.excuses)

            print("Created card for:", name) 
            self.cards.append("kaart_" + name + ".tex")
            
        for card in self.cards:
            print("Generating pdf from " + card, end='')
            subprocess.run(["pdflatex.exe", card, 
                            "-output-directory", card.replace(".tex", ""),
                            "-quiet"])
            
            



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", action='append', help="Name of the contestent.", dest="names")

    args = parser.parse_args()

    if args.names:
        generator = BingoGenerator(args.names) 
    else:
        generator = BingoGenerator()
    generator.run()