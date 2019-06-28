

def print_odd_even(num):
    if isinstance(num, int):
        if num % 2:
            print("ODD")
        else:
            print("EVEN")
    else:
        print("Given number is not an int.")

