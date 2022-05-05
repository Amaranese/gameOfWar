import itertools
from universe.classes import PTc,warDataBase,NATIONS,friendship,warAssets,techAssets,gameTracker,techEras

# returns how many moves remain and error code.
def checkMoves(myNation,duplicateToCheck):
    mlimit = int(myNation.moveLimit)
    moveArray = myNation.Nextmoves.split(':')
    pendingCount = 0
    mvs = 0
    for item in moveArray:
        if 'pending' in item:
            pendingCount +=1
        if len(item) > 0:
            mvs += 1


    movesLeft = int(mlimit-mvs+pendingCount)
    if movesLeft < 1: 
        return(movesLeft,1)
    for item in moveArray:
        if duplicateToCheck in item:
            return(movesLeft,2)
    return(movesLeft,0)


def buyResource(myNation,purchaseAmount,commodity,PT,db):
    credits = int(myNation.wealth)
    commodity = commodity
    purchaseAmount = int(purchaseAmount)
    commodityPrice = 99999 


    for p in PT:
        if commodity == 'gold':
            commodity = 'gold,goldPrice'
            commodityPrice = p.goldPrice
        if commodity == 'rareMetals':
            commodity = 'rareMetals,rareMetalsPrice'
            commodityPrice = p.rmPrice
        if commodity == 'gems':
            commodity = 'gems,gemsPrice'
            commodityPrice = p.gemsPrice
        if commodity == 'oil':
            commodity = 'oil,oilPrice'
            commodityPrice = p.oilPrice

    cost = purchaseAmount * commodityPrice

    if cost > credits:
        print('Not enough credits, sorry \n')
        return(1,'Not enough credits, sorry')
    if purchaseAmount < 1:
        print('Enter a correct amount \n')
        return(1,'Enter a correct amount')

    # Deduct cost & Place Order 
    myNation.wealth -= cost
    myNation.Nextmoves += str('buy' + ',' + str(commodity) + ',' + str(purchaseAmount) + ':')
    print(myNation)
    db.session.commit()
    return(0,'Thanks for your purchase')



def sellResource(myNation,sellAmount,commodity,PT,db):
    credits = int(myNation.wealth)
    sellAmount = int(sellAmount)
    commodity = commodity

    if commodity == 'gold':
        myStock = myNation.gold
        price   = PT.goldPrice
    if commodity == 'rareMetals':
        myStock = myNation.rareMetals
        price   = PT.rmPrice
    if commodity == 'gems':
        myStock = myNation.gems
        price   = PT.gemsPrice
    if commodity == 'oil':
        myStock = myNation.oil
        price   = PT.oilPrice

    sellAmount = sellAmount

    value = sellAmount * price

    if sellAmount > myStock:
        print('Not enough stock, sorry \n')
        return(1,'Not enough sock, sorry')
    if sellAmount < 1:
        print('Enter a correct amount \n')
        return(1,'Enter a correct amount')

    # Ridiculous I have to do this ....

    # setattr(PT, "goldPrice", 200)
    # db.session.commit()


    if commodity == 'gold':
        myNation.gold -= sellAmount
    if commodity == 'rareMetals':
        myNation.rareMetals -= sellAmount
    if commodity == 'gems':
        myNation.gems -= sellAmount
    if commodity == 'oil':
        myNation.oil -= sellAmount

    
    myNation.Nextmoves += str('sell' + ',' + str(commodity) + ',' + str(sellAmount) + ',' +  str(value) + ':')
    print(myNation)
    db.session.commit()
    return(0,'Thanks for your purchase')



def investCountryFunction(myNation,investAmount,selected,db):
    credits = int(myNation.wealth)
    investAmount = int(investAmount)

    if investAmount > credits:
        print('Not enough credits, sorry \n')
        return(1,'Not enough credits, sorry')
    if investAmount < 1:
        print('Enter a correct amount \n')
        return(1,'Enter a correct amount')


    # PLACE ORDER
    # Decrement wealth now
    myNation.wealth -= investAmount
    nationsOriginalWealth = selected.wealth
    wait = 4
    myNation.Nextmoves += str('Submitted' + ',' + 'investCountry' + ',' + str(selected.country) + ',' +  str(investAmount) + ',' +  str(nationsOriginalWealth) + ',' +  str(wait)+ ':')
    db.session.commit()
    print(myNation)

    return(0,str('Thanks ' + str(selected.country) + ' will appreciate your investment \n ' + str(' Your profits will be paid into your account after ' + str(wait) + ' moves.')))



