from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
a = 0
while a < 10:
    robotArm.grab()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()