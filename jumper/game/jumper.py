class Jumper:
    """A drawing that represents the progress of the game

    Attributes:
        _lives(int): Available lifes for the game.
        _parachute(list): A list with a parachute drawing.
    """
    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (puzzle): An instance of Puzzle.
        """
        self._lives = 5
        self._parachute = ['  ___  ', ' /___\ ', ' \   / ','  \ /  ', '   o   ','  /|\  ','  / \  ',' ', '^^^^^^^'  ]

    
    def get_parachute(self):
        """Gets the parachute list.
        
        Returns: Parachute list
        """
        return self._parachute

    def get_lives(self):
        """Gets available lifes.
        
        Returns: lives(int)
        """
        return self._lives 

    def set_lives(self, lives):
        """Modify the lives attribute
        """
        self._lives=lives


