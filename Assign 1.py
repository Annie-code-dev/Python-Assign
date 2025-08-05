x = int (input("Enter an number: "))
y = int (input("Enter another number: "))
operation = input("Enter the operation (+, -, *, /): ")
results = eval(f"{x} {operation} {y}")
print (x, operation, y, "=", results)

