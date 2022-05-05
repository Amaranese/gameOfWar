""""
PROGRAM OVERVIEW: 
This module is contained within the processRound loop of the next round function. 
This module places the nextmove orders (currentNation.Nextmoves) for each country. 
Moves are capped at 2 in a while loop that checks moves, but room for 5 tries (a pass or no selection is also possible a a move)





"""



import sys
import time
import copy
import random
from universe.classes import PTc,warDataBase,NATIONS,friendship,warAssets,techAssets,gameTracker,initializeObjects,techEras,techEraBonus,techEraCost,PTcHistory,printDialogue,dialogue
from universe.routesFunctions  import checkMoves




# Need to make buying more sophisticated rather than chosing a random commodity
# Remember to deduct might from hard drill
# Buffer drill by tech level 

def setAIMoves(PARM_ARRAY,db,currentNation,averageRPOne,AverageRPTwo,AverageRPThree,index,flag):
    NATION_ASSETS = PARM_ARRAY[0]
    WAR_ASSETS    = PARM_ARRAY[1]
    TECH_ASSETS   = PARM_ARRAY[2]
    WAR_DATABASE  = PARM_ARRAY[3]
    TECH_COST_DB  = PARM_ARRAY[4]
    TECH_BONUS_DB = PARM_ARRAY[5]
    PRICE_TRACKER = PARM_ARRAY[6]
    FRIENDSHIP    = PARM_ARRAY[7]
    GAME_TRACKER  = PARM_ARRAY[8]
    year          = PARM_ARRAY[9]

    # Capping AI at one for now 
    moveLimit    = int(currentNation.moveLimit)
    aggression   = int(currentNation.aggression)
    creativity   = int(currentNation.creativity)
    materialism  = int(currentNation.materialism)
    prudence     = int(currentNation.prudence)
    wealth       = int(currentNation.wealth)
    era          = currentNation.era
    myTech       = db.session.query(techAssets).filter_by(country=currentNation.country,era=currentNation.era).first()
    myWar        = db.session.query(warAssets).filter_by(country=currentNation.country,era=currentNation.era).first()
    notes        = str(currentNation.notes)
    #print('########' + str(currentNation.country) + '  ' + str(notes))

    
    
    moveCounter = 0
    while checkMoves(currentNation,'%^')[0] > 1:
        #Ensure no countries take more moves than the limit
        if moveCounter > 3: break
        # Returns index 0 = finance, 1 = war, 2 science, 3 politics
        bias = calculateBias(currentNation,wealth,materialism,aggression,creativity,prudence)

        #HAS FinanceNANCE BIAS
        if bias == 0:
            choice = [1,2,3,4,5]
            choice = random.choice(choice)
            if choice == 1: gambleMessage = gamble(currentNation,db) # GAMBLE 
            
            if choice == 2: buyMessage = aiBuy(PRICE_TRACKER,currentNation,materialism,aggression,db) # BUY
            
            if choice == 3: sellMessage = aiSell(PRICE_TRACKER,currentNation,materialism,aggression,db) # SELL
            
            if choice == 4: investMessage = investResource(currentNation,PRICE_TRACKER,db) # Invest Resource
            
            if choice == 5: invCmessage = investNation(currentNation,PRICE_TRACKER,db) # Invest in nation

        # HAS BIAS TOWARDS WAR
        if bias == 1:
            choice = [1,2,3,4,5]
            choice = random.choice(choice)
            # DRILL
            if choice == 1: drillMessage = drill(currentNation,myWar,db)
            # BUILD
            if choice == 2: buildMessage = build(currentNation,WAR_DATABASE,aggression,materialism,myTech,db)
            # SCRAP
            if choice == 3: scrapMessage = scrap(currentNation,myWar,aggression, db)
            # ESPIONAGE~
            if choice == 4: espionageMessage = espionage(currentNation,aggression,prudence,db)
       
        #HAS BIAS TOWARDS SCIENCE
        if bias == 2:
            if '1' in notes.split(':'):
                #print('#####TRYING TO LEVEL UP')
                advanceMessage = advanceEra(currentNation,db)
            grantMessage = gainResearchPoints(currentNation,averageRPOne,AverageRPTwo,AverageRPThree,aggression,creativity,db)
            completeTech = researchTechnology(currentNation,era,creativity,averageRPOne,AverageRPTwo,AverageRPThree,myTech,db)

        moveCounter += 1


    # If No moves, then pass
    if len(currentNation.Nextmoves) == 0:
        print(str(currentNation.country) + ' chose to pass')
        currentNation.Nextmoves= 'pass:'
    

    
    moveTotal = currentNation.Nextmoves
    print('XXXXXXXENDROUND XXXXXXXXX ')
    print(str(currentNation.country) + ' moves: ' + str(moveTotal))
    print(str(currentNation.country) + ' moves: ' + str(moveTotal))
    printRow = printDialogue('all',str(str(str(currentNation.country) + ' moves: ' + str(moveTotal))),db)
    printRow = printDialogue('all',str(str('----------------')),db)
    print('XXXXXXXENDROUND XXXXXXXXX ')

    return(0,'pass')

