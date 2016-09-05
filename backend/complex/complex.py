#!/usr/bin/python3

from room import Room, RoomType

import random
from enum import IntEnum

class ComplexType(IntEnum):
    beginner = 1
    expert_competition = 2
    expert_suspicion = 3

class Complex:
    'The complex in which the game happens. Additionally to the Central Room and Room\
    25, the complex is made of 23 rooms with various effects'

    def __init__(self, complex_type):
        self.complex_type = complex_type
        self.rooms = self.__complex_type_shuffled_rooms(complex_type)

    def __complex_type_rooms(self, complex_type):
        if self.complex_type == ComplexType.beginner:
            return [Room(RoomType.empty_chamber), Room(RoomType.empty_chamber),
                    Room(RoomType.empty_chamber), Room(RoomType.empty_chamber),
                    Room(RoomType.empty_chamber), Room(RoomType.empty_chamber),
                    Room(RoomType.empty_chamber), Room(RoomType.empty_chamber),
                    Room(RoomType.dark_chamber), Room(RoomType.dark_chamber),
                    Room(RoomType.cold_chamber), Room(RoomType.cold_chamber),
                    Room(RoomType.trapped_chamber), Room(RoomType.trapped_chamber),
                    Room(RoomType.flooded_chamber), Room(RoomType.flooded_chamber),
                    Room(RoomType.acid_bath), Room(RoomType.acid_bath),
                    Room(RoomType.vortex_chamber), Room(RoomType.vortex_chamber),
                    Room(RoomType.mortal_chamber), Room(RoomType.control_room)]
        elif self.complex_type == ComplexType.expert_competition:
            return [Room(RoomType.empty_chamber), Room(RoomType.empty_chamber),
                    Room(RoomType.empty_chamber), Room(RoomType.empty_chamber),
                    Room(RoomType.dark_chamber), Room(RoomType.dark_chamber),
                    Room(RoomType.cold_chamber), Room(RoomType.cold_chamber),
                    Room(RoomType.trapped_chamber), Room(RoomType.trapped_chamber),
                    Room(RoomType.flooded_chamber), Room(RoomType.flooded_chamber),
                    Room(RoomType.acid_bath), Room(RoomType.acid_bath),
                    Room(RoomType.twin_chamber), Room(RoomType.twin_chamber),
                    Room(RoomType.prison_chamber), Room(RoomType.prison_chamber),
                    Room(RoomType.mortal_chamber), Room(RoomType.vortex_chamber),
                    Room(RoomType.control_room), Room(RoomType.illusion_chamber)]
        else:
            return  [Room(RoomType.empty_chamber), Room(RoomType.empty_chamber),
                    Room(RoomType.empty_chamber), Room(RoomType.empty_chamber),
                    Room(RoomType.empty_chamber), Room(RoomType.empty_chamber),
                    Room(RoomType.dark_chamber), Room(RoomType.dark_chamber),
                    Room(RoomType.cold_chamber), Room(RoomType.cold_chamber),
                    Room(RoomType.trapped_chamber), Room(RoomType.trapped_chamber),
                    Room(RoomType.flooded_chamber), Room(RoomType.flooded_chamber),
                    Room(RoomType.acid_bath), Room(RoomType.acid_bath),
                    Room(RoomType.mortal_chamber), Room(RoomType.mortal_chamber),
                    Room(RoomType.vortex_chamber), Room(RoomType.control_chamber), 
                    Room(RoomType.illusion_chamber), Room(RoomType.moving_chamber)]

    def  __complex_type_shuffled_rooms(self, complex_type):
        rooms = self.__complex_type_rooms(complex_type)
        random.shuffle(rooms)
        interior = [Room(RoomType.central_room)] + random[:9]
        exterior = [Room(RoomType.vision_chamber)] + [Room(RoomType.room_25)] + random[9:22]
        random.shuffle(rooms)
        return interior + exterior

        



 
    