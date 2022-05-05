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


def gambleAction(nextMove,currentNation,flag,db):
    nextMove = nextMove.split(',')

    printRow = printDialogue(flag,str(''),db)
    printRow = printDialogue(flag,str('### ' + str(currentNation.country) + ' chose to gamble '),db)
    

    
    amount = int(nextMove[1])
    originalFinanceScore = int(currentNation.wealth) + amount
    winnings = random.randint((round(0.3*amount)), round(2.5*amount)) 
    currentNation.wealth += winnings
    db.session.commit()

    difference = int(currentNation.wealth) - originalFinanceScore  

    if difference > 0:
        printRow = printDialogue(flag,str(str(str(currentNation.country) + ' gained  +' + str(difference))),db)
    elif difference < 0:
        printRow = printDialogue(flag,str(str(str(currentNation.country) + ' lost  ' + str(difference))),db)
    else:
        printRow = printDialogue(flag,str(str(str(currentNation.country) + ' broke even  ' + str(difference))),db)
        
    printRow = printDialogue(flag,str(str('Gambled         : ' + str(amount))),db)
    printRow = printDialogue(flag,str(str('Winnings        : ' + str(winnings))),db)
    printRow = printDialogue(flag,str(str('Finance credits : ' + str(currentNation.wealth))),db)
    
    return(0, 'Success')


def buyAction(nextMove,currentNation,PRICE_TRACKER,flag,db):
    nextMove = nextMove.split(',')
    commodity = nextMove[1]
    key       = nextMove[2]
    amount    = int(nextMove[3])
    price     = getattr(PRICE_TRACKER, key)
    stock     = getattr(PRICE_TRACKER, commodity)
    myStock   = getattr(currentNation, commodity)
    cost      = amount * int(price)

    printRow = printDialogue(flag,str(str('### ' + str(currentNation.country) + ' chose to buy ')),db)
    printRow = printDialogue(flag,str(str('Credits    : ' + str(currentNation.wealth))),db)
    printRow = printDialogue(flag,str(str(str(commodity) + ' purchased : ' + str(amount))),db)
    printRow = printDialogue(flag,str(str('Total Cost :' + str(cost))),db)

    
    # UPDATE Reduce stock and deliver goods to user
    setattr(PRICE_TRACKER, commodity, (int(stock)   - amount))
    setattr(currentNation, commodity, (int(myStock) + amount))
    printRow = printDialogue(flag,str(str('New total : ' + str(getattr(currentNation, commodity)))),db)
    
    db.session.commit()
    return(0, 'Success')

def sellAction(nextMove,currentNation,PRICE_TRACKER,flag,db):
    nextMove = nextMove.split(',')
    commodity = nextMove[1]
    amount    = int(nextMove[2])
    value     = nextMove[3]

    stock     = getattr(PRICE_TRACKER, commodity)
    myStock   = getattr(currentNation, commodity)


    printRow = printDialogue(flag,str(str('### ' + str(currentNation.country) + ' chose to sell')),db)
    printRow = printDialogue(flag,str(str('Credits    : ' + str(currentNation.country))),db)
    printRow = printDialogue(flag,str(str(str(commodity) + ' owned : ' + str(myStock))),db)
    printRow = printDialogue(flag,str(str(str(commodity) + ' sold  : ' +  str(amount))),db)
    
    
    # UPDATE Increase stock and credit user
    setattr(PRICE_TRACKER, commodity, (int(stock)   + amount))
    currentNation.wealth +=  int(value)
    printRow = printDialogue(flag,str(str(str(currentNation.country) + ' was paid ' + str(value))),db)
    printRow = printDialogue(flag,str(str('New Credits Total   : ' + str(currentNation.wealth))),db)

    db.session.commit()
    return(0, 'Success')


