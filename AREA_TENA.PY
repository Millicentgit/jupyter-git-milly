import math

RADIUS = 3

# calculate the circle's area
area = math.pi * math.pow(RADIUS, 2)

# rounds the area down to two decimal places
rounded_area = math.floor(area * 100) / 100

print(area)  # outputs 28.2743...
print(rounded_area)  # outputs 28.27