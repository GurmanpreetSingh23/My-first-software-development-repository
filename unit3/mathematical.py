# Program to calculate the area of a rectangle until the user wants to quit
active = True

while active: # Looping statement
    print("\n--- Area Calculator ---")
    length_input = input("Enter the length (or type 'quit' to exit): ")

    if length_input.lower() == 'quit': # Conditional statement
        active = False
    else:
        width_input = input("Enter the width: ")
        
        # Convert inputs to numbers (Mathematical Operation)
        length = float(length_input)
        width = float(width_input)
        area = length * width
        
        print(f"The area of the rectangle is: {area}")

print("Thank you for using the calculator!")