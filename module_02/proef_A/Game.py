BEGIN_VRAAG = """
You are the best trained commander of an army. You have been at war with your enemy for years, and your king is done with it. 
He sends you and a few other knights out with a letter to end the war.
Starting your journey, you have to choose 2 paths first: forest or village.
Choose wich path to go: """
PAD1_VRAAG = """
You and your team chose the forest. But in the forest they have to choose another route.
One leads to the swamp, and the other one to the elf village.
Choose wich path to go: swamp or elf village? """
SPULLEN_VRAAG = """
You enter the elf village, and the elfs greet you politely.    
They offer you some supplies for a very low price. But you don't really wanna pay.
What will you do: buy or steal? """
ELF_WINKEL_PAD = """.
You steal the supplies and run. The elfs don't like thiefs. They shoot 5 men in their leg.
You don't want to leave them, but you don't know if you can save them.
What will you do: save them (just type 'save') or continue? """
PAD2_VRAAG = """
You want to save them, but you have to continue.
Eventually you reach the lake, but you need to get across.
How will you cross the river: swim or use a log (just type 'log')? """
GROT_VRAAG = """
You and your team cut down a tree to use the log as a bridge.
You managed to get across the river using the log. On the other side, there is a cave.
You and your team enter the cave. After walking in a straight line for a while, 2 paths appear.
One path is blocked off, and the other is a dangerous looking mine.
Wich path to take: mine or blocked off area (just type 'blocked')? """
TROLL_VRAAG = """
You enter the mine, and the path is pretty dangerous.
There are a lot holes and sharp rocks to watch out for. But out of nowhere, a big troll appears.
What will you do: fight, run or yell at it (just type 'yell')? """
MINEN_VRAAG1 = """
You all start yelling at the troll. It gets scared, and runs away.
You continue the path, and come across a wall full off gold ores.
Will you mine it? (type 'yes' or 'no') """
MINEN_VRAAG2 = """
You start running from the troll. But he takes bigger steps so it catches up.
It punches 6 men, and they don't survive.
You continue the path, and come across a wall full off gold ores.
Will you mine it? (type 'yes' or 'no') """
EINDE = """
You don't have enough money. The guards won't let you in.
Then one of the guards said: 'you could give up some of your men. If you give 3 men, we will let you in.
You hesitate, but you have to give up 3 men. After a while, 3 men step forward.
The guards open the gate and let you go in.
You talk to the enemy king about peace, and that is the story of how the war ended.
>>> THE END <<<"""
BIJL_VRAAG = """
You and your team choose the village.
You enter the village, but all the villagers went silent.
You tell them you are no threat, but they still don't really trust you.
You enter the shop and they sell a very shiny, beautiful and expensive battle axe.
But the axe is a bit too expensive.
What will you do? Ask for a cheaper price (just type 'cheaper') or steal: """
REDDEN_VRAAG = """
You steal the axe and run. The villagers get really mad and out of anger they trap 3 of your men.
You want to save them but you don't know if you should.
What will you do? Save of continue: """
MUUR_VRAAG1 = """
You know you can't save them, so you just move along.
You arrive at the city wall. You walk towards it, but the gate is closed.
The guards don't really trust you yet, and are strict.
You noticed a barrel full of gunpowder in the village, but you could also just ask.
What will you do? Blow up the wall (just type 'blow up') or ask: """
MUUR_VRAAG2 = """
You ask if it can be made cheaper, but the shopkeeper tells you that the axe is the only one ever made and that they won't make it cheaper.
You say you understand and you move on.
Eventually you arive at the city wall. But the gate is closed shut.
You notice a gunpowder barrel in the village, but you can also just ask the guards, but they seem in a bad mood...
What will you do? Blow the wall up (just type 'blow up') or ask: """
ERLANGS_VRAAG = """
You ask the guards if you can get past, but they say no.
But you really have to get past.
What will you do? threaten or tell who you sent (just type 'tell'): """
BANDIETEN_VRAAG = """
The guards accept it and open the gate for you.
You get on the other side, into a big open area. And out of nowhere some bandits appear.
They tell you that they want all your stuff. But you won't just give your items to the bandits.
But you don't know if you can beat them.
What will you do? Run, fight or surrender: """
BEWAKERS_VRAAG1 = """"
You run away, but the badits shoot 5 men with their crossbows straight in the neck.
They don't survive, and you continue the path.
You walk up a hill and see the enemy castle in the distance. Waving the letter around, you walk towards it.
But at the gate stand some guards, who are not happy.
How can you be let in? Choose ask or threaten: """
BEWAKERS_VRAAG2 = """
Because you are all better trained and better equipped, you managed to defeat the bandits.
You walk up a hill and see the enemy castle in the distance. Waving the letter around, you walk towards it.
But at the gate stand some guards, who are not happy.
How can you be let in? Choose ask or threaten: """
PAD3_VRAAG = """
You mined the gold. You put it in your bags and continue the journey.
You and your team walk to the exit of the cave, and end up on the other side.
You see the enemy castle in the distance. Waving the letter around, you walk towards it.
But at the gate stand some guards, who are not happy.
How can you be let in? Choose ask or threaten: """
WEL_MINEN = """
You mined the gold. You put it in your bags and continue the journey.
You and your team walk to the exit of the cave, and end up on the other side.
You see the enemy castle in the distance. Waving the letter around, you walk towards it.
But at the gate stand some guards, who are not happy.
How can you be let in? Choose ask or threaten: """
NIET_MINEN = """
You didn't mine the gold.
You and your team walk to the exit of the cave, and end up on the other side.
You see the enemy castle in the distance. Waving the letter around, you walk towards it.
But at the gate stand some guards, who are not happy.
How can you be let in? Choose ask or threaten: """
KAN_NIET_MINEN = """
You have nothing to mine the gold with.
You and your team walk to the exit of the cave, and end up on the other side.
You see the enemy castle in the distance. Waving the letter around, you walk towards it.
But at the gate stand some guards, who are not happy.
How can you be let in? Choose ask or threaten: """
soldaten = 20
geld = 100
naam = input("""Before we start, what is your name? """)
intro = input(f"""
Hello {naam}! Here are some tips: You have 20 soldiers with you, and you start off with 100 coins. One of the first paths is harder than the other.
That is all you need to know now. 
Good luck on your journey! Are you ready (just type 'yes or no')? """)
if intro == 'no':
    print("Then why are you playing this?")
