
"""
# ---------------------------------------------------------------------
#   PROGRAM SPEC 
#   NAME: gameOfWar
#   DATE OF CREATION: 16 JUNE 2020
#   PROGRAM TYPE: Python Text game
#   SUMMARY: This program runs a sereis of standard if, for, while loops
#            user inputs and write to file methods. 
#            The aim of the game is for a user to play through a series
#            of time and improve their overall selected countries score. 
#           
# ---------------------------------------------------------------------
"""

"""
THINGS TO SAVE

NAME
YEAR
ARRAY
rank 
selected country 


NOTES: 

myNation is a list, with the first element pointing to the country dict 
myNationIndex may be required

TODO

- VIEW STATS OF ANY COUNTRY ...
- VIEW AVERAGE OF TRADE
- UNLOCK MORE MUSIC At certain points
- Shop




"""


"""
# ---------------------------------------------------------------------
# UTILITIES 
# ---------------------------------------------------------------------
"""
import sys
import time
import copy
import random

# IMPORT UNIVERSAL UTILITIES
from gameConquest_utilities import slow_print as slow_print
from gameConquest_utilities import med_print as med_print
from gameConquest_utilities import fast_print as fast_print
from gameConquest_utilities import superfast_print as superfast_print
from gameConquest_utilities import clearScreen as clearScreen
from gameConquest_utilities import preferencePrint as preferencePrint
from gameConquest_utilities import options as options
from gameConquest_utilities import music as music

# FUNCTIONS
from gameFunctionSelection import selectNation as selectNation
from gameFunctionSelection import stats as stats
from actionFunctions import action as action
from actionFunctions import nextYear as nextYear
#from AIOrderFunctions import setAIMoves as setAIMoves

# CUSTOM MENUES
import selectionFinance  as fin 
import selectionWar      as warMenu
import selectionPolitics as politics
import selectionIntro    as start



