# IMPORT UNIVERSAL UTILITIES
from gameConquest_utilities import slow_print as slow_print
from gameConquest_utilities import med_print as med_print
from gameConquest_utilities import fast_print as fast_print
from gameConquest_utilities import superfast_print as superfast_print
from gameConquest_utilities import clearScreen as clearScreen
from gameConquest_utilities import preferencePrint as preferencePrint
from gameConquest_utilities import options as options
from gameConquest_utilities import music as music




"""
# =======================================================================
# =======================================================================
# MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU 
# =======================================================================
#                           FUNCTIONS
#     FUNCTION selectNation
#     FUNCTION stats
#     FUNCTION music
#     PROCEEDURE start game
# =======================================================================
# MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU MENU 
# =======================================================================
"""

def selectNation(NATION_ARRAY):
    clearScreen()
    NationChoice = ''
    nationSelected = ''
    while nationSelected != 'Y':
        print('')
        print('Printing nation list')
        print('')

        for x in range(0, len(NATION_ARRAY)):
            print(str(x) + '. ' + str(NATION_ARRAY[x][-1]))
        print('')
        while NationChoice not in range(0, len(NATION_ARRAY)):
            try:
                NationChoice = int(input('Please chose a country \n'))
            except:
                print("Entered incorrectly, please try again")

        fast_print('Your chosen country is : ' +    str(NATION_ARRAY[NationChoice][-1]) + '\n')
        print('')
        buffer = input('Press Enter to continue \n')
        clearScreen()
        myNation = NATION_ARRAY[NationChoice]
        playerNationIndex = NationChoice
        nationSelected = 'Y'
    return(myNation,playerNationIndex)


