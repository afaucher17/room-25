#!/usr/bin/python

from enum import Enum

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

    def __init__(self, room_type, hidden=True):
        self.room_type = room_type
        self.hidden = hidden

    def get_room_ranger(self):
        if int(self.room_type) < 3:
            return RoomDanger.neutral
        elif int(self.room_type) < 8:
            return RoomDanger.green
        elif int(self.room_type) < 12:
            return RoomDanger.yellow
        else:
            return RoomDanger.red

    def displayRoomType(self):
        print(self.room_type)

    def __str__(self):
        return '??' if self.hidden else self.ABBR[self.room_type]

    def __repr__(self):
        return self.room_type.name


