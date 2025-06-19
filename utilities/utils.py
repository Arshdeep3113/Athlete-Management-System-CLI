from Athlete import Athlete
from BallPlayer import BallPlayer
from BasketballPlayer import BasketballPlayer
from FootballPlayer import FootballPlayer
from HockeyPlayer import HockeyPlayer
from Swimmer import Swimmer
import matplotlib.pyplot as plt
"""
This module provides utility functions for managing athletes, including loading data from a file,
printing statistics, deleting athletes, saving data to a file, displaying athlete information,
and displaying charts of athlete statistics."""

def loadFile(fileName, athletes):
    # Loads athletes from a file and appends them to the athletes list.
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # Determine the type of athlete based on the line prefix and create an instance of the corresponding class.
            if line.startswith("Swimmer: "):
                athlete = Swimmer.parse(line)
            elif line.startswith("BasketballPlayer: "):
                athlete = BasketballPlayer.parse(line)
            elif line.startswith("FootballPlayer: "):
                athlete = FootballPlayer.parse(line)
            elif line.startswith("HockeyPlayer: "):
                athlete = HockeyPlayer.parse(line)
            else:
                continue

            athletes.append(athlete)

    return athletes


def printStatistics(athletes):
    # Prints statistics about the athletes, including the number of athletes by type and sport,
    # endorsements, goals scored, and touchdowns.
    #Initializes dictionaries to store endorsements, goals scored, and touchdowns.
    endorsements = {}
    goalsScored = {}
    touchdowns = {}
    # Initializes counters for different types of athletes.
    total_hockey_players = 0
    total_ball_players = 0 
    total_basketball_players = 0
    total_football_players= 0
    total_swimmers = 0
    total_athletes = len(athletes)
    # Iterates through the list of athletes and collects statistics based on their type.
    for athlete in athletes:
        if isinstance(athlete, HockeyPlayer):
            if athlete.get_goals_scored() >= 0:
                goalsScored[athlete.get_name()] = athlete.get_goals_scored()
            total_hockey_players +=1
        elif isinstance(athlete, FootballPlayer):
            if athlete.get_endorsement():
                endorsements[athlete.get_endorsement()] = endorsements.get(athlete.get_endorsement(), 0) + 1 
            if athlete.get_touchdowns() >= 0:
                touchdowns[athlete.get_name()] = athlete.get_touchdowns()
            total_football_players +=1
        elif isinstance(athlete, BasketballPlayer):
            if athlete.get_endorsement():
                endorsements[athlete.get_endorsement()] = endorsements.get(athlete.get_endorsement(), 0) + 1 
            total_basketball_players += 1
        elif isinstance(athlete, Swimmer): 
            total_swimmers += 1
    # Calculates the total number of ball players (basketball and football).
    total_ball_players = total_basketball_players + total_football_players

    # Prints the statistics.
    print(f"Statistics:\n"
          f"-------------------\n"
          f"{total_athletes} Athletes\n"
          f"{total_hockey_players} Hockey players\n"
          f"{total_ball_players} Ball players "
          f"({total_basketball_players} Basketball and {total_football_players} Football)\n"
          f"{total_swimmers} Swimmers\n")
    
    # Prints the endorsements, goals scored, and touchdowns.
    print(f"Endorsement:\n"
          f"-------------------")
    for sponsors, count in sorted(endorsements.items()):
        print(f"{sponsors} ({count})")
    # Converts the dictionaries to lists for sorting and printing.
    list_goals_scored = list(goalsScored.items())
    list_touchdowns = list(touchdowns.items())

    # Sorts the lists by name and then by goals scored or touchdowns.
    def sort_alphabetically(name):
        return name[0]
    
    def sort_by_goals(goals):
        return goals[1]
    
    def sort_by_touchdowns(td):
        return td[1]
    # Sorts the lists of goals scored and touchdowns. Then by alphabetically if there is a tie in goals or touchdowns.
    list_goals_scored.sort(key= sort_alphabetically)
    list_goals_scored.sort(key= sort_by_goals, reverse= True)

    print(f"\nGoals Scored:\n"
          f"-------------------")
    for name, goals in list_goals_scored:
        print(f"{goals} {name}")

    list_touchdowns.sort(key= sort_alphabetically)
    list_touchdowns.sort(key= sort_by_touchdowns, reverse= True)

    print(f"\nTouchdowns\n"
          f"-------------------")
    for name, td in list_touchdowns:
        print(f"{td} {name}")
    print("")


