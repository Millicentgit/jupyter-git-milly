# A1_T2.py

def is_odd(number):
    """Check if a number is odd."""
    return number % 2 != 0

def sum_odd_numbers(num_list):
    """Sum all odd numbers in a list."""
    return sum(num for num in num_list if is_odd(num))

def main():
    # Example test list
    test_list = [1, 5, -8, 58, 85, 805, 510, -21, 4, 16]
    
    # Sum odd numbers
    result = sum_odd_numbers(test_list)
    
    # Output the result
    print(f"The sum of odd numbers in the list is {result}.")

    # Test the is_odd function
    print("\nTesting is_odd function:")
    for num in test_list:
        print(f"{num} is odd? {'Yes' if is_odd(num) else 'No'}")

if __name__ == "__main__":
    main()
