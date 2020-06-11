import mainChess,kim
import time
import stig2

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
#    spielstand = [{'id': 'f3', 'pos': [4, 5], 'type': 'bauer', 'farbe': 'b'}, {'id': 'f0', 'pos': [3, 3], 'type': 'bauer', 'farbe': 'w'}, {'id': 'f2', 'pos': [3, 4], 'type': 'bauer', 'farbe': 'b'}, {'id': 'f1', 'pos': [4, 3], 'type': 'bauer', 'farbe': 'w'}]
#    spielstand = [{'id': 'f1', 'pos': [4, 2], 'type': 'bauer', 'farbe': 'w'}, {'id': 'f3', 'pos': [4, 5], 'type': 'bauer', 'farbe': 'b'}, {'id': 'f0', 'pos': [3, 3], 'type': 'bauer', 'farbe': 'w'}, {'id': 'f2', 'pos': [3, 4], 'type': 'bauer', 'farbe': 'b'}]
#    spielstand = [{'id': 'f0', 'pos': [3,1], 'type': 'bauer', 'farbe' : 'w'},{'id': 'f1', 'pos': [4,1], 'type': 'bauer', 'farbe' : 'w'},{'id': 'f2', 'pos': [5,1], 'type': 'bauer', 'farbe' : 'w'},{'id': 'f3', 'pos': [6,1], 'type': 'bauer', 'farbe' : 'w'},{'id': 'f4', 'pos': [3,6], 'type': 'bauer', 'farbe' : 'b'},{'id': 'f5', 'pos': [4,6], 'type': 'bauer', 'farbe' : 'b'}]
    return spielstand

def white(spielstand):
    return stig2.move(spielstand)

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
        print(spielstand)
        mainChess.drawSpielstand(spielstand)
        time.sleep(sleep)


if __name__ == "__main__":
    main()