def deleteAthlete(athletes):
    # Deletes an athlete from the list based on their name.
    name = input("Enter the name you would like to delete: ")
    athlete_found = False
    for athlete in athletes:
        if athlete.get_name() == name:
            athlete_found = True
            break
    # If the athlete is found, ask for confirmation before deleting.
    if athlete_found:
        print(f"Are you sure you want to delete {name}?")
        confirmation = input("By confirming this, every mention of {name} will be removed(y/n): ")
        # If the user confirms, delete the athlete from the list.
        if confirmation == "y":
            athletes[:] = [athlete for athlete in athletes if athlete.get_name() != name]
            print(f"{name} has been deleted successfully.") 
        else:
            # If the user does not confirm, print a message and exit.
            print(f"Exiting...")
            return
    else:
        # If the athlete is not found, print a message and exit.
        print(f"The athlete name {name} is not in the list. Exiting...")   


def saveFile(file, athletes):
    # Saves the list of athletes to a file.
    confirmation = input("Do you want to save the file? (y/n): ")
    # If the user confirms, write the athletes to the file.
    # If the user does not confirm, print a message and exit.
    if confirmation.lower() == 'y' or confirmation.lower() == 'yes':
        with open(file, "w") as file:
            for athlete in athletes:
                file.write(str(athlete) + "\n")
        print(f"File saved successfully.\n")
    else:
        print(f"Exiting without saving.")
        return
    

def athleteInfo(athletes):
    # Displays information about a specific athlete based on their name.
    name = input("Enter the athletes name: ")
    found = False
    for athlete in athletes:
        # Check if the athlete's name matches the input name.
        # If it matches, print the athlete's statistics and endorsement if applicable.
        if athlete.get_name() == name:
            found = True
            if isinstance (athlete, (BasketballPlayer, FootballPlayer)):
                athlete.print_stats()
                athlete.print_endorsement()
                break
            else:
                # If the athlete is not a BallPlayer, just print the stats.
                athlete.print_stats()
                break
    if found:
        print(f"Information for {name} displayed successfully.\n")
    else:
        print(f"Name {name} not found in the list of athletes.")


