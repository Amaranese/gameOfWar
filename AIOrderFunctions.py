import sys
import time
import copy
import random

from gameConquest_utilities  import checkMoves as checkMoves

# TO DO ------



# Need to make buying more sophisticated rather than chosing a random commodity
# Remember to deduct might from hard drill
# Buffer drill by tech level 

def setAIMoves(index,currentNation,ARRAY_DICT):
    NATION_ARRAY   = ARRAY_DICT['NATION_ARRAY']
    PRICE_TRACKER  = ARRAY_DICT['PRICE_TRACKER']
    WAR_BRIEFING   = ARRAY_DICT['WAR_BRIEFING']
    TECH_MAP       = ARRAY_DICT['TECH_MAP']

    # Capping AI at one for now 
    moveLimit    = int(currentNation[0]['Special']['moveLimit'])
    aggression   = currentNation[0]['Special']['aggression']
    creativity   = currentNation[0]['Special']['creativity']
    materialism  = currentNation[0]['Special']['materialism']
    prudence     = currentNation[0]['Special']['prudence']
    wealth       = currentNation[0]['Finance']['wealth'] 


    
    for moveNumber in range(1, 10):
        moves = checkMoves(currentNation,"%^")[0]
        #Ensure no countries take more moves than the limit
        while checkMoves(currentNation,"%^")[0] > 1:
            bias = calculateBias(currentNation,materialism,aggression,creativity,prudence)

            # HAS FINANCE BIAS
            if bias == 0:
                # GAMBLE 
                currentNation = gamble(currentNation)
                # BUY
                currentNation = aiBuy(PRICE_TRACKER,currentNation,materialism)
                # SELL
                currentNation = aiSell(PRICE_TRACKER,currentNation,aggression,materialism)
                # Invest Resource
                currentNation = investResource(currentNation,PRICE_TRACKER)
                # Invest in nation
                currentNation = investNation(currentNation,PRICE_TRACKER,NATION_ARRAY)

            # HAS BIAS TOWARDS WAR
            if bias == 1:
                # TODO: Add logic
                currentNation = drill(currentNation,NATION_ARRAY)
                # BUILD
                currentNation = build(currentNation,WAR_BRIEFING,aggression,materialism)
                # SCRAP
                currentNation = scrap(currentNation,WAR_BRIEFING,NATION_ARRAY)
                # ESPIONAGE~
                currentNation = espionage(currentNation,NATION_ARRAY,aggression,prudence)
           
            # HAS BIAS TOWARDS SCIENCE
            if bias == 2:

                currentNation = advanceEra(currentNation,NATION_ARRAY,aggression,TECH_MAP)
                currentNation = gainResearchPoints(currentNation,NATION_ARRAY,aggression,TECH_MAP)
                currentNation = researchTechnology(currentNation,NATION_ARRAY,aggression,TECH_MAP)


    # If No moves, then pass
    if len(currentNation[0]['Nextmoves']) == 0:
        currentNation[0]['Nextmoves']= [['pass']]
        
    return(currentNation)

def calculateBias(currentNation,materialism,aggression,creativity,prudence):
    # Calculate bias values
    wealth       = currentNation[0]['Finance']['wealth']
    financeBias  = materialism + random.randint(0,100)
    warBias      = aggression  + random.randint(0,100)
    scienceBias  = creativity  + random.randint(0,100)
    politicsBias = prudence    + random.randint(0,100)
    values = (financeBias,warBias,scienceBias)
    bias = values.index(max(values))
    return(bias)



