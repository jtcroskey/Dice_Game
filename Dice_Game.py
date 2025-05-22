# Single player dice game
# 
# Goal of the game is to get the highest score possible. Each turn you get three rolls. After each roll, you choose what dice you want to roll and which dice you want to hold onto. 
# After the third roll you choose what section of the scorecard you want to fill in. 
# If you don't meet the criteria for a certain section of the scorecard, you can take a zero on that section. 
# At the end of every turn (i.e. after the third dice roll in a turn) a score section must be filled in. This cannot be skipped. Each score section can only be filled in once per game. 
# Note that the positioning of the dice in slots "A","B","C","D","E" does not matter for scoring purposes.
# 
# The scorecard goes as follows:
# "ones": Minimum of three "1"s needed. Add up the value of the amount of dice you have showing "1". Example: "1","1","1","1","5" scores 4.  
# "twos": Minimum of three "2"s needed. Add up the value of the amount of dice you have showing "2". Example: "1","2","2","2","5" scores 6.
# "threes": Minimum of three "3"s needed. Add up the value of the amount of dice you have showing "3". Example: "2","3","3","3","6" scores 9.
# "fours": Minimum of three "4"s needed. Add up the value of the amount of dice you have showing "4". Example: "1","3","4","4","4" scores 12
# "fives": Minimum of three "5"s needed. Add up the value of the amount of dice you have showing "5". Example: "3","5","5","5","6" scores 15.
# "sixes": Minimum of three "6"s needed. Add up the value of the amount of dice you have showing "6". Example: "3","6","6","6","6" scores 24. 
# "three of a kind": Minimum of three dice showing the same number. Add up the value of all five dice. Example:"4","5","5","5","6" scores 25.
# "four of a kind": Minimum of four dice showing the same number. Add up the value of all five dice. Example: "3","3","3","3","5" scores 17. 
# "full house": Requires three matching dice showing the same number and two dice showing the same number (but not the same number as the three other dice). Example: "1","1","1","5","5". Always 25 points.
# "four straight": Requires four sequential dice. The fifth die doesn't matter. Example: "2","3","4","5","5". Always 30 points. 
# "five straight": Requires five sequential dice. The fifth die doesn't matter. Example: "2","3","4","5","6". Always 40 points. 
# "five of a kind": Requires all five dice to show the same number. Example: "3","3","3","3","3". Always 50 points. 
# "Wildcard": No requirements. Add up the value of all dice. Example: "1","3","3","5","5" scores 17. 
#
# If the collective value of the "ones", "twos", "threes", "fours", "fives", and "sixes" score sections add up to 63 points or higher, there is a 25 point score bonus. 
# The total score reflects the collective value of all score sections plus the bonus

#####################################################################

import random
p1 = [0]*15
p1[14] = sum(p1[0:14])
p1_status = ["unfilled"]*13

#####################################################################


