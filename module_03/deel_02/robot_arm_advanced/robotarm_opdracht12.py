from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
a = 10
for y in range(10):
    a = a - 1
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == 'red':
        for z in range(a):
            robotArm.moveRight()
        robotArm.drop()
        for e in range(a):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()