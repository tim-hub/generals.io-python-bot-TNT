from init_game import general
import logging
from generals_io_client import generals
import math

enermy_capital_value=1000
enermy_city_value=100
empty_city_value=50
our_city_value=10
empty_tile_value=4
enerymy_tile_value=2

logging.basicConfig(level=logging.DEBUG)

# first_update=general.get_updates()[0]
# rows=first_update['rows']
# cols=first_update['cols']
# our_flag=first_update['player_index']
# general_y, general_x =first_update['generals'][our_flag]
turn=0
rows=20
cols=20
our_flag=0

general_y, general_x =0,0
general_position=(general_y,general_x)
tiles=[]
armies=[]
cities=[]
generals_list=[]


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
    return math.fabs(position1[0]-position2[0])+math.fabs(position1[1]-position2[1])

def how_far_from_general(position):
    return (position, general_position)


# def is_inland(y,x):
#
#     if y+1<cols and y-1>=0 and x-1>=0 and x+1<rows \
#             and tiles[y][x+1] ==our_flag and tiles[y][x-1]==our_flag \
#             and tiles[y-1][x]==our_flag and tiles[y+1][x]==our_flag:
#         return True;

def get_tiles_with_priority():
    destinations_with_priority={}
    tiles_we_see=[]

    for y in range(0,len(tiles)):
        for x in range(0, len(tiles[y])):

            is_fog=tiles[y][x] ==generals.FOG
            is_obstacle=tiles[y][x]==generals.OBSTACLE
            # what tiles we can see
            if  (is_fog==False and is_obstacle==False  ):
                tiles_we_see.append((y,x))   #get what we see in the map


            # these two lines of codes will make the generals and city be remebered
            is_a_capital = (y, x) in generals_list
            is_a_city = (y, x) in cities
            is_ours = tiles[y][x] == our_flag
            is_empty = tiles[y][x] == generals.EMPTY

            have_soldiers = armies[y][x] >0

            p = get_priority_of_destination(is_a_capital, is_a_city, is_ours, is_empty, have_soldiers)

            if p > 0:
                destinations_with_priority[(y, x)] = p







                    # is_in_fog= tiles[y][x] ==generals.FOG
                    # is_obstacle = tiles[y][x] == generals.OBSTACLE

                    # how_many_armies=armies[y][x] ## only visible

                    # how_far=how_far_from_general((y,x))


    # return priorities_of_destinations
    return destinations_with_priority, rank_all_we_see(destinations_with_priority,tiles_we_see)


def get_priority_of_destination(is_a_capital, is_a_city, is_ours, is_empty, have_soldiers):
    p = 0

    if is_a_capital and  is_ours ==False : #enermies capital
        p += enermy_capital_value
    elif is_a_city:
        if  is_ours: #our city
            p+=our_city_value
        elif is_empty: # empty city
            p += empty_city_value
        else: # it belongs to enermies
            p += enermy_city_value
    elif is_empty: # empty tile
        p += empty_tile_value

    elif is_ours == False and have_soldiers: #enermy tile
        p += enerymy_tile_value

    return p

def rank_all_we_see(destinations, tiles_we_see):
    # print tiles_ranked
    tiles_we_rank={}
    for destination_position in destinations:
        priority = destinations[destination_position]


        for tile in tiles_we_see:
            distance = get_distance(destination_position, tile)

            if (tile !=generals.MOUNTAIN):
                p=get_priority_of_the_tile(priority,distance)

                if tile in destinations:
                    p=priority

                if tile in tiles_we_rank:
                    tiles_we_rank[tile]+=p
                else:
                    tiles_we_rank[tile] = p





    return tiles_we_rank


def get_priority_of_the_tile(priority, distance ):
    # print priority
    # print distance
    # print cols+rows
    # print cols
    p=(-math.log(distance+1, cols+rows)+1)*priority # 0: +infinate, cols:0, 1:1
    # print  p
    return float ("{0:.3f}".format(p))


# def what_tiles_we_see():
#     tiles_we_see = []
#     for y in range(0,len(tiles)):
#         for x in range(0, len(tiles[y])):
#             if  ((tiles[y][x] !=generals.FOG and tiles[y][x]!=generals.OBSTACLE ) ):
#                 tiles_we_see.append((y,x))   #get what we see in the map
#     return tiles_we_see


def what_tiles_we_have():
    armies_we_have={}
    tiles_we_own=[]
    borders=[]
    inlands=[]
    for y in range(0,len(tiles)):
        for x in range(0, len(tiles[y])):
            if tiles[y][x] ==our_flag:
                # we own this places
                armies_we_have[(y,x)]=armies[y][x]
                tiles_we_own.append((y,x))
                # if is_inland(y,x):
                #     inlands.append((y,x))
                # else:
                #     borders.append((y,x))

    return armies_we_have, tiles_we_own,borders,inlands






for state in general.get_updates():

    # get position of your general
    our_flag = state['player_index']
    try:
        general_y, general_x = state['generals'][our_flag]
    except KeyError:
        break

    rows, cols = state['rows'], state['cols']

    turn = state['turn']
    tiles = state['tile_grid']
    armies = state['army_grid']
    cities = state['cities']
    generals_list = state['generals']

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





    armies_we_have, tiles_we_own, borders, inlands = what_tiles_we_have()




    # print(basic_turn_info)

    # empties=empties_near(tiles_we_own, tiles)
    # print empties
    # empties_distances, destination_of_lowest_distance=get_empties_distances(empties, (general_y, general_x))
    # print empties_distances
    # print  destination_of_lowest_distance
    # corp=which_corp_near_there(tiles_we_own, destination_of_lowest_distance)
    # print corp
    #
    #
    # if armies_we_have[corp]>1:
    #     general.move(corp[0], corp[1], destination_of_lowest_distance[0], destination_of_lowest_distance[1])

    destinations,tiles_ranked = get_tiles_with_priority()
    starts = armies_we_have

    we_can={}
    best_priority=0

    best_move=((general_position),general_position+(1,0))

    for destination_position in tiles_ranked:
        priority = tiles_ranked[destination_position]
        for corp_position in starts:
            number=starts[corp_position]
            # print (destination_position,corp_position)
            if tiles[destination_position[0]][destination_position[1]] !=generals.MOUNTAIN and \
                            get_distance(destination_position,corp_position) <=1 and number>1 and \
                            number>armies[destination_position[0]][destination_position[1]]:

                # first and not necessary



                we_can[corp_position, destination_position]=priority
                if priority>best_priority:
                    best_priority=priority
                    best_move=(corp_position, destination_position)




    from console_output import game_output
    game_output(state, ranks=tiles_ranked)

    print best_move, best_priority
    print destinations
    print tiles_ranked
    des=best_move[1]
    corp = best_move[0]

    general.move(corp[0], corp[1], des[0], des[1])








