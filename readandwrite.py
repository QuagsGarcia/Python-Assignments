# Function to read and display the dataset
def read_and_display_data(file_path):
    try:
        # Opens the file in read mode
        with open(file_path, 'r') as file:
            # Reads each line in the file and split it into a list of tuples (name, age, place)
            data = [tuple(line.strip().split(',')) for line in file]

            # Sorts the data alphabetically based on names
            sorted_data = sorted(data, key=lambda x: x[0])

            # Prints column headers for the dataset
            print(f"{'Name':<25}{'Age':<25}{'Place Born'}")

            # Goes through each tuple in the sorted data
            for entry in sorted_data:
                # Displays the separator line
                print('-' * 75)

                # Ensures that the tuple has at least three values before unpacking to prevent the too many values to unpack error
                if len(entry) >= 3:
                    name, age, place = entry[:3]
                    # Displays the formatted information, replaces the spaces for better user experience, and the place only replaces the first space.
                    print(f"{name:<25}{age.replace(' ', ''):<25}{place.replace(' ', '', 1)}")
                else:
                    # error message when there arent enough values
                    print(f"Error: Tuple does not contain enough values - {entry}")

    except FileNotFoundError:
        # Prints an error message if the specified file is not found
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        # Prints a generic error message for any other exceptions
        print(f"An error occurred: {e}")

# Specifies the file path
file_path = 'info.txt'

# Calls the function to read and display the dataset
read_and_display_data(file_path)
# Used to see the final result when opening the file in python
exit = input("Press enter to exit.")