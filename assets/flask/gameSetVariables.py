import random 
"""


Spend Research points to upgrade an area



LEVEL = %Completion/50
ON COMPLETION OF TECH = GAIN BONUS

json array to be 'one', 'two'...

INDUSTRIAL REVOLUTION['Wool':0,'Production Line':0, 'glass manufacturing': 0, 'cement': 0, 'Electricity': 0]
INFORMATIONAGE ['DigitalElectronics':0, 'Internet':0, 'Mobile':0, 'Cloud':0, 'IOT':0]

- worry about industry later


TECH_ARRAY = [{'EON':
{'INDUSTRIAL REVOLUTION':    ,
'INFORMATION AGE' {'ONE': ['Tech']['knowledge'] ,   } .
},

}]
"""


def setVariables(WAR_BRIEFING):
    NATION_ARRAY = []
    USA = {}
    UK = {}
    CHINA  = {}
    INDIA = {}
    RUSSIA  = {}
    GERMANY = {}
    ITALY = {}
    SPAIN  = {}
    FRANCE = {}
    JAPAN = {}
    BRAZIL = {}
    SOUTHKOREA = {}
    SOUTHAFRICA = {}
    PAKISTAN = {}
    INDONESIA = {}
    NIGERIA = {}
    MEXICO = {}
    EGYPT = {}
    VIETNAM = {}
    IRAN = {}
    KENYA = {}
    NATION_ARRAY = [[USA,'USA'],[UK,'UK'],[GERMANY,'GERMANY'],[CHINA,'CHINA'],[INDIA,'INDIA'],[RUSSIA,'RUSSIA'],[ITALY,'ITALY'],[SPAIN,'SPAIN'],[FRANCE,'FRANCE'],[JAPAN,'JAPAN'],[BRAZIL,'BRAZIL'],[SOUTHKOREA,'SOUTHKOREA'],[SOUTHAFRICA,'SOUTHAFRICA'],[PAKISTAN,'PAKISTAN'],[INDONESIA,'INDONESIA'],[NIGERIA,'NIGERIA'],[MEXICO,'MEXICO'],[EGYPT,'EGYPT'],[VIETNAM,'VIETNAM'],[IRAN,'IRAN'],[KENYA,'KENYA']]

    era          = 'INDUSTRIAL REVOLUTION'

    # 'weapons':{'1':[]
    # 'weapons':{'1':['name',amount,level]
    UNITONE    = WAR_BRIEFING['weapons'][era]['1'][0]
    UNITTWO    = WAR_BRIEFING['weapons'][era]['2'][0]
    UNITTHREE  = WAR_BRIEFING['weapons'][era]['3'][0]
    UNITFOUR   = WAR_BRIEFING['weapons'][era]['4'][0]
    UNITFIVE   = WAR_BRIEFING['weapons'][era]['5'][0]
    UNITSIX    = WAR_BRIEFING['weapons'][era]['6'][0]
    UNITSEVEN  = WAR_BRIEFING['weapons'][era]['7'][0]
    UNITEIGHT  = WAR_BRIEFING['weapons'][era]['8'][0]

    POWERONE    = WAR_BRIEFING['weapons'][era]['1'][1]
    POWERTWO    = WAR_BRIEFING['weapons'][era]['2'][1]
    POWERTHREE  = WAR_BRIEFING['weapons'][era]['3'][1]
    POWERFOUR   = WAR_BRIEFING['weapons'][era]['4'][1]
    POWERFIVE   = WAR_BRIEFING['weapons'][era]['5'][1]
    POWERSIX    = WAR_BRIEFING['weapons'][era]['6'][1]
    POWERSEVEN  = WAR_BRIEFING['weapons'][era]['7'][1]
    POWEREIGHT  = WAR_BRIEFING['weapons'][era]['8'][1]


    
    score        = 100
    wealth       = 500 
    gems         = 5
    raremetals   = 0
    oil          = 0
    might        = 100  
    troops       = 500
    aggression   = 0 



    for nation in NATION_ARRAY:
        nation[0]['Score']    = score 
        nation[0]['Finance']  = {'wealth': wealth, 'level': 'PickPocket', 'gold':60, 'gems':gems, 'raremetals':raremetals,  'oil':oil,}
        # Add drones, robots, etc later
        nation[0]['War']      = {'might': might,    'level': 'Private', 'weapons':{'1':[UNITONE,troops,1,POWERONE],'2':[UNITTWO,0,1,POWERTWO],'3':[UNITTHREE,0,1,POWERTHREE],'4':[UNITFOUR,0,1,POWERFOUR],'5':[UNITFIVE,0,1,POWERFIVE],'6':[UNITSIX,0,1,POWERSIX],'7':[UNITSEVEN,0,1,POWERSEVEN],'8':[UNITEIGHT,0,1,POWEREIGHT]}, 'firePower':0}
        nation[0]['Tech']     = {'knowledge' : 0,'level': 0,'era': era,'research points': 100, 'researched':{'one':[0,'',0],'two':[0,'',0],'three':[0,'',0],'four':[0,'',0],'five':[0,'',0]}, 'assets':{'universities':0,'techHubs':0,'scientists':0,'engineers':0,'mathematicians':0,'entrepreneurs':0}, 'prestigue':0}
        nation[0]['Politics'] = {'influence':0, 'level' : 'Back Bencher', 'stability':0, 'backing':0}
        nation[0]['Special']  = {'chance': 0, 'moveLimit':2, 'aggression':random.randint(0,100), 'creativity':random.randint(0,100), 'materialism':random.randint(0,100), 'prudence':random.randint(0,100), 'bonusUnits': [], 'notes': []}

        nation[0]['Friendship'] = {}
        for state in NATION_ARRAY:
            friendship = random.randint(-10,50)
            if nation[1] != state[1]:
                nation[0]['Friendship'][state[1]] = {'level': friendship,'warDate': 0,'initiated': 0,'noWars': 0,'declared': 0,'attacked': 0,'lost': 0,'won': 0}

        nation[0]['Citizens']  = {'population': 0, 'contentment': 0, 'fertility': 0}
        nation[0]['hints']     = 'off'
        nation[0]['Global']    = {'backing': 0, 'respect': 0, 'fear': 0}
        nation[0]['Nextmoves'] = []
        score      = score - 5
        wealth     = wealth - 5
        gems       = gems + 5
        raremetals = raremetals + 5
        oil        = oil + 5
        might      = might - 3
        troops     = troops -1


    # EXCEPTIONS 
    USA['Finance']['oil'] = 200
    RUSSIA['Finance']['oil'] = 200

    return(NATION_ARRAY)

