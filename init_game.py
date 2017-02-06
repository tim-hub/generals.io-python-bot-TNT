#!/bin/python
from generals_io_client import generals
import logging
from config import USER_ID, USER_NAME,GAME_ID

logging.basicConfig(level=logging.DEBUG)

# 1v1
# general = generals.Generals(USER_ID, USER_NAME, '1v1')

# ffa
# general = generals.Generals('your userid', 'your username', 'ffa')

# private game
general = generals.Generals(USER_ID, USER_NAME, 'private', GAME_ID)

# print USER_ID
# print GAME_ID

# 2v2 game
# general = generals.Generals('your userid', 'your username', 'team')

