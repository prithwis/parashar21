#Copyright (c) 2022, Prithwis Mukerjee
#All rights reserved.
#
#This source code is licensed under the GNU GPL v3.0 -style license found in the
#LICENSE file in the root directory of this source tree. 
# --------------------------------------------------
# Global Variables
global LordOf, Lord, GrahaLordBhav, LordRashiN,LordRashiA,LordInfo
global GrahaBhava, LordBhav, BhavOfGraha_LordInfo
global BhavN, BhavA, BhavNBhavA
global GRashiN, GRashiA
global GLon, GRet, pName, GLonRet, pTags, cID
global ChartType, ChartColour, ChartFile
global ReportFile, document
# ------------------------------------------
global gregflag,iflag,hsysP
global chart
global BoL
global Graha, GMalefic
global exaL,exaU, exaR, debL, debU, debR, mool3R
global friends, enemies, neutrals
global exaltG, exaltL, debilL,debilG,mool3G,mool3L,ownHouseG,ownHouseL,inFriendG,inEnemyG,inNeutralG,inFriendL,inEnemyL,inNeutralL, Positions
global Gx, GAspects, GAspectedBy,BAspectedBy,BAspectedByBL,GAspects2, GAspectedBy2,BAspectedBy2,BAspectedByBL2,Aspects
global GConjunctsG, BLConjunctsG, BLConjunctsBL, Conjuncts
global yogsFound, yogList
global AnalysisType
global kollection   # MongoDB collection that stores the horoscope charts
global beneficG, maleficG, BenMalG
global VimDasha

from datetime import datetime
from datetime import timedelta

# ------------------------------------------

BoL = ' '
#LordOf = {"Ari":"Ma","Tau":"Ve","Gem":"Me","Can":"Mo","Leo":"Su","Vir":"Me","Lib":"Ve","Sco":"Ma","Sag":"Ju","Cap":"Sa","Acq":"Sa","Pis":"Ju"} 
LordOf = {"Mesh":"Ma","Vrish":"Ve","Mithun":"Me","Karkat":"Mo","Simha":"Su","Kanya":"Me","Tula":"Ve","Vrishchik":"Ma","Dhanu":"Ju","Makar":"Sa","Kumbh":"Sa","Meen":"Ju"} 

#converts a Rashi number to the Rashi name
#
RashiName = ["RashiName","Mesh","Vrish","Mithun","Karkat","Simha","Kanya","Tula","Vrishchik","Dhanu","Makar","Kumbh","Meen"]
def RashiN2A(n):
    return RashiName[n]

Graha = ['Su','Mo','Ma','Me','Ju','Ve','Sa']
GMalefic = {"Su":False,"Mo":False,"Ma":False,"Me":False,"Ju":True,"Ve":False,"Sa":False,"Ra":True,"Ke":True}


#Range of Exaltation
#Ref LHAE - page 30 specifies only certain parts of a Rashi are exalted
exaL = {"La":999,"Su":0,"Mo":30,"Ma":270,"Me":150,"Ju":90,"Ve":330,"Sa":180,"Ra":999,"Ke":999}  # Lower Bound
exaU = {"La":999,"Su":10,"Mo":33,"Ma":298,"Me":165,"Ju":95,"Ve":357,"Sa":200,"Ra":999,"Ke":999}  # Upper Bound

# Alternatively the entire Rashi can be made exalted 

exaR = {'La':99,'Su':1, 'Mo':2, 'Ma':10, 'Me':6,'Ju':4,'Ve':12,'Sa':7,'Ra':99,'Ke':99}

#Range of Debilitation
#Ref LHAE - page 30
debL = {"La":999,"Su":180,"Mo":210,"Ma":90,"Me":330,"Ju":270,"Ve":150,"Sa":0,"Ra":999,"Ke":999}  # Lower Bound
debU = {"La":999,"Su":190,"Mo":213,"Ma":118,"Me":345,"Ju":275,"Ve":177,"Sa":20,"Ra":999,"Ke":999}  # Upper Bound

#Alternatively the entire Rashi can be debilitated

debR = {'La':99,'Su':7, 'Mo':8, 'Ma':4, 'Me':12,'Ju':10,'Ve':6,'Sa':1,'Ra':99,'Ke':99}
mool3R = {'La':99,'Su':5, 'Mo':2, 'Ma':1, 'Me':6,'Ju':9,'Ve':7,'Sa':11,'Ra':99,'Ke':99}

# page 34

friends = {'Su':['Mo','Ma','Ju'], 'Mo':['Su','Me'],'Ma':['Su','Mo','Ju'],'Me':['Su','Ve'],'Ju':['Su','Mo','Ma'], 'Ve':['Me','Ve'],'Sa':['Me','Sa']}
#print(friends)
enemies ={'Su':['Ve','Sa'],'Mo':[],'Ma':['Me'],'Me':['Mo'],'Ju':['Me','Ve'],'Ve':['Su','Mo','Ma'],'Sa':['Su','Mo']}
#print(enemies)
neutrals = {'Su':['Me'],'Mo':['Ma','Ju','Ve','Sa'],'Ma':['Sa','Ve'],'Me':['Sa','Ma','Ju'],'Ju':['Sa'],'Ve':['Ju'],'Sa':['Ma','Ju']}
#print(neutrals)
# ------------------------------------------------------------------------------

Gx = ['La','Su', 'Mo', 'Ma', 'Me', 'Ju', 'Ve', 'Sa','Ra','Ke']

# ------------------------------------------------------------------------------
# Structure of Chart object and corresponding fields in MongoDB database
# Not all the database fields are retrieved while generating reports 
#

