from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
x = 0
while x > 0:
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == 'white' or kleur == 'red' or kleur == 'blue' or kleur == 'green' or kleur == 'yellow':
        robotArm.moveRight()
        robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()