elif intro == 'yes':
    begin = input(BEGIN_VRAAG)
    if begin == 'forest':
        pad1 = input(PAD1_VRAAG)
        if pad1 == 'swamp':
            print("""
You and your team get stuck in the mud. You all start sinking slowely.
GAME OVER""")
        elif pad1 == 'elf village':
            spullen = input(SPULLEN_VRAAG)
            if spullen == 'buy':
                elf_winkel = input("""
You can buy a new shiny sword, but there is also a pickaxe on sale.
What will you buy: sword or pickaxe? """)
                if elf_winkel == 'pickaxe' or elf_winkel == 'sword':
                    betaalt = geld - 30
                    pad2 = input(f"""
You bought the {elf_winkel} for 30 coins from the shop, but you realize the rest of your team can't afford anything.
Eventually you reach the lake, but you need to get across.
How will you cross the river: swim or use a log (just type 'log')? """)
            elif spullen == 'steal':
                elf_winkel =  input(ELF_WINKEL_PAD)
                if elf_winkel == 'continue':
                    pad2 = input(PAD2_VRAAG)
                    if pad2 == 'swim':
                        print("""
You all take of your armor and try to swim across.
But the water is flowing too fast, and you all get taken bty the water.
Swimming also started to get really difficult, so you all drown.
GAME OVER""")
                    elif pad2 == 'log':
                        grot = input(GROT_VRAAG)
                        if grot == 'blocked':
                            print("""
You enter a dark and narrow cave system.
You all get lost and after walking around witch no succes, you all fall in a pit.
GAME OVER""")
                        elif grot == 'mine':
                            troll = input(TROLL_VRAAG)
                            if troll == 'fight':
                                print("""
The troll is way bigger and stronger than you.
He hits you and you fly backwards.
You don't surive the attack.
GAME OVER""")
                            elif troll == 'yell':
                                minen = input(MINEN_VRAAG1)
                            elif troll == 'run':
                                minen = input(MINEN_VRAAG2)
                                if elf_winkel == 'pickaxe' and minen == 'yes':
                                    pad3 = input(PAD3_VRAAG)
                                elif elf_winkel == 'pickaxe' and minen == 'no':
                                    pad3 = input(NIET_MINEN)
                                elif elf_winkel == 'sword' and minen == 'yes':
                                    pad3 = input(KAN_NIET_MINEN)
                                elif elf_winkel == 'sword' and minen == 'no':
                                    pad3 = input(NIET_MINEN)
                                elif elf_winkel == 'continue' and minen == 'yes':
                                    pad3 = input(WEL_MINEN)
                                elif elf_winkel == 'continue' and minen == 'no':
                                    pad3 = input(NIET_MINEN)
                                    if pad3 == 'ask' and minen == 'yes':
                                        kasteel = print("""
One of the guards sais: 'Listen up! If you have something to give us, we will let you in.
You ask them what they want, and they say that they want money. You give them the money and supplies.
You give all the money and supplies you have and they let you in.
You talk to the enemy king about peace, and that is the story of how the war ended.
>>> THE END <<<""")    
                                        if minen == 'no' or spullen == 'steal': 
                                            print("You lost a few men. You can do better!")
                                        elif troll == 'run' or (spullen == 'steal' and troll == 'run') or spullen == ('steal' and (pad3 == 'ask' and minen == 'no')) or (spullen == 'steal' and troll == 'run' and (pad3 == 'ask' and minen == 'no')):
                                            print("You lost a lot of men. You can do better!")
                                        else:
                                            print("You lost no men. Well done!") 
                                                
                                    elif pad3 == 'ask' and minen == 'no':
                                        kasteel = print(EINDE)
                                        
                                        if minen == 'no' or spullen == 'steal':
                                            print("You lost a few men. You can do better!")
                                        elif troll == 'run' or (spullen == 'steal' and troll == 'run') or (spullen == 'steal' and minen == 'no') or (troll == 'run' and minen == 'no') or (spullen == 'steal' and troll == 'run' and minen == 'no'):
                                            print("You lost a lot of men. You can do better!")
                                        else:
                                            print("You lost no men. Well done!")
                                                
                                    elif pad3 == 'threaten':
                                        print("""
You threaten the guards, and that makes them really mad.
The guards on top of the towers aim their bow and shoot.
They hit you right in the head.
GAME OVER""")

