import sys
import time
import copy
import random
from universe.classes import PTc,warDataBase,NATIONS,friendship,warAssets,techAssets,gameTracker,initializeObjects,techEras,techEraBonus,techEraCost,PTcHistory,dialogue,printDialogue



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


# This function takes the process research order from nation and deducts RP 
# to increase % completion of selected technology (choice)
def processResearch(nextMove,currentNation,CURRENT_TECH_ASSETS,nextMoveIndex,flag,db):
    nextMove                 = nextMove.split(',')
    pending                  = nextMove[0]
    job                      = nextMove[1]
    era                      = nextMove[2]
    choice                   = nextMove[3]
    techKey                  = nextMove[4]
    required                 = int(nextMove[5])
    earnedSoFar              = getattr(CURRENT_TECH_ASSETS,techKey)

    
    #['Submitted', 'research', 'INDUSTRIAL REVOLUTION', 'Manufacturing Line', 'twoRp', '100']

    researchedItemName       = choice
    remaining                = required - int(earnedSoFar)
    pointsOwned              = int(currentNation.RP)
    pointsToSpend            = round(pointsOwned * 0.2) # Test the last number, it may need reduced: spend = devcompletion speed

    #Skip this move if not enough points
    if pointsOwned < pointsToSpend:
        print('Not enough points')
        return(0,'notEnough')
    # Skip if already max
    if remaining < 1:
        print(str(choice) + 'maxed out for ' + str(currentNation.country))
        return(0,'Maxed out')

    # Deduct RP 
    currentNation.RP -= pointsToSpend
    
    # UPDATE RESEARCH COMPLECTION
    newCompletionTotal      = int(earnedSoFar) + pointsToSpend
    setattr(CURRENT_TECH_ASSETS,techKey,newCompletionTotal)
    db.session.commit()
    earnedSoFar             = getattr(CURRENT_TECH_ASSETS,techKey)
    
    # UPDATE RESEARCH COMPLETION PERCENT 
    techPKey = techKey[:-2] + 'P'
    completionPercent = (int(earnedSoFar)/required) * 100
    setattr(CURRENT_TECH_ASSETS,techPKey,round(completionPercent))
    db.session.commit()
    #Update remaining
    remaining         = required - int(earnedSoFar)
    # Cap
    if remaining < 0: remaining = 0
    if completionPercent > 100: completionPercent = 100
    pointsOwned       = int(currentNation.RP)

    printRow = printDialogue(flag,str(str(str(currentNation.country) + ' Research Update')),db)
    printRow = printDialogue(flag,str(str('Researched Item: ' + str(researchedItemName))),db)
    printRow = printDialogue(flag,str(str('Research points spent = ' + str(pointsToSpend))),db)
    printRow = printDialogue(flag,str(str('Research: remaining   = ' + str(remaining) + ' , completion ' + str(round(completionPercent,2)) + '%')),db)
    printRow = printDialogue(flag,str('RP Owned = ' + str(pointsOwned)),db)
    printRow = printDialogue(flag,str(),db)


    # process reward
    if remaining < 1:
        setattr(CURRENT_TECH_ASSETS,techPKey,100)
        moveArray = updateMoveArray(currentNation,'research'," ")
        currentNation.Nextmoves = moveArray
        NATION_ARRAY = processResearchReward(researchedItemName,currentNation,techPKey,flag,db)
        db.session.commit()
    else:
        # Continue the move
        nextMove = str('pending' + ',' + 'research' + ',' + str(era) + ',' +  str(choice) + ',' +  str(techKey) + ',' +  str(required)+ ':')
        moveArray = updateMoveArray(currentNation,'research',nextMove)
        currentNation.Nextmoves = moveArray
        db.session.commit()
        printRow = printDialogue(flag,str(),db)
        str('Completion ' + str(completionPercent) + '%')

    return(0,'success')

