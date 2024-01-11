# There might occur exceptions and errors while writing programs and those errors must be handled
# properly. Python provides try...except block to handle such errors.


# Errors can be broadly classified as:
# 1. Syntactic Error
# 2. Non-Syntactic Error

# Non-syntactic error can be further classified as:
# 1. ValueError
# 2. TypeError
# 3. KeyError
# 4. IndexError
# 5. ZeroDivisionError
# 6. NameError and so on


# Let's handle the errors

try:
    num = int(input("Enter a number"))
    print(num)
except:
    print("Please enter a valid number")



try:
    num = int(input("Enter a number"))
    print(num)
except ValueError:
    print("Please enter a valid number")



try:
    num = int(input("Enter a number"))
    print(num)
except (ValueError, IndexError, TypeError):
    print("Please enter a valid number")


try:
    num = int(input("Enter a number"))
    print(num)
except ValueError:
    print("Please enter a valid number")
except TypeError:
    print("TypeError")
except IndexError:
    print("IndexError")


try:
    num = int(input("Enter a number"))
except ValueError:
    print("Please enter a valid number")
else:
    print(num)


try:
    num = int(input("Enter a number"))
except ValueError:
    print("Please enter a valid number")
else:
    print(num)
finally:
    print("Finally block")

