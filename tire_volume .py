import math
from datetime import datetime

width = float(input('Enter the width of the tire in mm (ex 205):'))
ar = float(input('Enter the aspect ratio of the tire (ex 60):'))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15):'))
date = datetime.now()

Volume = (math.pi *width**2 *ar * (width * ar + 2540 * diameter)) / 10000000000

if Volume < 30:
    price = 10
elif Volume == 30:
    price = 15
else:
    price = 20

print(f'The approximate volume is {Volume:.2f} liters, and the price is {price}')
answer = input('Do you want to buy this tire?')

if answer == 'yes':
    phone = input('What is you phone number?')
    with open("volume.text", "at") as volume_file:
        print(f"{date:%Y-%m-%d},{width},{ar},{diameter},{Volume:.2f},{price},{phone}", file=volume_file)
else:
    print('Okay,Thank you!')