def scorecard(p1,p1_status):
    print("\n")
    print("______________________________________________________________________________________________________________________________________________________________________________")
    print("|      |      |        |       |       |       |                 |                |            |               |               |                |          ||       ||       |")
    print("| ones | twos | threes | fours | fives | sixes | three of a kind | four of a kind | full house | four straight | five straight | five of a kind | wildcard || bonus || total |")
    print("|______|______|________|_______|_______|_______|_________________|________________|____________|_______________|_______________|________________|__________||_______||_______|")
    print("|      |      |        |       |       |       |                 |                |            |               |               |                |          ||       ||       |")

    #ones
    print("|  ",end="")
    if p1_status[0] == "filled":
        if p1[0] < 10:
            print(p1[0],"",end="")
        elif p1[0] >= 10:
            print(p1[0],end="")
    elif p1_status[0] == "unfilled":
        print("  ",end="")
    print("  ",end="")

    #twos
    print("|  ",end="")
    if p1_status[1] == "filled":
        if p1[1] < 10:
            print(p1[1],"",end="")
        elif p1[1] >= 10:
            print(p1[1],end="")
    elif p1_status[1] == "unfilled":
        print("  ",end="")
    print("  ",end="")

    #threes
    print("|  ",end="")
    if p1_status[2] == "filled":
        if p1[2] < 10:
            print(p1[2],"",end="")
        elif p1[2] >= 10:
            print(p1[2],end="")
    elif p1_status[2] == "unfilled":
        print("  ",end="")
    print("    ",end="")

    #fours
    print("|  ",end="")
    if p1_status[3] == "filled":
        if p1[3] < 10:
            print(p1[3],"",end="")
        elif p1[3] >= 10:
            print(p1[3],end="")
    elif p1_status[3] == "unfilled":
        print("  ",end="")
    print("   ",end="")

    #fives
    print("|  ",end="")
    if p1_status[4] == "filled":
        if p1[4] < 10:
            print(p1[4],"",end="")
        elif p1[4] >= 10:
            print(p1[4],end="")
    elif p1_status[4] == "unfilled":
        print("  ",end="")
    print("   ",end="")

    #sixes
    print("|  ",end="")
    if p1_status[5] == "filled":
        if p1[5] < 10:
            print(p1[5],"",end="")
        elif p1[5] >= 10:
            print(p1[5],end="")
    elif p1_status[5] == "unfilled":
        print("  ",end="")
    print("   ",end="")

    #three of a kind
    print("|  ",end="")
    if p1_status[6] == "filled":
        if p1[6] < 10:
            print(p1[6],"",end="")
        elif p1[6] >= 10:
            print(p1[6],end="")
    elif p1_status[6] == "unfilled":
        print("  ",end="")
    print("             ",end="")

    #four of a kind
    print("|  ",end="")
    if p1_status[7] == "filled":
        if p1[7] < 10:
            print(p1[7],"",end="")
        elif p1[7] >= 10:
            print(p1[7],end="")
    elif p1_status[7] == "unfilled":
        print("  ",end="")
    print("            ",end="")

    #full house
    print("|  ",end="")
    if p1_status[8] == "filled":
        if p1[8] < 10:
            print(p1[8],"",end="")
        elif p1[8] >= 10:
            print(p1[8],end="")
    elif p1_status[8] == "unfilled":
        print("  ",end="")
    print("        ",end="")

    #four straight
    print("|  ",end="")
    if p1_status[9] == "filled":
        if p1[9] < 10:
            print(p1[9],"",end="")
        elif p1[9] >= 10:
            print(p1[9],end="")
    elif p1_status[9] == "unfilled":
        print("  ",end="")
    print("           ",end="")

    #five straight
    print("|  ",end="")
    if p1_status[10] == "filled":
        if p1[10] < 10:
            print(p1[10],"",end="")
        elif p1[10] >= 10:
            print(p1[10],end="")
    elif p1_status[10] == "unfilled":
        print("  ",end="")
    print("           ",end="")

    #five of a kind
    print("|  ",end="")
    if p1_status[11] == "filled":
        if p1[11] < 10:
            print(p1[11],"",end="")
        elif p1[11] >= 10:
            print(p1[11],end="")
    elif p1_status[11] == "unfilled":
        print("  ",end="")
    print("            ",end="")

    #wildcard
    print("|  ",end="")
    if p1_status[12] == "filled":
        if p1[12] < 10:
            print(p1[12],"",end="")
        elif p1[12] >= 10:
            print(p1[12],end="")
    elif p1_status[12] == "unfilled":
        print("  ",end="")
    print("      ",end="")

    #bonus
    print("||  ",end="")
    if p1[13] == 0:
        print("0    ||",end="")
    elif p1[13] == 35:
        print(p1[13],"  ||",end="")

    #total
    print("  ",end="")
    if p1[14] == 0:
        print("0    |")
    elif p1[14] < 10:
        print(" ",p1[14]," |")
    elif p1[14] < 100:
        print(p1[14],"  |")
    elif p1[14] >= 100:
        print(p1[14]," |")
    print("|______|______|________|_______|_______|_______|_________________|________________|____________|_______________|_______________|________________|__________||_______||_______|")
    print("\n")

#####################################################################

