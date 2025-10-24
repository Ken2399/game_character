class GameCharacter:
    """Playable character in a video game.
    """
    
    def __init__(self,name):
        """ Initializing a game character.
        Attributes:
            name(str): character's name.
            inventory(dict): character's inventory (resource: resource level)
        """
        self.name = name
        self.inventory = {}