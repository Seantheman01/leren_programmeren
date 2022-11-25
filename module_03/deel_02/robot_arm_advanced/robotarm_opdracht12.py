from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for x in range(9):
    robotArm.grab()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()