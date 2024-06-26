#Copyright (c) 2022, Prithwis Mukerjee
#All rights reserved.
#
#This source code is licensed under the GNU GPL v3.0 -style license found in the
#LICENSE file in the root directory of this source tree. 
# --------------------------------------------------
# Global Variables
import p21
import p21swe
# --------------------------------------------------
#Utility functions 

import pandas as pd
import dateutil
import matplotlib.pyplot as plt
import math
#import math
import numbers
#import string_utils

import json

#from docx import Document
#from docx.shared import Inches
#from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime
from datetime import timedelta

#import swisseph as swe
import pytz




# append one ditionary after another

def appendDict(d1,d2):
    for i in range(len(d2)):
        k = list(d2.keys())[i]
        v = list(d2.values())[i]
        d1[k] = v


# --------------------------------------------------
#converting dict{ionary} to list and back

d2l = lambda dic: [(k, v) for (k, v) in dic.items()]
l2d = lambda lis: dict(lis)



# --------------------------------------------------

#Determines and stores the Bhava in list BhavN
#BhavN[1] has Rashi Number corresponding to First Bhav
#BhavA[2] has the Rashi name corresponding to Second Bhava
#
def C10_DetermineBhavs():

    p21.BhavN = [p21.BoL]
    for ix in range(1,13):
        if ix == 1:
            p21.BhavN.append(p21.GRashiN['La'])
        else:
            N = p21.BhavN[ix-1]+1
            if N > 12:
                N = N - 12
            p21.BhavN.append(N)
        
    
    p21.BhavA = list(map(lambda x : p21.RashiN2A(x) if isinstance(x, numbers.Integral) else p21.BoL,p21.BhavN))
    
    p21.BhavNBhavA = {
        'BhavN': p21.BhavN,
        'BhavA': p21.BhavA
    }

# --------------------------------------------------

#Determines the Lord of each Bhava
#Determines the Rashi number where each Lord resides
#Determines the Rashi name where each Lord resides
#
def C11_DetermineLord():

    #p21.LordOf = {"Ari":"Ma","Tau":"Ve","Gem":"Me","Can":"Mo","Leo":"Su","Vir":"Me","Lib":"Ve","Sco":"Ma","Sag":"Ju","Cap":"Sa","Acq":"Sa","Pis":"Ju"}
    #print(LordOf)
    p21.Lord = list(map(lambda x : p21.LordOf[p21.RashiN2A(x)] if isinstance(x, numbers.Integral) else p21.BoL, p21.BhavN))
    #print("Lord : ", p21.Lord)
    p21.LordRashiN = list(map(lambda x : p21.GRashiN[x] if x != p21.BoL else p21.BoL, p21.Lord))
    #print("Rashi # of Lord : ",p21.LordRashiN)
    p21.LordRashiA = list(map(lambda x : p21.GRashiA[x] if x != p21.BoL else p21.BoL, p21.Lord))
    #print("Rashi Name of Lord :",p21.LordRashiA)

# --------------------------------------------------

#Determines the Bhava where each Graha is Lord
#Grahas other than Sun and Moon are Lords of Two Bhava
#Since index returns only the first position where an instance is found
#A simple index() does not return the second position
# https://stackoverflow.com/questions/22267241/how-to-find-the-index-of-the-nth-time-an-item-appears-in-a-list


    p21.GrahaLordBhav = {}
    for G in ('Su','Mo','Ma','Me','Ju','Ve','Sa'):
            L = [i for i, n in enumerate(p21.Lord) if n == G]
            p21.GrahaLordBhav[G] = L
    #print('Bhav where Graha is Lord : ',p21.GrahaLordBhav)
    
    p21.LordInfo = {
     'Lord' : p21.Lord,
     'LordRashiN' : p21.LordRashiN,
     'LordRashiA' : p21.LordRashiA,
     'GrahaLordBhav' : p21.GrahaLordBhav
    }


def C12_BhavOfGraha_Lord():

#Determines the Bhava where Each planet resides
#Lagna always resides in First Bhava
#
    p21.GrahaBhava ={"La":1}
    for G in ('Su','Mo','Ma','Me','Ju','Ve','Sa','Ra','Ke'):
        p21.GrahaBhava[G] = p21.BhavN.index(p21.GRashiN[G])
    #print (p21.GrahaBhava)

#Determines the Bhav where each Lord resides
#

    p21.LordBhav =[p21.BoL]
    for L in range (1,13):
        p21.LordBhav.append(p21.BhavN.index(p21.GRashiN[p21.Lord[L]]))
    #print(p21.LordBhav)

    p21.BhavOfGraha_LordInfo = {
     'GRashiN' : p21.GRashiN,
     'GrahaBhava' : p21.GrahaBhava,
     'LordBhav' : p21.LordBhav
    }


def C12A_StoreRashiOfGraha():

#Determines the Rashi where Each planet resides

    
    
    print(p21.GRashiN)
    print(p21.GRashiA)





#
# MULTI STATUS
#

# the low parameter is used to indicate that the entire Rashi is used for exaltation
# the high parameter is used to indicate that only the specific part of the Rashi is used

def C21A_checkGexa(x,level = 'low'):
    if level == 'low':
        if p21.GRashiN[x] == p21.exaR[x]:
            return x,True
        else:
            return x,False
        
    if level == 'high':
        lon = p21.GLon[x]
        if lon > p21.exaL[x] and lon <= p21.exaU[x]:
            return x,True
        else:
            return x,False
    
