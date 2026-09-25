# Functional Treat Project
# Data Analyzer and Transformer Program

dataset = []   # Global dataset
summary = {}   # Global summary dictionary

def input_data():
    global dataset
    choice = input("Enter data for a 1D array (separated by spaces):\n")
    dataset = list(map(int, choice.split()))
    print("\nData has been stored successfully!\n")

def display_summary():
    global dataset, summary
    if not dataset:
        print("No data available!\n")
        return
    summary = {
        "total": len(dataset),
        "min": min(dataset),
        "max": max(dataset),
        "sum": sum(dataset),
        "avg": sum(dataset)/len(dataset)
    }
    print("\nData Summary:")
    print(f"- Total elements: {summary['total']}")
    print(f"- Minimum value: {summary['min']}")
    print(f"- Maximum value: {summary['max']}")
    print(f"- Sum of all values: {summary['sum']}")
    print(f"- Average value: {summary['avg']:.2f}\n")

def factorial(n):
    """Recursive factorial function"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def calculate_factorial():
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {num} is: {factorial(num)}\n")

def filter_data():
    global dataset
    if not dataset:
        print("No data available!\n")
        return
    threshold = int(input("Enter a threshold value to filter out data above this value:\n"))
    filtered = list(filter(lambda x: x >= threshold, dataset))
    print("\nFiltered Data (values >= threshold):")
    print(", ".join(map(str, filtered)) + "\n")

def sort_data():
    global dataset
    if not dataset:
        print("No data available!\n")
        return
    print("Choose sorting option:\n1. Ascending\n2. Descending")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        dataset.sort()
        print("\nSorted Data in Ascending Order:")
    else:
        dataset.sort(reverse=True)
        print("\nSorted Data in Descending Order:")
    print(", ".join(map(str, dataset)) + "\n")

def dataset_statistics():
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

# Run the program
if __name__ == "__main__":
    main_menu() 
