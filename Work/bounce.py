# bounce.py
#
# Exercise 1.5
ball_height = 100 # Meters

for i in range(10):
    ball_height = ball_height * (3 / 5)
    print((i + 1), round(ball_height, 4))