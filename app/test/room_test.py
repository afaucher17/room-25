from context import complex
from complex.room import Room, RoomType, RoomEvent, RoomEventType
from complex.player import Player, PlayerStatus

import unittest

class TestRoomMethods(unittest.TestCase):
    def test_vision_chamber(self):
        test = Room(RoomType.vision_chamber)
        player = Player()
        self.assertEqual(RoomEvent(RoomEventType.vision), test.on_room_enter([], player, []))
        self.assertEqual(player.current_room, test)

    def test_control_chamber(self):
        test = Room(RoomType.control_chamber)
        player = Player()
        self.assertEqual(RoomEvent(RoomEventType.control), test.on_room_enter([], player, []))
        self.assertEqual(player.current_room, test)

    def test_moving_chamber(self):
        test = Room(RoomType.moving_chamber)
        player = Player()
        self.assertEqual(RoomEvent(RoomEventType.moving), test.on_room_enter([], player, []))
        self.assertEqual(player.current_room, test)

    def test_twin_chamber_hidden(self):
        test = Room(RoomType.twin_chamber)
        twin = Room(RoomType.twin_chamber, True)
        player = Player()
        rooms = [test, Room(RoomType.central_room), twin]
        self.assertEqual(RoomEvent(RoomEventType.no_event), test.on_room_enter(rooms, player, []))
        self.assertEqual(player.current_room, test)

    def test_twin_chamber_revealed(self):
        test = Room(RoomType.twin_chamber)
        twin = Room(RoomType.twin_chamber, False)
        player = Player()
        rooms = [test, Room(RoomType.central_room), twin]
        self.assertEqual(RoomEvent(RoomEventType.player_move, player, test, twin), test.on_room_enter(rooms, player, []))
        self.assertEqual(player.current_room, twin)

    def test_twin_chamber_revealed_another_order(self):
        test = Room(RoomType.twin_chamber)
        twin = Room(RoomType.twin_chamber, False)
        player = Player()
        rooms = [twin, Room(RoomType.central_room), test]
        self.assertEqual(RoomEvent(RoomEventType.player_move, player, test, twin), test.on_room_enter(rooms, player, []))
        self.assertEqual(player.current_room, twin)

    def test_twin_chamber_no_twin(self):
        test = Room(RoomType.twin_chamber)
        twin = Room(RoomType.twin_chamber, False)
        player = Player()
        rooms = []
        self.assertEqual(RoomEvent(RoomEventType.no_event), test.on_room_enter(rooms, player, []))
        self.assertEqual(player.current_room, test)

    def test_empty_chamber(self):
        test = Room(RoomType.empty_chamber)
        player = Player()
        self.assertEqual(RoomEvent(RoomEventType.no_event), test.on_room_enter([], player, []))
        self.assertEqual(player.current_room, test)

    def test_vortex_room(self):
        test = Room(RoomType.vortex_room)
        central = Room(RoomType.central_room)
        player = Player()
        rooms = [test, Room(RoomType.twin_chamber), central]
        self.assertEqual(RoomEvent(RoomEventType.player_move, player, test, central), test.on_room_enter(rooms, player, []))
        self.assertEqual(player.current_room, central)

    def test_prison_cell(self):
        test = Room(RoomType.prison_cell)
        player = Player()
        event = test.on_room_enter([], player, [])
        self.assertEqual(player.current_room, test)
        self.assertEqual(player.status, PlayerStatus.imprisonned)
        self.assertEqual(RoomEvent(RoomEventType.player_imprisonned, player), event)

    def test_cold_chamber(self):
        test = Room(RoomType.cold_chamber)
        player = Player()
        event = test.on_room_enter([], player, [])
        self.assertEqual(player.current_room, test)
        self.assertEqual(player.status, PlayerStatus.frozen)
        self.assertEqual(RoomEvent(RoomEventType.player_frozen, player), event)

    def test_dark_chamber(self):
        test = Room(RoomType.dark_chamber)
        player = Player()
        event = test.on_room_enter([], player, [])
        self.assertEqual(player.current_room, test)
        self.assertEqual(player.status, PlayerStatus.blind)
        self.assertEqual(RoomEvent(RoomEventType.player_blind, player), event)

    def test_trapped_chamber(self):
        test = Room(RoomType.trapped_chamber)
        player = Player()
        event = test.on_room_enter([], player, [])
        self.assertEqual(player.current_room, test)
        self.assertEqual(player.status, PlayerStatus.trapped)
        self.assertEqual(RoomEvent(RoomEventType.player_trapped, player), event)

    def test_mortal_chamber(self):
        test = Room(RoomType.mortal_chamber)
        player = Player()
        event = test.on_room_enter([], player, [])
        self.assertEqual(player.current_room, test)
        self.assertTrue(player.dead)
        self.assertEqual(RoomEvent(RoomEventType.player_death, player), event)

    def test_illusion_chamber(self):
        test = Room(RoomType.illusion_chamber)
        player = Player()
        self.assertEqual(RoomEvent(RoomEventType.illusion), test.on_room_enter([], player, []))
        self.assertEqual(player.current_room, test)

    def test_flooded_chamber(self):
        test = Room(RoomType.flooded_chamber)
        player = Player()
        event = test.on_room_enter([], player, [])
        self.assertEqual(player.current_room, test)
        self.assertTrue(test.locked)
        self.assertEqual(player.status, PlayerStatus.flooded)
        self.assertEqual(RoomEvent(RoomEventType.player_flooded, player), event)

    def test_acid_bath_solo(self):
        test = Room(RoomType.acid_bath)
        player = Player()
        event = test.on_room_enter([], player, [player])
        self.assertEqual(player.current_room, test)
        self.assertEqual(RoomEvent(RoomEventType.no_event), event)

    def test_acid_bath_multi(self):
        test = Room(RoomType.acid_bath)
        player = Player()
        event = test.on_room_enter([], player, [player, Player(), Player(), Player()])
        self.assertEqual(player.current_room, test)
        self.assertEqual(RoomEvent(RoomEventType.no_event), event)

    def test_acid_bath_two_same_room(self):
        test = Room(RoomType.acid_bath)
        player = Player()
        player2 = Player()
        players = [player, Player(), player2, Player()]
        test.on_room_enter([], player2, players)
        event = test.on_room_enter([], player, players)
        self.assertEqual(player.current_room, test)
        self.assertEqual(RoomEvent(RoomEventType.player_death, player2), event)

if __name__ == '__main__':
    unittest.main()