selCols = {
            '_id':0,
            'pid.name':1,               # Personal ID (name : str)  - obfuscated for privacy
            'pid.tags':1,               # Tags associated with individual
            #'pid.ChartType':1,         # chartType ['Rashi','Navamsa'] - currently only Rashi charts are stored, not Navamsa, however Navamsa is printed
            #'pid.ck':1,                # String carring original data as follows [Gender][YYYY][MM][YY][HH:mm][TZoffset][Lat][Lon]
            'pid.cID':1,                # Random String of Len 12, unique chartID
            #'BhavN':1,                 # [ List of Bhavs] -- not used in reporting
            #'BhavA':1,                 # [ List of Rashi Names for each Bhav] - not used in reporting
            'GRet':1,                   # Is Graha Retrograde?  { Graha: boolean }
            'GLon':1,                   # Graha Long { Graha : Long }
            'Lord':1,                   # Lords [ List of Bhav Lords]
            #'LordRashiN':1,            # [ Rashi number where each Lord resides] - not used in reporting
            #'LordRashiA':1,            # [ Rashi name where each Lord resides] - not used in reporting
            'GRashiN':1,                # [ Rashi number where each Graha resides]
            'GrahaLordBhav':1,          # Graha Lord of Bhav  { Graha : [List of Bhavs where Graha is Lord ]}
            'GrahaBhava':1,             # Graha Location in Bhav { Graha : Bhav }                         
            'LordBhav':1,               # Bhav Location of Lord [ List of Bhavs ]
            'exaltG':1,                 # Is Graha Exalted? { Graha : <boolean> }
            'exaltL':1,                 # Is Lord Exalted ? [ List of booleans]
            'debilG':1,                 # Is Graha Debilitated ? { Graha : <boolean>}
            'debilL':1,                 # Is Lord Debilitated ? [ List of booleans]
            'inFriendG':1,              # Is Graha in Friendly House ? { Graha : boolean}        
            'inFriendL':1,              # Is Lord in Friendly House ? [ List of booleans]
            'inEnemyG':1,               # Is Graha in Enemy House ?  { Graha : boolean}
            'inEnemyL':1,               # Is Lord in Enemy House ? [ List of Booleans]
            'GAspects2':1,              # Graha aspect whom ? { Graha : [ List of Grahas aspected]}
            'GAspectedBy2':1,           # Graha aspectedby whom ? { Graha : [ List of Grahas that aspect this Graha]}
            'BAspectedBy2':1,           # Bhava apectedby whom  ? { BhavNumber : [ List of Grahas that aspect this Bhav]}
            'BAspectedByBL2':1,         # Bhava apectedby whom  ? { BhavNumber : [ List of Bhava Lords]}
            'GConjunctsG2' :1 ,         # Which Graha Conjuncts Which Graha { Graha : [ List of Conjunct Grahas]} 
            'BLConjunctsG2':1 ,         # Which BhavLord conjuncts which Graha { Lord : [ List of Conjunct Grahas]}
            'BLConjunctsBL2':1,         # Which Bhav Lord conjuncts with Bhav Lord ( Lord : [ List of Lords]}
            'beneficG':1,               # Which Graha is Benefic for the Lagna of the person { Graha : <boolean> }
            'maleficG':1                # Which Graha is Malefic for the Lagna of the person { Graha : <boolean> }
           }

# --------------------------------------------------
yogsFound = []
AnalysisType = 'Rashi'                  # Default analysis type, alternate is Navamsha
# --------------------------------------------------
Subject = ''                            # Name of subject whose Gochar  is required
Gochar = False                          # Boolean used to catch Subject Moon Longitude
SubMoonLong = 0                         # Subjects Moon Longitude preserved for setting Lagna longitude of Gochar
gName = '_Gochar'                       # Dummy name for Gochar Chart 
# ----------------------------------------------------
# Vimsottari Dasha 
Nks1 = ['Ashwini','Bharani','Krittika','Rohini','Mrigashira','Ardra','Punarvasu','Pushya','Aslesha','Magha','P_Phalguni','U_Phalguni','Hasta','Chitra','Swati']
Nks2 = ['Vishakha','Anuradha','Jyeshtha','Mula','P_Ashada','U_Ashada','Shravana','Dhanistha','Shatavisha','P_Bhadrapad','U_Bhadrapad','Revati']
Nks = Nks1+Nks2
DashaSeq = ['Ke','Ve','Su','Mo','Ma','Ra','Ju','Sa','Me']

# Dasha Duration in Years
DashaDuration =[7,20,6,10,7,18,16,19,17]                                 # in years

#
#DashaDuraFract = [0.058,0.167,0.05,0.083,0.058,0.15,0.133,0.158,0.142]
DashaDuraFract = list(map(lambda x: x/120, DashaDuration))

#Dasha Duration in Days
#DashaDurationD =[2557,7305,2192,3653,2557,6575,5844,6940,6209]
#DashaDurationD = list(map(lambda x: round(365.25*x), DashaDuration))
DashaDurationD = list(map(lambda x: 365.25*x, DashaDuration))

DashaStart = ['Ke','Ve','Su','Mo','Ma','Ra','Ju','Sa','Me','Ke','Ve','Su','Mo','Ma','Ra','Ju','Sa','Me','Ke','Ve','Su','Mo','Ma','Ra','Ju','Sa','Me']
NksGap = 360/27

DoB = datetime.strptime("1999/1/1", "%Y/%m/%d")
printDasha = False

#print('imported p21')
