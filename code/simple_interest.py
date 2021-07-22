def main():
    principal = read_float("Enter the principal: ")
    rate = read_float("Enter the rate of interest: ")
    time = read_integer("Enter the number of years: ")

    simple_interest = calculate_simple_interest(principal, rate, time)

    print(f"After {time} years at {rate}% interest, the investment",
        f"will be worth ${format_output(simple_interest)}")

def calculate_simple_interest(principal, rate, time):
    """Given principal, rate, and time, calculate simple interest accrual.
    
    Use formula A = P * (1 + rt), where P is principal, r is annual rate, and 
    t is interest. Parameters are P, r, and t
    """
    return round(principal * (1 + (rate / 100) * time), 2)

def format_output(number):
    """If input number is a whole number, truncate to an integer.
    
    Otherwise, round to two decimal spaces.
    """
    if number.is_integer():
        return int(number)
    else:
        return round(number, 2)

def read_float(prompt):
    """Read decimal/float from user with given prompt.
    
    Will continue to request until valid input is given. Refuses
    negative answers.
    """
    while True:
        try:
            user_input = float(input(prompt))
            if user_input < 0:
                raise ValueError
            return user_input
        except ValueError:
            print("ERROR: Please enter valid input.")

def read_integer(prompt):
    """Read decimal/float from user with given prompt.
    
    Will continue to request until valid input is given. Refuses
    negative answers.
    """
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 0:
                raise ValueError
            return user_input
        except ValueError:
            print("ERROR: Please enter valid input.")

if __name__ == "__main__":
    main()