if begin == 'village':
    pad1 = input(BIJL_VRAAG)
    if pad1 == 'steal':
        redden = input(REDDEN_VRAAG)
        if redden == 'save':
            muur = print("""
You go back to save your men, but the villagers lure you in their trap.
You are now stuck and can't get out.
GAME OVER""")
        elif redden == 'continue':
            muur = input(MUUR_VRAAG1)
    elif pad1 == 'cheaper':
        muur = input(MUUR_VRAAG2)
        if muur == 'blow up':
            print("""
The wall is too strong, and the guards get very mad at you.
They shoot you straight in the neck, and you die.
GAME OVER""")
        elif muur == 'ask':
            erlangs = input(ERLANGS_VRAAG)
            if erlangs == 'tell':
                bandieten = input(BANDIETEN_VRAAG)
                if bandieten == 'surrender':
                    print("""
The bandits tie everyone up and steal your supplies.
Evryone is left behind, laying in the grass.
GAME OVER""")
                elif bandieten == 'run':
                    bewakers = input(BEWAKERS_VRAAG1)
                elif bandieten == 'fight':
                    bewakers = input(BEWAKERS_VRAAG2) 
                    if bewakers == 'ask':
                        kasteel = print("""
One of the guards sais: 'Listen up! If you have something to give us, we will let you in.
You ask them what they want, and they say that they want money. You give them the money and supplies.
You give all the money and supplies you have and they let you in.
You talk to the enemy king about peace, and that is the story of how the war ended.
>>> THE END <<<""")      
                        if pad1 == 'steal' or bandieten == 'run':
                            print("You lost a few men. You can do better!")
                        elif pad1 == 'steal' and bandieten == 'run':
                            print("You a lot of men. You can do better!")
                        else:
                            print("You lost no men. Well done!")
                                
                    elif bewakers == 'threaten':
                            print("""
You threaten the guards, and that makes them really mad.
The guards on top of the towers aim their crossbows and shoot.
They hit you right in the neck.
GAME OVER""")