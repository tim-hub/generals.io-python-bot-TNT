# Generalsio

Python client for interacting with the multiplayer web game [generals.io](http://generals.io). It can be used to build bots to play the game in an automated fashion.


## Setup

    pip install -r requirements.txt


## Example usage

    import generals


    # 1v1 on north america server
    g = generals.Generals('your userid', 'your username', '1v1')

    # ffa on eu server
    # g = generals.Generals('your userid', 'your username', 'ffa', region='eu')

    # private game
    # g = generals.Generals('your userid', 'your username', 'private', 'your gameid')

    # 2v2 game
    # g = generals.Generals('your userid', 'your username', 'team')

    for update in g.get_updates():

        # get position of your general
        pi = update['player_index']
        y, x = update['generals'][pi]

        # move units from general to arbitrary square
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (0 <= y+dy < update['rows'] and 0 <= x+dx < update['cols']
                    and update['tile_grid'][y+dy][x+dx] != generals.MOUNTAIN):
                g.move(y, x, y+dy, x+dx)
                break