def displayChart(athletes):
    #Gets the total number of athletes by type and sport.
    total_hockey_players = HockeyPlayer.get_number_of_hockey_players()
    total_ball_players = BallPlayer.get_number_of_ball_players()
    total_basketball_players = BasketballPlayer.get_number_of_basketball_players()
    total_football_players = FootballPlayer.get_number_of_football_players()
    total_swimmers = Swimmer.get_number_of_swimmers()
    total_athletes = total_hockey_players+total_ball_players+total_swimmers

    #Calculates the percentage of athletes by type and sport.
    per_of_hockey_players = (total_hockey_players/total_athletes)*100
    per_of_ball_players = (total_ball_players/total_athletes)*100
    per_of_basketball_players = (total_basketball_players/total_athletes)*100
    per_of_football_players = (total_football_players/total_athletes)*100
    per_of_swimmers = (total_swimmers/total_athletes)*100

    # Initializes variables to calculate total salaries and average salaries by type and sport.
    athlete_total_salary = 0
    hockey_player_salary = 0
    ball_player_palary = 0
    basketball_player_salary = 0
    football_player_salary = 0
    swimmer_salary = 0
    
    # Iterates through the list of athletes to calculate total salaries and average salaries by type and sport.
    for athlete in athletes:
        athlete_total_salary += athlete.get_salary()
        if isinstance(athlete, HockeyPlayer) and (athlete.get_salary() != 0.0):
            hockey_player_salary += athlete.get_salary()
        elif isinstance(athlete, BasketballPlayer) and (athlete.get_salary() != 0.0):
            basketball_player_salary += athlete.get_salary()
        elif isinstance(athlete, FootballPlayer) and (athlete.get_salary() != 0.0):
            football_player_salary += athlete.get_salary()
        elif isinstance(athlete, Swimmer) and (athlete.get_salary() != 0.0):
            swimmer_salary += athlete.get_salary()
    # Calculates the total salary for ball players (basketball and football).
    ball_player_palary = basketball_player_salary + football_player_salary

    # Calculates the average salary by type and sport. 
    # If there are no athletes of a certain type or sport, the average salary is set to 0.
    average_hockey_player_salary = hockey_player_salary / total_hockey_players if total_hockey_players > 0 else 0
    average_ball_player_salary = ball_player_palary / total_ball_players if total_ball_players > 0 else 0
    average_basketball_player_salary = basketball_player_salary / total_basketball_players if total_basketball_players > 0 else 0
    average_football_player_salary = football_player_salary / total_football_players if total_football_players > 0 else 0
    average_swimmer_salary = swimmer_salary / total_swimmers if total_swimmers > 0 else 0
    while True:
        # Displays a menu for the user to choose which chart to display.
        print(f"1. Number of athletes by type\n"
          f"2. Number of athletes by Sport\n"
          f"3. Average salary by type\n"
          f"4. Average salary by Sport\n"
          f"5. Endorsement count\n"
          f"6. Exit\n")
    
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Displays the number of athletes by type and their percentages.
            print(f"HocketyPlayers: {total_hockey_players} ({per_of_hockey_players})\n"
              f"BallPlayers: {total_ball_players} ({per_of_ball_players})\n"
              f"Swimmers: {total_swimmers} ({per_of_swimmers})\n")
            labels = ['HockeyPlayers', 'BallPlayers', 'Swimmers']
            sizes = [total_hockey_players, total_ball_players, total_swimmers]
            colors = None
            # Creates a pie chart to visualize the number of athletes by type.
            plt.pie(sizes, labels=labels,colors=colors, autopct= '%1.1f%%',startangle=90)

            plt.axis('equal')
            plt.title('Number of Athletes by Type')
            plt.show()
        elif choice == "2":
            # Displays the number of athletes by sport and their percentages.
            print(f"BasketballPlayers: {total_basketball_players} ({per_of_basketball_players})\n"
                  f"FootballPlayers: {total_football_players} ({per_of_football_players})\n"
                  f"HockeyPlayers: {total_hockey_players} ({per_of_hockey_players})\n"
                  f"Swimmers: {total_swimmers} ({per_of_swimmers})\n")
            labels = ['BasketballPlayers', 'FootballPlayers', 'HockeyPlayers', 'Swimmers']
            sizes = [total_basketball_players, total_football_players, total_hockey_players, total_swimmers]
            colors = None
            # Creates a pie chart to visualize the number of athletes by sport.
            plt.pie(sizes, labels=labels,colors=colors, autopct= '%1.1f%%',startangle=90)
            plt.axis('equal')
            plt.title('Number of Athletes by Sport')
            plt.show()
        elif choice == "3":
            # Displays the average salary by type and their values.
            print(f"HockeyPlayers: {average_hockey_player_salary:.2f}.\n"
                  f"BallPlayer: {average_ball_player_salary:.2f}\n"
                  f"Swimmers: {average_swimmer_salary:.2f}\n")
            labels = ['HockeyPlayers', 'BallPlayers', 'Swimmers']
            sizes = [average_hockey_player_salary, average_ball_player_salary, average_swimmer_salary]
            colors = None
            # Creates a pie chart to visualize the average salary by type.
            plt.pie(sizes, labels=labels,colors=colors, autopct= '%1.1f%%',startangle=90)
            plt.axis('equal')
            plt.title('Average Salary by Type')
            plt.show()
        elif choice == "4":
            # Displays the average salary by sport and their values.
            print(f"BasketballPlayers: {average_basketball_player_salary:.2f}\n"
                  f"FootballPlayers: {average_football_player_salary:.2f}\n"
                  f"HockeyPlayers: {average_hockey_player_salary:.2f}\n"
                  f"Swimmers: {average_swimmer_salary:.2f}\n")
            labels = ['BasketballPlayers', 'FootballPlayers', 'HockeyPlayers', 'Swimmers']
            sizes = [average_basketball_player_salary, average_football_player_salary, average_hockey_player_salary, average_swimmer_salary]
            colors = None
            # Creates a pie chart to visualize the average salary by sport.
            plt.pie(sizes, labels=labels,colors=colors, autopct= '%1.1f%%', startangle=90)
            plt.axis('equal')
            plt.title('Average Salary by Sport')
            plt.show()
        elif choice == "5":
            # Displays the endorsement count for ball players and their values.
            endorsements = {}
            # Iterates through the list of athletes to count endorsements for ball players.
            for athlete in athletes:
                if isinstance(athlete, (BallPlayer)) and athlete.get_endorsement():
                    endorsements[athlete.get_endorsement()] = endorsements.get(athlete.get_endorsement(), 0) + 1
            print(f"Endorsement Count:\n")
            for sponsor, count in endorsements.items():
                print(f"{sponsor}: ({count})")
            print("")
            labels = list(endorsements.keys())
            sizes = list(endorsements.values())
            colors = None
            # Creates a pie chart to visualize the endorsement count.
            plt.pie(sizes, labels=labels,colors=colors, autopct= '%1.1f%%', startangle=90)
            plt.axis('equal')
            plt.title('Endorsement Count')
            plt.show()
        elif choice == "6":
            print(f"Exiting the chart display.\n")
            break
        else:
            print(f"Invalid choice. Please try again.")

