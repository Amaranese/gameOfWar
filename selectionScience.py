# All WAR Menu Function

from gameConquest_utilities import slow_print as slow_print
from gameConquest_utilities import med_print as med_print
from gameConquest_utilities import fast_print as fast_print
from gameConquest_utilities import superfast_print as superfast_print
from gameConquest_utilities import clearScreen as clearScreen
from gameConquest_utilities  import preferencePrint as preferencePrint
from gameConquest_utilities  import checkMoves as checkMoves
from gameConquest_utilities  import selectCountry as selectCountry




def techMenu(myNation,year,PRICE_TRACKER,TECH_MAP):
    flag = ''
    techSelection = ' '
    while techSelection != 'XYZFFJJJJJJ':
        clearScreen()
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('        WELCOME TO THE TECHNOLOGY INSTITUE %       ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team                : ' + str(myNation[1]))
        print('Year                   : ' + str(year))
        print('Knowledge       (KP)   : ' + str(myNation[0]['Tech']['knowledge']) )
        print('Era                    : ' + str(myNation[0]['Tech']['era']))
        print('Research Points (RP)   : ' + str(myNation[0]['Tech']['research points']) ) 
        print('Level                  : ' + str(myNation[0]['Tech']['level']))
        print(' ')
        print('')
        flag = showAssets(myNation,year,flag)
        print('')
        print('[A] Academia')
        print('[R] Research')
        print('[S] Show Tech Assets')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        techSelection = str(input('Please chose an option \n')).upper()
        if techSelection == 'A':
            print('Not ready yet..')
            #myNation = academiaMenu(myNation,year,TECH_MAP)
        if techSelection == 'R':
            myNation = researchMenu(myNation,year,TECH_MAP)
        if techSelection == 'O':
            fast_print('not ready')
        if techSelection == 'T':
            fast_print('not ready')
        if techSelection == 'T':
            fast_print('not ready')
        if techSelection == 'S':
            flag = 'yes'
        if techSelection == 'R' or techSelection == '':
            return(myNation)
    return(myNation)


def academiaMenu(myNation,year,TECH_MAP):
    flag = ''
    academicSelection = ' '
    while academicSelection != 'XYZFFJJJJJJ':
        clearScreen()
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('        + x % THIS IS ACADEMIA + X %               ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team                : ' + str(myNation[1]))
        print('Year                   : ' + str(year))
        print('Knowledge       (KP)   : ' + str(myNation[0]['Tech']['knowledge']) )
        print('Era                    : ' + str(myNation[0]['Tech']['era']))
        print('Research Points (RP)   : ' + str(myNation[0]['Tech']['research points']) ) 
        print('Level                  : ' + str(myNation[0]['Tech']['level']))
        print(' ')
        print('')
        flag = showAssets(myNation,year,flag)
        print('')
        print('[R] Research Grant')
        print('[C] Collaborate')
        print('[G] Grant')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        academicSelection = str(input('Please chose an option \n')).upper()
        if academicSelection == 'A':
            fast_print('not ready')
            #myNation = drillMenu(myNation,year,WAR_BRIEFING)
        if academicSelection == 'R':
            fast_print('not ready')
        if academicSelection == 'O':
            fast_print('not ready')
        if academicSelection == 'T':
            fast_print('not ready')
        if academicSelection == 'T':
            fast_print('not ready')
        if academicSelection == 'S':
            flag = 'yes'
        if academicSelection == 'R' or academicSelection == '':
            return(myNation)
    return(myNation)


def showAssets(myNation,year,flag):
    if flag == 'yes':
        universities     = myNation[0]['Tech']['assets']['universities']
        techHubs         = myNation[0]['Tech']['assets']['techHubs']
        scientists       = myNation[0]['Tech']['assets']['scientists']
        engineers        = myNation[0]['Tech']['assets']['engineers']
        mathematicians   = myNation[0]['Tech']['assets']['mathematicians']
        entrepreneurs    = myNation[0]['Tech']['assets']['entrepreneurs']
        print('Institues      : ' + str(universities + techHubs))
        print('--------------')
        print('Universities : ' + str(universities ))
        print('TechHubs  : ' + str(techHubs))
        print('')
        print('Staff      : ' + str(gunboats + destroyers + carriers))
        print('--------------')
        print('Scientists: ' + str(scientists))
        print('Engineers: ' + str(engineers))
        print('Mathematicians : ' + str(mathematicians))
        print('Entrepreneurs : ' + str(entrepreneurs))
        print('')
        print('Total Prestige : ' + str(myNation[0]['Tech']['prestigue']) )
        print(' ')
        input('Enter to continue \n')
        clearScreen()
        flag = 'no'
    return(flag)