def C21B_checkLexa(x):
    if x == p21.BoL:
        return False
    else:
        return p21.exaltG[x]

def C21C_checkGdeb(x, level = 'low'):
    
    if level == 'low':
        if p21.GRashiN[x] == p21.debR[x]:
            return x,True
        else:
            return x,False
    
    if level == 'high':
        lon = p21.GLon[x]
        if lon > p21.debL[x] and lon <= p21.debU[x]:
            return x,True
        else:
            return x,False
    
    
def C21D_checkLdeb(x):
    if x == p21.BoL:
        return False
    else:
        return p21.debilG[x]
        
def C21E_checkm3G(x):
    
    if p21.GRashiN[x] == p21.mool3R[x]:
        return x,True
    else:
        return x,False
        
def C21F_checkOwnHG(x):
    if x == p21.LordOf[p21.GRashiA[x]]:
        return x, True
    else:
        return x, False
        
        
#check f(riends)e(nemy)n(eutral)
#
def C21G_checkfen(x,Z):
    if p21.LordOf[p21.GRashiA[x]] in Z[x]:
        return x,True
    else:
        return x,False


def C21_DeterminePositions():
    p21.exaltG = l2d(list(map(lambda x: C21A_checkGexa(x), p21.Graha)))               # determines if Graha is Exalted
    #print('Exalted Graha',p21.exaltG)
    p21.exaltL = list(map(lambda x: C21B_checkLexa(x),p21.Lord))                       # determines if Lord is exalted
    #print('Exalted Lord',p21.exaltL)
    
    p21.debilG = l2d(list(map(lambda x: C21C_checkGdeb(x),p21.Graha)))               # determines if Graha is debilitated
    #print('Debilited Graha',p21.debilG)
    p21.debilL = list(map(lambda x: C21D_checkLdeb(x),p21.Lord))
    #print('Debilited Lord',p21.debilL)
    
    p21.mool3G = l2d(list(map(lambda x: C21E_checkm3G(x),p21.Graha))) 
    #print('Mool3G',p21.mool3G)
    p21.mool3L = [False]*13

    for ix in range(1,13):
        #print(ix)
        p21.mool3L[ix] = p21.mool3G[p21.Lord[ix]]
    #print('Mool3L',p21.mool3L)

    p21.ownHouseG = l2d(list(map(lambda x: C21F_checkOwnHG(x),p21.Graha)))
    #print('ownHouseG',p21.ownHouseG)
    
    p21.ownHouseL = [False]*13

    for ix in range(1,13):
        #print(ix)
        p21.ownHouseL[ix] = p21.ownHouseG[p21.Lord[ix]]
    #print('ownHouseL',p21.ownHouseL)
    
    
    p21.inFriendG =  l2d(list(map(lambda x: C21G_checkfen(x,p21.friends),p21.Graha)))
    p21.inEnemyG =  l2d(list(map(lambda x: C21G_checkfen(x,p21.enemies),p21.Graha)))
    p21.inNeutralG =  l2d(list(map(lambda x: C21G_checkfen(x,p21.neutrals),p21.Graha)))
    
    #print('inFriendG',p21.inFriendG)
    #print('inEnemyG',p21.inEnemyG)
    #print('inNeutralG',p21.inNeutralG)

    p21.inFriendL = [False]*13
    p21.inEnemyL = [False]*13
    p21.inNeutralL = [False]*13

    for ix in range(1,13):
        p21.inFriendL[ix] = p21.inFriendG[p21.Lord[ix]]
        p21.inEnemyL[ix] = p21.inEnemyG[p21.Lord[ix]]
        p21.inNeutralL[ix] = p21.inNeutralG[p21.Lord[ix]]
        
    #print('inFriendL',p21.inFriendL)
    #print('inEnemyL',p21.inEnemyL)
    #print('inNeutralL',p21.inNeutralL)
    
    p21.Positions = {
        'exaltG' : p21.exaltG,
        'debilG' : p21.debilG,
        #'mool3G' : p21.mool3G,
        'ownHouseG' : p21.ownHouseG,
        'inFriendG' : p21.inFriendG,
        'inEnemyG' : p21.inEnemyG,
        #'inNeutralG' : p21.inNeutralG,
        'exaltL' : p21.exaltL,
        'debilL' : p21.debilL,
        #'mool3L' : p21.mool3L,
        'ownHouseL' : p21.ownHouseL,
        'inFriendL' : p21.inFriendL,
        'inEnemyL' : p21.inEnemyL
        #'inNeutralL' : p21.inNeutralL,
    }


# --------------------------------------------------

# Convert the longitude of a Graha into its Rashi of residence
#
# Navamsa is different
# http://www.oocities.org/talk2astrologer/LearnAstrology/Details/Navamsa.html
#
# the logic for placing a Graha in a 'Navamsa' Rashi is as follows
# starting from Longitude 0 [ 'Normal' Aries / Mesha start point]
# upto Longitude 360, we divide the longitudes in 108 partitions with each 
# partition being 3.33333 degrees. These 108 partitions are now numbered 
# sequentially, except that once we reach 12, the next partition is 1, not
# 13. So we have 9 sequences running from 1 - 12 each. The number corresponding
# to the partition where the Graha falls is the Navamsa Rashi of the Graha


def Long2Rashi(x):
    
    if p21.ChartType == 'Rashi':
        RashiNumber = math.floor(x[1]/30)+1
        return x[0],RashiNumber
    if p21.ChartType == 'Navamsa':
        N1 = math.floor(x[1]/3.333333)+1
        N2 = N1%12
        if N2 == 0:
            RashiNumber = 12
        else:
            RashiNumber = N2
        return x[0],RashiNumber

