import mainChess,stig,kim
import time

def initGame():
    spielstand = [
        {
            "id"  : "f0",
            "pos" : ["d","2"],
            "type": "bauer",
            "farbe": "w"
        },
        {
            "id"  : "f1",
            "pos" : ["e","2"],
            "type": "bauer",
            "farbe": "w"
        },
        {
            "id"  : "f2",
            "pos" : ["d","7"],
            "type": "bauer",
            "farbe": "b"
        },
        {
            "id"  : "f3",
            "pos" : ["e","7"],
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
    return kim.move(spielstand, 'b')

def mainLoop(spielstand, zugNr):
    if zugNr % 2 == 0:
        spielstand = white(spielstand)
    else:
        spielstand = black(spielstand)
    return spielstand


def main():
    spielstand = initGame()
    sleep = 2
    mainChess.drawSpielstand(spielstand)
    time.sleep(sleep)
    finished   = False
    zugNr      = 0
    while(not finished):
        spielstand = mainLoop(spielstand, zugNr)
        if spielstand == None:
            finished = True
            continue
        zugNr += 1
        print(zugNr)
        mainChess.drawSpielstand(spielstand)
        time.sleep(sleep)


if __name__ == "__main__":
    main()