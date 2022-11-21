from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for x in range(5):
    for y in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for z in range(2):
        robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()