def rolling():

    #first roll of turn
    D = [1,2,3,4,5,6]
    reroll = ["","","","",""]
    dice_name = ["A","B","C","D","E"]
    dice_value = [random.choice(D),random.choice(D),random.choice(D),random.choice(D),random.choice(D)]
    print("\n"*2,"Results of first roll:","\n"*2," ",dice_name[0]," ",dice_name[1]," ",dice_name[2]," ",dice_name[3]," ",dice_name[4],"\n"," ",dice_value[0]," ",dice_value[1]," ",dice_value[2]," ",dice_value[3]," ",dice_value[4])

    for counter in [0,1,2,3,4]:
        print("\n","Would you like to roll dice ",dice_name[counter]," on this roll?","\n","Enter 'y' to roll dice ",dice_name[counter]," on this roll or enter 'n' to not roll dice ",dice_name[counter]," on this roll")
        reroll[counter] = input("Player input = ")
        while reroll[counter] not in ["y","n"]:
            print("You made an invalid selection. Please try again.")
            reroll[counter] = input("Player input = ")

    #second roll of turn   
    for counter in [0,1,2,3,4]:
        if reroll[counter] == "y":
            dice_value[counter] = random.choice(D)
    print("\n"*2,"Results of second roll:","\n"*2," ",dice_name[0]," ",dice_name[1]," ",dice_name[2]," ",dice_name[3]," ",dice_name[4],"\n"," ",dice_value[0]," ",dice_value[1]," ",dice_value[2]," ",dice_value[3]," ",dice_value[4])

    for counter in [0,1,2,3,4]:
        print("\n","Would you like to roll dice ",dice_name[counter]," on this roll?","\n","Enter 'y' to roll dice ",dice_name[counter]," on this roll or enter 'n' to not roll dice ",dice_name[counter]," on this roll")
        reroll[counter] = input("Player input = ")
        while reroll[counter] not in ["y","n"]:
            print("You made an invalid selection. Please try again.")
            reroll[counter] = input("Player input = ")

    #third roll of turn      
    for counter in [0,1,2,3,4]:
        if reroll[counter] == "y":
            dice_value[counter] = random.choice(D)
    print("\n"*2,"Results of third roll:","\n"*2," ",dice_name[0]," ",dice_name[1]," ",dice_name[2]," ",dice_name[3]," ",dice_name[4],"\n"," ",dice_value[0]," ",dice_value[1]," ",dice_value[2]," ",dice_value[3]," ",dice_value[4],"\n"*2)







    #check what score the dice are theoretically worth (after last roll of turn)
    number_of_ones = 0
    number_of_twos = 0
    number_of_threes = 0
    number_of_fours = 0
    number_of_fives = 0
    number_of_sixes = 0
    p1potential = [0]*13

    #check ones
    for counter1 in [0,1,2,3,4]:
        if dice_value[counter1] == 1:
            number_of_ones = number_of_ones + 1

    if number_of_ones == 3:
        p1potential[0] = 3
    elif number_of_ones == 4:
        p1potential[0] = 4
    elif number_of_ones == 5:
        p1potential[0] = 5
    else:
        p1potential[0] = 0
        
    #check twos 
    for counter2 in [0,1,2,3,4]:
        if dice_value[counter2] == 2:
            number_of_twos = number_of_twos + 1

    if number_of_twos == 3:
        p1potential[1] = 6
    elif number_of_twos == 4:
        p1potential[1] = 8
    elif number_of_twos == 5:
        p1potential[1] = 10
    else:
        p1potential[1] = 0

    #check threes
    for counter3 in [0,1,2,3,4]:
        if dice_value[counter3] == 3:
            number_of_threes = number_of_threes + 1

    if number_of_threes == 3:
        p1potential[2] = 9
    elif number_of_threes == 4:
        p1potential[2] = 12
    elif number_of_threes == 5:
        p1potential[2] = 15
    else:
        p1potential[2] = 0

    #check fours
    for counter4 in [0,1,2,3,4]:
        if dice_value[counter4] == 4:
            number_of_fours = number_of_fours + 1

    if number_of_fours == 3:
        p1potential[3] = 12
    elif number_of_fours == 4:
        p1potential[3] = 16
    elif number_of_fours == 5:
        p1potential[3] = 20
    else:
        p1potential[3] = 0

    #check fives
    for counter5 in [0,1,2,3,4]:
        if dice_value[counter5] == 5:
            number_of_fives = number_of_fives + 1

    if number_of_fives == 3:
        p1potential[4] = 15
    elif number_of_fives == 4:
        p1potential[4] = 20
    elif number_of_fives == 5:
        p1potential[4] = 25
    else:
        p1potential[4] = 0

    #check sixes
    for counter6 in [0,1,2,3,4]:
        if dice_value[counter6] == 6:
            number_of_sixes = number_of_sixes + 1

    if number_of_sixes == 3:
        p1potential[5] = 18
    elif number_of_sixes == 4:
        p1potential[5] = 24
    elif number_of_sixes == 5:
        p1potential[5] = 30
    else:
        p1potential[5] = 0

    #check three of a kind
    if (number_of_ones >= 3) or (number_of_twos >= 3) or (number_of_threes >= 3) or (number_of_fours >= 3) or (number_of_fives >= 3) or (number_of_sixes >= 3):
        p1potential[6] = sum(dice_value)

    #check four of a kind
    if (number_of_ones >= 4) or (number_of_twos >= 4) or (number_of_threes >= 4) or (number_of_fours >= 4) or (number_of_fives >= 4) or (number_of_sixes >= 4):
        p1potential[7] = sum(dice_value)

    #check full house
    if ((number_of_ones == 3) or (number_of_twos == 3) or (number_of_threes == 3) or (number_of_fours == 3) or (number_of_fives == 3) or (number_of_sixes == 3)) and ((number_of_ones == 2) or (number_of_twos == 2) or (number_of_threes == 2) or (number_of_fours == 2) or (number_of_fives == 2) or (number_of_sixes == 2)):
        p1potential[8] = 25

    #check four straight
    for one_check in [0,1,2,3,4]:
        if dice_value[one_check] == 1:
            for two_check in [0,1,2,3,4]:
                if dice_value[two_check] == 2:
                    for three_check in [0,1,2,3,4]:
                        if dice_value[three_check] == 3:
                            for four_check in [0,1,2,3,4]:
                                if dice_value[four_check] == 4:
                                    p1potential[9] = 30

    for two_check in [0,1,2,3,4]:
        if dice_value[two_check] == 2:
            for three_check in [0,1,2,3,4]:
                if dice_value[three_check] == 3:
                    for four_check in [0,1,2,3,4]:
                        if dice_value[four_check] == 4:
                            for five_check in [0,1,2,3,4]:
                                if dice_value[five_check] == 5:
                                    p1potential[9] = 30

    for three_check in [0,1,2,3,4]:
        if dice_value[three_check] == 3:
            for four_check in [0,1,2,3,4]:
                if dice_value[four_check] == 4:
                    for five_check in [0,1,2,3,4]:
                        if dice_value[five_check] == 5:
                            for six_check in [0,1,2,3,4]:
                                if dice_value[six_check] == 6:
                                    p1potential[9] = 30                                            

    #check five straight
    for one_check in [0,1,2,3,4]:
        if dice_value[one_check] == 1:
            for two_check in [0,1,2,3,4]:
                if dice_value[two_check] == 2:
                    for three_check in [0,1,2,3,4]:
                        if dice_value[three_check] == 3:
                            for four_check in [0,1,2,3,4]:
                                if dice_value[four_check] == 4:
                                    for five_check in [0,1,2,3,4]:
                                        if dice_value[five_check] == 5:
                                            p1potential[10] = 40

    for two_check in [0,1,2,3,4]:
        if dice_value[two_check] == 2:
            for three_check in [0,1,2,3,4]:
                if dice_value[three_check] == 3:
                    for four_check in [0,1,2,3,4]:
                        if dice_value[four_check] == 4:
                            for five_check in [0,1,2,3,4]:
                                if dice_value[five_check] == 5:
                                    for six_check in [0,1,2,3,4]:
                                        if dice_value[six_check] == 6:
                                            p1potential[10] = 40

    #check five of a kind
    if (number_of_ones == 5) or (number_of_twos == 5) or (number_of_threes == 5) or (number_of_fours == 5) or (number_of_fives == 5) or (number_of_sixes == 5):
        p1potential[11] = 50

    #check wildcard
    p1potential[12] = sum(dice_value)

    #return p1potential
    return p1potential

