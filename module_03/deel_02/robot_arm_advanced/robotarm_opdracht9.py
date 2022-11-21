from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

robotArm. grab()
for x in range(6):
    robotArm.moveRight()
robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()