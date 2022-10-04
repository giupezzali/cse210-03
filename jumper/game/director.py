from asyncore import write
from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper
from colorama import Fore, Back, Style

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The game's puzzle.
        terminal_service: For getting and displaying information on the terminal.
        guess_letter(str): A letter which is a guess from the player 
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        self.guess_letter = '' 
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Display puzzle and jumper and ask for player's guess.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.print_in_line(self._puzzle.get_puzzle())
        print(' ')
        self._terminal_service.display_list(self._jumper.get_parachute())
        self.guess_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._puzzle.validate_guess(self.guess_letter)

    def _do_updates(self):
        """Updates the parachute and points .

        Args:
            self (Director): An instance of Director.
        """    
        self._jumper.set_lives(self._terminal_service.validate_answer(self.guess_letter, self._puzzle.get_word_selected(), self._jumper.get_lives(), self._jumper.get_parachute()))
        
        
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """ 
        # self._is_playing = (self._jumper.get_lives() > 0 and self._puzzle.keep_playing())
        if self._jumper.get_lives() > 0:
            if self._puzzle.keep_playing():
                self._is_playing
            else:
                self._terminal_service.print_in_line(self._puzzle.get_puzzle())
                print()
                self._terminal_service.display_list(self._jumper.get_parachute())
                self._terminal_service.write_text(Fore.CYAN + f'\nThe word was: {self._puzzle.get_word_selected().upper()}')
                print(Fore.CYAN + '\nCongratulations, you guessed it! :D\n')
                self._is_playing = False
        else:
            self._is_playing = False
                
    
