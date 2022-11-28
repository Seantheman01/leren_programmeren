from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
a = 1
while True:
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur != '':
        for x in range(a):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(a):
            robotArm.moveLeft()
        a += 1
    else:
        break

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()