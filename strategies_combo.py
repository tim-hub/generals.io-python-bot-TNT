from init_game import general
import logging
from generals_io_client import generals
import math

logging.basicConfig(level=logging.DEBUG)

# first_update=general.get_updates()[0]
# rows=first_update['rows']
# cols=first_update['cols']
# our_flag=first_update['player_index']
# general_y, general_x =first_update['generals'][our_flag]
rows=20
cols=20
pi=0
general_y, general_x =0,0
tiles=[]
armies=[]
cities=[]


def position_plus(a,b):
    return (a[0]+b[0],a[1]+b[1])

def grid_to_index(y,x):
    return y*cols+x

def index_to_grid(index):
    return index/cols, index%cols

# def get_distance(y1,x1,y2,x2):
#     return math.sqrt(
#         math.pow(y1-y2,2)-math.pow(x1-x2,2)
#     )
def get_distance(position1,position2):

    # logging.info( '%s %s' % (position1, position2))
    # return math.sqrt(
    #     math.pow(position1[0]-position2[0],2)+math.pow(position1[1]-position2[1],2)
    # )
    return math.fabs(position1[0] - position2[0]) + math.fabs(position1[1] - position2[1])
def is_inland(y,x):

    if y+1<cols and y-1>=0 and x-1>=0 and x+1<rows \
            and tiles[y][x+1] ==pi and tiles[y][x-1]==pi \
            and tiles[y-1][x]==pi and tiles[y+1][x]==pi:
        return True;


def what_tiles_we_have(tiles, armies):
    armies_we_have={}
    tiles_we_own=[]
    borders=[]
    inlands=[]
    for y in range(0,len(tiles)):
        for x in range(0, len(tiles[y])):
            if tiles[y][x] ==pi:
                # we own this places
                armies_we_have[(y,x)]=armies[y][x]
                tiles_we_own.append((y,x))
                if is_inland(y,x):
                    inlands.append((y,x))
                else:
                    borders.append((y,x))

    return armies_we_have, tiles_we_own,borders,inlands

def empties_near(tiles_we_own):
    empties=[]
    for tile in tiles_we_own:
        y=tile[0]
        x=tile[1]
        if y+1<cols:
            if tiles[y+1][x]==-1 and (y+1,x) not in cities:
                empties.append((y+1,x))
        if y-1>0:
            if tiles[y-1][x]==-1 and(y-1,x) not in cities:
                empties.append((y-1,x))
        if x+1<rows:
            if tiles[y][x+1]==-1 and (y,x+1) not in cities:
                empties.append((y,x+1))
        if x-1>0:
            if tiles[y][x-1]==-1 and (y,x-1) not in cities:
                empties.append((y,x-1))

    return empties

def get_empties_distances(empties, general_position):



    empties_distances={}
    lowest=get_distance(empties[0],general_position)
    logging.info('distance between first empty and general is %s' %lowest)
    destination_of_lowest_distance=empties[0]
    for empty  in empties: #emptys' positions

        distance=get_distance(general_position,empty)

        if distance<lowest:
            lowest=distance
            destination_of_lowest_distance=empty


        empties_distances[empty]= distance

    return empties_distances, destination_of_lowest_distance


def which_corp_near_there( tiles_we_own, destination):

    for tile in tiles_we_own:
        # print tile

        if position_plus( tile,(1,0))==destination or position_plus(tile, (-1, 0))==destination or \
                position_plus(tile, (0, 1))==destination or position_plus(tile, (0, -1))==destination:
            return tile
    return (general_y,general_x)










def defeat():
    pass


print position_plus((1,1),(2,2))

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
    turn=update['turn']

    # move_to units from general to arbitrary square
    # for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #     if (0 <= general_y+dy < state['rows'] and 0 <= general_x+dx < state['cols']
    #             and state['tile_grid'][general_y+dy][general_x+dx] != generals.MOUNTAIN):
    #         general.move(general_y, general_x, general_y+dy, general_x+dx)
    #         break

    # for k,v in state:
    #     print '%s : %s' %(k,v)
    # print  state
    # explore(general_y, general_x, get_radius(rows, cols))

    # print armies

    # move_to(general_y, general_x, general_y + 0, general_x + 1)
    # move_to(general_y, general_x, general_y - 0, general_x - 1)
    # move_to(general_y, general_x, general_y + 1, general_x -0)
    # move_to(general_y, general_x, general_y - 1, general_x - 0)

    # if tiles[general_y+1][general_x] !=generals.MOUNTAIN and armies[general_y+1][general_x]==0:
    #     general.move(general_y,general_x,general_y+1,general_x)
    # if tiles[general_y-1][general_x] !=generals.MOUNTAIN and armies[general_y-1][general_x]==0:
    #     general.move(general_y,general_x,general_y-1,general_x)
    # if tiles[general_y][general_x+1] !=generals.MOUNTAIN and armies[general_y][general_x+1]==0:
    #     general.move(general_y,general_x,general_y,general_x+1)
    # if tiles[general_y][general_x-1] !=generals.MOUNTAIN and armies[general_y][general_x-1]==0:
    #     general.move(general_y,general_x,general_y,general_x-1)
    # print what_tiles_we_have(tiles, armies)





    armies_we_have, tiles_we_own, borders, inlands=what_tiles_we_have(tiles,armies)


    basic_turn_info='''
    Turn: %s
    Map(Tiles):
    %s
    Cities:
    %s
    Armies We Have:
    %s
    ''' %(turn, armies, cities, armies_we_have)

    print(basic_turn_info)

    empties=empties_near(tiles_we_own)
    print empties
    empties_distances, destination_of_lowest_distance=get_empties_distances(empties, (general_y, general_x))
    print empties_distances
    print  destination_of_lowest_distance
    corp=which_corp_near_there(tiles_we_own, destination_of_lowest_distance)
    print corp


    if armies_we_have[corp]>1:
        general.move(corp[0], corp[1], destination_of_lowest_distance[0], destination_of_lowest_distance[1])








