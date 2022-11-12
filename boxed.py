import math

number = int(input('Enter the number of items:'))
item = int(input('Enter the number of items per box:'))

box_number = math.ceil(number/item)

print(f'For {number}items, packing {item} items in each box, you will need {box_number} boxes.')
