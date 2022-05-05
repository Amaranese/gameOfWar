
# DESIGN & BRAINSTORMING  (DEVELOPER NOTES)  
 
# EACH STREAM HAS TO BE HUGE FUN IN ITSELF
## IDEAS   

- OPEN UP SELECTION FEATURES USING FLAG
- FUTURE TECH 
- TIME MACHINE 
- OFF WORLD MINING COLONIES
- REPLICANTS
- TRADE MIGHT FOR TECHLEVEL ETC...
- Higher friendship produces more positive actions....
- Allies can buy stuff/weapons off each other for reduced prices



## NEWS BOARD 

NewsArray = []

storyList  - each story comes with an affect (i.e. value of gold has increased)
updateList - LevelUP, X&Y are at war etc 

### TECH  

# TODO 
Work out how to rename wararray
update warbriefing for different functions
print('**todo** FUNCTION TO CHECK WHEN STOCK IS 10% AND PUT ALERTS')
  
# TECH PROMOTION
LEVEL = %Completion/50
ON COMPLETION OF TECH = GAIN BONUS


TECH_ARRAY = [{'EON':
{'INDUSTRIAL REVOLUTION':    ,
'INFORMATION AGE' {'ONE': ['Tech']['knowledge'] ,   } .
},

}]
- GROW VERTICALLY
- Gain Research points
- Spend Research points to up level
- When level = 10 = unlock next Era

- need more uses for reseaech points
- GROW HORIZONTALLY

- .... (maybe unlock Era early)
- 50,000 credits 2000 might to unlock information era
- You get the tech, but you lack the knowledge points
- Knowledge increases overall score but also boosts politics, etc

- Spend Research points to unlock industry



- Weapons change based on Era
- (Buy Microchips knowledge x 10 each round)



## COMPETITION 

Friendship - 40


### WAR

negative
---------
| degree | Options           | News Result                                   | frienship threshold | 
|--------|-------------------|-----------------------------------------------|---------------------|
| low    | espionage         | X & Y are at a state of unease                |    40 - 50  -10  0         |
| mid    | covert operations | X & Y are undergoing heightened tensions      |    30 - 40  -20 -10        |
| high   | tactical strikes  | Major hostilities have erupted with X & Y     |    20 - 30  -30 -20       |
| top    | full_outWar       | X/Y has declared all out war on x/y           |    0  - 20  -40-        |
  

- Espionage        - Get stats on enemy, reduces their moves to 0
- covert           - Does damage, steal may reduce friendship significantly (needs warrank above...)
- tactical strike  - Does damage, takes damage (big loss in backing)(needs warrank above...)
- war              - Engaged in fight to finish. 
damage = (add as more functions added) weapons, might, influence,backing, stability , economy, science...etc

  

RULES OF WAR
1. Options only become available at decreasing levels of friendship
2. Friendship can be increased/decreased by certain actions 
3. If a nation is predisposed to war or if a nation has friendship < 30: prefer military moves
4. Once war started, can only be broken by a loss, a truce or a surrender.  


pseudo 

WAR_FUNCTION
comes in action loop before AIaction

- iterateFriendshipArray:
- is X & Y at war?
- If yes, skip actions or restrict actions.




STARTING CONFLICT 
  
1. All up to full_outwar is optional
2. First to drop under 20 'declares war' or high chance. User can continue to ignore
3. Each round forces only war moves (no other options available)

END CONFLICT

- Surrender = lose might, wealth....etc
- Truce     = submit request
- Victory   = Win lots, lose backing gain influence
- Loss      =  might = 0, economy = 0, science =0 or politics = 0 
  


friendshipArray[country][friendship,warDate, started-it 0,1, numberofWars(forthiscountryonly), declaredWar,declaredUpon, nolost, nowon,]

AI CONSIDERATIONS 

1. Only consider X move with country based upon friendship.
2. Initialise Friendship array


Functions to add: 

actionFunction declareWar():
is
actionFunction isAtWar():
no = continue
yes = 


### FINANCE 

negative 

- low  = reduced 
- mid  = covert operations
- high = sanctions
- top  = trade_war 

### SCIENCE

negative
- low  = espionage
- mid  = covert operations
- high = tactical strikes
- top  = full_outWar




5. COMPLETE 

- Buying gold, metals, oil, gems.
- Menu - pulls prices from json price tracker
- buy(myNation,price_tracker,year)
- you can buy: credits // price 
- BUY
- SELL
- DRILL
- BUILD
- SCRAP
- GAMBLE
- Only perform exchange rate change at the end. 
