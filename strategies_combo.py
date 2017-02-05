from init_game import general
import logging
import generals
import math

logging.basicConfig(level=logging.DEBUG)

# first_update=general.get_updates()[0]
# rows=first_update['rows']
# cols=first_update['cols']
# pi=first_update['player_index']
# general_y, general_x =first_update['generals'][pi]
rows=20
cols=20
pi=0
general_y, general_x =0,0
tiles=[]
armies=[]
cities=[]

my_armies=[]


def get_distance(y1,x1,y2,x2):
    return math.sqrt(
        math.pow(y1-y2,2)-math.pow(x1-x2,2)
    )

def what_tiles_we_have(tiles, armies):
    we_have={}
    for y in range(0,len(tiles)):
        for x in range(0, len(tiles[y])):
            if tiles[y][x] ==pi:
                we_have[(y,x)]=armies[y][x]
    return we_have

def grid_to_index(y,x):
    return y*cols+x

def index_to_grid(index):
    return index/cols, index%cols


def defeat():
    pass


for update in general.get_updates():

    # get position of your general
    pi = update['player_index']
    try:
        general_y, general_x = update['generals'][pi]
    except KeyError:
        break

    rows, cols = update['rows'], update['cols']

    tiles = update['tile_grid']
    armies = update['army_grid']
    cities = update['cities']

    # move_to units from general to arbitrary square
    # for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #     if (0 <= general_y+dy < update['rows'] and 0 <= general_x+dx < update['cols']
    #             and update['tile_grid'][general_y+dy][general_x+dx] != generals.MOUNTAIN):
    #         general.move(general_y, general_x, general_y+dy, general_x+dx)
    #         # break

    # for k,v in update:
    #     print '%s : %s' %(k,v)
    # print  update
    # explore(general_y, general_x, get_radius(rows, cols))

    # print armies

    # move_to(general_y, general_x, general_y + 0, general_x + 1)
    # move_to(general_y, general_x, general_y - 0, general_x - 1)
    # move_to(general_y, general_x, general_y + 1, general_x -0)
    # move_to(general_y, general_x, general_y - 1, general_x - 0)

    if tiles[general_y+1][general_x] !=generals.MOUNTAIN and armies[general_y+1][general_x]==0:
        general.move(general_y,general_x,general_y+1,general_x)
    if tiles[general_y-1][general_x] !=generals.MOUNTAIN and armies[general_y-1][general_x]==0:
        general.move(general_y,general_x,general_y-1,general_x)
    if tiles[general_y][general_x+1] !=generals.MOUNTAIN and armies[general_y][general_x+1]==0:
        general.move(general_y,general_x,general_y,general_x+1)
    if tiles[general_y][general_x-1] !=generals.MOUNTAIN and armies[general_y][general_x-1]==0:
        general.move(general_y,general_x,general_y,general_x-1)
    print what_tiles_we_have(tiles, armies)



