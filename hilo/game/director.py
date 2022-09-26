from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        current_card = First card value
        next_card = A second card value
        score (int): The score for the entire game.
        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.current_card = 0
        self.next_card = 0
        self.score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.do_updates()
            self.do_outputs()
            self.get_inputs()
            

    def get_inputs(self):
        """Asks the player if they want to keep playing.

        Args:
            self (Director): An instance of Director.
        """
        if self.score > 0:
            keep_playing = input("Keep Playing? [y/n] ")
            self.is_playing = ( keep_playing == "y")
        else:
            self.is_playing = False

    def do_updates(self):
        """Ask if the next card is higher or lower. Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        card = Card()
        card.random_card()

        if card.current_card == card.next_card:
            card.random_card()
        
        self.current_card = card.current_card
        self.next_card = card.next_card

        print(f'The current card is: {self.current_card}')
        guess = input('Higher or lower? [h/l] ')
        
        if guess == 'h' and self.next_card > self.current_card:
            self.score += 100
        elif guess == 'l' and self.current_card > self.next_card:
            self.score += 100

        else:
            self.score -= 75
        
        

    def do_outputs(self):
        """Displays the second card and the score. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        

        print(f"Next card was: {self.next_card}")
        print(f"Your score is: {self.score}\n")
        self.is_playing = (self.score > 0)
            