#####################################################################

def scoring(p1potential,p1,p1_status):

    finishedscoring = "no"

    while finishedscoring == "no":

        print("What section of the scorecard would you like to fill in?")
        score_entry = input("Player input = ")

        if (score_entry == "ones") and (p1_status[0] == "unfilled"):
            p1[0] = p1potential[0]
            p1_status[0] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "twos") and (p1_status[1] == "unfilled"):
            p1[1] = p1potential[1]
            p1_status[1] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "threes") and (p1_status[2] == "unfilled"):
            p1[2] = p1potential[2]
            p1_status[2] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "fours") and (p1_status[3] == "unfilled"):
            p1[3] = p1potential[3]
            p1_status[3] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "fives") and (p1_status[4] == "unfilled"):
            p1[4] = p1potential[4]
            p1_status[4] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "sixes") and (p1_status[5] == "unfilled"):
            p1[5] = p1potential[5]
            p1_status[5] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "three of a kind") and (p1_status[6] == "unfilled"):
            p1[6] = p1potential[6]
            p1_status[6] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "four of a kind") and (p1_status[7] == "unfilled"):
            p1[7] = p1potential[7]
            p1_status[7] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "full house") and (p1_status[8] == "unfilled"):
            p1[8] = p1potential[8]
            p1_status[8] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "four straight") and (p1_status[9] == "unfilled"):
            p1[9] = p1potential[9]
            p1_status[9] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "five straight") and (p1_status[10] == "unfilled"):
            p1[10] = p1potential[10]
            p1_status[10] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "five of a kind") and (p1_status[11] == "unfilled"):
            p1[11] = p1potential[11]
            p1_status[11] = "filled"
            finishedscoring = "yes"

        elif (score_entry == "wildcard") and (p1_status[12] == "unfilled"):
            p1[12] = p1potential[12]
            p1_status[12] = "filled"
            finishedscoring = "yes"

        else:
            print("You made an invalid selection. Please try again.")

    if sum(p1[0:6]) >= 63:
        p1[13] = 35
    p1[14] = sum(p1[0:14])

    return p1, p1_status

#####################################################################

#thirteen rounds
for number_of_turns in range(1,14):
    scorecard(p1,p1_status)
    beginningofturn = input("Press 'enter' to begin turn.")
    p1potential = rolling()
    p1, p1_status = scoring(p1potential,p1,p1_status)

#end of game

scorecard(p1,p1_status)
print("\n"*2,"GAME OVER","\n"*2)

#####################################################################