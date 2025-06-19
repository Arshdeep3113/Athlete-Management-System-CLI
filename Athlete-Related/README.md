Here’s a brief description of each of the core “athlete” modules in the project:

Athlete.py
Defines the abstract base class Athlete with common attributes (name, age, country, salary) and abstract methods for printing stats and endorsements. Manages a class‐level counter of total athletes.

BallPlayer.py
Intermediate subclass of Athlete for team‐sport players. Adds team and jersey_number fields and provides default implementations of print_stats() and print_endorsement() that subclasses can override.

BasketballPlayer.py
Extends BallPlayer for basketball. Adds three_point_percentage and rebounds attributes, overrides print_stats() to display shooting and rebound metrics, and customizes endorsement messaging.

FootballPlayer.py
Extends BallPlayer for football. Adds touchdowns and passing_yards fields, overrides print_stats() to report scoring and yardage, and implements its own endorsement text.

HockeyPlayer.py
Extends BallPlayer for hockey. Adds goals_scored, stick_brand, and skate_size fields; overrides print_stats() to show goal counts and equipment info; customizes endorsements.

Swimmer.py
Subclass of Athlete for swimmers. Adds stroke_style and personal_best_time attributes, implements print_stats() to display stroke and best‐time, and provides a swim‐specific endorsement message.