def PrintResearch(paddingArray):
     
    for item in paddingArray:
        paddingLen = 20 - len(item[1])
        padding    = ''
        for x in range(0,paddingLen): padding = padding + ' '
        print(str(item[1]) + str(padding) + ' : ' + str(item[2]) + '%')
    total = paddingArray[0][2] + paddingArray[1][2] +  paddingArray[2][2] + paddingArray[3][2] +paddingArray[4][2]
    if total > 499:
        print(' ')
        fast_print('***CONGRATULATIONS YOU CAN NOW ADVANCE YOUR ERA***')
    return('off')
            
def printCurrentResearch(myNation):

    for item in myNation[0]['Nextmoves']:
        if 'research' in item:
            print('You are currently researching ***' + str(myNation[0]['Tech']['researched'][item[3]][1]) + '***')

def researchMenu(myNation,year,TECH_MAP):
    flag = ''
    advanceFlag = 'On'
    researchSelection = ' '
    while researchSelection != 'XYZFFJJJJJJ':
        one   = myNation[0]['Tech']['researched']['one']
        two   = myNation[0]['Tech']['researched']['two']
        three = myNation[0]['Tech']['researched']['three']
        four  = myNation[0]['Tech']['researched']['four']
        five  = myNation[0]['Tech']['researched']['five']
        clearScreen()
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('        777777 RESEARCH HUB 7777777                ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team                : ' + str(myNation[1]))
        print('Year                   : ' + str(year))
        print('Knowledge       (KP)   : ' + str(myNation[0]['Tech']['knowledge']) )
        print('Era                    : ' + str(myNation[0]['Tech']['era']))
        print('Research Points (RP)   : ' + str(myNation[0]['Tech']['research points']) ) 
        print('Level                  : ' + str(myNation[0]['Tech']['level']))
        print(' ')
        print('')
        print('Development Completion')
        print('===================')
        if advanceFlag == 'On':
            advanceFlag = PrintResearch([one,two,three,four,five])
        flag = showAssets(myNation,year,flag)
        print('')
        printCurrentResearch(myNation)
        print('')
        print('[A] Advance Era')
        print('[D] Develop Technology')
        print('[G] Research Grant')
        print('[P] Purchase Technology')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        researchSelection = str(input('Please chose an option \n')).upper()
        if researchSelection == 'A':
            myNation = advanceEra(myNation,one,two,three,four,five,TECH_MAP,era = myNation[0]['Tech']['era'])
        if researchSelection == 'D':
            myNation = selectTech(myNation,one,two,three,four,five,TECH_MAP)
        if researchSelection == 'G':
            myNation = gainResearchPoints(myNation)
        if researchSelection == 'P':
            print('not ready..')
        if researchSelection == 'S':
            flag = 'yes'
        if researchSelection == 'R' or researchSelection == '':
            return(myNation)
    return(myNation)

# SELECT TECH
# CHECK TECH NOT ALREADY MAX
# CHECK REQUIRED POINTS 
# CONVERT MY%RP TO RP