def calculateBias(currentNation,wealth,materialism,aggression,creativity,prudence):
    # Calculate bias values
    wealth       = int(wealth)
    financeBias  = materialism + random.randint(0,100)
    warBias      = aggression  + random.randint(0,100)
    scienceBias  = creativity  + random.randint(0,100)
    politicsBias = prudence    + random.randint(0,100)
    values = (financeBias,warBias,scienceBias,prudence)
    bias = values.index(max(values))
    return(bias)



def build(currentNation,WAR_DATABASE,aggression,materialism,myTech,db):

    
    friendship.query.filter_by(country=currentNation.country).order_by(friendship.level).all()
    buildBias = 1
    if (aggression + materialism) > 150:
        buildBias = 2
    elif (aggression + materialism) > 100:
        buildBias = 3
    elif (aggression + materialism) > 75:
        buildBias = 4
    else:
        buildBias = 10


    buildProbability = random.randint(0, buildBias)
    if buildProbability == 1:
        wealth               = int(currentNation.wealth)
        aggressionAdjusted   = (aggression) / 100

        allowedAssets = []
        allowedAssets = allowedTech(currentNation,db)
        unit = random.choice(allowedAssets)

        price        = warDataBase.query.filter_by(era=currentNation.era, unit_key=int(unit)).first().price
        wait         = warDataBase.query.filter_by(era=currentNation.era, unit_key=int(unit)).first().buildTime
        bonusMight   = warDataBase.query.filter_by(era=currentNation.era, unit_key=int(unit)).first().mightBonus
        selectedUnit = warDataBase.query.filter_by(era=currentNation.era, unit_key=int(unit)).first().unit_name
        # Key needed as look up for war assets
        warArray     = {'1':"wOneAmount","2":"wTwoAmount",'3':"wThreeAmount",'4':"wFourAmount",'5':"wFiveAmount",'6':"wSixAmount",'7':"wSevenAmount",'8':"wEightAmount"} 
        warKey       = warArray[unit]

        
        maxpurchase = int(wealth // int(price))
        adjusted    = round((aggressionAdjusted * maxpurchase))

        if adjusted > 0:
            maxBuy = round(random.randint(adjusted, maxpurchase))
        elif maxpurchase > 0:
            maxBuy = round(random.randint(0,maxpurchase))
        else:
            # No money so skipping
            return(0,'dropped')
        
        # If they can't afford even one  
        if maxBuy < 1:
            return(0,'cant afford')

        purchaseAmount = random.randint(1,maxBuy)
        cost = purchaseAmount * price


        # Deduct cost & Place Order 
        currentNation.wealth -=  cost
        nextMove = str('Submitted' + ',' + 'WeaponsBuild' + ',' + str(selectedUnit) + ',' +  str(purchaseAmount) + ',' +  str(wait) + ',' +  str(bonusMight) + ',' + str(warKey) + ':')
        currentNation.Nextmoves += nextMove
        db.session.commit()
    return(0,'success')



def scrap(currentNation,myWar,aggression,db):
    wealth               = int(currentNation.wealth )
    aggressionAdjusted   = (aggression) / 100
    warArray             = {'1':"wOneAmount","2":"wTwoAmount",'3':"wThreeAmount",'4':"wFourAmount",'5':"wFiveAmount",'6':"wSixAmount",'7':"wSevenAmount",'8':"wEightAmount"} 
    era                  = currentNation.era
    scrapProbability = 10
    # Fill array with weapons above 0
    scrapArray = []
    counter = 0
    for key,value in warArray.items():
        stock = getattr(myWar, value)
        if int(stock) > 0:
            counter += 1
            name    = getattr(myWar, str(value[:-6]))
            warKey  = value
            price   = warDataBase.query.filter_by(era=era,unit_key=key).first().price 
            might   = warDataBase.query.filter_by(era=era,unit_key=key).first().mightBonus 
            item    = [name,stock,warKey,price,might]
            scrapArray.append(item)

    # Random weapon to scrap
    if counter < 1:
        return(0,'no units to scrap')
    elif counter == 1:
        choice = scrapArray[0]
    elif counter > 1:
        choice = random.choice(scrapArray)
    else:
        print("Something went wrong: " +str(counter))
        return(1,'fail')

    #print('choice len for debug ' + str(len(choice)) + str(choice))
    # if poor, scrap
    averageMight,averageWealth,averageKnowledge,averageInfluence = getAverages()
    poor          = 0.6*int(averageWealth)
    if wealth < poor: scrapProbability = 3
    # Set parms if passes threshold
    if random.randint(0,scrapProbability) == 2:
        name         = choice[0]
        stock        = int(choice[1])
        warAmountKey = choice[2]
        price        = int(choice[3])
        reducedMight = choice[4]
        adjusted     = round((aggressionAdjusted * stock))
        maxScrap     = round(random.randint(adjusted, stock))

        scrapAmount = random.randint(1,maxScrap)
        valuation   = scrapAmount * price

        # Deducts units and places order 
        setattr(myWar,warAmountKey,int(stock-scrapAmount))
        db.session.commit()
        nextMove = str('Submitted' + ',' + 'WeaponsScrap' + ',' + str(name) + ',' +  str(scrapAmount) + ',' +  str(valuation) + ',' +  str(reducedMight)+ ':')
        currentNation.Nextmoves += nextMove
    return(0,'success')


def allowedTech(currentNation,db):
    # Get % research completion for each tech stream
    myTech  = db.session.query(techAssets).filter_by(country=currentNation.country,era=currentNation.era).first()

    firstTech    = myTech.oneP
    secondTech   = myTech.twoP
    thirdTech    = myTech.threeP
    fourthTech   = myTech.fourP
    fifthTech    = myTech.fiveP

    allowedAssets = []
    if firstTech > -1:
        allowedAssets.append('1')
    if firstTech > 99:
        allowedAssets.append('2')
    if secondTech > 99:
        allowedAssets.append('3')
    if thirdTech > 99:
        allowedAssets.append('4') 
        allowedAssets.append('5')
        allowedAssets.append('6')
    if fourthTech > 99:
        allowedAssets.append('7')
    if fifthTech > 99:
        allowedAssets.append('8')

    return(allowedAssets)





# DRILL IF MIGHT IS < 80% of Average
# Pick a military branch, save asset details to array, place order 
def drill(currentNation,myWar,db):

    returnCode = checkMoves(currentNation,'drill')[1]
    if returnCode > 0: return(0,'already drilled')

    # BUILD PROBABILITY
    #-----------------
    averageMight,averageWealth,averageKnowledge,averageInfluence = getAverages()
    might = int(currentNation.might)

    drillChance = 0
    if might < (0.5 * averageMight):
        drillChance += random.randint(0,8)
    elif might < (0.8 * averageMight):
        drillChance += random.randint(0,6)
    else:
        drillChance += random.randint(0,4)

    # Warmongers gonna be warmongers
    if might > (2.5 * averageMight):
        drillChance += random.randint(0,20)
    # Drop out if threshold not met
    if drillChance < 2:
        return(0,'dropped')


    unitOne      = int(myWar.wOneAmount)
    unitTwo      = int(myWar.wTwoAmount)
    light        = unitOne + unitTwo
    
    unitThree    = int(myWar.wThreeAmount)
    unitFour     = int(myWar.wFourAmount)
    unitFive     = int(myWar.wFiveAmount)
    core         = unitThree + unitFour + unitFive
    
    unitSix      = int(myWar.wSixAmount)
    unitSeven    = int(myWar.wSevenAmount)
    heavy        = unitSix + unitSeven
    
    unitEight    = int(myWar.wEightAmount)
        
    branchChoiceArray = []

    if light > 1:
        branchChoiceArray.append('light')
    if core > 1:
        branchChoiceArray.append('core')
    if heavy > 1:
        branchChoiceArray.append('heavy')

    # in the event there are no units
    if len(branchChoiceArray) < 1:
        return(0,'dropped')

    branchChoice = random.choice(branchChoiceArray)

    # based upon selection 
    # set up order form and clear out units for training
    if branchChoice == 'light':
        units = str(myWar.wOneAmount) + ',' + str(myWar.wTwoAmount) + ':'
        branch = 'Light Units'
        myWar.wOneAmount = 0
        myWar.wTwoAmount = 0
        db.session.commit()
    elif branchChoice == 'core':
        units =  str(myWar.wThreeAmount) + ',' + str(myWar.wFourAmount) + ',' + str(myWar.wFiveAmount) +':'
        branch = 'Core Division'
        myWar.wThreeAmount =0 
        myWar.wFourAmount  =0
        myWar.wFiveAmount  =0
        db.session.commit()
    elif branchChoice == 'heavy':
        units = str(myWar.wSixAmount) + ',' + str(myWar.wSevenAmount) + ':'
        branch = 'Heavy Forces'
        myWar.wSixAmount   = 0
        myWar.wSevenAmount = 0
        db.session.commit()
    else:
        return(0,'dropped')


    aggression          = int(currentNation.aggression)
    augmentedAggresion  = random.randint(0,(100 + aggression))

    # Ive tilted this a bit more towards harder drilling: can amend later
    if augmentedAggresion > 120:
        exposure = 'hard'
    elif augmentedAggresion > 85:
        exposure = 'medium'
    else:
        exposure = 'soft'
    
    drillOrder = 'drill' + ',' + str(branch) + ',' + str(exposure) + ',' + units
    # Place Order
    currentNation.Nextmoves += drillOrder
    db.session.commit()
    return(0,'success')

# Probability of purchase depends how much the price is lower than average
def aiBuy(PRICE_TRACKER,currentNation,materialism,aggression,db):


    materialism = int(materialism)
    commodity = random.choice(('gold','gems','rareMetals','oil'))
    averageKey = commodity + 'Average'
    priceKey   = commodity + 'Price'

    CommodityPrice        = int(getattr(PRICE_TRACKER,priceKey))
    averageCommodityPrice = int(getattr(PRICE_TRACKER,averageKey))

    if averageCommodityPrice == 0:
        averageCommodityPrice = 0.1
    percentageDecrease = ((averageCommodityPrice - CommodityPrice)/averageCommodityPrice)
   
    # Higher materialism increases buy probability
    if percentageDecrease > 0.80:
        maxBuyProbability = 30
    elif percentageDecrease > 0.50:
        maxBuyProbability = 20
    elif percentageDecrease > 0.20:
        maxBuyProbability = 15
    else:
        maxBuyProbability = 10

    buyProbability =  (materialism / 100 ) * random.randint(0,maxBuyProbability)
    # make the order
    if buyProbability > 1:
        # submit order
        price        = CommodityPrice
        credits      = currentNation.wealth
        aggression   = currentNation.aggression / 100
        maxpurchase = int(credits // price)

        compensatedMax = round(aggression * maxpurchase)
        if compensatedMax < 3:
            currentNation.Nextmoves = "pass:"
            db.session.commit()
            return(0,'success')

        purchaseAmount = random.randint(1, compensatedMax)
        cost = purchaseAmount * price

        # Deduct cost & Place Order 
        commodity = commodity + ',' + priceKey
        currentNation.wealth     -=  cost
        currentNation.Nextmoves += str('buy' + ',' + str(commodity) + ',' + str(purchaseAmount) + ':')
        db.session.commit()
        
    return(0,'success')


def aiSell(PRICE_TRACKER,currentNation,materialism,aggression,db):
    materialism = int(materialism)
    commodity = random.choice(('gold','gems','rareMetals','oil'))
    averageKey = commodity + 'Average'
    priceKey   = commodity + 'Price'
    
    CommodityPrice        = int(getattr(PRICE_TRACKER,priceKey))
    averageCommodityPrice = int(getattr(PRICE_TRACKER,averageKey))



    percentageIncrease = ((CommodityPrice - averageCommodityPrice)/averageCommodityPrice)
   
    if percentageIncrease > 0.80:
        maxSellProbabiliy = 4
    elif percentageIncrease > 0.50:
        maxSellProbabiliy = 3
    elif percentageIncrease > 0.20:
        maxSellProbabiliy = 2
    else:
        maxSellProbabiliy = 1

    # max value is 6
    sellProbability =  round((aggression + materialism)/100) + maxSellProbabiliy

    if sellProbability > 3:
        # decrease stock
        # submit order
        price                  = CommodityPrice
        myStock                = int(getattr(currentNation, commodity))
        aggressionPercentage   = (aggression / 100)

        compensatedMax = round(aggressionPercentage * myStock)
        if compensatedMax > myStock or compensatedMax < 1:
            return(0,'success')

        # purchase choice
        sellAmount = random.randint(1, compensatedMax)
        value = sellAmount * price
        # Deduct stock & Place Order 
        postDeduction = myStock - sellAmount
        setattr(currentNation,commodity,postDeduction)
        currentNation.Nextmoves += str('sell' + ',' + str(commodity) + ',' + str(sellAmount) + ',' +  str(value) + ':')
        db.session.commit()
        
    return(0,'success')


def gamble(currentNation,db):
    # Roughly 25% chance of having a gamble
    gambleAction = random.randint(0,10)
    if gambleAction < 3:

        returnCode,amount = arbitrarySpendAmount(currentNation)
        if returnCode > 0: 
            print('not enough')
            return(0, 'not enough')

        currentNation.wealth     -= amount
        currentNation.Nextmoves  += str('gamble'+ ',' + str(amount) + ':')
        db.session.commit()
    return(1,'success')


def investResource(currentNation,PRICE_TRACKER,db):

    # CHECK MAX MOVES
    returnCode = checkMoves(currentNation,'investResource')[1]
    if returnCode > 0: 
        return(0,'duplicate')


    # Convert history string into list of numbers
    goldString       = getattr(PRICE_TRACKER,'goldHistory')
    rareMetalsString = getattr(PRICE_TRACKER,'rareMetalsHistory')
    gemsString       = getattr(PRICE_TRACKER,'gemsHistory')
    oilString        = getattr(PRICE_TRACKER,'oilHistory')

    gold,rareMetals,gems,oil = [],[],[],[]
    for item in goldString.split(','): gold.append(int(float(item)))
    for item in rareMetalsString.split(','): rareMetals.append(int(float(item)))
    for item in gemsString.split(','): gems.append(int(float(item)))
    for item in oilString.split(','): oil.append(int(float(item)))



    resource = 'N'
    if non_decreasing(gold) and len(gold) > 2:
        resource = 'gold'
    if non_decreasing(rareMetals) and len(rareMetals) > 2:
        resource = 'rareMetals'
    if non_decreasing(gems) and len(gems) > 2:
        resource = 'gems'
    if non_decreasing(oil) and len(oil) > 2:
        resource = 'oil'

    if resource == 'N':
        print('not yet, dropped out')
        return(0,'dropped out')

    returnCode,spendAmount = arbitrarySpendAmount(currentNation)
    if returnCode > 0: 
        print('not enough')
        return(0, 'not enough')

    # PLACE ORDER & Decrement wealth now
    currentNation.wealth -=  spendAmount
    investedPrice = getattr(PRICE_TRACKER,str(str(resource) + 'Price'))
    wait = 4
    currentNation.Nextmoves += str('Submitted' + ',' + 'investResource' + ',' + str(resource) + ',' +  str(spendAmount) + ',' +  str(investedPrice) + ',' +  str(wait)+ ':')
    db.session.commit()
    return(0,'success')


def investNation(currentNation,PRICE_TRACKER,db):

    # CHECK MAX MOVES
    returnCode = checkMoves(currentNation,'investCountry')[1]
    if returnCode > 0: 
        return(currentNation)

    # MORE LOGIC REQUIRED
    friendList = returnBestFriends(currentNation)
    friend = random.choice(friendList)
    if int(friend.level) < 30:
        print('no friends over 30 for ' + str(currentNation.country))
        return(0,'drop out')

    # Pick a random value to invest
    returnCode,spendAmount = arbitrarySpendAmount(currentNation)
    if returnCode > 0: 
        return(currentNation)


    # PLACE ORDER Decrement wealth now
    currentNation.wealth -= spendAmount
    friendsOriginalWealth = NATIONS.query.filter_by(country=friend.targetCountry).first().wealth
    wait = 4
    nextMove = str('Submitted' + ',' + 'investCountry' + ',' + str(friend.targetCountry) + ',' +  str(spendAmount) + ',' +  str(friendsOriginalWealth) + ',' +  str(wait)+ ':')
    currentNation.Nextmoves += nextMove
    return(0,'success')


def non_increasing(L):
    return all(x>=y for x, y in zip(L, L[1:]))

def non_decreasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))

