import copy

def getSpielstandCalc(spielstand):
    col = {'a' : 0, 'b' : 1,'c' : 2, 'd' : 3,'e' : 4, 'f' : 5,'g' : 6,'h' : 7 }
    row = {'1' : 0, '2' : 1,'3' : 2, '4' : 3,'5' : 4, '6' : 5,'7' : 6,'8' : 7 }

    for figure in spielstand:
        figure['pos'][0] = col[figure['pos'][0]]
        figure['pos'][1] = row[figure['pos'][1]]

    return spielstand




def belegtePos(spielstand):
    belegtePos = []
    for figure in spielstand:
        belegtePos.append(figure['pos'])
    return belegtePos

def pawnmove(figure, spielstand):
    moves = [] # liste von figures
    belPos = belegtePos(spielstand)
    if figure['farbe'] == 'w':
        k = 1
    else:
        k = -1

    x,y = figure['pos']
    posPos = [x, y + k]
    if (posPos not in belPos):
        figureMove = copy.deepcopy(figure)
        figureMove['pos'] = posPos
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

def filterFiguresOnBoard(moves):
    """ 
    Input:
        moves ist eine Liste von FigureMoves
    Output:
        moves ist eine Liste von FigureMoves die auf dem Brett stehen
    """
    for figureMove in moves:
        for p in range(2):
            if (figureMove['pos'][p] > 7 or figureMove['pos'][p] < 0 ):
                moves.remove(figureMove)
    return moves


def filterFiguresOnFigures(moves, spielstand):
    """ 
    Input:
        moves ist eine Liste von FigureMoves
    Output:
        movesNoPunch Liste von moves ohne Schlagen
        movesPunch   Liste von moves die eine Figur Schlagen
        punched      Liste von potentiell geschlagenen Figuren
    """
    movesNoPunch = []
    movesPunch   = []
    punched      = []
    movesNotValid= []
    for figureMove in moves:
        for figure in spielstand:
            posMove = figureMove['pos']
            pos     = figure['pos']
            if (posMove == pos): # Zwei Figuren stehen auf dem gleichen Feld
                if figureMove['farbe'] != figure['farbe']:
                    movesPunch.append(figureMove)
                    punched   .append(figure)
                else:
                    movesNotValid.append(figureMove)
        if figureMove not in movesPunch and figureMove not in movesNotValid:
            movesNoPunch.append(figureMove)

    return movesNoPunch, movesPunch, punched

def drawSpielstand(spielstand):
    belPos = belegtePos(spielstand)
    for j in range(8):
        rowString = ''
        for i in range(8):
            if [i,j] in belPos:
                for figure in spielstand:
                    if figure['pos'] == [i,j]:
                        if figure['farbe'] == 'w':
                            rowString += ' B'
                        else:
                            rowString += ' b'
            elif (i + j) % 2 == 0:
                rowString += ' #'
            else:
                rowString += '  '
        print(rowString)






