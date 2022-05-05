    # All Finance Menu Function

# IMPORT UNIVERSAL UTILITIES
from universe.classes import PTc,warDataBase,NATIONS,friendship,warAssets,techAssets,gameTracker,initializeObjects,techEras,techEraBonus,techEraCost,PTcHistory,dialogue,printDialogue

import sys
import time
import copy
import random

"""

TO DO 

MVP
1. Drill troops Increases might by random small amount
DRILL INCREASE MIGHTINCREASE = RANDOM * LEVEL

ONCE POLITICS IS DONE 

2. Combat Manevres increases might and political will
3. Buy assets (need money and political will)


ONCE TECH IS DONE 

1. Tech level unlocks more items 


"""

# rather than match on index, will match on term
# a Submitted order will change to pending, or an existing .
# pending order will be updated with new wait count.
def updateMoveArray(currentNation,matchingTerm,adjustedMove):
    moves = currentNation.Nextmoves.split(':')
    x = 0
    moveArray = ""
    # item1 is the command for the move i.e. 'gainresearch'
    for item in moves:
        if matchingTerm in item:
            moveArray += adjustedMove + ":"
        else:
            moveArray += item + ":"
        x+=1 
    return(moveArray)


# Takes the build order placed by currentNation
# Awards the unit
# Awards might proportional to mightvalue x totalMight X 1/2 the number of units ordered
# This scales the more you buy and type you buy

def drill(nextMove,currentNation,myWar,nextMoveIndex,flag,db):
    nextMove =  nextMove.split(',')
    move      = nextMove[0]
    branch    = nextMove[1]
    intensity = nextMove[2]
    units     = nextMove[3:]
    might     = int(currentNation.might)
    credits   = int(currentNation.wealth)



    printRow = printDialogue(flag,str(str('### ' + str(currentNation.country) + ' chose to train their ' + str(branch))),db)
    printRow = printDialogue(flag,str(str('Intensity: ' + str(intensity) )),db)
    
    

    # RETURN UNITS
    if branch == 'Light Units':
        myWar.wOneAmount = int(units[0])
        myWar.wTwoAmount  = int(units[1])
    if branch == 'Core Division':
        myWar.wThreeAmount = int(units[0])
        myWar.wFourAmount  = int(units[1])
        myWar.wFiveAmount  = int(units[2])
    if branch == 'Heavy Forces':
        myWar.wSixAmount = int(units[0])
        myWar.wSevenAmount  = int(units[1])



    if intensity == 'soft':
        bonusMight = round((random.randint(1,8) / 100) * might)
        currentNation.might += bonusMight
        printRow = printDialogue(flag,str(str('Might gained    : ' + str(bonusMight))),db)
        printRow = printDialogue(flag,str(str('New Might Total : ' + str(currentNation.might))),db)
        db.session.commit()
        return(0,'soft complete')

    if intensity == 'medium':

        # WIN MIGTH
        bonusMight = round((random.randint(8,14) / 100) * might)
        currentNation.might +=  bonusMight
        # WIN CREDITS
        bonusCredits = round((random.randint(1,5) / 100) * credits)
        currentNation.wealth +=   bonusCredits

        printRow = printDialogue(flag,str(str(str(currentNation.country) + ' impressed the top leadership and won financial backing.')),db)
        printRow = printDialogue(flag,str('Credits gained    : ' + str(bonusCredits) ),db)
        
        

        # LOSE A PORTION OF UNITS 
        lossProbability = random.randint(0,8)
        lossAmount = 0.25
        flag = 'True'
        if lossProbability == 3:
            # RETURN UNITS
            if branch == 'Light Units':
                myWar.wOneAmount    = round(int(units[0]) * (random.randint(0,25)/100))
                myWar.wTwoAmount    = round(int(units[1]) * (random.randint(0,25)/100))
            if branch == 'Core Division':
                myWar.wThreeAmount  = round(int(units[0]) * (random.randint(0,25)/100))
                myWar.wFourAmount   = round(int(units[1]) * (random.randint(0,25)/100))
                myWar.wFiveAmount   = round(int(units[2]) * (random.randint(0,25)/100))
            if branch == 'Heavy Forces':
                myWar.wSixAmount    = round(int(units[1]) * (random.randint(0,25)/100))
                myWar.wSevenAmount  = round(int(units[2]) * (random.randint(0,25)/100))
            printRow = printDialogue(flag,str(str('**Units lost** Accidents in training drill has resulted in losses.')),db)
            db.session.commit()

        printRow = printDialogue(flag,str('Might gained    : ' + str(bonusMight)),db)
        printRow = printDialogue(flag,str(str('New Might Total : ' + str(currentNation.might))),db)
        
        db.session.commit()
        return(0,'medium complete')

    if intensity == 'hard':

        # WIN MIGTH
        bonusMight = round((random.randint(14,20) / 100) * might)
        currentNation.might +=  bonusMight
        # WIN CREDITS
        bonusCredits = round((random.randint(5,10) / 100) * credits)
        currentNation.wealth +=   bonusCredits

        printRow = printDialogue(flag,str(str(str(currentNation.country) + ' impressed the top leadership and won financial backing.')),db)
        printRow = printDialogue(flag,str(str('Credits gained    : ' + str(bonusCredits))),db)
        
        # LOSE A PORTION OF UNITS 
        lossProbability = random.randint(0,8)
        flag = 'True'
        if lossProbability == 3:
            # RETURN UNITS
            if branch == 'Light Units':
                myWar.wOneAmount    = round(int(units[0]) * (random.randint(0,40)/100))
                myWar.wTwoAmount    = round(int(units[1]) * (random.randint(0,40)/100))
            if branch == 'Core Division':
                myWar.wThreeAmount  = round(int(units[0]) * (random.randint(0,40)/100))
                myWar.wFourAmount   = round(int(units[1]) * (random.randint(0,40)/100))
                myWar.wFiveAmount   = round(int(units[2]) * (random.randint(0,40)/100))
            if branch == 'Heavy Forces':
                myWar.wSixAmount    = round(int(units[1]) * (random.randint(0,40)/100))
                myWar.wSevenAmount  = round(int(units[2]) * (random.randint(0,40)/100))
            printRow = printDialogue(flag,str(str('**Units lost** Accidents in training drill has resulted in losses.')),db)
            db.session.commit()

        printRow = printDialogue(flag,str(str('Might gained    : ' + str(bonusMight))),db)
        printRow = printDialogue(flag,str(str('New Might Total : ' + str(currentNation.might))),db)
        
        db.session.commit()
        return(0,'medium complete')

    return(0,'Complete')