def selectTech(myNation,one,two,three,four,five,TECH_MAP):
    # Check isn't already researching a tech
    returnCode = checkMoves(myNation,'research')[1]
    if returnCode > 0: 
        for item in myNation[0]['Nextmoves']:
            if 'research' in item:
                clearScreen()
                input('You are currently developing ' + str(item[3]) + ' please wait until this is complete. \n')
        return(myNation)


    era           = str(myNation[0]['Tech']['era'])
    researched    = myNation[0]['Tech']['researched']
    techSelected  = ''
    accepted      = ['1','2','3','4','5']
    choiceArray   = ['one','two','three','four','five']
    choice        = ''

    clearScreen()
    while techSelected != 'Y':
        print('-----SELECT A TECHNOLOGY------')
        print('')
        print('1. ' + str(one[1]))
        print('2. ' + str(two[1]))
        print('3. ' + str(three[1]))
        print('4. ' + str(four[1]))
        print('5. ' + str(five[1]))
        selection = str(input('Select a Tech to Research \n'))
        if selection in accepted:
            choice = choiceArray[accepted.index(selection)]
            techSelected = 'Y'
    
    
    required         = TECH_MAP['EraCost'][era][choice]['rp']
    myTechPoints     = researched[choice][0]
    remaining        = required - myTechPoints
    
    if myTechPoints > (required - 1):
        input('You have already maxed this Tech stream. Please try another. Once all streams complete, Era will progress \n')
        return(myNation)

    input('You selected : ' + str(researched[choice][1]))
    # Nextmove contains = submitted flag(changes to pending), research flag, era for lookup, techname, pointsremaining
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [['submitted','research',era, choice,required]]

    print('Next moves are ' + str(myNation[0]['Nextmoves']))


    return(myNation)

def gainResearchPoints(myNation):
    wealth    = myNation[0]['Finance']['wealth']

    if wealth < 100:
        input('You dont have enough money to engage in research.')
        return(myNation)

    # CHECK MAX MOVES
    returnCode = checkMoves(myNation,'gainResearch')[1]
    if returnCode > 0: 
        fast_print('You are already collecting research points.')
        return(myNation)

    intensity = 'low'
    while intensity != 'XYZFFJJJJJJ':
        print('[S] Soft       ')
        print('[M] Medium     ')
        print('[H] Hard      ')
        print('[O] Overtime   ')
        print('[I] More Info')
        print('')
        print('[R] Return')
        intensity = input('How hard do you want to invest in research grants? \n').upper()
        clearScreen()
        if intensity == 'S':
            researchOrder = ['submitted','gainResearch','Soft',0,2]
            break
        if intensity == 'M':
            researchOrder = ['submitted','gainResearch','Medium',10,4]
            break
        if intensity == 'H':
            researchOrder = ['submitted','gainResearch','Hard',15,6]
            break
        if intensity == 'O':
            researchOrder = ['submitted','gainResearch','Overtime',25,8]
            break
        if intensity == 'I':
            fast_print('Research grants awards knowledge and research points (RP) that will be rewarded each round but comes at a cost of wealth and time. \n')
            print('[S] Soft       : 2 rounds at no cost     - small bonus each round.')
            print('[M] Medium     : 4 rounds at 10% wealth  - small rp & knowledge bonus each round.')
            print('[H] Hard       : 6 rounds at 15% wealth  - medium rp and knowledge bonus each round.')
            print('[O] Overtime   : 8 rounds at 25% wealth  - Large rp and knowledge bonus each round.')
            input('Enter to continue \n')
        if intensity == 'R' or intensity == '':
            return(myNation)

    # Deduct credits
    amount = round((researchOrder[3]/100) * wealth)
    print('Amount spent on research is  $' + str(amount))
    myNation[0]['Finance']['wealth']-= amount

    #Add spend amount to order array to improve reward calculation 
    researchOrder.append(amount)

    # Place Order
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [researchOrder]
    print('')
    input('Your ' + str(researchOrder[2]) + ' research grant will award you points each round that can be spent on developing technology. \nPress enter to continue  \n')
    return(myNation)

def advanceEra(myNation,one,two,three,four,five,TECH_MAP,era):
    # Check isn't already researching a tech
    returnCode = checkMoves(myNation,'advanceEra')[1]
    if returnCode > 0: 
        return(myNation)


    era           = str(myNation[0]['Tech']['era'])
    total = one[2] + two[2] + three[2] + four[2] + five[2]
    if total < 500:
        input('Not enough Development progress. Please complete development of all five tech stacks first. \n')
    
    # Place Order
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + ['advanceEra']

    input(str(myNation[1]) + ' will progress to the ' + str( TECH_MAP['nextEra'][era]) )

    return(myNation)

