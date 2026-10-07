dataset = []   # Stores the user input data as a list
summary = {}   # Stores summary statistics of the dataset

def input_data():
    """Function to input data into the dataset.
    Uses global variable 'dataset' to store user input."""
    global dataset
    choice = input("Enter data for a 1D array (separated by spaces):\n")
    dataset = list(map(int, choice.split()))   # Convert input string to list of integers
    print("\nData has been stored successfully!\n")

def display_summary():
    """Function to display summary of dataset using built-in functions.
    Stores results in global 'summary' dictionary."""
    global dataset, summary
    if not dataset:   # Check if dataset is empty
        print("No data available!\n")
        return
    summary = {
        "total": len(dataset),          # Total number of elements
        "min": min(dataset),            # Minimum value
        "max": max(dataset),            # Maximum value
        "sum": sum(dataset),            # Sum of all values
        "avg": sum(dataset)/len(dataset) # Average value
    }
    # Display summary
    print("\nData Summary:")
    print(f"- Total elements: {summary['total']}")
    print(f"- Minimum value: {summary['min']}")
    print(f"- Maximum value: {summary['max']}")
    print(f"- Sum of all values: {summary['sum']}")
    print(f"- Average value: {summary['avg']:.2f}\n")

def factorial(n):
    """Recursive function to calculate factorial of a number.
    Base case: factorial(0) = factorial(1) = 1
    Recursive case: n * factorial(n-1)"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def calculate_factorial():
    """Function to take user input and calculate factorial using recursion."""
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {num} is: {factorial(num)}\n")

def filter_data():
    """Function to filter dataset using a threshold value.
    Demonstrates use of lambda function with filter()."""
    global dataset
    if not dataset:
        print("No data available!\n")
        return
    threshold = int(input("Enter a threshold value to filter out data above this value:\n"))
    filtered = list(filter(lambda x: x >= threshold, dataset))   # Keep values >= threshold
    print("\nFiltered Data (values >= threshold):")
    print(", ".join(map(str, filtered)) + "\n")

def sort_data():
    """Function to sort dataset in ascending or descending order.
    Demonstrates list.sort() method."""
    global dataset
    if not dataset:
        print("No data available!\n")
        return
    print("Choose sorting option:\n1. Ascending\n2. Descending")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        dataset.sort()   # Sort ascending
        print("\nSorted Data in Ascending Order:")
    else:
        dataset.sort(reverse=True)   # Sort descending
        print("\nSorted Data in Descending Order:")
    print(", ".join(map(str, dataset)) + "\n")

def dataset_statistics():
    """
    Function to display dataset statistics.
    Demonstrates returning multiple values (min, max, sum, average).
    """
    global dataset
    if not dataset:
        print("No data available!\n")
        return
    minimum = min(dataset)
    maximum = max(dataset)
    total = sum(dataset)
    average = total/len(dataset)
    print("\nDataset Statistics:")
    print(f"- Minimum value: {minimum}")
    print(f"- Maximum value: {maximum}")
    print(f"- Sum of all values: {total}")
    print(f"- Average value: {average:.2f}\n")

def main_menu():
    """
    Main menu function to provide options to the user.
    Runs in a loop until user chooses to exit.
    """
    while True:
        print("Welcome to the Data Analyzer and Transformer Program\n")
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("Please enter your choice: ")
        if choice == "1":
            input_data()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            calculate_factorial()
        elif choice == "4":
            filter_data()
        elif choice == "5":
            sort_data()
        elif choice == "6":
            dataset_statistics()
        elif choice == "7":
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main_menu()
