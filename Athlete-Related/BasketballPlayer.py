from BallPlayer import BallPlayer
"""This module defines the BasketballPlayer class, which inherits from the BallPlayer class.
It represents a player in basketball, with attributes for three-point percentage and rebounds."""

class BasketballPlayer(BallPlayer):
    #Tracks the number of basketball players creared
    __number_of_basketball_players = 0
    
    # Constructor for BasketballPlayer class
    # Initializes the player with name, age, team name, jersey number, country, salary,
    # endorsement, three-point percentage, and rebounds. Also increments the number of basketball players.
    def __init__(self, name, age, team_name, jersey_number, country=None, salary=0.0, endorsement=None,three_point_pct=0.0, rebounds=0):
        super().__init__(name, age,team_name,jersey_number,country,salary,endorsement)
        self.__three_point_pct = float(three_point_pct)
        self.__rebounds = int(rebounds)
        type(self).__number_of_basketball_players += 1
        print(f"Basketball Player '{self.get_name()}', {self.get_age()} created; total # of basketball players {BasketballPlayer.get_number_of_basketball_players()}.")
    #Getter methods for the attributes
    def get_three_point_pct(self):
        return self.__three_point_pct

    def get_rebounds(self):
        return self.__rebounds
    
    @classmethod
    # Getter method for the number of basketball players
    def get_number_of_basketball_players(cls):
        return cls.__number_of_basketball_players
    # Prints the statistics of the basketball player, including three-point percentage and total rebounds.
    def print_stats(self):
        print(f"Three point percentage: {self.get_three_point_pct()}\n"
              f"Total rebounds: {self.get_rebounds()}")
    # Returns a string representation of the BasketballPlayer object.
    def __str__(self):
        result = "BasketballPlayer: "
        result += self.get_name() + "," + str(self.get_age()) + "," + self.get_team_name() + "," + str(self.get_jersey_number())
        # Add country, salary, endorsement, three-point percentage, and rebounds if they are set, else add empty fields
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
        if self.get_three_point_pct() >= 0.10:
            result += "," + str(self.get_three_point_pct())
        else:
            result += ","
        if self.get_rebounds() >= 0:
            result += "," + str(self.get_rebounds())
        else:
            result += ","
        return result
        
    @staticmethod    
    def parse(line):
        line = line.strip()

        if line.startswith("BasketballPlayer: "):
            line = line[18:]
         
        tokens = [token.strip() for token in line.split(',')]

        name = tokens[0]
        age = int(tokens[1])
        team_name = tokens[2]
        jersey_number = int(tokens[3])
        # Check if country is set, if not, keep it None
        country = tokens[4] if len(tokens) > 4  and tokens[4] else None
        # Check if salary is set, if not, keep it 0.0
        salary = float(tokens[5]) if len(tokens) > 5 and tokens[5] else 0.0
        # Check if endorsement is set, if not, keep it None
        endorsement = tokens[6] if len(tokens) > 6 and tokens[6] else None
        # Check if three-point percentage is set, if not, keep it 0.0
        three_point_pct = float(tokens[7]) if len(tokens) > 7  and tokens[7] else 0.0
        # Check if rebounds is set, if not, keep it -1
        rebounds = int(tokens[8]) if len(tokens) > 8  and tokens[8] else -1
        # Create and return a BasketballPlayer object with the parsed values
        return BasketballPlayer(name,age,team_name, jersey_number, country, salary, endorsement, three_point_pct, rebounds)



        


