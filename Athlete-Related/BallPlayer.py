from Athlete import Athlete
""""
This module defines the BallPlayer class, which inherits from the Athlete class.
It represents a player in a ball sport, with attributes for team name, jersey number.
"""
class BallPlayer(Athlete):
    # Class variable to keep track of the number of ball players
    __number_of_ball_players = 0
    # Constructor for BallPlayer class
    # Initializes the player with name, age, team name, jersey number, country, salary,
    # and endorsement. Also increments the number of ball players.
    def __init__(self,name, age, team_name, jersey_number, country=None, salary=0.0,endorsement=None):
        BallPlayer.__number_of_ball_players += 1
        super().__init__(name, age, country, salary)
        self.__team_name = team_name
        self.__jersey_number = int(jersey_number)
        self.__endorsement = endorsement
        if type(self) is BallPlayer:
            print(f"Ball Player '{self.get_name()}', {self.get_age()} created; total # of BallPlayers: {BallPlayer.get_number_of_ball_players()}.")
            
    #Getter methods for the attributes
    def get_team_name(self):
        return self.__team_name
    
    def get_jersey_number(self):
        return self.__jersey_number
    
    def get_endorsement(self):
        return self.__endorsement
    
    @classmethod
    def get_number_of_ball_players(cls):
        return cls.__number_of_ball_players
    # Prints the endorsement of the player, if any.
    def print_endorsement(self):
        print(f"Player {self.get_name()} is endorsed by {self.get_endorsement()}\n")
    

    

        
