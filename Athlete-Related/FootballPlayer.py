from BallPlayer import BallPlayer
"""
This module defines the FootballPlayer class, which inherits from the BallPlayer class.
It represents a player in football, with attributes for touchdowns and passing yards."""
class FootballPlayer(BallPlayer):
    # Class variable to keep track of the number of football players
    __number_of_football_players = 0
    # Constructor for FootballPlayer class
    # Initializes the player with name, age, team name, jersey number, country, salary,
    # endorsement, touchdowns, and passing yards. Also increments the number of football players.
    def __init__(self, name, age, team_name, jersey_number, country=None, salary=0.0, endorsement=None, touchdowns=0, passing_yards=0):
        super().__init__(name, age, team_name, jersey_number, country, salary, endorsement)
        self.__touchdowns = int(touchdowns)
        self.__passing_yards = int(passing_yards)
        type(self).__number_of_football_players += 1
        print(f"Football player '{self.get_name()}', {self.get_age()} created; total #of football players {FootballPlayer.get_number_of_football_players()}.")
    #Getter methods for the attributes
    def get_touchdowns(self):
        return self.__touchdowns
    
    def get_passing_yards(self):
        return self.__passing_yards
    
    @classmethod
    def get_number_of_football_players(cls):
        return cls.__number_of_football_players
    
    # Prints the statistics of the football player, including touchdowns and passing yards.
    def print_stats(self):
        print(f"Total touchdowns: {self.get_touchdowns()}\nTotal passing yards: {self.get_passing_yards()}")
    
    # Returns a string representation of the FootballPlayer object.
    def __str__(self):
        result = "FootballPlayer: "
        result += self.get_name() + "," + str(self.get_age()) + "," + self.get_team_name() + "," + str(self.get_jersey_number())
        # Add country, salary, endorsement, touchdowns, and passing yards if they are set, else add empty fields
        if self.get_country():
            result += "," + self.get_country()
        else:
            result += ","
        if self.get_salary() > 0:
            result += "," + str(self.get_salary())
        else:
            result += ","
        if self.get_endorsement():
            result += "," + self.get_endorsement()
        else:
            result += ","
        if self.get_touchdowns() >= 0:
            result += "," + str(self.get_touchdowns())
        else:
            result += ","
        if self.get_passing_yards() != 0:
            result += "," + str(self.get_passing_yards())
        else:
            result += ","
        return result
    
    @staticmethod
    def parse(line):
        #Remove whitespace from the line
        line = line.strip()
        #Remove the "FootballPlayer: " prefix if it exists
        if line.startswith("FootballPlayer: "):
            line = line[16:]
        
        #Split the line by commas and strip whitespace from each token
        tokens = [token.strip() for token in line.split(',')]
        name = tokens[0]
        age = int(tokens[1])
        team_name = tokens[2]
        jersey_number = int(tokens[3])
        # Check if country is set, if not, keep it None
        country = tokens[4] if len(tokens) > 4 and tokens[4] else None
        # Check if salary is set, if not, keep it 0.0
        salary = float(tokens[5]) if len(tokens) > 5  and tokens[5] else 0.0
        # Check if endorsement is set, if not, keep it None
        endorsement = tokens[6] if len(tokens) > 6  and tokens[6] else None
        # Check if touchdowns is set, if not, keep it -1
        touchdowns = int(tokens[7]) if len(tokens) > 7  and tokens[7] else -1
        # Check if passing yards is set, if not, keep it 0
        passing_yards = int(tokens[8]) if len(tokens) > 8  and tokens[8] else 0
        # Create and return a FootballPlayer object with the parsed attributes
        return FootballPlayer(name,age,team_name,jersey_number,country,salary,endorsement,touchdowns,passing_yards)