def arbitrarySpendAmount(currentNation):
    creditsAvailable = int(currentNation.wealth)
    aggression       = int(currentNation.aggression)
    prudence         = int(currentNation.prudence)
    amount = 0

    # exit if credits too low
    if creditsAvailable < 10:
        return(1,amount)

    top = 0.7
    if aggression > prudence:
        top = 0.9
    if prudence > aggression:
        top = 0.5


    maxSpend = round((top) * creditsAvailable)

    if maxSpend > 1:
        amount = random.randint(1,maxSpend)
        return(0,amount)
    else:
        return(1,amount)
    return(1,amount)

# Get top 3 best friends by iterating array extracted from dict, then saving popping max val
def returnBestFriends(currentNation):
    friends = friendship.query.filter_by(country=currentNation.country).order_by(friendship.level).all()
    friendList = friends[-3:]
    return(friendList)

def returnPricks(currentNation):
    friends = friendship.query.filter_by(country=currentNation.country).order_by(friendship.level).all()
    friendList = friends[:3]
    return(friendList)



# Only attack if aggression high, prudence low, friendship low
def espionage(currentNation,aggression,prudence,db):

    # if friendship lower than 0 - espionage is possible.
    espionageThreshold = 0
    #----------------------
    # PROBABILITY LOGIC
    #----------------------
    hatersList = returnPricks(currentNation)
    prick = random.choice(hatersList)
    

    # ELIF SWITCH ATTACK PROBABILITY
    attackBias = 1
    if aggression > 70 and prudence < 30:
        attackBias = 4
    elif aggression > 70 and prudence < 50:
        attackBias = 5
    elif aggression > 65 and prudence < 50:
        attackBias = 6
    else:
        attackBias = 15

    attackProbability = random.randint(0, attackBias)


    # Only attack if really agressive, low prudence and frienship < 0
    if attackProbability == 1 and int(prick.level) < espionageThreshold:
        nextMove = str('espionage' + ',' + str(prick.targetCountry) + ':')
        currentNation.Nextmoves += nextMove
    return(0,'success')

