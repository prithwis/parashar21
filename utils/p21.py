# 𝓟𝓪𝓻𝓪𝓼𝓱𝓪𝓻21
# 𝓟𝓻𝓲𝓽𝓱𝔀𝓲𝓼 𝓜𝓾𝓴𝓮𝓻𝓳𝓮𝓮
# --------------------------------------------------
# Global Variables
global LordOf, Lord, GrahaLordBhav, LordRashiN,LordRashiA,LordInfo
global GrahaBhava, LordBhav, BhavOfGraha_LordInfo
global BhavN, BhavA, BhavNBhavA
global GRashiN, GRashiA
global GLon, GRet, pName, GLonRet
global ChartType
global ReportFile, document
# ------------------------------------------
global gregflag,iflag,hsysP
global chart
global BoL
global Graha, GMalefic
global exaL,exaU, exaR, debL, debU, debR, mool3R
global friends, enemies, neutrals
global exaltG, exaltL, debilL,debilG,mool3G,mool3L,ownHouseG,ownHouseL,inFriendG,inEnemyG,inNeutralG,inFriendL,inEnemyL,inNeutralL, Positions
# ------------------------------------------
BoL = ' '
LordOf = {"Ari":"Ma","Tau":"Ve","Gem":"Me","Can":"Mo","Leo":"Su","Vir":"Me","Lib":"Ve","Sco":"Ma","Sag":"Ju","Cap":"Sa","Acq":"Sa","Pis":"Ju"} 

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
