# Jopie van Dopie bingokaart generator

Mocht jopie ooit nog besluiten om weer te gaan hockeyen kan deze bingokaart-generator gebruikt worden om een spel te maken van zijn vele afmeldingen.

## Required software:
- pdflatex.exe (is waarschijnlijk al geinstalleerd als je TeXstudio gebruikt of een andere LaTeX editor)
- LaTeX package: tikz
- Python 3

## Genereren van bingokaarten
Als test kun je het beste eerst het programma runnen zonder input:
'''
python bingo_generator.py
'''

Mocht erg geen pdf verschijnen in een folder genaamd "kaart_Voornaam_Achternaam" dan je het beste kaart_Voornaam_Achternaam.tex openen in je LaTeX editor en vanuit daar te kijken wat de errors zijn.

Als alles werkt kun je meerdere bingokaarten genereren voor je teamgenoten met de '''-n ''' command line optie:
'''
python bingo_generator.py -n "Voornaam1 AchterNaam1" -n "Voornaam2 Achternaam2" 
'''

Voor elke naam wordt er een folder gemaakt waar de PDF in te vinden is.