def investResourceFunction(myNation,investAmount,commodityPrice,commodityToSubmit,db):
    credits = int(myNation.wealth)
    resource = commodityToSubmit
    investAmount = int(investAmount)
    commodityPrice = commodityPrice

    if investAmount > credits:
        print('Not enough credits, sorry \n')
        return(1,'Not enough credits, sorry')
    if investAmount < 1:
        print('Enter a correct amount \n')
        return(1,'Enter a correct amount')


    # PLACE ORDER
    # Decrement wealth now
    myNation.wealth -= investAmount
    wait = 4


    myNation.Nextmoves += str('Submitted' + ',' + 'investResource' + ',' + str(resource) + ',' +  str(investAmount) + ',' +  str(commodityPrice) + ',' +  str(wait)+ ':')
    db.session.commit()
    print(myNation)
    return(0,str('Thanks we appreciate your investment \n ' + str(' Your profits will be paid into your account after ' + str(wait) + ' moves.')))



def drill(myNation,myWar,division,intensity,db):
    division = division
    intensity = intensity
    # Check and deduct Units
    if division == 'Light Units':
        if int(myWar.wOneAmount) + int(myWar.wTwoAmount) < 1:
            return(1,'No light forces to train, sorry')
        
        drillOrder = 'drill' + ',' + 'Light Units' + ',' + str(intensity) + ',' + str(myWar.wOneAmount) + ',' + str(myWar.wTwoAmount) + ':'
        myWar.wOneAmount = 0
        myWar.wTwoAmount = 0
    if division == 'Core Division':
        if int(myWar.wThreeAmount) + int(myWar.wFourAmount)  + int(myWar.wFiveAmount) < 1:
            return(1,'No core forces to train, sorry')

        
        drillOrder = 'drill' + ',' + 'Core Division' + ',' + str(intensity) + ',' + str(myWar.wThreeAmount) + ',' + str(myWar.wFourAmount) + ',' + str(myWar.wFiveAmount) +':'
        myWar.wThreeAmount =0 
        myWar.wFourAmount  =0
        myWar.wFiveAmount  =0
    if division == 'Heavy Forces':
        if int(myWar.wSixAmount) + int(myWar.wSevenAmount) < 1:
            return(1,'No heavy units to train, sorry')
        
        drillOrder = 'drill' + ',' + 'Heavy Forces' + ',' + str(intensity) + ',' + str(myWar.wSixAmount) + ',' + str(myWar.wSevenAmount) + ':'
        myWar.wSixAmount   = 0
        myWar.wSevenAmount = 0

    db.session.commit()

    myNation.Nextmoves += drillOrder
    db.session.commit()
    print(myNation)


    return(0,str('Your ' + str(division) + ' will embark on training and be returned to you next round.'))


