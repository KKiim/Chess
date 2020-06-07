import mainChess,stig,kim
import time

def initGame():
    spielstand = [    
        {
            "id"  : "f0",
            "pos" : ["b","2"],
            "type": "bauer",
            "farbe": "w"
        },
        {
            "id"  : "f1",
            "pos" : ["a","7"],
            "type": "bauer",
            "farbe": "b"
        },
        {
            "id"  : "f2",
            "pos" : ["c","3"],
            "type": "bauer",
            "farbe": "b"
        }
    ]
    print (spielstand)
    spielstand = mainChess.getSpielstandCalc(spielstand)
    return spielstand

def white(spielstand):
    return stig.move(spielstand)

def black(spielstand):
    return kim.move(spielstand,'b')

def mainLoop(spielstand, zugNr):
    if zugNr % 2 == 0:
        spielstand = white(spielstand)
    else:
        spielstand = black(spielstand)
    return spielstand


def main():
    spielstand = initGame()
    mainChess.drawSpielstand(spielstand)
    time.sleep(10)
    finished   = False
    zugNr      = 0
    while(not finished):
        spielstand = mainLoop(spielstand, zugNr)
        zugNr += 1
        print(zugNr)
        mainChess.drawSpielstand(spielstand)
        time.sleep(10)


if __name__ == "__main__":
    main()