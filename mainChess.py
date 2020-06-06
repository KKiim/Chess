import copy

def getSpielstandCalc(spielstand):
    col = {'a' : 0, 'b' : 1,'c' : 2, 'd' : 3,'e' : 4, 'f' : 5,'g' : 6,'h' : 7 }
    row = {'1' : 0, '2' : 1,'3' : 2, '4' : 3,'5' : 4, '6' : 5,'7' : 6,'8' : 7 }

    for figure in spielstand:
        figure['pos'][0] = col[figure['pos'][0]]
        figure['pos'][1] = row[figure['pos'][1]]

    return spielstand

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
spielstand =  getSpielstandCalc(spielstand)



def belegtePos(spielstand):
    belegtePos = []
    for figure in spielstand:
        belegtePos.append(figure['pos'])
    return belegtePos

def pawnmove(figure):
    moves = [] # liste von figures
    belPos = belegtePos(spielstand)
    if figure['farbe'] == 'w':
        k = 1
    else:
        k = -1

    figureMove = copy.deepcopy(figure)
    figureMove['pos'][1] = figure['pos'][1] + k
    moves.append(figureMove)
    if figure['pos'][1] == 1:
        figureMove = copy.deepcopy(figure)
        figureMove['pos'][1] = figure['pos'][1] + 2 * k
        moves.append(figureMove)
    #neufigure = [figure['pos'][0] + 1, figure['pos'][1] + 1]
    posPos  = [figure['pos'][0] + k, figure['pos'][1] + k]
    posPos2 = [figure['pos'][0] - k, figure['pos'][1] + k]

    if posPos in belPos:
        figureMove = copy.deepcopy(figure)
        figureMove['pos'] = posPos
        moves.append(figureMove)

    if posPos2 in belPos:
        figureMove = copy.deepcopy(figure)
        figureMove['pos'] = posPos2
        moves.append(figureMove)
        
    return moves


def move(spielstand):
    spielstandCalc = getSpielstandCalc(spielstand)

 #   pawnmove(figure)

    return spielstand




