from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
a = 1
for y in range(10):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == 'red':
        for z in range(10 - a):
            robotArm.moveRight()
        robotArm.drop()
        for e in range(9 - a):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
        a += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()