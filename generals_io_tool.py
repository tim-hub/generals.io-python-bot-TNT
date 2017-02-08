# import math
#
# class GeneralToolBox():
#     '''This is collection of methods for the bot.
#     These method do not need to get data from update.
#     '''
#
#
#     def __init__(self, rows, cols, general_position):
#         self.rows=rows
#         self.cols=cols
#         self.general_position=general_position
#
#
#     def position_plus(self, a, b):
#         return (a[0] + b[0], a[1] + b[1])
#
#     def grid_to_index(self,y, x):
#         return y * self.cols + x
#
#     def index_to_grid(self,index):
#         return index / self.cols, index % self.cols
#
#     # def get_distance(y1,x1,y2,x2):
#     #     return math.sqrt(
#     #         math.pow(y1-y2,2)-math.pow(x1-x2,2)
#     #     )
#     def get_distance(self,position1, position2):
#         # logging.info( '%s %s' % (position1, position2))
#         # return math.sqrt(
#         #     math.pow(position1[0]-position2[0],2)+math.pow(position1[1]-position2[1],2)
#         # )
#         return math.fabs(position1[0] - position2[0]) + math.fabs(position1[1] - position2[1])
#
#     def how_far_from_general(self,position):
#         return (position, self.general_position)