import utils
"""This is the main module for the Athlete Management System.
It provides a command-line interface for managing athletes, including loading files,
printing statistics, deleting athletes, saving files, displaying athlete information,
and displaying charts.
"""
def main():
    # Initialize the list of athletes and a copy for updates
    # Initialize the file_modified flag to track if changes have been made
    print("Welcome to the Athlete Management System!")
    athletes = []
    updatedAthletes = []
    file_modified = False
    while True:
        print(f"1. Load File\n"
            f"2. Print Stats\n"
            f"3. Delete Athlete\n"
            f"4. Save File\n"
            f"5. Athlete Info\n"
            f"6. Display Chart\n"
            f"7. Exit\n")
        choice = input("Enter your choice: ")

        if choice == '1':
              # Load athletes from a file
              fileName = input("Enter the file name to load (e.g fileName.txt): ")
              try:
                  utils.loadFile(fileName, athletes)
                  updatedAthletes = athletes.copy()
                  print(f"File {fileName} loaded successfully.")
              except FileNotFoundError:
                  print(f"File {fileName} not found. Please try again.")
        elif choice == '2':
            # Print statistics of the athletes
            # Check if athletes list is empty before printing statistics
            if not athletes:
                print("No athletes loaded. Please load a file first.")
            else:
                utils.printStatistics(updatedAthletes)
        elif choice == '3':
            # Delete an athlete from the list
            # Check if athletes list is empty before attempting to delete
            if not athletes:
                print("No athletes loaded. Please load a file first.")
            else:
                utils.deleteAthlete(updatedAthletes)
                # Update the file and list after deletion
                file_modified = True
        elif choice == '4':
            # Save the updated athletes list to a file
            if not athletes:
                print("No athletes loaded. Please load a file first.")
            else:
                # Check if there are unsaved changes before saving
                utils.saveFile(fileName, updatedAthletes)
                file_modified = False
        elif choice == '5':
            #Check if athletes list is empty before displaying athlete info
            if not athletes:
                print("No athletes loaded. Please load a file first.")
            else:
                # Display information about the specific athlete 
                utils.athleteInfo(updatedAthletes)
        elif choice == '6':
            #Check if athletes list is empty before displaying chart
            if not athletes:
                print("No athletes loaded. Please load a file first.")
            else:
                # Display a chart of the athletes
                utils.displayChart(updatedAthletes)
        elif choice == '7':
            #if the user chooses to exit, check if there are unsaved changes
            if file_modified:
                print(f"You have some unsaved changes.")
                #Option to save changes before exiting
                utils.saveFile(fileName, updatedAthletes)
            else:
                # If no changes were made, exit the program
                print("Exiting the program.")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")


# This is the entry point of the program
# It calls the main function to start the Athlete Management System.
if __name__ == "__main__":
    main()
