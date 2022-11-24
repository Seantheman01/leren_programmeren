from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for x in range(1,5):
    for y in range(x):
        robotArm.grab()
        for a in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for b in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()