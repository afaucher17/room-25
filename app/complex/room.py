#!/usr/bin/python3

from enum import Enum

try:
    from . import player
except:
    import player

class RoomType(Enum):
    central_room = 1
    room_25 = 2
    vision_chamber = 3
    moving_chamber = 4
    control_chamber = 5
    twin_chamber = 6
    empty_chamber = 7
    vortex_room = 8
    prison_cell = 9
    cold_chamber = 10
    dark_chamber = 11
    trapped_chamber = 12
    mortal_chamber = 13
    illusion_chamber = 14
    flooded_chamber = 15
    acid_bath = 16

class RoomDanger(Enum):
    green = 1
    yellow = 2
    red = 3
    neutral = 4

class RoomEventType(Enum):
    no_event = 0
    vision = 1
    moving = 2
    control = 3
    illusion = 4
    room_25 = 5
    player_move = 6
    player_death = 7
    player_trapped = 8
    player_imprisonned = 9
    player_flooded = 10
    player_frozen = 11
    player_blind = 12
    reveal = 13

class RoomEvent:
    def __init__(self, room_event_type=RoomEventType.no_event, player=None, start=None, destination=None):
        self.room_event_type=room_event_type
        self.player = player
        self.start = start
        self.destination = destination

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

class Room:
    'A room in the complex, they have different attributes'
    ABBR = dict([(RoomType.central_room, 'CR'), (RoomType.room_25, '25'),
        (RoomType.vision_chamber, 'VC'), (RoomType.moving_chamber, 'MC'),
        (RoomType.control_chamber, 'CC'), (RoomType.twin_chamber, 'TC'),
        (RoomType.empty_chamber, 'EC'), (RoomType.vortex_room, 'VR'),
        (RoomType.prison_cell, 'PC'), (RoomType.cold_chamber, 'CO'),
        (RoomType.dark_chamber, 'DC'), (RoomType.trapped_chamber, 'TC'),
        (RoomType.mortal_chamber, 'MC'), (RoomType.illusion_chamber, 'IC'),
        (RoomType.flooded_chamber, 'FC'), (RoomType.acid_bath, 'AB')])


    def __init__(self, room_type, hidden=True, locked=False):
        self.room_type = room_type
        self.hidden = hidden
        self.locked = locked

    def get_room_ranger(self):
        if int(self.room_type) < 3:
            return RoomDanger.neutral
        elif int(self.room_type) < 8:
            return RoomDanger.green
        elif int(self.room_type) < 12:
            return RoomDanger.yellow
        else:
            return RoomDanger.red

    def _twin_effect(self, rooms, pl, players):
        twin = next((room for room in rooms if room is not self and room.room_type == RoomType.twin_chamber and room.hidden == False), None)
        if twin == None:
            return []
        else:
            pl.current_room = twin
            return [RoomEvent(RoomEventType.player_move, pl, self, twin)]

    def _vortex_effect(self, rooms, pl, players):
        central_room = next(room for room in rooms if room.room_type == RoomType.central_room)
        pl.current_room = central_room
        return [RoomEvent(RoomEventType.player_move, pl, self, central_room)]

    def _prison_effect(self, rooms, pl, players):
        pl.status = player.PlayerStatus.imprisonned
        return [RoomEvent(RoomEventType.player_imprisonned, pl)]

    def _cold_effect(self, rooms, pl, players):
        pl.status = player.PlayerStatus.frozen
        return [RoomEvent(RoomEventType.player_frozen, pl)]

    def _blind_effect(self, rooms, pl, players):
        pl.status = player.PlayerStatus.blind
        return [RoomEvent(RoomEventType.player_blind, pl)]

    def _trapped_effect(self, rooms, pl, players):
        pl.status = player.PlayerStatus.trapped
        return [RoomEvent(RoomEventType.player_trapped, pl)]

    def _mortal_effect(self, rooms, pl, players):
        pl.dead = True
        return [RoomEvent(RoomEventType.player_death, pl)]

    def _flooded_effect(self, rooms, pl, players):
        self.locked = True
        pl.status = player.PlayerStatus.flooded
        return [RoomEvent(RoomEventType.player_flooded, pl)]

    def _acid_bath(self, rooms, pl, players):
        prevpl = next((p for p in players if p is not pl and p.current_room == self), None)
        if prevpl == None:
            return []
        prevpl.dead = True
        return [RoomEvent(RoomEventType.player_death, prevpl)]

    def _room_switch(self, rt, rooms, pl, players):
        if rt == RoomType.vision_chamber:
            return [RoomEvent(RoomEventType.vision)]
        elif rt == RoomType.moving_chamber:
            return [RoomEvent(RoomEventType.moving)]
        elif rt == RoomType.control_chamber:
            return [RoomEvent(RoomEventType.control)]
        elif rt == RoomType.twin_chamber:
            return self._twin_effect(rooms, pl, players)
        elif rt == RoomType.vortex_room:
            return self._vortex_effect(rooms, pl, players)
        elif rt == RoomType.prison_cell:
            return self._prison_effect(rooms, pl, players)
        elif rt == RoomType.cold_chamber:
            return self._cold_effect(rooms, pl, players)
        elif rt == RoomType.dark_chamber:
            return self._blind_effect(rooms, pl, players)
        elif rt == RoomType.trapped_chamber:
            return self._trapped_effect(rooms, pl, players)
        elif rt == RoomType.mortal_chamber:
            return self._mortal_effect(rooms, pl, players)
        elif rt == RoomType.illusion_chamber:
            return [RoomEvent(RoomEventType.illusion)]
        elif rt == RoomType.flooded_chamber:
            return self._flooded_effect(rooms, pl, players)
        elif rt == RoomType.acid_bath:
            return self._acid_bath(rooms, pl, players)
        else:
            return []


    def on_room_enter(self, rooms, pl, players):
        event_list = []
        if self.hidden:
            self.hidden = False
            event_list += [RoomEvent(RoomEventType.reveal)]
        pl.current_room = self
        rt = self.room_type
        return event_list + self._room_switch(rt, rooms, pl, players)

    def displayRoomType(self):
        print(self.room_type)

    def __str__(self):
        return self.ABBR[self.room_type]

    def __repr__(self):
        return self.room_type.name