def investResource(nextMove,currentNation,PRICE_TRACKER,flag,nextMoveIndex,db):
    nextMove         = nextMove.split(',')

    pending          = nextMove[0]
    job              = nextMove[1]
    resource         = nextMove[2]
    spendAmount      = int(float(nextMove[3]))
    investedPrice    = int(float(nextMove[4]))
    wait             = int(nextMove[5])
    moveIndex = nextMoveIndex # Get position in country array

    if resource == "gold":
        key = 'goldPrice'
    if resource == "rareMetals":
        key = 'rareMetalsPrice'
    if resource == 'gems':
        key = 'gemsPrice'
    if resource == 'oil':
        key = 'oilPrice'


    # IF NOT YET READY
    if wait > 0:
        wait = wait - 1

        printRow = printDialogue(flag,str(str('### ' + str(currentNation.country) + ' chose to Invest in ' + str(resource))),db)
        printRow = printDialogue(flag,str(str('Time Remaining : ' + str(wait))),db)
        
        adjustedMove = 'pending' + ',' + str(job) + ',' + str(resource) + ',' + str(spendAmount) + ',' + str(investedPrice) + ',' + str(wait) + ',' + str(key) + ':'
        
        moveArray = updateMoveArray(currentNation,'investResource',adjustedMove)
        currentNation.Nextmoves = moveArray
        db.session.commit()


    if wait < 1:
        currentPrice = getattr(PRICE_TRACKER, key)
        priceDiff = int(currentPrice) - investedPrice
        original = currentNation.wealth

        if priceDiff > 0:
            bonus = round(priceDiff * spendAmount * (random.randint(1,300)/100))
            currentNation.wealth += bonus
            printRow = printDialogue(flag,str(str(str(currentNation.country) + ' made a profit of $' + str(bonus))),db)
            
        if priceDiff < 0:
            priceDiff = -priceDiff
            token = round((priceDiff/investedPrice) * investedPrice)
            loss = round(spendAmount - token)
            currentNation.wealth  += loss
            printRow = printDialogue(flag,str(str(str(currentNation.country) + ' made a loss, but recouped $' + str(loss))),db)
            
        if priceDiff == 0:
            token = round(investedPrice + (investedPrice * (random.randint(1,18)/100)))
            currentNation.wealth += (token + spendAmount)
            str(str(currentNation.country) + ' made no profit, but gained token interest of $' + str(token))

        printRow = printDialogue(flag,str(str('Credits changed from $' + str(original) + ' to $' + str(currentNation.wealth))),db)
        
        # Find this index in nextmove array and blank it out
        moveArray = updateMoveArray(currentNation,'investResource'," ")
        currentNation.Nextmoves = moveArray
        db.session.commit()



    return(0,'complete')


