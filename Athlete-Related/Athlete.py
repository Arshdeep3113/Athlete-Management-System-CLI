class Athlete:
    """Athlete Module
    This module defines the Athlete class, which serves as a base class for all athletes.
    It contains common attributes and methods that all athletes share, such as name, age,
    country, and salary."""
    __number_of_athletes = 0
    # Class variable to keep track of the number of athletes 
    # Constructor for Athlete class
    def __init__(self, name, age, country=None, salary=0.0):
        Athlete.__number_of_athletes += 1
        self.__name = name
        self.__age = age
        self.__country = country
        self.__salary = salary
        if type(self) is Athlete:
            print(f"Athlete '{self.get_name()}', age {self.get_age()} created; total # of athletes: {Athlete.get_number_of_athletes()}.")
    
    # Getter methods for the attributes
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_country(self):
        return self.__country
    
    def get_salary(self):
        return self.__salary
    
    # Getter method for the number of athletes
    @classmethod
    def get_number_of_athletes(cls):
        return cls.__number_of_athletes
    # Method to print the statistics of the athlete, lets subclasses implement their own statistics.
    def print_stats(self):
        raise NotImplementedError("Subclasses must implement print_endorsement()")
    # Method to print the endorsement of the athlete, lets subclasses implement their own endorsement.
    def print_endorsement(self):
        raise NotImplementedError("Subclasses must implement print_endorsement()")
    
    def __str__(self):
        return f"Athlete: {self.get_name()}, {self.get_age()}, {self.get_country()}, {self.get_salary()}\n"

