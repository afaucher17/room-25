#!/usr/bin/python3

class PlayerAction(Enum):
    look = 1
    move = 2
    push = 3
    control = 4

class PlayerType(Enum):
    prisoner = 1
    guard = 2

class PlayerStatus(Enum):
    normal = 1
    blind = 2
    trapped = 3
    prisonned = 4
    frozen = 5
    flooded = 6

class Player:
    'A player in the game'

    def __init__(self, player_position=PlayerPosition(), player_type=PlayerType.prisoner, current_room=None, player_position=(0, 0), player_status=PlayerStatus, dead=False):
        self.player_position = player_position
        self.player_type = player_type
        self.current_room = current_room
        self.player_position = player_position
        self.player_status = player_status
        self.trapped_count = 0
        self.flooded_count = 0
        sef.dead = dead