# --------------------------------------------------
#Defines the Horoscope in terms of locating planets in their Rashis

def R11_LocateGrahaInRashi():
    
    
    #print('Loc',p21.ChartType)
    p21.GRashiN = l2d(list(map(lambda x : Long2Rashi(x), d2l(p21.GLon))))
    #print(p21.GRashiN)

    p21.GRashiA = {}
    for k,v in p21.GRashiN.items():
        p21.GRashiA[k] = p21.RashiN2A(v)
        
    #print(p21.GRashiA)
    
# --------------------------------------------------

#Aspects

# ---------------------------------------------------

def RashiGapA(R2,R1):
    if (R2>R1):
        return R2-R1
    else:
        return R2-R1+12
    
def addToD(x,D,y):
    if x in D:
        D[x].add(y)
    else:
        D[x] = set()
        D[x].add(y)
        
# convert set in dictionary value to list
# this is required for JSON formatting 

# Bhav number as dict keys have to be converted to str()
# Otherwise could not store in MongoDB
def csidtil(D):
    nD = dict()
    for k in D:
        nD[k] = list(D[k])
        
    #print(nD)
    return(nD)

def C31_DetermineAspects():

    p21.GAspects = dict()           # Which Graha aspects which other Graha
    p21.GAspectedBy = dict()        # Which Graha is aspected by which other Graha
    p21.BAspectedBy = dict()        # Which Bhav is aspected by which other Graha
    p21.BAspectedByBL = dict()      # Which Bhav is aspected by which Bhav Lord



    for O1 in p21.Gx:
        for O2 in p21.Gx:
            #Normal 7th Aspect
            if (RashiGapA(p21.GRashiN[O2],p21.GRashiN[O1]) == 6):
                #print(O1,GRashiN[O1],O2,GRashiN[O2],RashiGapA(GRashiN[O2],GRashiN[O1]))
                if not (O1 in ['Ra','Ke'] and O2 in ['Ra','Ke']):
                    addToD(O1,p21.GAspects,O2)
                    addToD(O2,p21.GAspectedBy,O1)
            #Mars 4,8th Aspect
            if (O1 == 'Ma') and (
                (RashiGapA(p21.GRashiN[O2],p21.GRashiN[O1]) == 3) or
                (RashiGapA(p21.GRashiN[O2],p21.GRashiN[O1]) == 7)):
                addToD(O1,p21.GAspects,O2)
                addToD(O2,p21.GAspectedBy,O1)
            #Jupiter 5,9th Aspect
            if (O1 == 'Ju') and (
                (RashiGapA(p21.GRashiN[O2],p21.GRashiN[O1]) == 4) or
                (RashiGapA(p21.GRashiN[O2],p21.GRashiN[O1]) == 8)):
                addToD(O1,p21.GAspects,O2)
                addToD(O2,p21.GAspectedBy,O1)
            #Saturn 3,10th Aspect
            if (O1 == 'Sa') and (
                (RashiGapA(p21.GRashiN[O2],p21.GRashiN[O1]) == 2) or
                (RashiGapA(p21.GRashiN[O2],p21.GRashiN[O1]) == 9)):
                addToD(O1,p21.GAspects,O2)
                addToD(O2,p21.GAspectedBy,O1)


    # Bhav number as dict keys have to be converted to str()
    # Otherwise could not store in MongoDB
    for O1 in p21.Gx:
        for BN in range(1,13):
            #Normal 7th Aspect
            if (RashiGapA(p21.BhavN[BN],p21.GRashiN[O1]) == 6):
                #print(O1,GRashiN[O1],O2,GRashiN[O2],RashiGapA(GRashiN[O2],GRashiN[O1]))
                addToD(str(BN),p21.BAspectedBy,O1)
               
            #Mars 4,8th Aspect
            if (O1 == 'Ma') and (
                (RashiGapA(p21.BhavN[BN],p21.GRashiN[O1]) == 3) or
                (RashiGapA(p21.BhavN[BN],p21.GRashiN[O1]) == 7)):
                addToD(str(BN),p21.BAspectedBy,O1)
             
            #Jupiter 5,9th Aspect
            if (O1 == 'Ju') and (
                (RashiGapA(p21.BhavN[BN],p21.GRashiN[O1]) == 4) or
                (RashiGapA(p21.BhavN[BN],p21.GRashiN[O1]) == 8)):
                addToD(str(BN),p21.BAspectedBy,O1)
                
            #Saturn 3,10th Aspect
            if (O1 == 'Sa') and (
                (RashiGapA(p21.BhavN[BN],p21.GRashiN[O1]) == 2) or
                (RashiGapA(p21.BhavN[BN],p21.GRashiN[O1]) == 9)):
                addToD(str(BN),p21.BAspectedBy,O1)
     
    #print("BAspectedBy",p21.BAspectedBy)
    
    for BN1 in range(1,13):
        for BN2 in range(1,13):      
            if str(BN1) in p21.BAspectedBy.keys():
                if  p21.Lord[BN2] in p21.BAspectedBy[str(BN1)]:
                    addToD(str(BN1),p21.BAspectedByBL,str(BN2))
    
    #print("GAspects",p21.GAspects)
    #print("GAspectedBy",p21.GAspectedBy)
    #print("BAspectedBy",p21.BAspectedBy)  
    
    # Bhav number as dict keys have to be converted to str()
    # Otherwise could not store in MongoDB
    
    p21.GAspects2 = csidtil(p21.GAspects)
    p21.GAspectedBy2 = csidtil(p21.GAspectedBy)
    p21.BAspectedBy2 = csidtil(p21.BAspectedBy)
    p21.BAspectedByBL2 = csidtil(p21.BAspectedByBL)

    #print("GAspects2",p21.GAspects2)
    #print("GAspectedBy2",p21.GAspectedBy2)
    #print("BAspectedBy2",p21.BAspectedBy2)
    
    p21.Aspects = {
    'GAspects2'   :p21.GAspects2,
    'GAspectedBy2':p21.GAspectedBy2,
    'BAspectedBy2':p21.BAspectedBy2,
    'BAspectedByBL2':p21.BAspectedByBL2
    }

