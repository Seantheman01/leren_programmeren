from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for x in range(8):
    robotArm.moveRight()
for y in range(9):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
        
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()