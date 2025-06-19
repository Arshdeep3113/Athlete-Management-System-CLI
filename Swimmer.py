from Athlete import Athlete
"""Swimmer Module
This module defines the Swimmer class, which inherits from the Athlete class.
It represents a swimmer, with attributes for stroke style and personal best time."""
class Swimmer(Athlete):
    # Class variable to keep track of the number of swimmers
    __number_of_swimmers = 0
    # Constructor for Swimmer class
    # Initializes the swimmer with name, age, stroke style, country, salary,
    # and personal best time. Also increments the number of swimmers.
    def __init__(self, name, age, stroke_style, country=None, salary=0.0, personalBestTime=0.0):
        super().__init__(name, age, country, salary)
        self.__stroke_style = stroke_style
        self.__personal_best_time = float(personalBestTime)
        type(self).__number_of_swimmers += 1
        print(f"Swimmer '{self.get_name()}', {self.get_age()} created; total #of swimmers {Swimmer.get_number_of_swimmers()}.")

    # Getter methods for the attributes
    def get_stroke_style(self):
        return self.__stroke_style
    
    def get_personal_best_time(self):
        return self.__personal_best_time
    
    # Class method to get the number of swimmers
    @classmethod
    def get_number_of_swimmers(cls):
        return cls.__number_of_swimmers
    
    # Prints the statistics of the swimmer, including stroke style and personal best time.
    def print_stats(self):
        print(f"Stroke style: {self.get_stroke_style()}\n"
              f"Personal best time: {self.get_personal_best_time()}")

    def __str__(self):
        result = "Swimmer: "
        result += self.get_name() + "," + str(self.get_age()) + "," + self.get_stroke_style()
        # Add country, salary, and personal best time if they are set, else add empty fields
        if self.get_country():
            result += "," + self.get_country()
        else:
            result += ","
        if self.get_salary() > 0:
            result += "," + str(self.get_salary())
        else:
            result += ","
        if self.get_personal_best_time() > 0:
            result += "," + str(self.get_personal_best_time())
        else:
            result += ","
        return result

    @staticmethod
    # Parses a line of text to create a Swimmer object.
    def parse(line):
        # Strip whitespace from the line
        line = line.strip()
        # Remove the "Swimmer: " prefix if it exists
        if line.startswith("Swimmer: "):
            line = line[9:]
        # Split the line by commas and strip whitespace from each token
        tokens = [token.strip() for token in line.split(',')]

        name = tokens[0]
        age = int(tokens[1])
        stroke_style = tokens[2]
        # Check if country is set, if not, keep it None
        country = tokens[3] if len(tokens) > 3  and tokens[3] else None
        # Check if salary is set, if not, keep it 0.0
        salary = float(tokens[4]) if len(tokens) > 4  and tokens[4] else 0.0
        # Check if personal best time is set, if not, keep it 0.0
        personal_best_time = float(tokens[5]) if len(tokens) > 5  and tokens[5] else 0.0
        # Create and return a Swimmer object with the parsed attributes
        return Swimmer(name, age, stroke_style, country, salary, personal_best_time)
        
        





        
    
    


