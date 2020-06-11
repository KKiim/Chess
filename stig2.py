import mainChess as mc 
import copy



Material = {
    'bauer':1,
    'springer':3,
    'laeufer':3,
    'turm':5,
    'dame':9,
    'koenig':10000
}

Farbe = 'w'
Counter_Color = 'b'




def move_on_board(move):
    if move['tgtpos'][0]>7 or move['tgtpos'][0]<0 or move['tgtpos'][1]>7 or move['tgtpos'][1]<0:
        check = False
    else:
        check = True
    return check

def occ_pos(spiels):
    '''Returns [[position,farbe],...].'''
    positions = []
    for figure in spiels:
        positions.append([figure['pos'],figure['farbe']])
    return positions

def spiels_after_move(move,spiels):
    fig_id = move['id']
    spielscopy = copy.deepcopy(spiels)
    for figure in spielscopy:
        if figure['id'] == fig_id:
            figure['pos'] = move['tgtpos']
    return spielscopy


def pawn_move(figure,spiels):
    moves = []
    f_pos = figure['pos']
    f_id = figure['id']
    if figure['farbe']=='w':
        k = 1
        start = 1
        counter_color = 'b'
    else:
        k = -1
        start = 6
        counter_color = 'w'
    
    move = {'id':f_id , 'type':'bauer', 'initpos':figure['pos'],'tgtpos':'init','take':False}

    move['tgtpos'] = [f_pos[0], f_pos[1]+k]
    moves.append(move.copy())

    if f_pos[1] == start:
        move['tgtpos'] = [f_pos[0], f_pos[1]+2*k]
        moves.append(move.copy())
    
    if [f_pos[0]+k,f_pos[1]+1,counter_color] in occ_pos(spiels):
        move['tgtpos'] = [f_pos[0]+k, f_pos[1]+1]
        move['take'] = True
        moves.append(move.copy())

    if [f_pos[0]+k,f_pos[1]-1,counter_color] in occ_pos(spiels):
        move['tgtpos'] = [f_pos[0]+k, f_pos[1]-1]
        move['take'] = True
        moves.append(move.copy())

    return moves



def material_count(spiels):
    summe = []
    for figure in spiels:
        if figure['farbe'] == Farbe:
            summe.append(Material[figure['type']])
        else:
            summe.append(-1*Material[figure['type']])
    count = sum(summe)
    return count

def attack_count(spiels):
    count = 0
    for figure in spiels:
        for move in pawn_move(figure,spiels):
            if [move['tgtpos'],Counter_Color] in occ_pos(spiels):
                count += 1            # hier muss noch beachtet werden, dass es besser ist eine Dame als einen Bauern anzugreifen
    return count 

def progress_count(spiels):
    summe = []
    count = 0
    for figure in spiels:
        if Farbe =='w':
            if Farbe == figure['farbe']:
                count +=1
                summe.append(figure['pos'][1])
        else:
            if Farbe == figure['farbe']:
                count +=1
                summe.append(7-figure['pos'][1])
    return sum(summe)/count 


def all_pos_spiels(spiels):
    moves = []
    spielss = []
    for figure in spiels:
        if figure['farbe']==Farbe:
            figure_moves=pawn_move(figure,spiels)
            for move in figure_moves:
                moves.append(move)
    for move in moves:
        spiels_after_m = spiels_after_move(move,spiels)
        spielss.append(copy.deepcopy(spiels_after_m))
    return spielss

    #decken
   
    #attackiert

   
    #next move?



def move(spielstand):
    counts=[]
    all_pos_s = all_pos_spiels(spielstand)
    for spiels in all_pos_s:
        count = progress_count(spiels)+attack_count(spiels)+3*material_count(spiels)
        counts.append(count)
    max_index = counts.index(max(counts))
    return all_pos_s[max_index]