# Perform this move to get RP if..
# AI has less RP than the average required for any tech
# AI has more than 100
# Degree of commitment is a factor of agression
# Wealth invested is a percentage determined by intesnsity

def gainResearchPoints(currentNation,averageRPOne,AverageRPTwo,AverageRPThree,aggression,creativity,db):
    wealth    = int(currentNation.wealth)
    era       = currentNation.era
    rpOwned   = int(currentNation.RP)

    # CHECK MAX MOVES
    returnCode = checkMoves(currentNation,'gainResearch')[1]
    if returnCode > 0: 
        #print(str(currentNation.country) + ' ALREADY GAINING RESEARCHING  ######')
        return(0,'already researching')


    # Work out Average RP required for this Era
    rpAverageCost = int(averageRPCost(currentNation,averageRPOne,AverageRPTwo,AverageRPThree))

    # CHECK WEALTH
    if wealth < 100:
        return(0,'too poor to research')

    prob = 0

    if rpOwned < rpAverageCost: prob += 2

    if creativity > 80 and aggression > 60:
        prob += 4
    elif creativity > 70 and aggression > 50: 
        prob += 3
    elif creativity > 60:
        prob += 2
    elif creativity > 60:
        prob += 1

    researchProbability = prob + random.randint(0,2)
    #print('RESEARCH PROBABILITY: ' + str(researchProbability))
    # The two numbers are : INVESTMENT PERCENTAGE & WaitRounds
    if researchProbability > 6: # far below average
        intensity = 'Overtime'
        amount = round((25/100) * wealth)
        researchOrder = 'submitted' + ',' + 'gainResearch' + ',' + 'overtime' + ','  + '25' + ',' + '8' + ',' + str(amount) +  ':'
    elif researchProbability > 5: # quite a bit below average
        intensity = 'Hard'
        amount = round((15/100) * wealth)
        researchOrder = 'submitted' + ',' + 'gainResearch' + ',' + 'hard' + ','  + '15' + ',' + '6' + ',' + str(amount) +':'
    elif researchProbability > 4: # just under average
        intensity = 'Medium'
        amount = round((10/100) * wealth)
        researchOrder = 'submitted' + ',' + 'gainResearch' + ',' + 'medium' + ','  + '10' + ',' + '4' + ',' + str(amount) +':'
    elif researchProbability > 2: # has double required
        intensity = 'Soft'
        amount = 0
        researchOrder = 'submitted' + ',' + 'gainResearch' + ',' + 'soft' + ','  + '0' + ',' + '2' + ',' + str(amount) +':'
    else:
        return(currentNation)

    #Deduct in advance
    currentNation.wealth -= amount
    currentNation.Nextmoves += researchOrder
    print('##### RESEARCH ORDER SUBMITTED BY : ' + str(currentNation.country))
    db.session.commit()

    return(0,'success')