def build(currentNation,WAR_BRIEFING,aggression,materialism):


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
        wealth               = currentNation[0]['Finance']['wealth'] 
        aggressionAdjusted   = (currentNation[0]['Special']['aggression']) / 100
        era                  = currentNation[0]['Tech']['era']

        allowedAssets = []
        allowedAssets = allowedTech(currentNation)
        unit = random.choice(allowedAssets)

        price      = WAR_BRIEFING['weapons'][era][unit][2]
        wait       = WAR_BRIEFING['weapons'][era][unit][3]
        bonusMight = WAR_BRIEFING['weapons'][era][unit][4]

        maxpurchase = int(wealth // price)
        adjusted    = round((aggressionAdjusted * maxpurchase))

        if adjusted > 0:
            maxBuy = round(random.randint(adjusted, maxpurchase))
        elif maxpurchase > 0:
            maxBuy = round(random.randint(0,maxpurchase))
        else:
            # No money so skipping
            return(currentNation)
        
        # If they can't afford even one  
        if maxBuy < 1:
            print('cant afford')
            return(currentNation)

        purchaseAmount = random.randint(1,maxBuy)
        cost = purchaseAmount * price


        # Deduct cost & Place Order 
        currentNation[0]['Finance']['wealth'] -=  cost
        currentNation[0]['Nextmoves'] += [['submitted','WeaponsBuild',unit, purchaseAmount,wait,bonusMight]]
    return(currentNation)



def scrap(currentNation,WAR_BRIEFING,NATION_ARRAY):
    wealth               = currentNation[0]['Finance']['wealth'] 
    aggressionAdjusted   = (currentNation[0]['Special']['aggression']) / 100
    techLevel            = currentNation[0]['Tech']['level']
    wealthArray          = []
    allowedAssets        = []
    allowedAssets        = allowedTech(currentNation)
    unit                 = random.choice(allowedAssets)
    stock                = currentNation[0]['War']['weapons'][unit][1]
    era                  = currentNation[0]['Tech']['era']
    scrapProbability = 10


    # Check to see if current country is poorer than 80% of average
    for country in NATION_ARRAY: wealthArray.append(country[0]['Finance']['wealth'])
    averageWealth = round((sum(wealthArray)/len(wealthArray)))
    poor          = 0.6*averageWealth
    if wealth < poor: scrapProbability = 3

    if random.randint(0,scrapProbability) == 2 and stock > 0:
        # Pick random unit to scrap
        price        = WAR_BRIEFING['weapons'][era][unit][2]
        reducedMight = WAR_BRIEFING['weapons'][era][unit][4]
        adjusted     = round((aggressionAdjusted * stock))
        maxScrap     = round(random.randint(adjusted, stock))

        if stock < 1 or maxScrap < 1:
            print('none to scrap')
            print('stock :' + str(stock))
            print('maxscrap: ' + str(maxScrap))
            return(currentNation)

        scrapAmount = random.randint(1,maxScrap)
        valuation   = scrapAmount * price

        # Deducts units and places order 
        currentNation[0]['War']['weapons'][unit][1] -=  scrapAmount
        currentNation[0]['Nextmoves']               +=  [['WeaponsScrap',unit, scrapAmount,valuation,reducedMight]]
    return(currentNation)


def allowedTech(currentNation):
    # Get % research completion for each tech stream
    firstTech    = currentNation[0]['Tech']['researched']['one'][2]
    secondTech   = currentNation[0]['Tech']['researched']['two'][2]
    thirdTech    = currentNation[0]['Tech']['researched']['three'][2]
    fourthTech   = currentNation[0]['Tech']['researched']['four'][2]
    fifthTech    = currentNation[0]['Tech']['researched']['five'][2]

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
    if fourthTech > 99:
        allowedAssets.append('6')
        allowedAssets.append('7')
    if fifthTech > 99:
        allowedAssets.append('8')

    return(allowedAssets)





# DRILL IF MIGHT IS < 80% of Average
# Pick a military branch, save asset details to array, place order 
def drill(currentNation,NATION_ARRAY):

    returnCode = checkMoves(currentNation,'drill')[1]
    if returnCode > 0: 
        #print(str(currentNation[1]) + 'Already drilling')
        return(currentNation)

    # BUILD PROBABILITY
    #-----------------
    averageMight,averageWealth,averageKnowledge,averageInfluence = getAverages(NATION_ARRAY)
    might = currentNation[0]['War']['might']

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
        return(currentNation)


    unitOne      = currentNation[0]['War']['weapons']['1']
    unitTwo      = currentNation[0]['War']['weapons']['2']
    light        = unitOne[1] + unitTwo[1]
    
    unitThree    = currentNation[0]['War']['weapons']['3']
    unitFour     = currentNation[0]['War']['weapons']['4']
    unitFive     = currentNation[0]['War']['weapons']['5']
    core         = unitThree[1] + unitFour[1] + unitFive[1]
    
    unitSix      = currentNation[0]['War']['weapons']['6']
    unitSeven    = currentNation[0]['War']['weapons']['7']
    heavy        = unitSix[1] + unitSeven[1]
    
    unitEight    = currentNation[0]['War']['weapons']['8']
        
    branchChoiceArray = []

    if light > 1:
        branchChoiceArray.append('light')
    if core > 1:
        branchChoiceArray.append('core')
    if heavy > 1:
        branchChoiceArray.append('heavy')

    # in the event there are no units
    if len(branchChoiceArray) < 1:
        return(currentNation)

    branchChoice = random.choice(branchChoiceArray)

    # based upon selection
    if branchChoice == 'light':
        units = [('1',unitOne[1]),('2',unitTwo[1])]
        branch = 'Light Units'
    elif branchChoice == 'core':
        units = [('3',unitThree[1]),('4',unitFour[1]),('5',unitFive[1])]
        branch = 'Core Division'
    elif branchChoice == 'heavy':
        units = [('6',unitSix[1]),('7',unitSeven[1])]
        branch = 'Heavy Forces'
    else:
        return(currentNation)


    aggression          = currentNation[0]['Special']['aggression']
    augmentedAggresion  = random.randint(0,(100 + aggression))

    # Ive tilted this a bit more towards harder drilling: can amend later
    if augmentedAggresion > 120:
        exposure = 'hard'
    elif augmentedAggresion > 85:
        exposure = 'medium'
    else:
        exposure = 'soft'

    drillOrder = ['drill',branch,exposure, units]

    # Deduct units
    for unit in units:
        unit = unit[0]
        currentNation[0]['War']['weapons'][unit][1] = 0

    # Place Order
    currentNation[0]['Nextmoves'] += [drillOrder]
    return(currentNation)

# Probability of purchase depends how much the price is lower than average
def aiBuy(PRICE_TRACKER,currentNation,materialism):

    commodity = random.choice(('gold','gems','raremetals','oil'))
   
    averageCommodityPrice = PRICE_TRACKER[commodity]['average']
    if averageCommodityPrice == 0:
        averageCommodityPrice = 0.1
    percentageDecrease = ((PRICE_TRACKER[commodity]['average'] - PRICE_TRACKER[commodity]['price'])/averageCommodityPrice)
   
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
        price        = PRICE_TRACKER[commodity]['price']
        credits      = currentNation[0]['Finance']['wealth']
        aggression   = (currentNation[0]['Special']['aggression'] / 100)
        maxpurchase = int(credits // price)

        compensatedMax = round(aggression * maxpurchase)
        if compensatedMax < 1:
            currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [['pass']]
            return(currentNation)

        purchaseAmount = random.randint(1, compensatedMax)
        cost = purchaseAmount * price

        # Deduct cost & Place Order 
        currentNation[0]['Finance']['wealth'] = currentNation[0]['Finance']['wealth'] - cost
        currentNation[0]['Nextmoves']        = currentNation[0]['Nextmoves'] + [['buy',commodity, purchaseAmount]]
        
    return(currentNation)


def aiSell(PRICE_TRACKER,currentNation,aggression,materialism):

    commodity = random.choice(('gold','gems','raremetals','oil'))
    percentageIncrease = ((PRICE_TRACKER[commodity]['price'] - PRICE_TRACKER[commodity]['average'])/PRICE_TRACKER[commodity]['average'])
   
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
        price                  = PRICE_TRACKER[commodity]['price']
        myStock                = currentNation[0]['Finance'][commodity]
        aggressionPercentage   = (aggression / 100)

        compensatedMax = round(aggressionPercentage * myStock)
        if compensatedMax > myStock or compensatedMax < 1:
            return(currentNation)

        # purchase choice
        purchaseAmount = random.randint(1, compensatedMax)
        value = purchaseAmount * price
        # Deduct stock & Place Order 
        currentNation[0]['Finance'][commodity]   = currentNation[0]['Finance'][commodity] - purchaseAmount
        currentNation[0]['Nextmoves']            = currentNation[0]['Nextmoves'] + [['sell',commodity, purchaseAmount, value]]
        
    return(currentNation)


def gamble(currentNation):
    # Roughly 25% chance of having a gamble
    gambleAction = random.randint(0,10)
    if gambleAction < 3:

        returnCode,amount = arbitrarySpendAmount(currentNation)
        if returnCode > 0: 
            print('not enough')
            return(currentNation)
        currentNation[0]['Finance']['wealth'] = currentNation[0]['Finance']['wealth'] - amount
        currentNation[0]['Nextmoves']         = currentNation[0]['Nextmoves'] + [['gamble',amount]]

    return(currentNation)


def investResource(currentNation,PRICE_TRACKER):

    # CHECK MAX MOVES
    returnCode = checkMoves(currentNation,'investResource')[1]
    if returnCode > 0: 
        #print('Already invested or moves used up')
        return(currentNation)

    gold       = PRICE_TRACKER['gold']['history'][-3:]
    raremetals = PRICE_TRACKER['raremetals']['history'][-3:]
    gems       = PRICE_TRACKER['gems']['history'][-3:]
    oil        = PRICE_TRACKER['oil']['history'][-3:]

    resource = 'N'
    if non_decreasing(gold) and len(gold) > 2:
        resource = 'gold'
    if non_decreasing(raremetals) and len(raremetals) > 2:
        resource = 'raremetals'
    if non_decreasing(gems) and len(gems) > 2:
        resource = 'gems'
    if non_decreasing(oil) and len(oil) > 2:
        resource = 'oil'

    if resource == 'N':
        #print('dropped out')
        return(currentNation)

    returnCode,spendAmount = arbitrarySpendAmount(currentNation)
    if returnCode > 0: 
        print('not enough')
        return(currentNation)

    # PLACE ORDER & Decrement wealth now
    currentNation[0]['Finance']['wealth'] -=  spendAmount
    investedPrice = PRICE_TRACKER[resource]['price']
    wait = 4
    currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [['Submitted','investResource',resource,spendAmount,investedPrice,wait]]

    return(currentNation)


def investNation(currentNation,PRICE_TRACKER,NATION_ARRAY):

    # CHECK MAX MOVES
    returnCode = checkMoves(currentNation,'investCountry')[1]
    if returnCode > 0: 
        return(currentNation)

    # MORE LOGIC REQUIRED
    friendList = returnBestFriends(currentNation)
    friend = random.choice(friendList)
    if friend[0] < 30:
        return(currentNation)

    # Pick a random value to invest
    returnCode,spendAmount = arbitrarySpendAmount(currentNation)
    if returnCode > 0: 
        print('not enough')
        return(currentNation)

    # get index by using value as lookup
    for x in range(0,len(NATION_ARRAY)): 
        if NATION_ARRAY[x][1] == friend[1]:
            friendIndex = x

    # PLACE ORDER Decrement wealth now
    currentNation[0]['Finance']['wealth'] -= spendAmount
    friendsOriginalWealth = NATION_ARRAY[friendIndex][0]['Finance']['wealth']
    wait = 4
    currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [['Submitted','investCountry',friendIndex,spendAmount,friendsOriginalWealth,wait]]

    return(currentNation)


def non_increasing(L):
    return all(x>=y for x, y in zip(L, L[1:]))

def non_decreasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))

