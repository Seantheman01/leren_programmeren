from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

robotArm. grab()
for x in range(6):
    robotArm.moveRight()
robotArm.drop()
for y in range(5):
    robotArm.moveLeft()
robotArm.grab()
for z in range(6):
    robotArm.moveRight()
robotArm.drop()
for a in range(6):
    robotArm.moveLeft()
robotArm.grab()
for b in range(6):
    robotArm.moveRight()
robotArm.drop()
for c in range(5):
    robotArm.moveLeft()
robotArm.grab()
for d in range(6):
    robotArm.moveRight()
robotArm.drop()
for e in range(6):
    robotArm.moveLeft()
robotArm.grab()
for f in range(6):
    robotArm.moveRight()
robotArm.drop()
for g in range(6):
    robotArm.moveLeft()
robotArm.grab()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()