def researchTechnology(currentNation,era,creativity ,averageRPOne,AverageRPTwo,AverageRPThree,myTech,db):
    wealth        = int(currentNation.wealth)
    era           = currentNation.era
    rpOwned       = currentNation.RP
    rpAverageCost = int(averageRPCost(currentNation,averageRPOne,AverageRPTwo,AverageRPThree))

    # CHECK MAX MOVES
    returnCode = checkMoves(currentNation,'research')[1]
    if returnCode > 0: 
        #print(str(currentNation.country) + ' ALREADY RESEARCHING  ######')
        return(0,'already researching')


    one    = int(myTech.oneP)
    two    = int(myTech.twoP)
    three  = int(myTech.threeP)
    four   = int(myTech.fourP)
    five   = int(myTech.fiveP)

    # If AI is behind on development (say 30% of average) then do research
    myAverageCompletion = (one +  two + three + four + five)/5
    averageCompletionForAll = int(averageResearchCompletion(currentNation,era,db))
    

    # print('average Cost             : ' + str(rpAverageCost))
    # print('Rp Owned                 : ' + str(rpOwned))
    # print('myAverageCompletion      : ' + str(myAverageCompletion))
    # print('averageCompletionForAll  : ' + str(averageCompletionForAll))
    # print('one' + str(one))

    # Sum up probabilities 
    researchTechProbability = 0
    if myAverageCompletion < (0.70 * averageCompletionForAll):
        researchTechProbability += 3

    if creativity > 80:
        researchTechProbability += 3

    if creativity > 67:
        researchTechProbability += 2
    if creativity > 50:
        researchTechProbability += 1
    if rpOwned > (0.1 * rpAverageCost):
        researchTechProbability += 2

    if rpOwned > (0.8 * rpAverageCost):
        researchTechProbability += 5

    researchTechProbability += random.randint(0,2)

    if researchTechProbability > 2:
        # Get the index key for the lowest researched tech stream
        # This could no doubt be done in a loop...lazy coding but it works
        choiceArray = []
        if one < 100:
            choiceArray.append(['one','oneRp'])
        if two < 100:
            choiceArray.append(['two','twoRp'])
        if three < 100:
            choiceArray.append(['three','threeRp'])
        if four < 100:
            choiceArray.append(['four','fourRp'])
        if five < 100:
            choiceArray.append(['five','fiveRp'])

        if len(choiceArray) < 1:
            advanceMessage = advanceEra(currentNation,db)
            return(0,'complete')


        # Sometimes wont always start from left to right
        targetTech        = random.choice(choiceArray)
        techKey           = targetTech[1]
        requiredRow       = db.session.query(techEraCost).filter_by(era=era).first()
        required          = getattr(requiredRow,techKey)
        techChoice        = getattr(myTech,targetTech[0])
        nextMove = str('Submitted' + ',' + 'research' + ',' + str(era) + ',' +  str(techChoice) + ',' +  str(techKey) + ',' +  str(required)+ ':')
        #PLACE ORDER 
        currentNation.Nextmoves += nextMove
        db.session.commit()

    return(0,'complete')