def investCountry(nextMove,currentNation,PRICE_TRACKER,flag,nextMoveIndex,db):
    nextMove                 = nextMove.split(',')
    pending                  = nextMove[0]
    job                      = nextMove[1]
    thereNation              = nextMove[2]
    spendAmount              = int(nextMove[3])
    nationsOriginalWealth    = int(nextMove[4])
    wait                     = int(nextMove[5])

    myNation                 = currentNation.country
    originalWealth           = currentNation.wealth




    #allies = db.session.query(friendship).filter_by(country='USA',targetCountry='UK').first()
    FriendshipAB     = db.session.query(friendship).filter_by(country=myNation,targetCountry=thereNation).first().level
    FrienshipBA      = db.session.query(friendship).filter_by(country=thereNation,targetCountry=myNation).first().level
    originalFriendshipAB = int(FriendshipAB)
    originalFrienshipBA  = int(FrienshipBA)
    # # IF NOT YET READY
    if wait > 0:
        wait = wait -1

        printRow = printDialogue(flag,str(str('### ' +  str(currentNation.country) + ' investing in ' + str(thereNation))),db)
        printRow = printDialogue(flag,str(str('Time Remaining : ' + str(wait))),db)
        
        mextMove = str('pending' + ',' + 'investCountry' + ',' + str(thereNation) + ',' +  str(spendAmount) + ',' +  str(nationsOriginalWealth) + ',' +  str(wait))
        moveArray = updateMoveArray(currentNation,'investCountry',mextMove)
        
        currentNation.Nextmoves = moveArray
        db.session.commit()
  

    if wait < 1:
        currentWealth          = int(db.session.query(NATIONS).filter_by(country=thereNation).first().wealth)
        wealthDiff             = currentWealth - nationsOriginalWealth
        myOriginalCredits      = int(currentNation.wealth)
        
        if wealthDiff > 0:
            bonus = round(wealthDiff * 0.2) + round(wealthDiff * 0.05 * spendAmount/100) + (spendAmount * 1.5)
            bonus = round(bonus)
            currentNation.wealth += + bonus
            printRow = printDialogue(flag,str(str(str(currentNation.country) + ' made a profit of $' + str(bonus))),db)
            
   
        if wealthDiff < 0:
            loss = 0.8 * spendAmount
            currentNation.wealth += round(currentNation.wealth + loss)
            printRow = printDialogue(flag,str(str(str(currentNation.country) + ' made a loss, but recouped $' + str(loss))),db)
            
        if wealthDiff == 0:
            token = round(nationsOriginalWealth + (nationsOriginalWealth * (random.randint(1,10)/100)))
            token = round(token)
            currentNation.wealth = round(currentNation.wealth + token + spendAmount)
            printRow = printDialogue(flag,str(str(str(currentNation.country) + ' made no profit, but gained token interest of $' + str(token))),db)
            

        # BOOST FRIENDSHIP
        FriendshipAB += int(originalFriendshipAB) + random.randint(1,15)
        FrienshipBA  += int(originalFrienshipBA) + random.randint(8,25)
        
        printRow = printDialogue(flag,str(str(str(thereNation) + ' greatly appreciates the investment from ' + str(myNation))),db) 
        printRow = printDialogue(flag,str(str('New friendship between ' + str(thereNation) + ' and ' + str(myNation) + ' has increased from ' + str(originalFriendshipAB) + ' to ' + str(FriendshipAB))),db) 
        printRow = printDialogue(flag,str(str('New friendship between ' + str(myNation) + ' and ' + str(thereNation) + ' has increased from ' + str(originalFrienshipBA) + ' to ' + str(FrienshipBA))),db) 
        printRow = printDialogue(flag,str(str('Credits changed from $' + str(originalWealth) + ' to $' + str(currentNation.wealth))),db) 
        
        
        moveArray = updateMoveArray(currentNation,'investCountry'," ")
        currentNation.Nextmoves = moveArray
        db.session.commit()
        print('complete')
        print(currentNation)

    return(0,'success')






def promotion(currentNation,flag,db):
    financeRank = ['PickPocket', 'Penny Pusher', 'Assistant', 'gambler', 'accountant', 'huslter', 'business magnate']
    wealth = int(currentNation.wealth)
    rank   = currentNation.fLevel
    if wealth > 5100 and rank == financeRank[0]:
        currentNation.fLevel = financeRank[1]
        rank   = currentNation.fLevel
        currentNation.notes = str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank) + ':')
        printRow = printDialogue(flag,str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':'),db)
        db.session.commit()
        

    if wealth > 10000 and rank == financeRank[1]:
        currentNation.fLevel = financeRank[2]
        rank   = currentNation.fLevel
        currentNation.notes = str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':')
        printRow = printDialogue(flag,str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':'),db)
        db.session.commit()
    if wealth > 15000 and rank == financeRank[2]:
        currentNation.fLevel = financeRank[3]
        rank   = currentNation.fLevel
        currentNation.notes = str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':')
        printRow = printDialogue(flag,str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':'),db)
        db.session.commit()
    if wealth > 20000 and rank == financeRank[3]:
        currentNation.fLevel = financeRank[4]
        rank   = currentNation.fLevel
        currentNation.notes = str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':')
        printRow = printDialogue(flag,str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':'),db)
        db.session.commit()

    if wealth > 30000 and rank == financeRank[4]:
        currentNation.fLevel = financeRank[5]
        rank   = currentNation.fLevel
        currentNation.notes = str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':')
        printRow = printDialogue(flag,str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':'),db)
        db.session.commit()
    if wealth > 40000 and rank == financeRank[5]:
        currentNation.fLevel = financeRank[6]
        rank   = currentNation.fLevel
        currentNation.notes = str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':')
        printRow = printDialogue(flag,str(str(currentNation.country) + ' levelled up! New Finance rank is ' + str(rank)+ ':'),db)
        db.session.commit()

    return(0,'success')
