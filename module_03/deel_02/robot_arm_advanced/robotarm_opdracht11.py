from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
for x in range(9):
    robotArm.grab()
    color = robotArm.scan()
    robotArm.drop()
    robotArm.moveRight()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()   
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()