def C41_DetermineConjuncts():

    p21.GConjunctsG = dict()        # Which Graha is conjunct which other Graha
    p21.BLConjunctsG = dict()       # Which Lord is conjunct by which Graha
    p21.BLConjunctsBL = dict()      # Which Bhav Lord is conjunct by which Bhav Lord



    for O1 in p21.Gx[1:]:                   # ignore 'La'
        for O2 in p21.Gx[1:]:               # ignore 'La'
            #Two Different Grahas in Same Rashi
            if (p21.GRashiN[O2] == p21.GRashiN[O1]) and (O2 != O1):
                addToD(O1,p21.GConjunctsG,O2)
                addToD(O2,p21.GConjunctsG,O1)
            
    #print(p21.GConjunctsG)
    #print(p21.Lord)
    
    
    for BN in range(1,13):
        for O1 in p21.Gx[1:]:                   # ignore 'La'
            if (p21.GRashiN[p21.Lord[BN]] == p21.GRashiN[O1]) and (p21.Lord[BN] != O1)  :
                addToD(str(BN),p21.BLConjunctsG,O1)
    #print(p21.BLConjunctsG)
    
    for BN1 in range(1,13):
        for BN2 in range(1,13):                   
            #if (p21.GRashiN[p21.Lord[BN1]] == p21.GRashiN[p21.Lord[BN2]]) and (str(BN2) not in p21.Lord[BN1]+p21.Lord[BN2])  :
            #if (p21.GRashiN[p21.Lord[BN1]] == p21.GRashiN[p21.Lord[BN2]])  and (p21.Lord[BN1] not in p21.GrahaLordBhav[p21.Lord[BN1]]) :
            if  p21.LordBhav[BN2] == p21.LordBhav[BN1] and (BN2 not in p21.GrahaLordBhav[p21.Lord[BN1]]) :
                addToD(str(BN1),p21.BLConjunctsBL,str(BN2))
    #print(p21.BLConjunctsBL)

    # Bhav number as dict keys have to be converted to str()
    # Otherwise could not store in MongoDB
    
    p21.GConjunctsG2 = csidtil(p21.GConjunctsG)
    p21.BLConjunctsG2 = csidtil(p21.BLConjunctsG)
    p21.BLConjunctsBL2 = csidtil(p21.BLConjunctsBL)
    
    p21.Conjuncts = {
    'GConjunctsG2'   :p21.GConjunctsG2,
    'BLConjunctsG2':p21.BLConjunctsG2,
    'BLConjunctsBL2':p21.BLConjunctsBL2
    }
    