def processResearchReward(researchedItemName,currentNation,techPKey,flag,db):
    
    printRow = printDialogue(flag,str(str('######' +str(researchedItemName) + ' Research Complete! #########')),db)
    printRow = printDialogue(flag,str(" "),db)
    techBonusRow = db.session.query(techEraBonus).filter_by(era=currentNation.era).first()
    bonusKey     = techPKey[:-1] 
    techBonus    = getattr(techBonusRow,bonusKey)
    
    techBonus = techBonus.split(':')
    for item in techBonus:
        item = item.split(',')
        if item[0] == 'K':
            printRow = printDialogue(flag,str(str('Knowledge boosted by ' + str(item[1]) + ' points.')),db)
            currentNation.KP += round(int(item[1]))
        if item[0] == 'R':
            printRow = printDialogue(flag,str(str('Research boosted by ' + str(item[1]) + ' points.')),db)
            currentNation.RP += round(int(item[1]))
        if item[0] == 'W':
            printRow = printDialogue(flag,str(str('Wealth increased by $' + str(item[1]))),db)
            currentNation.wealth += round(int(item[1]))
    db.session.commit()
    return(0,'success')


def gainResearch(nextMove,currentNation,nextMoveIndex,flag,db):
    nextMove                 = nextMove.split(',')
    pending                  = nextMove[0]
    job                      = nextMove[1]
    intensity                = nextMove[2]
    investedPercent          = int(nextMove[3])
    rounds                   = int(nextMove[4])
    invested                 = int(nextMove[5])
    RP                       = int(currentNation.RP)
    KP                       = int(currentNation.KP)



    if intensity == 'soft':
        bonusRP = round((0.1 * RP))
        if bonusRP < 25:
            bonusRP = 25
        bonusKP = 0
    elif intensity == 'medium':
        bonusRP = round((0.1 * RP) + (invested/3))
        bonusKP = round((0.1 * KP) + (invested/4))
    elif intensity == 'hard':
        bonusRP = round((0.2 * RP) + (invested/5))
        bonusKP = round((0.2 * KP) + (invested/6))
    elif intensity == 'overtime':
        bonusRP = round((0.3 * RP) + (invested/7))
        bonusKP = round((0.3 * KP) + (invested/8))


    # IF ROUNDS STILL TO GO, REWARD BONUS AND CONTINUE PENDING
    if rounds > 0:
        rounds = rounds -1

        #ADD REWARDS
        currentNation.RP  += round(bonusRP)
        currentNation.KP  += round(bonusKP)
        print('UPDATING RESEARCH ARRAY ')
        print(currentNation.Nextmoves)
        nextMove =  'pending' + ',' + 'gainResearch' + ',' + str(intensity) + ','  + str(investedPercent) + ',' + str(rounds) + ',' + str(invested) +':'
        moveArray = updateMoveArray(currentNation,'gainResearch',nextMove)
        currentNation.Nextmoves = moveArray
        db.session.commit()
        print(currentNation.Nextmoves)
        printRow = printDialogue(flag,str(str(str(currentNation.country) + ' Research Grant')),db)
        printRow = printDialogue(flag,str(str('Level ' + str(intensity))),db)
        printRow = printDialogue(flag,str(str('RP Bonus : +' + str(bonusRP))),db)
        printRow = printDialogue(flag,str(str('KP Bonus : +' + str(bonusKP))),db)
        printRow = printDialogue(flag,str(str('RP increased from ' + str(RP) + ' to ' + str(currentNation.RP))),db)
        printRow = printDialogue(flag,str(str('KP increased from ' + str(KP) + ' to ' + str(currentNation.KP))),db)
        printRow = printDialogue(flag,str(str('Rounds Remaining : ' + str(rounds))),db)

        # Clear out nextmove
        if rounds < 1:
            printRow = printDialogue(flag,str(str(str(currentNation.country) + ' Research Grant Funding complete.')),db)
            moveArray = updateMoveArray(currentNation,'gainResearch'," ")
            currentNation.Nextmoves = moveArray
            db.session.commit()
        return(0,'success')

    else:
        moveArray = updateMoveArray(currentNation,'gainResearch'," ")
        currentNation.Nextmoves = moveArray
        db.session.commit()
        return(0,'success')

    return(0,'success')