def arbitrarySpendAmount(currentNation):
    creditsAvailable = int(currentNation[0]['Finance']['wealth'])
    aggression       = currentNation[0]['Special']['aggression']
    prudence         = currentNation[0]['Special']['prudence']
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
    friendList = []
    friendshipArray = []

    for friend in currentNation[0]['Friendship']:
        friendshipArray.append((currentNation[0]['Friendship'][friend]['level'],friend))

    for x in range(0,3):
        allyValue =  max(friendshipArray,key=lambda item:item[0])[0]
        allyKey   =  max(friendshipArray,key=lambda item:item[0])[1]
        allyIndex = friendshipArray.index((allyValue,allyKey))
        friendList.append([allyValue,allyKey])
        friendshipArray.pop(allyIndex)

    return(friendList)

# Only attack if aggression high, prudence low, friendship low
def espionage(currentNation,NATION_ARRAY,aggression,prudence):

    # if friendship lower than 0 - espionage is possible.
    espionageThreshold = 0
    #----------------------
    # PROBABILITY LOGIC
    #----------------------
    maxHateArray = []
    for nation in currentNation[0]['Friendship']:
        maxHateArray.append(currentNation[0]['Friendship'][nation]['level'])
    minVal = min(maxHateArray)

    targetNation = ''
    for nation in currentNation[0]['Friendship']:
        if currentNation[0]['Friendship'][nation]['level'] == minVal:
            targetNation = nation
    

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


    #----------------------
    # ORDERS
    #----------------------

    # Only attack if really agressive, low prudence and frienship < 0
    if attackProbability == 1    and minVal < espionageThreshold:
        # get index 
        indexList = []
        for item in NATION_ARRAY:
            indexList.append(item[1])
        targetNationIndex = indexList.index(targetNation)

        espionageOrder = ['espionage',targetNationIndex]
        currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [espionageOrder]
    return(currentNation)

