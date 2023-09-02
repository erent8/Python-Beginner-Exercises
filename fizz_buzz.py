# We ask the user to input the start and end values.
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# We use a loop to process numbers from the start value to the end value.
for number in range(start, end + 1):
    # If the number is divisible by both 3 and 5, we print "FizzBuzz."
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # If the number is only divisible by 3, we print "Fizz."
    elif number % 3 == 0:
        print("Fizz")
    # If the number is only divisible by 5, we print "Buzz."
    elif number % 5 == 0:
        print("Buzz")
    # Other numbers that don't meet the above conditions are printed directly.
    else:
        print(number)