#
# Benefics, Malefics
#
def C51_DetermineBenMal():
    #
    # based on https://www.clickastro.com/blog/planets-in-birth-chart/   -- NOT USED
    # based on https://shrivinayakaastrology.com/Planets/beneficandmaleficplanets.html
    #
    L = p21.RashiN2A(p21.GRashiN['La'])
    #print(L)
    if L == 'Mesh':
        p21.beneficG = {'Su': True, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False}
        p21.maleficG = {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        
    elif L == 'Vrish':
        p21.beneficG = {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': True}
        p21.maleficG = {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        
    elif L == 'Mithun':
        p21.beneficG = {'Su': False, 'Mo': False, 'Ma': False, 'Me': False, 'Ju': False, 'Ve': True, 'Sa': True}
        p21.maleficG = {'Su': True, 'Mo': False, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        
    elif L == 'Karkat':
        p21.beneficG = {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': False, 'Ve': False, 'Sa': False}
        p21.maleficG = {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': True, 'Ve': False, 'Sa': True, 'Ra': False, 'Ke': False}
        
    elif L == 'Simha':
        p21.beneficG = {'Su': True, 'Mo': False, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False}
        p21.maleficG = {'Su': False, 'Mo': True, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': False, 'Ra': True, 'Ke': True}
        
    elif L == 'Kanya':
        p21.beneficG = {'Su': False, 'Mo': False, 'Ma': False, 'Me': False, 'Ju': False, 'Ve': True, 'Sa': False}
        p21.maleficG = {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        
    elif L == 'Tula':
        p21.beneficG = {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': True}
        p21.maleficG = {'Su': True, 'Mo': False, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        
    elif L == 'Vrishchik':
        p21.beneficG = {'Su': True, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False}
        p21.maleficG = {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': False, 'Ra': True, 'Ke': True}
        
    elif L == 'Dhanu':
        p21.beneficG = {'Su': True, 'Mo': False, 'Ma': True, 'Me': False, 'Ju': False, 'Ve': False, 'Sa': False}
        p21.maleficG = {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': False, 'Ra': True, 'Ke': True}
        
    elif L == 'Makar':
        p21.beneficG = {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': True}
        p21.maleficG = {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': False, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        
    elif L == 'Kumbh':
        p21.beneficG = {'Su': False, 'Mo': False, 'Ma': False, 'Me': False, 'Ju': False, 'Ve': True, 'Sa': True}
        p21.maleficG = {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        
    elif L == 'Meen':
        p21.beneficG = {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False}
        p21.maleficG = {'Su': True, 'Mo': False, 'Ma': False, 'Me': False, 'Ju': False, 'Ve': True, 'Sa': False, 'Ra': True, 'Ke': True}
        
    else:
        print("Wrong Lagna", L)
    #print('Benefic G', p21.beneficG) 
    #print('Malefic G', p21.maleficG)   
    p21.BenMalG = {
      'beneficG'  : p21.beneficG,
      'maleficG' : p21.maleficG 
    }
# -----------------------------------------------------
# Vimsottari Dasha Functions
#
#
def NextDasha(cd):
  cdIndex = p21.DashaSeq.index(cd)
  ndIndex = cdIndex+1
  if ndIndex > 8:
    ndIndex = 0
  return(p21.DashaSeq[ndIndex])

# Generates Dasha, Antardasha Dates
# 
def GetDasha():
  
  print('p21.SubMoonLong ',p21.SubMoonLong)
  BirthNks = int(p21.SubMoonLong/p21.NksGap)                    # Number of Birth Nakshatra
  print('Birth Nakshatra ',BirthNks,p21.Nks[BirthNks])
  
  BirthDasha = p21.DashaStart[BirthNks]                         # BirthDasha
  #print('BirthDasha ',BirthDasha)
  
  BirthDashaIndex = p21.DashaSeq.index(BirthDasha)
  #print('Birth Dasha Index', BirthDashaIndex, )

  DashaConsumedDeg = p21.SubMoonLong - BirthNks*p21.NksGap
  #print(DashaConsumedDeg)
  #DashaConsumedDuration = round((DashaConsumedDeg/p21.NksGap) * p21.DashaDurationD[BirthDashaIndex])
  DashaConsumedDuration = (DashaConsumedDeg/p21.NksGap) * p21.DashaDurationD[BirthDashaIndex]          # Rounding Causes cumulative errors

  #print('Birth Dasha Duration',p21.DashaDurationD[BirthDashaIndex], 'Birth Dasha Consumed Duration', DashaConsumedDuration )
  #DaysToStartOfBirthDasha = int(DashaConsumedDuration * 365)
  
  StartOfBirthDasha = p21.DoB - timedelta(days=DashaConsumedDuration)
  #print('Start of Birth Dasha',StartOfBirthDasha)
  #print('Date of Birth',p21.DoB)
  L1Dasha = BirthDasha
  StartOfL1Dasha = StartOfBirthDasha
  p21.VimDasha = {}
  for i in range(9):
    L1DashaDuration = p21.DashaDurationD[p21.DashaSeq.index(L1Dasha)]
    EndOfL1Dasha = StartOfL1Dasha + timedelta(days=L1DashaDuration)
    DashaDict = {}
    
    DashaDict['Start'] = StartOfL1Dasha.strftime("%d %b %Y")
    DashaDict['End'] = EndOfL1Dasha.strftime("%d %b %Y")
    DashaDict['Duration'] = L1DashaDuration
    L2Dasha = L1Dasha
    StartOfL2Dasha = StartOfL1Dasha
    for j in range(9):
      AntarDashaDict = {}
      #L2DashaDuration = round(L1DashaDuration * p21.DashaDuraFract[p21.DashaSeq.index(L2Dasha)])
      L2DashaDuration = L1DashaDuration * p21.DashaDuraFract[p21.DashaSeq.index(L2Dasha)]

      #L2DashaDuration = L1DashaDuration * p21.DashaDuraFract[p21.DashaSeq.index(L2Dasha)]
      EndOfL2Dasha = StartOfL2Dasha + timedelta(days=L2DashaDuration)
      AntarDashaDict['Start'] = StartOfL2Dasha.strftime("%d %b %Y")
      AntarDashaDict['End'] = EndOfL2Dasha.strftime("%d %b %Y")
      AntarDashaDict['Duration'] = L2DashaDuration
      #AntarDashaDict['Antardasha'] = L2Dasha
      #AntarDashaDict[L2Dasha] = AntarDashaDictX
      DashaDict[L2Dasha] = AntarDashaDict
      #L2Dasha = p21utils.NextDasha(L2Dasha)
      L2Dasha = NextDasha(L2Dasha)
      StartOfL2Dasha = EndOfL2Dasha
    p21.VimDasha[L1Dasha] = DashaDict
    #print(i+1,'Dasha',Dasha,'Starts',StartOfDasha,'Ends',EndOfDasha,'Followed by',p21utils.NextDasha(Dasha))
    #L1Dasha = p21utils.NextDasha(L1Dasha)
    L1Dasha = NextDasha(L1Dasha)
    StartOfL1Dasha = EndOfL1Dasha
  

# --------------------------------------------------



def GenAshtakVargaData_v1():                                         # Deprecated
#
# Calculation of AshtaVarga Points  has been taken from the following website
# 1 https://www.thevedichoroscope.com/asthvarga-lessons/asthvarga-lessons-1/
# 2 https://ashtakvargajyoti.wordpress.com/category/ashtakvarga-system/
# 3 https://blog.indianastrologysoftware.com/the-ashtakavarga-of-moon/
#
# Tested on 3 Aug 2023. 
# though there are minor variations in each source, we have checked the Ashtakvarga Points
# on the 8 sample horoscopes in the main notebook and in each case, the checksum correct 337 
#In case other horoscopes do not add up to this exact 337 number,the following data may have to be reviewed
#
    def nxt(s,p):
        d = s+p-1
        if d > 12:
            d = d - 12
        return(d)
    #
    # Bhinna Ashtak Varga Points for Su
    # ----------------------------------------
    b8v_Su = [0,0,0,0,0,0,0,0,0,0,0,0]

    start = p21.GRashiN['Su']
    for i in [1,2,4,7,8,9,10,11]:
        b8v_Su[nxt(start,i)-1] = b8v_Su[nxt(start,i)-1] + 1
    start = p21.GRashiN['Mo']
    for i in [3,6,10,11]:
        b8v_Su[nxt(start,i)-1] = b8v_Su[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ma']
    for i in [1,2,4,7,8,9,10,11]:
        b8v_Su[nxt(start,i)-1] = b8v_Su[nxt(start,i)-1] + 1
    start = p21.GRashiN['Me']
    for i in [3,5,6,9,10,11,12]:
        b8v_Su[nxt(start,i)-1] = b8v_Su[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ju']
    for i in [5,6,9,11]:
        b8v_Su[nxt(start,i)-1] = b8v_Su[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ve']
    for i in [6,7,12]:
        b8v_Su[nxt(start,i)-1] = b8v_Su[nxt(start,i)-1] + 1
    start = p21.GRashiN['Sa']
    for i in [1,2,4,7,8,9,10,11]:
        b8v_Su[nxt(start,i)-1] = b8v_Su[nxt(start,i)-1] + 1
    start = p21.GRashiN['La']
    for i in [3,4,6,10,11,12]:
        b8v_Su[nxt(start,i)-1] = b8v_Su[nxt(start,i)-1] + 1
        
    #print('b8v_Su',b8v_Su)
        
    #
    # Bhinna Ashtak Varga Points for Mo
    # ----------------------------------------
    
   
    b8v_Mo = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    start = p21.GRashiN['Su']
    for i in [3,6,7,8,10,11]:
        b8v_Mo[nxt(start,i)-1] = b8v_Mo[nxt(start,i)-1] + 1
    start = p21.GRashiN['Mo']
    for i in [1,3,6,7,9,10,11]:                                       # https://ashtakvargajyoti.wordpress.com/2014/12/08/moons-ashtakvarga-basic-understanding/
        b8v_Mo[nxt(start,i)-1] = b8v_Mo[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ma']
    for i in [2,3,5,6,10,11]:
        b8v_Mo[nxt(start,i)-1] = b8v_Mo[nxt(start,i)-1] + 1
    start = p21.GRashiN['Me']
    for i in [1,3,4,5,7,8,10,11]:
        b8v_Mo[nxt(start,i)-1] = b8v_Mo[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ju']
    for i in [1,2,4,7,8,10,11]:
        b8v_Mo[nxt(start,i)-1] = b8v_Mo[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ve']
    for i in [3,4,5,7,9,10,11]:
        b8v_Mo[nxt(start,i)-1] = b8v_Mo[nxt(start,i)-1] + 1
    start = p21.GRashiN['Sa']
    for i in [3,5,6,11]:
        b8v_Mo[nxt(start,i)-1] = b8v_Mo[nxt(start,i)-1] + 1
    start = p21.GRashiN['La']
    for i in [3,6,10,11]:
        b8v_Mo[nxt(start,i)-1] = b8v_Mo[nxt(start,i)-1] + 1
    
    #print('b8v_Mo 2',b8v_Mo)

    #
    # Bhinna Ashtak Varga Points for Ma
    # ----------------------------------------
    b8v_Ma = [0,0,0,0,0,0,0,0,0,0,0,0]

    start = p21.GRashiN['Su']
    for i in [3,5,6,10,11]:
        b8v_Ma[nxt(start,i)-1] = b8v_Ma[nxt(start,i)-1] + 1
    start = p21.GRashiN['Mo']
    for i in [3,6,11]:
        b8v_Ma[nxt(start,i)-1] = b8v_Ma[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ma']
    for i in [1,2,4,7,8,10,11]:
        b8v_Ma[nxt(start,i)-1] = b8v_Ma[nxt(start,i)-1] + 1
    start = p21.GRashiN['Me']
    for i in [3,5,6,11]:
        b8v_Ma[nxt(start,i)-1] = b8v_Ma[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ju']
    for i in [6,10,11,12]:
        b8v_Ma[nxt(start,i)-1] = b8v_Ma[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ve']
    for i in [6,8,11,12]:
        b8v_Ma[nxt(start,i)-1] = b8v_Ma[nxt(start,i)-1] + 1
    start = p21.GRashiN['Sa']
    for i in [1,4,7,8,9,10,11]:
        b8v_Ma[nxt(start,i)-1] = b8v_Ma[nxt(start,i)-1] + 1
    start = p21.GRashiN['La']
    for i in [1,3,6,10,11]:
        b8v_Ma[nxt(start,i)-1] = b8v_Ma[nxt(start,i)-1] + 1
        
    #print('b8v_Ma',b8v_Ma)
    
    #
    # Bhinna Ashtak Varga Points for Me
    # ----------------------------------------
    b8v_Me = [0,0,0,0,0,0,0,0,0,0,0,0]

    start = p21.GRashiN['Su']
    for i in [5,6,9,11,12]:
        b8v_Me[nxt(start,i)-1] = b8v_Me[nxt(start,i)-1] + 1
    start = p21.GRashiN['Mo']
    for i in [2,4,6,8,10,11]:
        b8v_Me[nxt(start,i)-1] = b8v_Me[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ma']
    for i in [1,2,4,7,8,9,10,11]:
        b8v_Me[nxt(start,i)-1] = b8v_Me[nxt(start,i)-1] + 1
    start = p21.GRashiN['Me']
    for i in [1,3,5,6,9,10,11,12]:
        b8v_Me[nxt(start,i)-1] = b8v_Me[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ju']
    for i in [6,8,11,12]:
        b8v_Me[nxt(start,i)-1] = b8v_Me[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ve']
    for i in [1,2,3,4,5,8,9,11]:
        b8v_Me[nxt(start,i)-1] = b8v_Me[nxt(start,i)-1] + 1
    start = p21.GRashiN['Sa']
    for i in [1,2,4,7,8,9,10,11]:
        b8v_Me[nxt(start,i)-1] = b8v_Me[nxt(start,i)-1] + 1
    start = p21.GRashiN['La']
    for i in [1,2,4,6,8,10,11]:
        b8v_Me[nxt(start,i)-1] = b8v_Me[nxt(start,i)-1] + 1
        
    #print('b8v_Me',b8v_Me)
    
    #
    # Bhinna Ashtak Varga Points for Ju
    # ----------------------------------------
    b8v_Ju = [0,0,0,0,0,0,0,0,0,0,0,0]

    start = p21.GRashiN['Su']
    for i in [1,2,3,4,7,8,9,10,11]:
        b8v_Ju[nxt(start,i)-1] = b8v_Ju[nxt(start,i)-1] + 1
    start = p21.GRashiN['Mo']
    for i in [2,5,7,9,11]:
        b8v_Ju[nxt(start,i)-1] = b8v_Ju[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ma']
    for i in [1,2,4,7,8,10,11]:
        b8v_Ju[nxt(start,i)-1] = b8v_Ju[nxt(start,i)-1] + 1
    start = p21.GRashiN['Me']
    for i in [1,2,4,5,6,9,10,11]:                                                   # error data # https://ashtakvargajyoti.wordpress.com/category/ashtakvarga-system/
        b8v_Ju[nxt(start,i)-1] = b8v_Ju[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ju']
    for i in [1,2,3,4,7,8,10,11]:
        b8v_Ju[nxt(start,i)-1] = b8v_Ju[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ve']
    for i in [2,5,6,9,10,11]:
        b8v_Ju[nxt(start,i)-1] = b8v_Ju[nxt(start,i)-1] + 1
    start = p21.GRashiN['Sa']
    for i in [3,5,6,12]:
        b8v_Ju[nxt(start,i)-1] = b8v_Ju[nxt(start,i)-1] + 1
    start = p21.GRashiN['La']
    for i in [1,2,4,5,6,7,9,10,11]:
        b8v_Ju[nxt(start,i)-1] = b8v_Ju[nxt(start,i)-1] + 1
        
    #print('b8v_Ju',b8v_Ju)
    
    #
    # Bhinna Ashtak Varga Points for Ve
    # ----------------------------------------
    b8v_Ve = [0,0,0,0,0,0,0,0,0,0,0,0]

    start = p21.GRashiN['Su']
    for i in [8,11,12]:
        b8v_Ve[nxt(start,i)-1] = b8v_Ve[nxt(start,i)-1] + 1
    start = p21.GRashiN['Mo']
    for i in [1,2,3,4,5,8,9,11,12]:
        b8v_Ve[nxt(start,i)-1] = b8v_Ve[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ma']
    for i in [3,5,6,9,11,12]:
        b8v_Ve[nxt(start,i)-1] = b8v_Ve[nxt(start,i)-1] + 1
    start = p21.GRashiN['Me']
    for i in [3,5,6,9,11]:
        b8v_Ve[nxt(start,i)-1] = b8v_Ve[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ju']
    for i in [5,8,9,10,11]:
        b8v_Ve[nxt(start,i)-1] = b8v_Ve[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ve']
    for i in [1,2,3,4,5,8,9,10,11]:
        b8v_Ve[nxt(start,i)-1] = b8v_Ve[nxt(start,i)-1] + 1
    start = p21.GRashiN['Sa']
    for i in [3,4,5,8,9,10,11]:
        b8v_Ve[nxt(start,i)-1] = b8v_Ve[nxt(start,i)-1] + 1
    start = p21.GRashiN['La']
    for i in [1,2,3,4,5,8,9,11]:
        b8v_Ve[nxt(start,i)-1] = b8v_Ve[nxt(start,i)-1] + 1
        
    #print('b8v_Ve',b8v_Ve)
    
    #
    # Bhinna Ashtak Varga Points for Sa
    # ----------------------------------------
    b8v_Sa = [0,0,0,0,0,0,0,0,0,0,0,0]

    start = p21.GRashiN['Su']
    for i in [1,2,4,7,8,10,11]:
        b8v_Sa[nxt(start,i)-1] = b8v_Sa[nxt(start,i)-1] + 1
    start = p21.GRashiN['Mo']
    for i in [3,6,11]:
        b8v_Sa[nxt(start,i)-1] = b8v_Sa[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ma']
    for i in [3,5,6,10,11,12]:
        b8v_Sa[nxt(start,i)-1] = b8v_Sa[nxt(start,i)-1] + 1
    
    start = p21.GRashiN['Me']
    for i in [6,8,9,10,11,12]:
        b8v_Sa[nxt(start,i)-1] = b8v_Sa[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ju']
    for i in [5,6,11,12]:
        b8v_Sa[nxt(start,i)-1] = b8v_Sa[nxt(start,i)-1] + 1
    start = p21.GRashiN['Ve']
    for i in [6,11,12]:
        b8v_Sa[nxt(start,i)-1] = b8v_Sa[nxt(start,i)-1] + 1
    start = p21.GRashiN['Sa']
    for i in [3,5,6,11]:
        b8v_Sa[nxt(start,i)-1] = b8v_Sa[nxt(start,i)-1] + 1
    start = p21.GRashiN['La']
    for i in [1,3,4,6,10,11]:
        b8v_Sa[nxt(start,i)-1] = b8v_Sa[nxt(start,i)-1] + 1
        
    #print('b8v_Sa',b8v_Sa)
    # 
    # Sarva Ashatak Varga Points
    #
    #SarvaAshtakVarga([b8v_Su,b8v_Mo,b8v_Ma,b8v_Me,b8v_Ju,b8v_Ve,b8v_Sa])
    return([b8v_Su,b8v_Mo,b8v_Ma,b8v_Me,b8v_Ju,b8v_Ve,b8v_Sa])
    


def SarvaAshtakVarga():
# 
# Sarva Ashatak Varga Points
# Adding up the Varga points for all Grahas in  a Rashi to get the Rashi Sum
#
    s8v = GenAshtakVargaData_v1()
    print('SarvaAshtakVarga | Rashi', p21.GRashiN)
    #print('GRashiN : ', p21.GRashiN)
    rashiSum = [0,0,0,0,0,0,0,0,0,0,0,0]
    #for i in range(7):
    #    print(p21.Graha[i],s8v[i])
    for i in range(12):
        rashiSum[i] = 0
        for j in range(7):
            rashiSum[i] = rashiSum[i]+s8v[j][i]
    
    chksum = 0
    for i in range(12):
        chksum = chksum + rashiSum[i]
    print(' +',rashiSum, ' = ',chksum)
    #print('chksum',chksum)
    #
    # Slide from Rashi to Bhav
    #
    print('SarvaAshtakVarga | Bhav', p21.BhavN)
    #print('BhavN : ',p21.BhavN)
    #s8vB = [[] for x in range(12)]
    s8vB = [[] for x in range(7)]
    #print(p21.BhavA)
    for g in range(7):
        temp = [0,0,0,0,0,0,0,0,0,0,0,0]
        for b in range(12):
            #print(g,b,temp)
            
            b1 = b+1;
            if b1 > 12:
                b1 = b1 - 12
            #print(g,b,b1,s8v[g],p21.BhavN[b1])
            temp[b] = s8v[g][int(p21.BhavN[b1])-1]
            #print(g,b,b1,temp)
        s8vB[g] = temp
    # --------------------------
    bhavSum = [0,0,0,0,0,0,0,0,0,0,0,0]
    #for i in range(7):
    #    print(p21.Graha[i],s8vB[i])
    for i in range(12):
        bhavSum[i] = 0
        for j in range(7):
            bhavSum[i] = bhavSum[i]+s8vB[j][i]
    
    bchksum = 0
    for i in range(12):
        bchksum = bchksum + bhavSum[i]
    print(' +',bhavSum, ' = ',bchksum)
    #print('chksum',chksum)
    Bandhu = bhavSum[0]+ bhavSum[4] + bhavSum[8]
    Sevak = bhavSum[1]+ bhavSum[5] + bhavSum[9]
    Poshak = bhavSum[2] + bhavSum[6] + bhavSum[10]
    Ghatak = bhavSum[3] + bhavSum[7] + bhavSum[11]
    print('Bandhu: ',Bandhu,'Sevak: ',Sevak,'Poshak: ',Poshak,'Ghatak: ',Ghatak)
    return(s8v,rashiSum,s8vB,bhavSum,[Bandhu,Sevak,Poshak,Ghatak,bchksum])

# ----------------------------------------------------------------------------------
# For Transits 
# ----------------------------------------------------------------------------------
def getTransitData(cDT):
    DoB_Day = int(cDT.strftime("%-d"))
    DoB_Mon = int(cDT.strftime("%-m"))
    DoB_Year = int(cDT.strftime("%Y"))
    #print(DoB_Time)
    DoB_Time = '12:01'
    PoB_Lat = 25.43
    PoB_Lon = 81.85
    Name = p21.gName
    Gender = 'x'
    tag1 = 'nil'
    tag3 = 'nil'
    tag5 = 'nil'
    p21.pName = p21.gName
    p21.ChartType = 'Rashi'
    TZ_OffHours = 5.5

    sData = [DoB_Day,DoB_Mon,DoB_Year,DoB_Time,TZ_OffHours,PoB_Lat,PoB_Lon,Name, Gender, tag1, tag3,tag5]
    sLabels = ['DoB_Day','DoB_Mon','DoB_Year','DoB_Time','TZ_OffHours','PoB_Lat','PoB_Lon','Name','Gender','tag1','tag3','tag5']
    return(pd.Series(sData, index = sLabels))
# ----------------------------------------------------------------------------------
def setTransitData(c):
    p21swe.C02_parsePersonData(c)
    p21swe.C03_convertDates()
    p21swe.C04_calculateGrahaPositions()
    p21swe.C05_buildGLonGRet()
    #p21.GLonRet['GLon']['La'] = RashiLon
    p21.GLonRet['GLon']['La'] = p21.SubMoonLong
    #p21utils.R11_LocateGrahaInRashi()
    R11_LocateGrahaInRashi()
    #print(p21.GRashiA)