def build(nextMove,currentNation,myWar,nextMoveIndex,flag,db):
    print(nextMove)
    nextMove =  nextMove.split(',')
    pending    = nextMove[0]
    job        = nextMove[1]
    name       = nextMove[2]
    amount     = int(nextMove[3])
    wait       = int(nextMove[4])
    bonusMight = int(float(nextMove[5]))
    warKey     = nextMove[6]
    moveIndex = nextMoveIndex # Get position in country array



    # IF NOT YET READY
    # DECREMENT BUILD TIME 
    if wait > 1:
        wait = wait -1

        printRow = printDialogue(flag,str(str('### ' + str(currentNation.country) + ' chose to build ')),db)
        printRow = printDialogue(flag,str(str(str(name) + ' to build : ' + str(amount))),db)
        printRow = printDialogue(flag,str(str('Build Time Remaining : ' + str(wait))),db)

        # Find index nextmoves and update it
        nextMove = str('pending' + ',' + 'WeaponsBuild' + ',' + str(name) + ',' +  str(amount) + ',' +  str(wait) + ',' +  str(bonusMight) + ',' +  str(warKey) + ':')
        moveArray = updateMoveArray(currentNation,'WeaponsBuild',nextMove)
        currentNation.Nextmoves = moveArray
        db.session.commit()
        return(0,'success')

    #IF READY (currently at 2 cus lazy)
    if wait <= 1:
        # Reward Unit
        stockOwned = int(getattr(myWar, warKey))
        setattr(myWar, warKey, (stockOwned + amount))
        stockOwned = int(getattr(myWar, warKey))
        
        # Reward Mightg
        bonusAdjustment = round((currentNation.might * bonusMight) * (amount/2))
        if bonusAdjustment < 1: bonusAdjustment  = 1
        currentNation.might += bonusAdjustment
        
        printRow = printDialogue(flag,str(str('### ' + str(currentNation.country) + ' Build complete ')),db)
        printRow = printDialogue(flag,str(str(str(name) + ' units built: ' + str(amount))),db)
        printRow = printDialogue(flag,str(str(str(name) + ' total : ' + str(stockOwned))),db)
        printRow = printDialogue(flag,str(str('Might gained : ' + str(bonusAdjustment))),db)
        printRow = printDialogue(flag,str(str('Might total  : ' + str(currentNation.might))),db)


        # Clear out existing array element
        moveArray = updateMoveArray(currentNation,'WeaponsBuild'," ")
        currentNation.Nextmoves = moveArray

        db.session.commit()
        return(0,'success')

    return(0,'success')


# Takes the scrap order placed by currentNation
# Awards money
# Deducts might proportional to mightvalue x totalMight x 1/5 the number of units scrapped

def scrap(nextMove,currentNation,myWar,nextMoveIndex,flag,db):
    nextMove =  nextMove.split(',')
    pending       = nextMove[0]
    job           = nextMove[1]
    unit          = nextMove[2]
    amount        = int(nextMove[3])
    valuation     = int(nextMove[4])
    reducedMight  = int(float(nextMove[5]))
    name = unit

    printRow = printDialogue(flag,str(str('### ' + str(currentNation.country) + ' chose to scrap')),db)
    printRow = printDialogue(flag,str(str(str(name) + ' to scrap : ' + str(amount))),db)
    
    

    # Award Credits and reduce might
    currentNation.wealth +=  valuation
    Adjustment = round((currentNation.might * reducedMight) * (amount/5))
    currentNation.might -=  Adjustment
    
    printRow = printDialogue(flag,str(str('Might lost    : -' + str(Adjustment))),db)
    printRow = printDialogue(flag,str(str('Might total   : ' + str(currentNation.might))),db)
    printRow = printDialogue(flag,str(str(str(currentNation.country) + ' was paid ' + str(valuation))),db)
    printRow = printDialogue(flag,str(str('Credits total : ' + str(currentNation.wealth))),db)
    
    return(0,'success')



