# 𝓟𝓪𝓻𝓪𝓼𝓱𝓪𝓻21
# 𝓟𝓻𝓲𝓽𝓱𝔀𝓲𝓼 𝓜𝓾𝓴𝓮𝓻𝓳𝓮𝓮
# --------------------------------------------------
# Global Variables
import p21
# --------------------------------------------------

import pandas as pd
import dateutil

import math
import numbers
import string    
import random # define the random module  
#import string_utils

from datetime import datetime
from datetime import timedelta

import swisseph as swe


# --------------------------------------------------
#Configure Swiss Ephemeris

def C01_configSWE():
    
    swe.version
    #Constants and Flags necessary for this application are set here
    #
    swe.set_ephe_path('/content/ephe') # set path to ephemeris files
    # Calendar : Julian or Gregorian
    SE_GREG_CAL = 1
    p21.gregflag = SE_GREG_CAL
    #
    # Ayanamsha type : Lahiri = 1
    swe.set_sid_mode(1)  # Lahiri Aynamsha
    #
    # whether speed will be calculated along with position of planet
    SEFLG_SPEED = int(256)
    p21.iflag = SEFLG_SPEED
    #hsys = P, Placidus
    #ascii P = 080
    p21.hsysP =  bytes('P', 'utf-8')
    
# --------------------------------------------------
#
def C02_parsePersonData(P):
    #global chart
    global LBDY, LBDM,LBDD,LBTh,LBTm,LBTs,tZone,natalLAT,natalLON
    
    LBDY = P['DoB_Year']     # Year of Birth, Local Time
    LBDM = P['DoB_Mon']      # Month of Birth, Local Time
    LBDD = P['DoB_Day']      # Day of Birth, Local Time

    LBTh = int(P['DoB_Time'].split(":")[0])                           # Hour of Birth, Local Time, 24 Hour Clock
    LBTm = int(P['DoB_Time'].split(":")[1])                          # Minute of Birth, Local Time
    LBTs = 0                           # Second of Birth, Local Time

    tZone = P['TZ_OffHours']                         # Time Zone Offset. East of Greenwich is +ve
    #print('ppd', LBDY, LBDM,LBDD,LBTh,LBTm,LBTs,tZone)
    #print(P['Gender'])
    natalLAT = P['PoB_Lat']
    natalLON = P['PoB_Lon']
    ck = P['Gender']+str(P['DoB_Year'])+str(P['DoB_Mon'])+str(P['DoB_Day'])+P['DoB_Time']+str(P['TZ_OffHours'])+str(P['PoB_Lat'])+str(P['PoB_Lon'])
    cID = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 12)))   # string of len 12 consisting of random uppercase and digits
    p21.chart = {
        "pid":{
            "tags" : [P['Voc1_Cat'],P['Voc2_Cat'],P['Voc3_Cat']],
            "ck" : ck,
            "chartType" : p21.ChartType,
            #"name": string_utils.shuffle(P['Name'][0:8])
            "name": P['Name'][0:10],
            "cID" : cID
        }
    }
    
# --------------------------------------------------

def C03_convertDates():
    global natalUT, ayanamsha
    # Date & Time of Birth
    #Time Zone Conversion
    UTCdt = swe.utc_time_zone(LBDY,LBDM,LBDD,LBTh,LBTm,LBTs,tZone)
    #print(UTCdt)
    # Date & Time of Birth
    # Convert UTC date to Julian Date
    JD = swe.utc_to_jd(UTCdt[0],UTCdt[1],UTCdt[2],UTCdt[3],UTCdt[4],0,p21.gregflag) # Second Value = 0
    #print (JD[0], JD[1])
    # JD[0] is Ephemeris Time
    # JD[1] is Universal Time 
    natalUT = JD[1]
    #print(natalUT, 'Julian Date of DTofB in Universal Time')
    #Ayanamsha
    ayanamsha = swe.get_ayanamsa(natalUT)
    #print('Lahiri Ayanamsha :', ayanamsha)
    
# --------------------------------------------------
#
def C04_calculateGrahaPositions():
    global bLon,bRet,P
    #Position of Planets
    #
    # body 0 = Sun, 1 = Moon, 2 = Merc, 3 = Ven, 4 = Mars, 5 = Jup, 6 = Sat, 11 = True Node (Rahu)
    bLon = []
    bRet = []
    for body in [0,1,2,3,4,5,6,11]:
        pData = swe.calc_ut(natalUT,body,p21.iflag)
        bLon.append(pData[0][0])
        if pData[0][3] >= 0:
            bRet.append(False)
        else :
            bRet.append(True)
    #for ix in range(len(bLon)) : print(ix, bLon[ix], bRet[ix])
    #-------------------------------------------------------------------
    #House Position and Ascendants
    P = swe.houses(natalUT,natalLAT,natalLON,p21.hsysP)
    
    #P = swe.houses_ex(natalUT,natalLAT,natalLON,hsysP)
    #for ix in range(len(P[0])) : print(ix, P[0][ix])
    #print('--')
    #for ix in range(len(P[1])) : print(ix, P[1][ix])

# --------------------------------------------------

# --------------------------------------------------
# Subtracts angles (eg Ayanamsha) from Longitudes 
# Required for conversion from Tropical (Western) to Sidereal (Indian) zodiac
#
def p21Sub (x,y):
    retVal = round(x - y,3)
    if retVal < 0:
        return retVal + 360
    else:
        return retVal
# --------------------------------------------------

def C05_buildGLonGRet():
    #global GLon, GRet
    p21.GLon = {
    'La':p21Sub(P[1][0],ayanamsha),
    'Su':p21Sub(bLon[0],ayanamsha),
    'Mo':p21Sub(bLon[1],ayanamsha),
    'Ma':p21Sub(bLon[4],ayanamsha),
    'Me':p21Sub(bLon[2],ayanamsha),
    'Ju':p21Sub(bLon[5],ayanamsha),
    'Ve':p21Sub(bLon[3],ayanamsha),
    'Sa':p21Sub(bLon[6],ayanamsha),
    'Ra':p21Sub(bLon[7],ayanamsha),
    'Ke':p21Sub(p21Sub(bLon[7],ayanamsha),180)
    }
    
    p21.GRet = {
    'La':False,
    'Su':False,
    'Mo':False,
    'Ma':bRet[4],
    'Me':bRet[2],
    'Ju':bRet[5],
    'Ve':bRet[3],
    'Sa':bRet[6],
    'Ra':False,
    'Ke':False
    }
    p21.GLonRet = {
        'GLon': p21.GLon,
        'GRet': p21.GRet
    }

print('p21swe imported')