def stats(NATION_ARRAY):
    clearScreen()
    print('Printing nation list')
    print('')
    
    print('|    NAME      |  SCORE   |  WEALTH  |     MIGHT    |KNOWLEDGE |INFLUENCE |   ')
    print('___________________________________________________________________________')

    rankCounter = []
    for x in range(0, len(NATION_ARRAY)):
        rankCounter.append((NATION_ARRAY[x][0]['Score'],x))
    rankCounter.sort(reverse=True)

    for x in range(0, len(rankCounter)):
        index = rankCounter[x][1]

        name = str(NATION_ARRAY[index][-1])
        for a in range(0, (14 - len(name))): name = name + ' '

        score = str(NATION_ARRAY[index][0]['Score'])
        for b in range(0, (10 - len(score))): score = score + ' '

        tradeScore = str(NATION_ARRAY[index][0]['Finance']['wealth'])
        for c in range(0, (10 - len(tradeScore))): tradeScore = tradeScore + ' '

        techScore = str(NATION_ARRAY[index][0]['Tech']['knowledge'])
        for d in range(0, (10 - len(techScore))): techScore = techScore + ' '

        warScore = str(NATION_ARRAY[index][0]['War']['might'])
        for e in range(0, (14 - len(warScore))): warScore = warScore + ' '

        politics = str(NATION_ARRAY[index][0]['Politics']['influence'])
        for f in range(0, (10 - len(politics))): politics = politics + ' '

        print( '|' + name + '|' + score + '|' + tradeScore + '|' + warScore + '|' + techScore + '|' + politics + '|' + '   '  )
    print('___________________________________________________________________________')
    print('')
    print('')
    buffer = input('Press enter to continue \n')
    clearScreen()
    print('Printing nation list')
    print('')
    print('|    NAME      |SCIENCE ERA              |FINANCE RANK        |FIREPOWER   |POLITICS LEVEL |   ')
    print('____________________________________________________________________________________________')

    for x in range(0, len(rankCounter)):
        index = rankCounter[x][1]

        name = str(NATION_ARRAY[index][-1])
        for a in range(0, (14 - len(name))): name = name + ' '

        era = str(NATION_ARRAY[index][0]['Tech']['era'])
        for b in range(0, (25 - len(era))): era = era + ' '

        fLevel = str(NATION_ARRAY[index][0]['Finance']['level'])
        for c in range(0, (20 - len(fLevel))): fLevel = fLevel + ' '

        firepower = str(NATION_ARRAY[index][0]['War']['firePower'])
        for d in range(0, (12 - len(firepower))): firepower = firepower + ' '

        pLevel = str(NATION_ARRAY[index][0]['Politics']['level'])
        for e in range(0, (15 - len(pLevel))): pLevel = pLevel + ' '

        print( '|' + name + '|' + era + '|' + fLevel + '|' + firepower + '|' + pLevel  + '|' + '   '  )
    
    print('____________________________________________________________________________________________')
    print('')
    print('')
    buffer = input('Press enter to continue \n')
    clearScreen()
    print('Printing Research Completion')
    print('')


    print('|    NAME      |' + 'Tech Stream One          ' + '|' + 'Tech Stream Two          ' + '|' + 'Tech Stream Three        ' + '|' + 'Tech Stream Four         '  + '|' +  'Tech Stream Five         '  + '|    ' )
    print('_________________________________________________________________________________________________________________________________________________')

    for x in range(0, len(rankCounter)):
        index = rankCounter[x][1]

        name = str(NATION_ARRAY[index][-1]) 
        for f in range(0, (14 - len(name))): name = name + ' '

        one = str(NATION_ARRAY[index][0]['Tech']['researched']['one'][1]) + ':' + str(NATION_ARRAY[index][0]['Tech']['researched']['one'][2]) + str('%')
        for g in range(0, (25 - len(one))): one = one + ' '

        two = str(NATION_ARRAY[index][0]['Tech']['researched']['two'][1]) + ':' +  str(NATION_ARRAY[index][0]['Tech']['researched']['two'][2]) + str('%')
        for h in range(0, (25 - len(two))): two = two + ' '

        three = str(NATION_ARRAY[index][0]['Tech']['researched']['three'][1])  + ':' +  str(NATION_ARRAY[index][0]['Tech']['researched']['three'][2]) + str('%')
        for i in range(0, (25 - len(three))): three = three + ' '

        four = str(NATION_ARRAY[index][0]['Tech']['researched']['four'][1]) + ':' +  str(NATION_ARRAY[index][0]['Tech']['researched']['four'][2]) + str('%')
        for j in range(0, (25 - len(four))): four = four + ' '

        five = str(NATION_ARRAY[index][0]['Tech']['researched']['five'][1]) + ':' +  str(NATION_ARRAY[index][0]['Tech']['researched']['five'][2]) + str('%')
        for k in range(0, (25 - len(five))): five = five + ' '

        print( '|' + name + '|' + one + '|' + two + '|' + three + '|' + four  + '|' + five  + '|' + '   '  )

    print('_________________________________________________________________________________________________________________________________________________')
    print('')
    print('')
    buffer = input('Press enter to continue \n')
    clearScreen()
    clearScreen()
    print('Printing Military Disposition')
    print('')

    print('|    NAME      |' + 'Light Units                   ' + '|' + '                          Core Division                     '  + '|    ' )
    print('___________________________________________________________________________________________________________')


    for x in range(0, len(rankCounter)):
        index = rankCounter[x][1]
        unitOne      = NATION_ARRAY[index][0]['War']['weapons']['1']
        unitTwo      = NATION_ARRAY[index][0]['War']['weapons']['2']
        unitThree    = NATION_ARRAY[index][0]['War']['weapons']['3']
        unitFour     = NATION_ARRAY[index][0]['War']['weapons']['4']
        unitFive     = NATION_ARRAY[index][0]['War']['weapons']['5']
        unitSix      = NATION_ARRAY[index][0]['War']['weapons']['6']
        unitSeven    = NATION_ARRAY[index][0]['War']['weapons']['7']
        unitEight    = NATION_ARRAY[index][0]['War']['weapons']['8']

        name = str(NATION_ARRAY[index][-1]) 
        for f in range(0, (14 - len(name))): name = name + ' '

        light = str(unitOne[0]) + ':' + str(unitOne[1]) + ' '  + str(unitTwo[0]) + ':' + str(unitTwo[1])
        for g in range(0, (30 - len(light))): light = light + ' '

        core = str(unitThree[0]) + ':' + str(unitThree[1]) + ' '  + str(unitFour[0]) + ':' + str(unitFour[1]) + ' '  + str(unitFive[0]) + ':' + str(unitFive[1])
        for h in range(0, (60 - len(core))): core = core + ' '

        print( '|' + name + '|' + light + '|' + core + '|' + '   '  )

    print('_________________________________________________________________________________________________________')
    print('')
    print('')
    buffer = input('Press enter to continue \n')
    clearScreen()

    print('')

    print('|    NAME      |' + '             Heavy Forces               ' + '|' + 'Super Weapons            '  + '|    ' )
    print('________________________________________________________________________________')


    for x in range(0, len(rankCounter)):
        index = rankCounter[x][1]
        unitOne      = NATION_ARRAY[index][0]['War']['weapons']['1']
        unitTwo      = NATION_ARRAY[index][0]['War']['weapons']['2']
        unitThree    = NATION_ARRAY[index][0]['War']['weapons']['3']
        unitFour     = NATION_ARRAY[index][0]['War']['weapons']['4']
        unitFive     = NATION_ARRAY[index][0]['War']['weapons']['5']
        unitSix      = NATION_ARRAY[index][0]['War']['weapons']['6']
        unitSeven    = NATION_ARRAY[index][0]['War']['weapons']['7']
        unitEight    = NATION_ARRAY[index][0]['War']['weapons']['8']

        name = str(NATION_ARRAY[index][-1]) 
        for f in range(0, (14 - len(name))): name = name + ' '

        heavy = str(unitSix[0]) + ':' + str(unitSix[1]) + ' '  + str(unitSeven[0]) + ':' + str(unitSeven[1])
        for i in range(0, (40 - len(heavy))): heavy = heavy + ' '

        superW = str(unitEight[0]) + ':' + str(unitEight[1])
        for j in range(0, (25 - len(superW))): superW = superW + ' '

        print( '|' + name + '|'  + heavy + '|' + superW  + '|' + '   '  )

    print('___________________________________________________________________________________')
    print('')
    print('')
    buffer = input('Press enter to continue \n')
    clearScreen()