def returnTechMap():
    TECH_MAP = {'Era':{'INDUSTRIAL REVOLUTION':{'one':'Wool','two':'Manufacturing Line','three':'Glass Production','four':'Cement','five':'Electricity'},
                      'INFORMATION AGE':{'one':'Digital Electronics','two':'Internet','three':'Mobile Technologies','four':'Cloud Computing','five':'Internet of Things'},
                      'SECOND ENLIGHTENMENT':{'one':'Decentralisation','two':'NeuralLink','three':'Artificial Intelligence','four':'Bio Computing','five':'The Convergance'}
                      
                      },
                'nextEra':{'INDUSTRIAL REVOLUTION':'INFORMATION AGE','INFORMATION AGE':'SECOND ENLIGHTENMENT'},
                'EraBonus':{

                'INDUSTRIAL REVOLUTION':{
                    'one': [('K',100)],
                    'two': [('W',400),('K',300)],
                    'three':[('W',500),('K',500),('R',200)],
                    'four':[('W',800),('K',1000),('R',400)],
                    'five':[('W',1000),('K',2000),('R',500)]},
                            
                'INFORMATION AGE':{
                    'one': [('K',2000)],
                    'two': [('W',4000),('K',3000)],
                    'three':[('W',5000),('K',5000),('R',2000)],
                    'four':[('W',8000),('K',10000),('R',4000)],
                    'five':[('W',10000),('K',20000),('R',5000)]},
                            
                'SECOND ENLIGHTENMENT':{
                    'one': [('K',10000)],
                    'two': [('W',40000),('K',30000)],
                    'three':[('W',50000),('K',500000),('R',20000)],
                    'four':[('W',80000),('K',100000),('R',40000)],
                    'five':[('W',100000),('K',200000),('R',50000)]}
                      
                      },
                'EraCost':{'INDUSTRIAL REVOLUTION':{'one':{'rp':50,'wealth':100},'two': {'rp':100,'wealth':100},'three':{'rp':200,'wealth':100},'four':{'rp':400,'wealth':100},'five':{'rp':50,'wealth':100}},
                            'INFORMATION AGE':{'one':{'rp':600,'wealth':100},'two':{'rp':1000,'wealth':100},'three':{'rp':2000,'wealth':100},'four':{'rp':4000,'wealth':100},'five':{'rp':6000,'wealth':100}},
                            'SECOND ENLIGHTENMENT':{'one':{'rp':6000,'wealth':100},'two':{'rp':10000,'wealth':100},'three':{'rp':12000,'wealth':100},'four':{'rp':14000,'wealth':100},'five':{'rp':16000,'wealth':100}}
                      
                      },

                      }
    return(TECH_MAP)

