class ActionType:
    look = 1
    push = 2
    move = 3
    control = 4

class ActionPool:
    
    def __init__(self, slot_1 = None, slot_2 = None, slot_3 = None):
        self.__slot_1 = slot_1
        self.__slot_2 = slot_2
        self.__slot_3 = slot_3

    def empty_pool(self):
        self.__slot_1 = None
        self.__slot_2 = None
        self.__slot_3 = None

    def set_pool(self, slot_1, slot_2, slot_3):
        self.__slot_1 = slot_1
        self.__slot_2 = slot_2
        self.__slot_3 = slot_3
        