# Perform this move to get RP if..
# AI has less RP than the average required for any tech
# AI has more than 100
# Degree of commitment is a factor of agression

def gainResearchPoints(currentNation,NATION_ARRAY,aggression,TECH_MAP):
    wealth    = currentNation[0]['Finance']['wealth']
    era       = currentNation[0]['Tech']['era']
    rpOwned   = currentNation[0]['Tech']['research points']

    # Work out Average RP required for this Era
    rpAverageCost = averageRPCost(TECH_MAP,era)

    # CHECK MAX MOVES
    returnCode = checkMoves(currentNation,'gainResearch')[1]
    if returnCode > 0: 
        #print(str(currentNation[1]) + 'Already researching')
        return(currentNation)

    # CHECK WEALTH
    if wealth < 100:
        return(currentNation)


    researchProbability = (rpAverageCost/rpOwned) +(aggression/100)


    # ELIF SWITCH MAX VALUE SELECTED
    if researchProbability > 4: # far below average
        intensity = 'Overtime'
        investmentPercentage = 25
        rounds = 8
    elif researchProbability > 1.8: # quite a bit below average
        intensity = 'Hard'
        investmentPercentage = 15
        rounds = 6
    elif researchProbability > 1: # just under average
        intensity = 'Medium'
        investmentPercentage = 10
        rounds = 4
    elif researchProbability > 0.8: # has double required
        intensity = 'Soft'
        investmentPercentage = 0
        rounds = 2
    else:
        return(currentNation)

    amount = round((investmentPercentage/100) * wealth)
    #Deduct in advance
    currentNation[0]['Finance']['wealth']-= amount

    researchOrder = ['submitted','gainResearch',intensity,investmentPercentage,rounds,amount]
    currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [researchOrder]
    # print(currentNation[1])
    # print(currentNation[0]['Nextmoves'])
    return(currentNation)