"""
# ---------------------------------------------------------------------
# END UTILITIES
# ---------------------------------------------------------------------
"""
# FINANCE LEVEL: PickPocket, Penny Pusher, Assistant, gambler, huslter, business magnate. 
USA           = {'Score': 90, 'Finance':{'wealth': 500,  'gold':60, 'gems':3, 'raremetals':10,  'oil':200, 'level': 'PickPocket'}  , 'War':{'might': 100, 'level': 'private', 'weapons':{'troops':500,'tanks':0,'gunboats':20,'destroyers':5,'carriers':1,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':70, 'creativity':80, 'materialism':70, 'prudence':30, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
UK            = {'Score': 75, 'Finance':{'wealth': 350,  'gold':45, 'gems':1, 'raremetals':20,  'oil':120, 'level': 'PickPocket'}   , 'War':{'might': 60, 'level': 'private', 'weapons':{'troops':140,'tanks':0,'gunboats':20,'destroyers':5,'carriers':1,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':60, 'creativity':70, 'materialism':65, 'prudence':50, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
CHINA         = {'Score': 90, 'Finance':{'wealth': 500,  'gold':20, 'gems':2, 'raremetals':200, 'oil':20,  'level': 'PickPocket'}   , 'War':{'might': 90, 'level': 'private', 'weapons':{'troops':900,'tanks':0,'gunboats':20,'destroyers':5,'carriers':1,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':70, 'creativity':30, 'materialism':90, 'prudence':60, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
INDIA         = {'Score': 65, 'Finance':{'wealth': 400,  'gold':50, 'gems':3, 'raremetals':30,  'oil':20,  'level': 'PickPocket'}   , 'War':{'might': 60, 'level': 'private', 'weapons':{'troops':850,'tanks':0,'gunboats':20,'destroyers':5,'carriers':1,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':40, 'creativity':30, 'materialism':20, 'prudence':50, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
RUSSIA        = {'Score': 60, 'Finance':{'wealth': 200,  'gold':25, 'gems':1, 'raremetals':20,  'oil':200, 'level': 'PickPocket'}   , 'War':{'might': 80, 'level': 'private', 'weapons':{'troops':200,'tanks':0,'gunboats':20,'destroyers':5,'carriers':1,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':80, 'creativity':20, 'materialism':60, 'prudence':40, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
GERMANY       = {'Score': 70, 'Finance':{'wealth': 300,  'gold':25, 'gems':1, 'raremetals':30,  'oil':10,  'level': 'PickPocket'}   , 'War':{'might': 60, 'level': 'private', 'weapons':{'troops':120,'tanks':0,'gunboats':20,'destroyers':5,'carriers':1,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':40, 'creativity':70, 'materialism':60, 'prudence':40, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
ITALY 		  = {'Score': 68, 'Finance':{'wealth': 200,  'gold':40, 'gems':2, 'raremetals':10,  'oil':30,  'level': 'PickPocket'}   , 'War':{'might': 60, 'level': 'private', 'weapons':{'troops':130,'tanks':0,'gunboats':20,'destroyers':5,'carriers':1,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':50, 'creativity':70, 'materialism':60, 'prudence':50, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
SPAIN 		  = {'Score': 68, 'Finance':{'wealth': 200,  'gold':45, 'gems':2, 'raremetals':10,  'oil':20,  'level': 'PickPocket'}   , 'War':{'might': 60, 'level': 'private', 'weapons':{'troops':130,'tanks':0,'gunboats':20,'destroyers':5,'carriers':1,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':50, 'creativity':70, 'materialism':50, 'prudence':60, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
FRANCE        = {'Score': 74, 'Finance':{'wealth': 200,  'gold':40, 'gems':5, 'raremetals':10,  'oil':10,  'level': 'PickPocket'}   , 'War':{'might': 60, 'level': 'private', 'weapons':{'troops':140,'tanks':0,'gunboats':20,'destroyers':5,'carriers':1,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':60, 'creativity':70, 'materialism':40, 'prudence':50, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
JAPAN         = {'Score': 70, 'Finance':{'wealth': 350,  'gold':35, 'gems':12, 'raremetals':100, 'oil':20,  'level': 'PickPocket'}  , 'War':{'might': 60, 'level': 'private', 'weapons':{'troops':220,'tanks':0,'gunboats':20,'destroyers':5,'carriers':1,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':30, 'creativity':70, 'materialism':40, 'prudence':40, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
BRAZIL        = {'Score': 55, 'Finance':{'wealth': 100,  'gold':15, 'gems':23, 'raremetals':30,  'oil':80,  'level': 'PickPocket'}  , 'War':{'might': 60, 'level': 'private', 'weapons':{'troops':100,'tanks':0,'gunboats':20,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':60, 'creativity':70, 'materialism':70, 'prudence':70, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
SOUTHKOREA    = {'Score': 50, 'Finance':{'wealth': 200,  'gold':25, 'gems':22, 'raremetals':80,  'oil':10,  'level': 'PickPocket'}  , 'War':{'might': 60, 'level': 'private', 'weapons':{'troops':100,'tanks':0,'gunboats':20,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':40, 'creativity':70, 'materialism':40, 'prudence':60, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
SOUTHAFRICA   = {'Score': 48, 'Finance':{'wealth': 100,  'gold':45, 'gems':27, 'raremetals':10,  'oil':60,  'level': 'PickPocket'}  , 'War':{'might': 40, 'level': 'private', 'weapons':{'troops':100,'tanks':0,'gunboats':30,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':40, 'creativity':70, 'materialism':70, 'prudence':50, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
PAKISTAN      = {'Score': 45, 'Finance':{'wealth': 100,  'gold':40, 'gems':23, 'raremetals':10,  'oil':80,  'level': 'PickPocket'}  , 'War':{'might': 40, 'level': 'private', 'weapons':{'troops':400,'tanks':10,'gunboats':30,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':70, 'creativity':70, 'materialism':80, 'prudence':40, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
INDONESIA     = {'Score': 40, 'Finance':{'wealth': 100,  'gold':20, 'gems':23, 'raremetals':40,  'oil':30,  'level': 'PickPocket'}  , 'War':{'might': 40, 'level': 'private', 'weapons':{'troops':300,'tanks':10,'gunboats':30,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':40, 'creativity':70, 'materialism':70, 'prudence':60, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
NIGERIA       = {'Score': 55, 'Finance':{'wealth': 100,  'gold':40, 'gems':26, 'raremetals':10,  'oil':90,  'level': 'PickPocket'}  , 'War':{'might': 40, 'level': 'private', 'weapons':{'troops':100,'tanks':10,'gunboats':30,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':40, 'creativity':70, 'materialism':80, 'prudence':55, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
MEXICO        = {'Score': 50, 'Finance':{'wealth': 100,  'gold':20, 'gems':23, 'raremetals':30,  'oil':90,  'level': 'PickPocket'}  , 'War':{'might': 40, 'level': 'private', 'weapons':{'troops':150,'tanks':10,'gunboats':30,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':50, 'creativity':70, 'materialism':70, 'prudence':40, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
EGYPT         = {'Score': 48, 'Finance':{'wealth': 100,  'gold':60, 'gems':24, 'raremetals':10,  'oil':110, 'level': 'PickPocket'}  , 'War':{'might': 40, 'level': 'private', 'weapons':{'troops':100,'tanks':10,'gunboats':30,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':60, 'creativity':70, 'materialism':60, 'prudence':65, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0},'hints':'on', 'Nextmoves' : []}
VIETNAM       = {'Score': 48, 'Finance':{'wealth': 150,  'gold':20, 'gems':22, 'raremetals':130, 'oil':30,  'level': 'PickPocket'}  , 'War':{'might': 40, 'level': 'private', 'weapons':{'troops':100,'tanks':10,'gunboats':30,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':40, 'creativity':70, 'materialism':70, 'prudence':45, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
IRAN          = {'Score': 52, 'Finance':{'wealth': 100,  'gold':60, 'gems':21, 'raremetals':10,  'oil':180, 'level': 'PickPocket'}  , 'War':{'might': 40, 'level': 'private', 'weapons':{'troops':100,'tanks':10,'gunboats':30,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':70, 'creativity':70, 'materialism':20, 'prudence':50, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
KENYA         = {'Score': 48, 'Finance':{'wealth': 100,  'gold':50, 'gems':27, 'raremetals':10,  'oil':80,  'level': 'PickPocket'}  , 'War':{'might': 40, 'level': 'private', 'weapons':{'troops':100,'tanks':10,'gunboats':30,'destroyers':5,'carriers':0,'jets':10,'bombers':3,'Nukes':0}, 'firePower':0}  , 'Tech':{'knowledge' : 0,'level': 0, 'science':0, 'engineering':0},  'Politics':{'influence':0, 'stability':0} , 'Special':{'chance': 0, 'moveLimit':2, 'aggression':50, 'creativity':70, 'materialism':70, 'prudence':45, 'bonusUnits': [], 'notes': []} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'hints':'on', 'Nextmoves' : []}
#TURKEY 	      = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#ETHIOPA       = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#PHILIPPINES   = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}
#BANGLADESH    = {'Score': 0, 'Finance':{'wealth': 8} , 'Tech':{'level': 0, 'science':0, 'engineering':0},  'Politics':{'leadership':0, 'stability':0} , 'Special':{'chance': 0} , 'Friendship':{} , 'Citizens':{'population': 0, 'contentment': 0, 'fertility': 0}, 'Nextmove' : 'pass'}

# PRice is % of remaining available 
PRICE_TRACKER = {'gold': {'price': 120, 'stock': 10000, 'priceChange': '+0', 'history':[120],'average':120},'raremetals': {'price': 60, 'stock': 2000, 'priceChange': '+0', 'history':[60],'average':60}, 'gems': {'price': 250, 'stock': 2000, 'priceChange': '+0', 'history':[250],'average':250}, 'oil': {'price': 12, 'stock': 10000, 'priceChange': '+0', 'history':[12],'average':12}}

# numbers are price, wait time, might valuation as percentage (ADDED ON). 
WAR_BRIEFING = {'weapons':{'troops':(10,2,0.001),'tanks':(300,2,0.01),'gunboats':(100,2,0.005),'destroyers':(2000,3,0.1),'carriers':(20000,4,1),'jets':(5000,2,0.3),'bombers':(7000,3,0.35),'Nukes':(100000,4,5)}}

NATION_ARRAY = [[USA,'USA'],[UK,'UK'],[GERMANY,'GERMANY'],[CHINA,'CHINA'],[INDIA,'INDIA'],[RUSSIA,'RUSSIA'],[ITALY,'ITALY'],[SPAIN,'SPAIN'],[FRANCE,'FRANCE'],[JAPAN,'JAPAN'],[BRAZIL,'BRAZIL'],[SOUTHKOREA,'SOUTHKOREA'],[SOUTHAFRICA,'SOUTHAFRICA'],[PAKISTAN,'PAKISTAN'],[INDONESIA,'INDONESIA'],[NIGERIA,'NIGERIA'],[MEXICO,'MEXICO'],[EGYPT,'EGYPT'],[VIETNAM,'VIETNAM'],[IRAN,'IRAN'],[KENYA,'KENYA']]


myNation = ''
buffer = ''
p = 'Me'

# Applies to AI move and Menu



"""
# =====================================================================
# =====================================================================
# =====================================================================
#                           START MENU
#     1. SELECT NATION OPTION
#     2. VIEW COUNTRY
#     3. VIEW RULES
#     4. VIEW CREDITS
#     5. START GAME 
# =====================================================================
# =====================================================================
# =====================================================================
"""



selection = ''
while selection != 'Done':
	clearScreen()
	print('*****************MENU*******************')
	print('')
	print('')
	print('[1] Start Game')
	print('[2] Select your Nation')
	print('[3] Country Stats')
	print('[4] Game rules')
	print('[5] Credits')
	print('[6] JukeBox')
	print('[7] Back')
	print('')
	print('')


	try:
		selection = int(input('Please chose an option \n'))
	except:
		print("Entered incorrectly, please try again")

	if selection == 1:
		if myNation == '':
			myNation,myNationIndex =selectNation(NATION_ARRAY)
		fast_print('Starting game... \n')
		clearScreen()
		break
	if selection == 2:
		myNation,myNationIndex = selectNation(NATION_ARRAY)
	if selection == 3:
		stats(NATION_ARRAY)
	if selection == 4:
		fast_print('The aim of the game is to gain the most points before the year 2100. \n')
		fast_print('This can be by winning on trade, military, culture or other. \n')
		fast_print('Remember, every action has its own consequence! \n')
		fast_print('Good Luck commander! \n' )
		buffer = input('Press enter to continue \n ')
		clearScreen()
	if selection == 5:
		fast_print('All credits go to Adam McMurchie... me! . \n')
		buffer = input('Press enter to continue \n ')
		clearScreen()
	if selection == 6:
		import webbrowser
		music()
	if selection == 7:
		exit()

"""
# =======================================================================
#
#                           INTRO GAME START
#	
#     1. CHECK GAME LOADED FLAG
#     2. LOAD GAME IF FLAG SET
#     3. GET USER NAME
#     4. INTRO SCENE
# =======================================================================
"""


gameLoaded = False

if gameLoaded:
	print('Welcome back commander')


year = 1949

# MUST UNCOMENT FOR FULL GAME

userName = 'DonnerKebab'
#userName = start.start(userName,myNation)






"""
# =======================================================================
# =======================================================================
# MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU 
# =======================================================================
#                           MAIN MENU MODE 
#     1. View Leaderboard
#     2. Finance Beuro
#     3. Ministry of war
#     4. Political Cabinet
#     5. Next Year
# =======================================================================
# MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU MAIN MENU
# =======================================================================
"""
def menuUpdate():
	for item in myNation[0]['Special']['notes']:
		if item == 'finance':
			print(""" 
	@('_')@
				""")
			med_print('**CONGRATULATIONS!** Finance Level UP!!')
	if len(myNation[0]['Special']['notes']) > 0:
		myNation[0]['Special']['notes'] = []
	

menuSelection = ' '
while menuSelection != 'E':
	clearScreen()
	print('*****************MENU*******************')
	print('')
	print('My Team: ' + str(myNation[1]))
	print('Year: ' + str(year))
	print('Wealth : ' + str(myNation[0]['Finance']['wealth']))
	print('Rank: ' + 'Junior')
	print('')
	print(""" 
            ______________
           |[]            |
           |  __________  |
           |  |        |  |
           |  | Home   |  |
           |  |________|  |
           |   ________   |
           |   [ [ ]  ]   |
           |___[_[_]__]___|

			""")
	print('[L] View Leaderboard')
	print('[F] Finance bureau')
	print('[W] Ministry of War')
	print('[P] Political Cabinet (not available)')
	print('[S] Science Department (not available)')
	print('[N] Next Year')
	print(' ')
	print(' ')
	menuUpdate()
	print(' ')
	print(' ')
	print('[O] Options')
	print('[X] Exit')
	print(' ')
	print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))
	print('****************************************')
	print(' ')
	print(' ')
	menuSelection = str(input('What would you like to do ' + str(userName) + '? \n')).upper()
	
	if menuSelection == 'L':
		stats(NATION_ARRAY)
	if menuSelection == 'F':
		myNation = fin.financeBeuro(myNation,year,PRICE_TRACKER)
	if menuSelection == 'W':
		myNation = warMenu.warMinistry(myNation,year,WAR_BRIEFING)
	if menuSelection == 'P':
		myNation = politics.politicalCabinet(myNation,year,PRICE_TRACKER)
	if menuSelection == 'S':
		fast_print('Not ready yet, sorry....')
	if menuSelection == 'N' or menuSelection == '':
		year, NATION_ARRAY,PRICE_TRACKER,WAR_BRIEFING,p = nextYear(year,myNation,NATION_ARRAY,myNationIndex,PRICE_TRACKER,WAR_BRIEFING,p)
	if menuSelection == 'O':
		p = options(p,NATION_ARRAY)
	if menuSelection == 'X':
		exit()
		



