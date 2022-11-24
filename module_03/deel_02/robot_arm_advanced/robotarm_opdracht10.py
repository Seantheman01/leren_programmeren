from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
a = 9
b = 8
for x in range(5):
    robotArm.grab()
    for y in range(a):
        robotArm.moveRight()
    robotArm.drop()
    for z in range(b):
        robotArm.moveLeft()
    a -= 2
    b -= 2

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()