import items

class Rooms(object):
    """ Parent class that holds all of the methods that each child room
    class will inherit.
    """

    def enter_room(self,choice):
        # returns a room object using the roomExits dictionary

        return self.exits[choice]()

    def get_credits(self,choice):
        # returns the credit value of the selected room.

        return self.exits[choice]().credits

class OasisLobby(Rooms):
    """ Room class object that initializes with a name, long longDescription,
    description, and a list of items that are class objects found int items.py.
    The exits attribute holds a string to send to the user for available
    neighbor rooms and is used to match against the roomExits dict.
    """

    def __init__(self):
        super(OasisLobby,self).__init__()
        self.name = "Oasis Main Lobby"
        self.credits = 0
        self.longDescription = ("Welcome to the Oasis. Here is where you start "
            "your journey.\nThere are a few NPCs standing around but no one "
            "apears to want to interact with you.")
        self.description = "The Oasis Main Lobby."
        self.items = items.random_items()
        self.exits = {"north": OasisTransport}

class OasisTransport(Rooms):
    """ Room class object that initializes with a name, long longDescription,
    description, and a list of items that are class objects found int items.py.
    The exits attribute holds a string to send to the user for available
    neighbor rooms and is used to match against the roomExits dict.
    """

    def __init__(self):
        super(OasisTransport,self).__init__()
        self.name = "Oasis Transport"
        self.credits = 0
        self.longDescription = ("The Oasis Transport. From here you can travel "
            "to any of the 27 sectors of the Oasis.\nBut be warned, some areas "
            "require credits and others are dangerous for low-level players.")
        self.description = "The Oasis Tranport Station."
        self.items = items.random_items()
        self.exits = {"south": OasisLobby,
                      "EnderVerse": EnderVerse}


class EnderVerse(Rooms):
    """ Room class object that initializes with a name, long longDescription,
    description, and a list of items that are class objects found int items.py.
    The exits attribute holds a string to send to the user for available
    neighbor rooms and is used to match against the roomExits dict.
    """

    def __init__(self):
        super(EnderVerse,self).__init__()
        self.name = "EnderVerse Docking Station"
        self.credits = 0
        self.longDescription = ("Welcome to the EnderVerse Sector. From here you "
            "can visit many of the planets found\n within Orson Scott Cards' "
            "Universe built around the Ender's Series.")
        self.description = "EnderVerse Docking Station."
        self.items = items.random_items()
        self.exits = {"OasisTransport": OasisTransport}
