from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
a = 10
for x in range(8):
    robotArm.moveRight()
for y in range(9):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == 'red':
        for z in range():
            robotArm.moveLeft
    else:
        robotArm.drop()
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()