def buildFunction(myNation,myWar,unitSelected,priceRow,buildAmount,db):
    credits = int(myNation.wealth)
    name    = unitSelected
    price   = int(priceRow.price)
    wait    = priceRow.buildTime
    bonusMight = priceRow.mightBonus

    # Get my tech row
    myTech  = db.session.query(techAssets).filter_by(country=myNation.country,era=myNation.era).first()
    # Price row is the row that this tech asset belongs to
    # Key is column on wardatabase  (returns number 1-8)
    key     = priceRow.unit_key
    purchaseAmount = int(buildAmount)


    # CHECK TECH LEVEL
    if key == 1:
        warKey = 'wOneAmount'
        print('No requirements')
    elif key == 2:
        warKey = 'wTwoAmount'
        if myTech.oneP < 100:
            return(1,str('Tech level too low, you need to unlock ' +str(myTech.one)))
    elif key == 3:
        warKey = 'wThreeAmount'
        if myTech.twoP < 100:
            return(1,'Tech level too low, you need to unlock ' +str(myTech.two))
    elif key == 4:
        warKey = 'wFourAmount'
        if myTech.threeP < 100:
            return(1,'Tech level too low, you need to unlock ' + str(myTech.three))
    elif key == 5:
        warKey = 'wFiveAmount'
        if myTech.threeP < 100:
            return(1,'Tech level too low, you need to unlock ' +str(myTech.three))
    elif key == 6:
        warKey = 'wSixAmount'
        if myTech.threeP < 100:
            return(1,'Tech level too low, you need to unlock ' +str(myTech.three))
    elif key == 7:
        warKey = 'wSevenAmount'
        if myTech.fourP < 100:
            return(1,'Tech level too low, you need to unlock ' +str(myTech.four))
    elif key == 8:
        warKey = 'wEightAmount'
        if myTech.fiveP < 100:
            return(1,'Tech level too low, you need to unlock ' +str(myTech.five))

    cost = purchaseAmount * price

    if cost > credits:
        return(1,'Not enough credits, sorry')
    if purchaseAmount < 1:
        return(1,'Enter a correct amount')

    # Deduct and place order
    myNation.wealth -= cost
    myNation.Nextmoves += str('Submitted' + ',' + 'WeaponsBuild' + ',' + str(unitSelected) + ',' +  str(purchaseAmount) + ',' +  str(wait) + ',' +  str(bonusMight) + ',' + str(warKey) + ':')
    print(myNation)
    db.session.commit()
    return(0,str('Thanks for buying  ' + str(unitSelected) ))


def scrapFunction(myNation,myWar,unitSelected,priceRow,scrapAmount,db):
    credits     = int(myNation.wealth)
    name        = unitSelected
    price       = int(priceRow.price)
    wait        = priceRow.buildTime
    bonusMight  = priceRow.mightBonus
    key         = priceRow.unit_key
    key         = str(key)
    indexDict   = {'1':'wOneAmount','2':'wTwoAmount','3':'wThreeAmount','4':'wFourAmount','5':'wFiveAmount','6':'wSixAmount','7':'wSevenAmount','8':'wEightAmount'}
    keyloc      = indexDict[key]
    stockOwned  = getattr(myWar, keyloc)
    scrapAmount = int(scrapAmount)

    print('debug')
    print('ordered: '+ str(name))
    print('key: ' + str(key))
    print('Amount: ' + str(scrapAmount))
    print('owned: ' + str(stockOwned))
    

    valuation = scrapAmount * price

    if scrapAmount > stockOwned:
        return(1,'you dont have enough stock, sorry')
    if scrapAmount < 1:
        return(1,'Enter a correct amount')

    # Deduct stock and place order
    setattr(myWar, keyloc, (stockOwned - scrapAmount))
    myNation.Nextmoves += str('Submitted' + ',' + 'WeaponsScrap' + ',' + str(unitSelected) + ',' +  str(scrapAmount) + ',' +  str(valuation) + ',' +  str(bonusMight)+ ':')
    print(myNation)
    db.session.commit()
    return(0,str('Thanks for scrapping  ' + str(unitSelected) + ' you will recieve your funds next round' ))


