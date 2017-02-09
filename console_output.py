import os
from generals_io_client.generals import FOG,EMPTY,OBSTACLE,MOUNTAIN

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def output(state, **kwargs):
    clear()
    #terrain /tiles
    terrain=state['tile_grid']
    armies=state['army_grid']
    pi=state['player_index']


