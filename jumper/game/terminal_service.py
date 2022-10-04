from colorama import Fore, Back, Style

class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    def display_list(self, a_list):
        """Gets a list and display it.

        Args: 
            self (TerminalService): An instance of TerminalService.
            draw (list): The list to display on the terminal.

        Returns:
            list: A list of objects.
        """
        for i in a_list:
            print(i)

                
    def print_in_line(self, a_list):
        """Gets a list and prints elements in the same line.

        Args: 
            self (TerminalService): An instance of TerminalService.
            puzzle (list): The list to display on the terminal.

        Returns:
            list: A list of objects.
        """
        for i in a_list:
            print(i, end=" ")
        

    def validate_answer(self, guess, word_selected, lives, parachute):
        """ Check if there are lives left and modifies the parachute.
        Args: 
            self (TerminalService): An instance of TerminalService.
            guess (str): A letter selected by the user
            word_selected(str): A random word
            lives(int): User's lives
            parachute(list): parachutes draw inside a list

        Return:
            Lives(int): Available lives.  

        """
        if lives > 0:
            if guess in word_selected:
                pass
            else:
                lives -= 1
                if lives == 0:
                    parachute[0] = '   x   '
                    self.display_list(parachute)
                    
                    print(Fore.RED + f'\nSorry, the word was: {word_selected.upper()}')
                    print(Fore.RED + '\nGame over x_x\n')
                
                else: 
                    parachute.pop(0)

        return lives        


    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)