def researchTechnology(currentNation,NATION_ARRAY,aggression,TECH_MAP):
    wealth        = currentNation[0]['Finance']['wealth']
    era           = str(currentNation[0]['Tech']['era'])
    researched    = currentNation[0]['Tech']['researched']
    rpOwned       = currentNation[0]['Tech']['research points']
    rpAverageCost = averageRPCost(TECH_MAP,era)

    # CHECK MAX MOVES
    returnCode = checkMoves(currentNation,'research')[1]
    if returnCode > 0: 
       #print(str(currentNation[1]) + ' already researching..')
        return(currentNation)

    # WORK OUT PROBABILITY FOR INVESTING IN TECH RESEARCH
    # If AI is behind on development (say 30% of average) then do research
    averageCompletion = averageResearchCompletion(currentNation)
    #print('average completion ' + str(averageCompletion))
    
    researchTechProbability = 0
    if averageCompletion < 50:
        researchTechProbability = 4

    if rpOwned > (0.8 * rpAverageCost):
        researchTechProbability += 2

    researchTechProbability += random.randint(0,5)
    

    if researchTechProbability > 4:
        # Get the index key for the lowest researched tech stream
        # This could no doubt be done in a loop...lazy coding but it works
        one    = currentNation[0]['Tech']['researched']['one'][2]
        two    = currentNation[0]['Tech']['researched']['two'][2]
        three  = currentNation[0]['Tech']['researched']['three'][2]
        four   = currentNation[0]['Tech']['researched']['four'][2]
        five   = currentNation[0]['Tech']['researched']['five'][2]
        selectionArray = [one,two,three,four,five]

        selectionIndex = selectionArray.index(min(selectionArray))
        choice = ['one','two','three','four','five'][selectionIndex]

        # Sometimes wont always start from left to right
        randomChoice = random.randint(0,1)
        if randomChoice == 1:
            choice = random.choice(['one','two','three','four','five'])

        required         = TECH_MAP['EraCost'][era][choice]['rp']
        myTechPoints     = researched[choice][0]
        remaining        = required - myTechPoints

        if myTechPoints > (required - 1):
            print(str(currentNation[1]) + ' maxed out all tech streams. ' + str(selectionArray))
            return(currentNation)

        #PLACE ORDER 
        currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + [['submitted','research',era, choice,required]]

    return(currentNation)


