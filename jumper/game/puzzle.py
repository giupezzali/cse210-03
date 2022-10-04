import random
from select import select

class Puzzle:
    """ A group of letters that form a secret word.
    The responsibiliy of a puzzle is to display a secret word, represented as underscores and replace with a word when the user guesses.
    
    Attributes:
        _word_list (list[str]): A list of words
        _word_selected (str): A random word from the list of words
        _puzzle (list[str]): A list of underscores 
    """

    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (puzzle): An instance of Puzzle.
        """
        self._word_list = ['capybara', 'platypus', 'parallelepiped', 'onomatopoeia', 'otorhinolaryngologist', 'temperature']
        self._word_selected = random.choice(self._word_list)
        self._puzzle = (['_ '] * len(self._word_selected))
        
        

    def get_puzzle(self):
        """Gets the puzzle.
        
        Returns: Puzzle list
        """
        return self._puzzle
        
    def get_word_selected(self):
        """Gets the word randomly selected.
        
        Returns: A randoom word
        """
        return self._word_selected

    def validate_guess(self, guess_letter):
        """Validates if the user's guessing is part of the word
        
        Args: 
        guess_letter(str): A user's guess
        """
        for i, l in enumerate(self._word_selected):
            if l == guess_letter.lower():
                self._puzzle[i] = l
                
    def keep_playing(self):
        """whether the player keeps playing
        Return: Boolean
        """
        s_puzzle = "".join(self._puzzle)
        return self._word_selected != s_puzzle





