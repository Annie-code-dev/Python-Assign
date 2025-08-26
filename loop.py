for number in range(1, 10):  # Loop through numbers 1 to 9
    if number == 5:
        print("Breaking the loop at 5")
        break  # Exit the loop when number is 5
    elif number % 2 == 0:
        print(f"Skipping {number} because it's even")
        continue  # Skip the rest of the loop body for even numbers
    print(f"Processing number: {number}")
    
    #function
    squares = []
    for x in range(5):
        squares.append(x**2)
    squares = [x**2 for x in range(5)]
print(squares)