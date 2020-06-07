import stig,kim
import time

def initGame():
    spielstand = [    
        {
            "pos" : ["b","2"],
            "type": "bauer",
            "farbe": "w"
        },
        {
            "pos" : ["a","7"],
            "type": "bauer",
            "farbe": "b"
        },
        {
            "pos" : ["c","3"],
            "type": "bauer",
            "farbe": "b"
        }
    ]
    print (spielstand)
    return spielstand

def white(spielstand):
    return stig.move(spielstand)

def black(spielstand):
    return kim.move(spielstand)

def mainLoop(spielstand, zugNr):
    if zugNr % 2 == 0:
        spielstand = white(spielstand)
    else:
        spielstand = black(spielstand)
    return spielstand


def main():
    spielstand = initGame()
    finished   = False
    zugNr      = 0
    while(not finished):
        spielstand = mainLoop(spielstand, zugNr)
        zugNr += 1
        print(spielstand , zugNr)
        time.sleep(10)


if __name__ == "__main__":
    main()