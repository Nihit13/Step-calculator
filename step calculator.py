print("step calculator")
pi = 3.14
distance = float(input("distance to be covered :"))
diameter = float(input("The diameter of the wheel:"))
step_angle = float(input("The step angle:"))
circumference = diameter * pi
total_revolutions = distance/circumference
steps_in_one_revolution = 360/step_angle
total_steps = steps_in_one_revolution * total_revolutions
print("The bot would take",total_steps,"steps")