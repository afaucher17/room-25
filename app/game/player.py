#!/usr/bin/python3

from enum import Enum

try:
    from . import action
except:
    import action

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

class PlayerEventType(Enum):
    no_event = 0
    death = 1

class PlayerEvent:
    def __init__(self, player_event_type):
        self.player_event_type = player_event_type

class Player:
    'A player in the game'

    def __init__(self, position=(0, 0), type=PlayerType.prisoner, current_room=None, status=PlayerStatus, dead=False):
        self.position = position
        self.type = type
        self.action = action.ActionPool()
        self.current_room = current_room
        self.status = status
        self.trapped = True
        self.flooded = True
        self.dead = dead

    def onTurnStart(self):
        self.flooded = self.status == PlayerStatus.flooded
        return PlayerEvent(PlayerEventType.no_event)

    def onActionStart(self):
        self.trapped = self.status == PlayerStatus.trapped
        return PlayerEvent(PlayerEventType.no_event)

    def onActionEnd(self):
        if self.trapped:
            self.dead = True
            return PlayerEvent(PlayerEventType.death)
        return PlayerEvent(PlayerEventType.no_event)

    def onLastActionEnd(self):
        if self.flooded:
            self.dead = True
            return PlayerEvent(PlayerEventType.death)
        return PlayerEvent(PlayerEventType.no_event)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False
