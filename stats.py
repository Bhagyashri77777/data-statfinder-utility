# A simple Data Science utility to calculate basic stats
print("--- 📊 Welcome to Neural Knights StatFinder 📊 ---")

while True:
    print("\n--- Main Menu ---")
    print("1. Calculate Data Stats (Average, Max, Min)")
    print("2. Exit the tool")
    
    choice = input("What do you want to do? (Enter 1 or 2): ")
    
    if choice == '1':
        data_input = input("Enter your numbers separated by spaces (e.g., 10 20 30): ")
        
        # Split the text into a list of words
        str_numbers = data_input.split()
        
        if len(str_numbers) == 0:
            print("No data entered! Please try again.")
            continue
            
        # Convert string numbers to real float numbers
        numbers = []
        for num in str_numbers:
            numbers.append(float(num))
            
        # Calculate the stats
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        max_val = max(numbers)
        min_val = min(numbers)
        
        print("\n--- 📈 Data Report ---")
        print("Total numbers entered :", count)
        print("Average (Mean)        :", round(average, 2))
        print("Maximum value         :", max_val)
        print("Minimum value         :", min_val)
        print("Status: Stats calculated successfully! ✅")
        
    elif choice == '2':
        print("Bye! Exiting StatFinder...")
        print("Keep coding for Google! ✨ - Built by Bhagyashri Gawali")
        break
        
    else:
        print("Wrong choice! Please enter 1 or 2.")

