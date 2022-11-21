from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

robotArm.moveRight()
robotArm.grab() 
for x in range(7):
    for y in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for z in range(8):
        robotArm.moveLeft()
    robotArm.grab()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()