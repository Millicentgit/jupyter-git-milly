# A1_T1.py

import math

# Constant for π
PI = math.pi

def calculate_cylinder_volume(radius, height):
    """Calculate the volume of a cylinder."""
    return PI * (radius ** 2) * height

def main():
    # Get user input
    radius = float(input("Enter the radius of the cylinder (in meters): "))
    height = float(input("Enter the height of the cylinder (in meters): "))

    # Calculate volume
    volume = calculate_cylinder_volume(radius, height)

    # Output the result
    print(f"The volume of the cylinder is {volume:.3f} cubic meters.")

if __name__ == "__main__":
    main()