def espionage(myNation,targetNation,friendshipLevel,db):

    # CHECK FRIENDSHIP EXCEEDS THRESHOLD
    espionageThreshold = 0
    if int(friendshipLevel) > espionageThreshold:
        return(1, str('sorry, your friendship with' + str(targetNation) + ' is ' + str(friendshipLevel) + '. Espionage is only available when friendship deteriorates below < ' + str(espionageThreshold) + '. \n Please check international relations option to view friendship levels.'))

    myNation.Nextmoves += 'espionage' + ',' + str(targetNation) + ':'
    db.session.commit()
    print(myNation)
    return(0,str('Espionage orders against ' + str(targetNation) + ' given.'))


    # espionageOrder = ''
    # espionageChoice = ""
    # while covertChoice != 'XYZFFJJJJJJ':
    #     print('[E] Economy')
    #     print('[M] Military')
    #     print('[S] Science')
    #     print('[P] Politics')
    #     print('[I] More Info')
    #     print('[R] Return')
    #     espionageChoice = input('What branch of the ' + str(NationChoice) + ' government do you wish to infiltrate? \n').upper()
    #     clearScreen()
    #     if espionageChoice == 'E':
    #         espionageOrder = ['espionage',NationChoice,'economy']
    #         break
    #     if espionageChoice == 'M':
    #         espionageOrder = ['espionage',NationChoice,'military']
    #         break
    #     if espionageChoice == 'S':
    #         espionageOrder = ['espionage',NationChoice,'science']
    #         break
    #     if espionageChoice == 'P':
    #         espionageOrder = ['espionage',NationChoice,'politics']
    #         break
    #     if espionageChoice == 'I':
    #         fast_print('Espionage lets you steal enemy assets, this gains benefits but can be risky and lead to war \n')
    #         print('Depending on what branch you target, will result in corresponding gains i.e. . \n')
    #         print('As your rank increases you can chose to target a specific branch of the government. \n')
    #         print('Military  : Might ++')
    #         print('******IF YOUR GAMBIT FAILS, THE CONSEQUENCES COULD BE SEVERE****')
    #         input('Enter to continue \n')
    #     if espionageChoice == 'R' or espionageChoice == '':
    #         return(myNation)


def advanceEra(playerTech,myNation,db):
    era        = myNation.era

    techOne    = playerTech.oneP
    techTwo    = playerTech.twoP
    techThree  = playerTech.threeP
    techFour   = playerTech.fourP
    techFive   = playerTech.fiveP

    total      = int(techOne) + int(techTwo) + int(techThree) + int(techFour) + int(techFive)

    if total < 500:
        return(1,'Not enough Development progress. Please complete development of all five tech stacks first.')

    era = myNation.era
    nextEraRow = db.session.query(techEras).filter_by(era=era).first()
    nextEra = nextEraRow.nextEra

    # Place Order
    myNation.Nextmoves += 'advanceEra' + ':'
    
    db.session.commit()
    return(0, str(str(myNation.country) + ' will progress to ' + str(nextEra) ))

def researchTech(techChoice,techKey,techCost,pointsEarned,myNation,playerTech,db):
    era        = myNation.era
    techChoice = techChoice
    # Get points earned for each stack
    required = int(techCost)
    myTechPoints = int(pointsEarned)


    if myTechPoints > (required - 1):
        return(1,'You have already maxed this Tech stream. Please try another. Once all streams complete, you can advance to the next era.')

    myNation.Nextmoves += str('Submitted' + ',' + 'research' + ',' + str(era) + ',' +  str(techChoice) + ',' +  str(techKey) + ',' +  str(required)+ ':')
    print(myNation)
    db.session.commit()
    
    return(0,str('You will now begin researching ' + str(techChoice)))


def researchGrant(myNation,intensity,db):
    intensity = str(intensity)
    wealth = int(myNation.wealth)

    if wealth < 100:
        return(1,'You dont have enough money to engage in research.')


    if intensity == 'soft':
        amount = 0
        researchOrder = 'submitted' + ',' + 'gainResearch' + ',' + 'soft' + ','  + '0' + ',' + '2' + ',' + str(amount) +':'
    if intensity == 'medium':
        amount = round((10/100) * wealth)
        researchOrder = 'submitted' + ',' + 'gainResearch' + ',' + 'medium' + ','  + '10' + ',' + '4' + ',' + str(amount) +':'
    if intensity == 'hard':
        amount =round((15/100)*wealth )
        researchOrder = 'submitted' + ',' + 'gainResearch' + ',' + 'hard' + ','  + '15' + ',' + '6' + ',' + str(amount) +':'
    if intensity == 'overtime':
        amount =round((25/100)*wealth )
        researchOrder = 'submitted' + ',' + 'gainResearch' + ',' + 'overtime' + ','  + '25' + ',' + '8' + ',' + str(amount) +  ':'

    # Deduct credits
    myNation.wealth -= amount
    myNation.Nextmoves += researchOrder
    db.session.commit()

    print(myNation)
    
    return(0,str('Your ' + str(intensity) + ' research grant will award you points each round that can be spent on developing technology.'))