def advanceEra(currentNation,db):
    
    # CHECK MAX MOVES
    returnCode = checkMoves(currentNation,'advanceEra')[1]
    if returnCode > 0: 
        return(0,'already selected advance era')
    myTech  = db.session.query(techAssets).filter_by(country=currentNation.country,era=currentNation.era).first()

    techOne    = myTech.oneP
    techTwo    = myTech.twoP
    techThree  = myTech.threeP
    techFour   = myTech.fourP
    techFive   = myTech.fiveP


    # Only upgrade if AI has completed all tech streams 5 x 100% completion ==500
    total      = int(techOne) + int(techTwo) + int(techThree) + int(techFour) + int(techFive)
    if total < 500:
        print(str(currentNation.country) +  'not enough to advance era')
        return(0, 'not enough to advance era')

    # Get Next era
    era = currentNation.era
    nextEraRow = db.session.query(techEras).filter_by(era=era).first()
    nextEra = nextEraRow.nextEra

    # Place Order
    currentNation.Nextmoves += 'advanceEra' + ':'
    db.session.commit()
    currentNation.notes = " "
    db.session.commit()
    print(currentNation.notes)    
    
    return(0,'success')




def averageRPCost(currentNation,averageRPOne,AverageRPTwo,AverageRPThree):
    era = currentNation.era
    if era == 'INDUSTRIAL REVOLUTION':
        rpAverageCost = averageRPOne
    if era == 'INFORMATION AGE':
        rpAverageCost = AverageRPTwo
    if era == 'SECOND ENLIGHTENMENT':
        rpAverageCost = AverageRPThree
    return(rpAverageCost)

def averageResearchCompletion(currentNation,era,db):
    completionArray   = []
    techObject = db.session.query(techAssets).filter_by(era=era).all()
    for item in techObject:
        completionArray.append(item.oneP)
        completionArray.append(item.twoP)
        completionArray.append(item.threeP)
        completionArray.append(item.fourP)
        completionArray.append(item.fiveP)

    AverageCompletion   = round(sum(completionArray)/len(completionArray))

    return(AverageCompletion)

def getAverages():
    nations = NATIONS.query.all()
    mightArray       = []
    wealthArray      = []
    knowledgeArray   = []
    influenceArray   = []
    for nation in nations:
        mightArray.append(int(nation.might))
        wealthArray.append(int(nation.wealth))
        knowledgeArray.append(int(nation.KP))
        influenceArray.append(int(nation.influence))

    averageMight     = sum(mightArray)/len(mightArray)
    averageWealth    = sum(wealthArray)/len(wealthArray)
    averageKnowledge = sum(knowledgeArray)/len(knowledgeArray)
    averageInfluence = sum(influenceArray)/len(influenceArray)
    return(averageMight,averageWealth,averageKnowledge,averageInfluence)