"""
Advancing the era means changing active column on techassets and warassets db
War Assets become upgraded, some units promoted but most converted to might 
KP rewareded 
"""
def advanceEra(nextMove,currentNation,myWar,nextMoveIndex,flag,db):

    # Define Weapons bonus awards 
    One    = int(myWar.wOneAmount)   * int(myWar.wOneLevel) * 1
    Two    = int(myWar.wTwoAmount)   * int(myWar.wTwoLevel) * 1
    Three  = int(myWar.wThreeAmount) * int(myWar.wThreeLevel) * 2
    Four   = int(myWar.wFourAmount)  * int(myWar.wFourLevel) * 2
    Five   = int(myWar.wFiveAmount)  * int(myWar.wFiveLevel) * 3
    Six    = int(myWar.wSixAmount)   * int(myWar.wSixLevel) * 4
    Seven  = int(myWar.wSevenAmount) * int(myWar.wSevenLevel) * 5
    Eight  = int(myWar.wEightAmount) * int(myWar.wEightLevel) * 5

    totalBonus  = One + Two + Three + Four + Five + Six + Seven + Eight

    upgradeOne   = int(myWar.wTwoAmount)
    upgradeTwo   = int(myWar.wThreeAmount)
    upgradeThree = (int(myWar.wFourAmount) * 2) + (int(myWar.wFiveAmount) * 10)  + (int(myWar.wSixAmount) * 20) + (int(myWar.wSevenAmount) * 50) + (int(myWar.wEightAmount) * 200)

    # Update Era
    era = currentNation.era
    nextEraRow = db.session.query(techEras).filter_by(era=era).first()
    nextEra = nextEraRow.nextEra

    # Deactivate current era 
    myTech = db.session.query(techAssets).filter_by(country=currentNation.country, era=era).first() 
    myTech.active = 0
    db.session.commit()

    # Update era 
    currentNation.era = nextEra  
    db.session.commit()

    # Update latest Era
    myTech = db.session.query(techAssets).filter_by(country=currentNation.country, era=currentNation.era).first() 
    myTech.active = 1
    db.session.commit()

    # REWARD KNOWLEDGE..
    knowledge = int(currentNation.KP)
    currentNation.KP += round((knowledge  * 0.15))
    if int(currentNation.KP) < 2: currentNation.KP =69
    db.session.commit()

    # DEACTIVATE PREVIOUS ERA IN WARARRAY
    myWar.active = 0
    db.session.commit() 

    # ACTIVATE NEXT ERA AND REWARD UNITS 
    myWar        = db.session.query(warAssets).filter_by(country=currentNation.country,era=currentNation.era).first()
    myWar.active = 1
    myWar.wOneAmount   = upgradeOne
    myWar.wTwoAmount   = upgradeTwo
    myWar.wThreeAmount = upgradeThree
    db.session.commit()

    currentNation.might += totalBonus
    db.session.commit()

    printRow = printDialogue(flag,str('++++++++++++++++++++++++++++++++++++++++++'),db)
    printRow = printDialogue(flag,str(str(str(currentNation.country) + ' has advanced to the ' + str(nextEra))),db)
    printRow = printDialogue(flag,str('++++++++++++++++++++++++++++++++++++++++++'),db)
    printRow = printDialogue(flag,str(str(str(currentNation.country)  + ' gained 10% knowledge.')),db)
    printRow = printDialogue(flag,str(str('Units converted to +' + str(totalBonus) + ' might.')),db)
    printRow = printDialogue(flag,str(str(str(currentNation.country) + ' now has ' + str(nextEra) + ' level military capabilities.')),db)
    
    return(0,'complete')
