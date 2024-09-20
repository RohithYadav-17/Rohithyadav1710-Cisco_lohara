def find_quotient(d,n):
    if n==0:
        raise ZeroDivisionError()
    return d/n

try:
    number = int(input("Enter a number "))
    result = find_quotient(10,number)

except ValueError:
    print("Invalid input! please enter a valid input")

except ZeroDivisionError:
    print("You can not divide by zero")

else:
    print(result)

finally:
    print("Cleaning UP")
print("End of a program")
