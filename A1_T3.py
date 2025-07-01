# A1_T3.py

def convert_to_feet_inches(height_m):
    """
    Convert height in meters to feet and inches.
    
    Parameters:
        height_m (float): Height in meters.

    Returns:
        tuple: (feet, inches) as integers
    """
    total_inches = height_m * 39.37
    feet = int(total_inches // 12)
    inches = int(round(total_inches % 12))
    return feet, inches

def parse_height_input(user_input):
    """
    Parse the height input and convert it to meters.

    Parameters:
        user_input (str): Height input string (e.g., '175 cm', '1.75 m', or '175').

    Returns:
        float: Height in meters.
    """
    parts = user_input.strip().lower().split()

    # No unit specified; assume cm
    if len(parts) == 1:
        value = float(parts[0])
        return value / 100  # cm to m

    value, unit = parts
    value = float(value)

    if unit == "m":
        return value
    elif unit == "cm":
        return value / 100
    else:
        raise ValueError("Unknown unit. Please use meters (m) or centimeters (cm).")

def main():
    user_input = input("Enter your height (e.g., '175 cm', '1.75 m', or '175'): ")

    try:
        height_m = parse_height_input(user_input)
        feet, inches = convert_to_feet_inches(height_m)
        print(f"Your height is approximately {feet}’{inches}” (US format).")
        print(f"Original input converted to meters: {height_m:.2f} m")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
