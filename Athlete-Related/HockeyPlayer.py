from enum import Enum, auto
from Athlete import Athlete
"""
HockeyPlayer Module

This module defines the HockeyPlayer class, which inherits from the Athlete class.
It represents a player in hockey, with attributes for position, goals scored,
stick brand, and skate size.

Enum HockeyPosition
This enum defines the possible positions a hockey player can have:
- FORWARD
- DEFENSEMAN
- GOALIE
"""

class HockeyPosition(Enum):
    FORWARD = auto()
    DEFENSEMAN = auto()
    GOALIE = auto()

class HockeyPlayer(Athlete):
    # Class variable to keep track of the number of hockey players
    __number_of_hockey_players = 0
    # Constructor for HockeyPlayer class
    # Initializes the player with name, age, country, salary, position, goals scored,
    # stick brand, and skate size. Also increments the number of hockey players.
    def __init__(self, name, age, country=None, salary=0.0, position:HockeyPosition=None,goals_scored=0,stick_brand=None,skate_size=0):
        super().__init__(name, age, country, salary)
        self.__position = position
        self.__goals_scored = goals_scored
        self.__stick_brand = stick_brand
        self.__skate_size = skate_size
        type(self).__number_of_hockey_players += 1
        # Print a message indicating the creation of a new hockey player
        print(f"Hockey player '{self.get_name()}', {self.get_age()} created; total #of hockey players {HockeyPlayer.get_number_of_hockey_players()}.")
    
    #Getter methods for the attributes
    def get_position(self):
        return self.__position
    
    def get_goals_scored(self):
        return self.__goals_scored
    
    def get_stick_brand(self):
        return self.__stick_brand
    
    def get_skate_size(self):
        return self.__skate_size
    
    @classmethod
    def get_number_of_hockey_players(cls):
        return cls.__number_of_hockey_players
    
    #Prints the statistics of the hockey player, including goals scored, stick brand, and skate size.
    def print_stats(self):
        print(f"Goals Scored: {self.get_goals_scored()}\n"
              f"Stick brand: {self.get_stick_brand()}\n"
              f"Skate size: {self.get_skate_size()}\n")
        
    #String representation of the HockeyPlayer object
    # Returns a string in the format: "HockeyPlayer: name,age,country,salary,position,goals_scored,stick_brand,skate_size"
    def __str__(self):
        result = "HockeyPlayer: "
        result += self.get_name() + "," + str(self.get_age())
        # Check if country is set, if not, add a comma and keep it empty
        if self.get_country():
            result += "," + self.get_country()
        else:
            result += ","
        # Check if salary is greater than 0, if not, add a comma and keep it empty
        if self.get_salary() > 0:
            result += "," + str(self.get_salary())
        else:
            result += ","
        # Check if position is set, if not, add a comma and keep it empty
        if self.get_position():
            result += "," + self.get_position().name
        else:
            result += ","
        # Check if goals scored is greater than or equal to 0, if not, add a comma and keep it empty
        if self.get_goals_scored() >= 0:
            result += "," + str(self.get_goals_scored())
        else:
            result += ","
        # Check if stick brand is set, if not, add a comma and keep it empty
        if self.get_stick_brand():
            result += "," + self.get_stick_brand()
        else:
            result += ","
        # Check if skate size is greater than 0, if not, add a comma and keep it empty
        if self.get_skate_size() > 0:
            result += "," + str(self.get_skate_size())
        else:
            result += ""
        return result
        
    
    @staticmethod
    # Static method to parse a line of text and create a HockeyPlayer object
    def parse(line):
        # Strip whitespace from the line
        line = line.strip()
        # Remove the "HockeyPlayer: " prefix if it exists
        if line.startswith("HockeyPlayer: "):
            line = line[14:]
        # Split the line by commas and strip whitespace from each token
        tokens = [token.strip() for token in line.split(',')]
        
        name = tokens[0]
        age = int(tokens[1])
        # Check if country is set, if not, keep it None
        country = tokens[2] if len(tokens) > 2  and tokens[2] else None
        # Check if salary is set, if not, default to 0.0
        salary = float(tokens[3]) if len(tokens) > 3  and tokens[3] else 0.0
        # Check if position is set, if not, default to None
        value = tokens[4].strip().upper() if len(tokens) > 4  and tokens[4] else None
        try:
            position = HockeyPosition[value]
        except (KeyError):
            position = None
        # Check if goals scored is set, if not, default to -1
        goals_scored = int(tokens[5]) if len(tokens) > 5  and tokens[5] else -1
        # Check if stick brand is set, if not, keep it None
        stick_brand = tokens[6] if len(tokens) > 6  and tokens[6] else None
        # Check if skate size is set, if not, default to 0
        skate_size = int(tokens[7]) if len(tokens) > 7  and tokens[7] else 0
        
        # Create and return a HockeyPlayer object with the parsed values
        return HockeyPlayer(name,age,country,salary,position,goals_scored,stick_brand,skate_size)
