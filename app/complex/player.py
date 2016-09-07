#!/usr/bin/python3

from enum import Enum

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
    imprisonned = 4
    frozen = 5
    flooded = 6

class Player:
    'A player in the game'

    def __init__(self, player_position=(0, 0), player_type=PlayerType.prisoner, current_room=None, status=PlayerStatus, dead=False):
        self.player_position = player_position
        self.player_type = player_type
        self.current_room = current_room
        self.status = status
        self.trapped_count = 0
        self.flooded_count = 0
        self.dead = dead

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False