def advanceEra(currentNation,NATION_ARRAY,aggression,TECH_MAP):
    era           = str(currentNation[0]['Tech']['era'])
    one           = currentNation[0]['Tech']['researched']['one'][2]
    two           = currentNation[0]['Tech']['researched']['two'][2]
    three         = currentNation[0]['Tech']['researched']['three'][2]
    four          = currentNation[0]['Tech']['researched']['four'][2]
    five          = currentNation[0]['Tech']['researched']['five'][2]

    # CHECK MAX MOVES
    returnCode = checkMoves(currentNation,'advanceEra')[1]
    if returnCode > 0: 
        return(currentNation)

    # Only upgrade if AI has completed all tech streams 5 x 100% completion ==500
    total = one + two + three + four + five
    if total < 500:
        return(currentNation)

    currentNation[0]['Nextmoves'] = currentNation[0]['Nextmoves'] + ['advanceEra']

    return(currentNation)




def averageRPCost(TECH_MAP,era):
    rpCostArray = []
    for techChoice in TECH_MAP['EraCost'][era].values():
        rpCostArray.append(techChoice['rp'])
    rpAverageCost = sum(rpCostArray)/len(rpCostArray)
    return(rpAverageCost)

def averageResearchCompletion(currentNation):
    completionArray = []
    for techChoice in currentNation[0]['Tech']['researched'].values():
        completionArray.append(techChoice[-1])

    AverageCompletion = sum(completionArray)/len(completionArray)
    return(AverageCompletion)

def getAverages(NATION_ARRAY):
    mightArray       = []
    wealthArray      = []
    knowledgeArray   = []
    influenceArray   = []
    for nation in NATION_ARRAY:
        mightArray.append(nation[0]['War']['might'])
        wealthArray.append(nation[0]['Finance']['wealth'])
        knowledgeArray.append(nation[0]['Tech']['knowledge'])
        influenceArray.append(nation[0]['Politics']['influence'])

    averageMight = sum(mightArray)/len(mightArray)
    averageWealth = sum(wealthArray)/len(wealthArray)
    averageKnowledge = sum(knowledgeArray)/len(knowledgeArray)
    averageInfluence = sum(influenceArray)/len(influenceArray)
    return(averageMight,averageWealth,averageKnowledge,averageInfluence)



