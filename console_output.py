import os
from generals_io_client.generals import FOG,EMPTY,OBSTACLE,MOUNTAIN

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def game_output(state, ranks=None):

    #terrain /tiles
    terrain=state['tile_grid']
    tiles=state['tile_grid']
    armies=state['army_grid']
    cities=state['cities']

    # basic info
    rows=state['rows']
    cols=state['cols']
    turn=state['turn']

    # player
    pi = state['player_index']
    generals=state['generals']
    usernames=state['usernames']
    teams=state['teams']
    stars=state['stars']

    #scores
    lands=state['lands']
    soldiers=state['armies']
    alives=state['alives']

    #others
    replay_url=state['replay_url']




    clear()
    print 'Turn', turn

    title='\t'
    for x in range(0,len(tiles[0])):
        title+='%s\t' %x
    print title

    for y in range(0,len(tiles)):
        this_row='%s\t' %y
        for x in range(0, len(tiles[y])):
            tile=tiles[y][x]
            l=''
            if tile==FOG:
                l='F'
            elif tile==EMPTY:
                l=' '
            elif tile==MOUNTAIN:
                l='M'
            elif tile==OBSTACLE:
                l='O'
            elif (y,x) in cities:
                l='C'
            else:
                l='P%s' %tile



            this_row+='%s,' %l

            number = armies[y][x]
            this_row+='%s,' %number

            # for pos in ranks:
            #     if pos==(y,x):
            #         this_row+='%s,' %ranks[pos]

            this_row+='\t'

        print this_row+'\t'
        print ''