# Target country loses next moves (via sabotage flag in array)
# Perpertrator gains x% might
# x% chance perpertrator gets captured resulting in loss of friendship.
def espionage(nextMove,currentNation,myWar,nextMoveIndex,flag,db):
    nextMove =  nextMove.split(',')
    nationChoice = nextMove[1]
    bonusPercent = random.randint(1,10)

    targetNation = db.session.query(NATIONS).filter_by(country=nationChoice).first()
    targetNation.Nextmoves = 'sabotaged' + ':'

    printRow = printDialogue(flag,str(str(str(targetNation.country) + ' has been infiltrated by an unknown advisary')),db)
    printRow = printDialogue(flag,str('==========================================='),db)
    printRow = printDialogue(flag,str(str(str(targetNation.country) + ' current actions sabotaged and will miss a round.')),db)
    
    printRow = printDialogue(flag,str(str(str(currentNation.country) + ' gained ' + str(bonusPercent) + '% might.' )),db)
    printRow = printDialogue(flag,str(str(str(currentNation.country) + ' original might value: ' + str(currentNation.might))),db)
      
    
    currentNation.might += round(int(currentNation.might) * (bonusPercent/100))
    printRow = printDialogue(flag,str(str(str(currentNation.country) + '      new might value: ' + str(currentNation.might))),db)
    
    discoverRisk = random.randint(0,5)
    if discoverRisk > -1:
        printRow = printDialogue(flag,str(str('### ' + str(targetNation.country) + ' captured the insurgent from ' + str(currentNation.country))),db)
        printRow = printDialogue(flag,str(str(str(targetNation.country) + ' friendship with ' + str(currentNation.country) + ' has decreased as a result.')),db)
        
        
        FrienshipBA = db.session.query(friendship).filter_by(country=targetNation.country,targetCountry=currentNation.country).first()
        printRow = printDialogue(flag,str(str(str(targetNation.country) + ' original friendship value: ' + str(FrienshipBA.level))),db)
        FrienshipBA.level -= random.randint(1,18)
        db.session.commit()

        printRow = printDialogue(flag,str(str(str(targetNation.country) + ' new friendship value: ' + str(int(FrienshipBA.level)))),db)


    return(0,'success')





def allowedTech(currentNation):

    # Get % research completion for each tech stream
    firstTech    = currentNation[0]['Tech']['researched']['one'][2]
    secondTech   = currentNation[0]['Tech']['researched']['two'][2]
    thirdTech    = currentNation[0]['Tech']['researched']['three'][2]
    fourthTech   = currentNation[0]['Tech']['researched']['four'][2]
    fifthTech    = currentNation[0]['Tech']['researched']['five'][2]

    # Return weapon number and random value awarded
    allowedAssets = []
    if firstTech > -1:
        allowedAssets.append(('1',random.randint(1,100)))
    if firstTech > 99:
        allowedAssets.append(('2',random.randint(1,20)))
    if secondTech > 99:
        allowedAssets.append(('3',random.randint(1,15)))
    if thirdTech > 99:
        allowedAssets.append(('4',random.randint(1,10)))
        allowedAssets.append(('5',random.randint(1,8)))
    if fourthTech > 99:
        allowedAssets.append(('6',random.randint(1,5)))
        allowedAssets.append(('7',random.randint(1,3)))
    if fifthTech > 99:
        allowedAssets.append(('8',1))

    return(allowedAssets)


def promotion(currentNation,p,index,playerNationIndex):
    warRank = ['Private', 'Lieutenant', 'Captain', 'Major', 'Commander', 'General', 'Supreme Commander']
    might   = currentNation[0]['War']['might']
    rank   = currentNation[0]['War']['level']
    if might > 150 and rank == warRank[0]:
        currentNation[0]['War']['level'] = warRank[1]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)

    if might > 300 and rank == warRank[1]:
        currentNation[0]['War']['level'] = warRank[2]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)

    if might > 500 and rank == warRank[2]:
        currentNation[0]['War']['level'] = warRank[3]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)

    if might > 800 and rank == warRank[3]:
        currentNation[0]['War']['level'] = warRank[4]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)

    if might > 2000 and rank == warRank[4]:
        currentNation[0]['War']['level'] = warRank[5]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)

    if might > 5000 and rank == warRank[5]:
        currentNation[0]['War']['level'] = warRank[6]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('warLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New War rank is ' + str(currentNation[0]['War']['level']),p,index,playerNationIndex)
    return(currentNation)

def firepower(currentNation,p,index,playerNationIndex):
    warRank = ['Private', 'Lieutenant', 'Captain', 'Major', 'Commander', 'General', 'Supreme Commander']
    might   = currentNation[0]['War']['might']
    rank   = currentNation[0]['War']['level']

    return(currentNation)
