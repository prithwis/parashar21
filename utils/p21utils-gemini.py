# Copyright (c) 2022, Prithwis Mukerjee
# All rights reserved.
# Licensed under the GNU GPL v3.0 -style license.
# Refactored for Parashar21 Engine Pipeline

import math
import numbers
import json
from datetime import datetime, timedelta
import pandas as pd
import pytz

import p21
import p21swe

# --------------------------------------------------
# Utility Functions
# --------------------------------------------------

def appendDict(d1, d2):
    """Appends elements of d2 into d1 in-place."""
    for k, v in d2.items():
        d1[k] = v

d2l = lambda dic: [(k, v) for (k, v) in dic.items()]
l2d = lambda lis: dict(lis)

def RashiGapA(R2, R1):
    """Calculates forward step distance from R1 to R2 in a 12-house system (0 to 11)."""
    if R2 >= R1:
        return R2 - R1
    else:
        return R2 - R1 + 12

def addToD(x, D, y):
    """Safely adds an element to a set inside a dictionary."""
    if x not in D:
        D[x] = set()
    D[x].add(y)

def csidtil(D):
    """Converts set values in a dictionary to lists for JSON serialization."""
    return {str(k): list(v) for k, v in D.items()}

# --------------------------------------------------
# House & Lordship Determination
# --------------------------------------------------

def C10_DetermineBhavs():
    """Determines and stores the Bhava numbers and Rashi names."""
    p21.BhavN = [p21.BoL]
    for ix in range(1, 13):
        if ix == 1:
            p21.BhavN.append(p21.GRashiN['La'])
        else:
            N = p21.BhavN[ix - 1] + 1
            if N > 12:
                N -= 12
            p21.BhavN.append(N)
            
    p21.BhavA = list(map(lambda x: p21.RashiN2A(x) if isinstance(x, numbers.Integral) else p21.BoL, p21.BhavN))
    
    p21.BhavNBhavA = {
        'BhavN': p21.BhavN,
        'BhavA': p21.BhavA
    }

def C11_DetermineLord():
    """Determines house lords and their Rashi positions."""
    p21.Lord = list(map(lambda x: p21.LordOf[p21.RashiN2A(x)] if isinstance(x, numbers.Integral) else p21.BoL, p21.BhavN))
    p21.LordRashiN = list(map(lambda x: p21.GRashiN[x] if x != p21.BoL else p21.BoL, p21.Lord))
    p21.LordRashiA = list(map(lambda x: p21.GRashiA[x] if x != p21.BoL else p21.BoL, p21.Lord))

    p21.GrahaLordBhav = {}
    for G in ('Su', 'Mo', 'Ma', 'Me', 'Ju', 'Ve', 'Sa'):
        L = [i for i, n in enumerate(p21.Lord) if n == G]
        p21.GrahaLordBhav[G] = L
        
    p21.LordInfo = {
        'Lord': p21.Lord,
        'LordRashiN': p21.LordRashiN,
        'LordRashiA': p21.LordRashiA,
        'GrahaLordBhav': p21.GrahaLordBhav
    }

def C12_BhavOfGraha_Lord():
    """Locates planets and house lords within the 12 Bhavas."""
    p21.GrahaBhava = {"La": 1}
    for G in ('Su', 'Mo', 'Ma', 'Me', 'Ju', 'Ve', 'Sa', 'Ra', 'Ke'):
        p21.GrahaBhava[G] = p21.BhavN.index(p21.GRashiN[G])

    p21.LordBhav = [p21.BoL]
    for L in range(1, 13):
        p21.LordBhav.append(p21.BhavN.index(p21.GRashiN[p21.Lord[L]]))

    p21.BhavOfGraha_LordInfo = {
        'GRashiN': p21.GRashiN,
        'GrahaBhava': p21.GrahaBhava,
        'LordBhav': p21.LordBhav
    }

# --------------------------------------------------
# Planetary Status Evaluation (Exaltation / Debilitation)
# --------------------------------------------------

def C21A_checkGexa(x, level='low'):
    if level == 'low':
        return x, (p21.GRashiN[x] == p21.exaR[x])
    if level == 'high':
        lon = p21.GLon[x]
        return x, (p21.exaL[x] < lon <= p21.exaU[x])

def C21B_checkLexa(x):
    return False if x == p21.BoL else p21.exaltG[x]

def C21C_checkGdeb(x, level='low'):
    if level == 'low':
        return x, (p21.GRashiN[x] == p21.debR[x])
    if level == 'high':
        lon = p21.GLon[x]
        return x, (p21.debL[x] < lon <= p21.debU[x])

def C21D_checkLdeb(x):
    return False if x == p21.BoL else p21.debilG[x]

def C21E_checkm3G(x):
    return x, (p21.GRashiN[x] == p21.mool3R[x])

def C21F_checkOwnHG(x):
    return x, (x == p21.LordOf[p21.GRashiA[x]])

def C21G_checkfen(x, Z):
    return x, (p21.LordOf[p21.GRashiA[x]] in Z[x])

def C21_DeterminePositions():
    """Evaluates planetary dignity states across Rashis."""
    p21.exaltG = l2d(list(map(C21A_checkGexa, p21.Graha)))
    p21.exaltL = list(map(C21B_checkLexa, p21.Lord))
    
    p21.debilG = l2d(list(map(C21C_checkGdeb, p21.Graha)))
    p21.debilL = list(map(C21D_checkLdeb, p21.Lord))
    
    p21.mool3G = l2d(list(map(C21E_checkm3G, p21.Graha)))
    p21.mool3L = [False] * 13
    for ix in range(1, 13):
        p21.mool3L[ix] = p21.mool3G.get(p21.Lord[ix], False)

    p21.ownHouseG = l2d(list(map(C21F_checkOwnHG, p21.Graha)))
    p21.ownHouseL = [False] * 13
    for ix in range(1, 13):
        p21.ownHouseL[ix] = p21.ownHouseG.get(p21.Lord[ix], False)

    p21.inFriendG = l2d(list(map(lambda x: C21G_checkfen(x, p21.friends), p21.Graha)))
    p21.inEnemyG = l2d(list(map(lambda x: C21G_checkfen(x, p21.enemies), p21.Graha)))
    p21.inNeutralG = l2d(list(map(lambda x: C21G_checkfen(x, p21.neutrals), p21.Graha)))

    p21.inFriendL = [False] * 13
    p21.inEnemyL = [False] * 13
    p21.inNeutralL = [False] * 13

    for ix in range(1, 13):
        lord = p21.Lord[ix]
        if lord != p21.BoL:
            p21.inFriendL[ix] = p21.inFriendG.get(lord, False)
            p21.inEnemyL[ix] = p21.inEnemyG.get(lord, False)
            p21.inNeutralL[ix] = p21.inNeutralG.get(lord, False)

    p21.Positions = {
        'exaltG': p21.exaltG,
        'debilG': p21.debilG,
        'ownHouseG': p21.ownHouseG,
        'inFriendG': p21.inFriendG,
        'inEnemyG': p21.inEnemyG,
        'exaltL': p21.exaltL,
        'debilL': p21.debilL,
        'ownHouseL': p21.ownHouseL,
        'inFriendL': p21.inFriendL,
        'inEnemyL': p21.inEnemyL
    }

def Long2Rashi(x):
    """Converts absolute longitude to Rashi index based on ChartType."""
    if p21.ChartType == 'Rashi':
        return x[0], math.floor(x[1] / 30) + 1
    elif p21.ChartType == 'Navamsa':
        N1 = math.floor(x[1] / 3.3333333333333335) + 1
        N2 = N1 % 12
        return x[0], (12 if N2 == 0 else N2)

def R11_LocateGrahaInRashi():
    """Maps longitudes to Rashi indices and names."""
    p21.GRashiN = l2d(list(map(Long2Rashi, d2l(p21.GLon))))
    p21.GRashiA = {k: p21.RashiN2A(v) for k, v in p21.GRashiN.items()}

# --------------------------------------------------
# Aspect Engine (Full Parashari Rules Matrix)
# --------------------------------------------------

def C31_DetermineAspects():
    """
    Calculates bi-directional planetary and house aspects.
    Special Aspects:
    - Mars: 4th (gap 3) & 8th (gap 7)
    - Jupiter: 5th (gap 4) & 9th (gap 8)
    - Saturn: 3rd (gap 2) & 10th (gap 9)
    - All Planets: 7th (gap 6)
    """
    p21.GAspects = dict()
    p21.GAspectedBy = dict()
    p21.BAspectedBy = dict()
    p21.BAspectedByBL = dict()

    # 1. Graha-to-Graha Aspects
    for O1 in p21.Gx:
        for O2 in p21.Gx:
            if O1 == O2:
                continue
            
            gap = RashiGapA(p21.GRashiN[O2], p21.GRashiN[O1])
            
            # Universal 7th Aspect
            if gap == 6 and not (O1 in ['Ra', 'Ke'] and O2 in ['Ra', 'Ke']):
                addToD(O1, p21.GAspects, O2)
                addToD(O2, p21.GAspectedBy, O1)

            # Special Planetary Aspects
            if O1 == 'Ma' and gap in (3, 7): # 4th and 8th aspects
                addToD(O1, p21.GAspects, O2)
                addToD(O2, p21.GAspectedBy, O1)
                
            if O1 == 'Ju' and gap in (4, 8): # 5th and 9th aspects
                addToD(O1, p21.GAspects, O2)
                addToD(O2, p21.GAspectedBy, O1)
                
            if O1 == 'Sa' and gap in (2, 9): # 3rd and 10th aspects
                addToD(O1, p21.GAspects, O2)
                addToD(O2, p21.GAspectedBy, O1)

    # 2. Graha-to-Bhava Aspects
    for O1 in p21.Gx:
        for BN in range(1, 13):
            gap = RashiGapA(p21.BhavN[BN], p21.GRashiN[O1])
            
            if gap == 6: # 7th house aspect
                addToD(str(BN), p21.BAspectedBy, O1)
            if O1 == 'Ma' and gap in (3, 7): # Mars 4th, 8th
                addToD(str(BN), p21.BAspectedBy, O1)
            if O1 == 'Ju' and gap in (4, 8): # Jupiter 5th, 9th
                addToD(str(BN), p21.BAspectedBy, O1)
            if O1 == 'Sa' and gap in (2, 9): # Saturn 3rd, 10th
                addToD(str(BN), p21.BAspectedBy, O1)

    # 3. Bhava-to-Bhava Lord Aspects
    for BN1 in range(1, 13):
        for BN2 in range(1, 13):
            if str(BN1) in p21.BAspectedBy:
                if p21.Lord[BN2] in p21.BAspectedBy[str(BN1)]:
                    addToD(str(BN1), p21.BAspectedByBL, str(BN2))

    p21.GAspects2 = csidtil(p21.GAspects)
    p21.GAspectedBy2 = csidtil(p21.GAspectedBy)
    p21.BAspectedBy2 = csidtil(p21.BAspectedBy)
    p21.BAspectedByBL2 = csidtil(p21.BAspectedByBL)

    p21.Aspects = {
        'GAspects2': p21.GAspects2,
        'GAspectedBy2': p21.GAspectedBy2,
        'BAspectedBy2': p21.BAspectedBy2,
        'BAspectedByBL2': p21.BAspectedByBL2
    }

def C41_DetermineConjuncts():
    """Identifies conjunctions between planets and house lords."""
    p21.GConjunctsG = dict()
    p21.BLConjunctsG = dict()
    p21.BLConjunctsBL = dict()

    # Graha - Graha Conjunctions
    for O1 in p21.Gx[1:]: # Ignore 'La'
        for O2 in p21.Gx[1:]:
            if O1 != O2 and p21.GRashiN[O2] == p21.GRashiN[O1]:
                addToD(O1, p21.GConjunctsG, O2)

    # House Lord - Graha Conjunctions
    for BN in range(1, 13):
        for O1 in p21.Gx[1:]:
            if p21.Lord[BN] != O1 and p21.GRashiN[p21.Lord[BN]] == p21.GRashiN[O1]:
                addToD(str(BN), p21.BLConjunctsG, O1)

    # House Lord - House Lord Conjunctions
    for BN1 in range(1, 13):
        for BN2 in range(1, 13):
            if p21.LordBhav[BN2] == p21.LordBhav[BN1] and (BN2 not in p21.GrahaLordBhav[p21.Lord[BN1]]):
                addToD(str(BN1), p21.BLConjunctsBL, str(BN2))

    p21.GConjunctsG2 = csidtil(p21.GConjunctsG)
    p21.BLConjunctsG2 = csidtil(p21.BLConjunctsG)
    p21.BLConjunctsBL2 = csidtil(p21.BLConjunctsBL)

    p21.Conjuncts = {
        'GConjunctsG2': p21.GConjunctsG2,
        'BLConjunctsG2': p21.BLConjunctsG2,
        'BLConjunctsBL2': p21.BLConjunctsBL2
    }

# --------------------------------------------------
# Functional Benefic/Malefic Evaluation
# --------------------------------------------------

def C51_DetermineBenMal():
    """Assigns functional benefics/malefics according to Lagna rules."""
    L = p21.RashiN2A(p21.GRashiN['La'])
    
    ben_mal_map = {
        'Mesh': (
            {'Su': True, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False},
            {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        ),
        'Vrish': (
            {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': True},
            {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        ),
        'Mithun': (
            {'Su': False, 'Mo': False, 'Ma': False, 'Me': False, 'Ju': False, 'Ve': True, 'Sa': True},
            {'Su': True, 'Mo': False, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        ),
        'Karkat': (
            {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': False, 'Ve': False, 'Sa': False},
            {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': True, 'Ve': False, 'Sa': True, 'Ra': False, 'Ke': False}
        ),
        'Simha': (
            {'Su': True, 'Mo': False, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False},
            {'Su': False, 'Mo': True, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': False, 'Ra': True, 'Ke': True}
        ),
        'Kanya': (
            {'Su': False, 'Mo': False, 'Ma': False, 'Me': False, 'Ju': False, 'Ve': True, 'Sa': False},
            {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        ),
        'Tula': (
            {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': True},
            {'Su': True, 'Mo': False, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        ),
        'Vrishchik': (
            {'Su': True, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False},
            {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': False, 'Ra': True, 'Ke': True}
        ),
        'Dhanu': (
            {'Su': True, 'Mo': False, 'Ma': True, 'Me': False, 'Ju': False, 'Ve': False, 'Sa': False},
            {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': False, 'Ra': True, 'Ke': True}
        ),
        'Makar': (
            {'Su': False, 'Mo': False, 'Ma': False, 'Me': True, 'Ju': False, 'Ve': True, 'Sa': True},
            {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': False, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        ),
        'Kumbh': (
            {'Su': False, 'Mo': False, 'Ma': False, 'Me': False, 'Ju': False, 'Ve': True, 'Sa': True},
            {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False, 'Ra': True, 'Ke': True}
        ),
        'Meen': (
            {'Su': False, 'Mo': True, 'Ma': True, 'Me': False, 'Ju': True, 'Ve': False, 'Sa': False},
            {'Su': True, 'Mo': False, 'Ma': False, 'Me': False, 'Ju': False, 'Ve': True, 'Sa': False, 'Ra': True, 'Ke': True}
        )
    }

    if L in ben_mal_map:
        p21.beneficG, p21.maleficG = ben_mal_map[L]
    else:
        print("Invalid Lagna:", L)

    p21.BenMalG = {
        'beneficG': p21.beneficG,
        'maleficG': p21.maleficG
    }

# --------------------------------------------------
# Vimsottari Dasha Engine
# --------------------------------------------------

def NextDasha(cd):
    cdIndex = p21.DashaSeq.index(cd)
    return p21.DashaSeq[(cdIndex + 1) % 9]

def GetDasha():
    """Generates complete Vimsottari Dasha and Antardasha dates."""
    BirthNks = int(p21.SubMoonLong / p21.NksGap)
    BirthDasha = p21.DashaStart[BirthNks]
    BirthDashaIndex = p21.DashaSeq.index(BirthDasha)

    DashaConsumedDeg = p21.SubMoonLong - (BirthNks * p21.NksGap)
    DashaConsumedDuration = (DashaConsumedDeg / p21.NksGap) * p21.DashaDurationD[BirthDashaIndex]

    StartOfBirthDasha = p21.DoB - timedelta(days=DashaConsumedDuration)

    L1Dasha = BirthDasha
    StartOfL1Dasha = StartOfBirthDasha
    p21.VimDasha = {}

    for _ in range(9):
        L1DashaDuration = p21.DashaDurationD[p21.DashaSeq.index(L1Dasha)]
        EndOfL1Dasha = StartOfL1Dasha + timedelta(days=L1DashaDuration)
        
        DashaDict = {
            'Start': StartOfL1Dasha.strftime("%d %b %Y"),
            'End': EndOfL1Dasha.strftime("%d %b %Y"),
            'Duration': L1DashaDuration
        }

        L2Dasha = L1Dasha
        StartOfL2Dasha = StartOfL1Dasha

        for _ in range(9):
            L2DashaDuration = L1DashaDuration * p21.DashaDuraFract[p21.DashaSeq.index(L2Dasha)]
            EndOfL2Dasha = StartOfL2Dasha + timedelta(days=L2DashaDuration)
            
            DashaDict[L2Dasha] = {
                'Start': StartOfL2Dasha.strftime("%d %b %Y"),
                'End': EndOfL2Dasha.strftime("%d %b %Y"),
                'Duration': L2DashaDuration
            }
            
            L2Dasha = NextDasha(L2Dasha)
            StartOfL2Dasha = EndOfL2Dasha

        p21.VimDasha[L1Dasha] = DashaDict
        L1Dasha = NextDasha(L1Dasha)
        StartOfL1Dasha = EndOfL1Dasha

# --------------------------------------------------
# Ashtakavarga Engine
# --------------------------------------------------

def GenAshtakVargaData():
    """Calculates Bhinna Ashtakavarga points and total Sarvashtakavarga (SAV)."""
    def nxt(s, p):
        d = s + p - 1
        return d - 12 if d > 12 else d

    # Initialize bindu vectors for 7 planets
    b8v = {g: [0] * 12 for g in ('Su', 'Mo', 'Ma', 'Me', 'Ju', 'Ve', 'Sa')}

    # 1. Sun (Su)
    rules_Su = {
        'Su': [1, 2, 4, 7, 8, 9, 10, 11], 'Mo': [3, 6, 10, 11], 'Ma': [1, 2, 4, 7, 8, 9, 10, 11],
        'Me': [3, 5, 6, 9, 10, 11, 12], 'Ju': [5, 6, 9, 11], 'Ve': [6, 7, 12],
        'Sa': [1, 2, 4, 7, 8, 9, 10, 11], 'La': [3, 4, 6, 10, 11, 12]
    }
    for ref, pos in rules_Su.items():
        for i in pos:
            b8v['Su'][nxt(p21.GRashiN[ref], i) - 1] += 1

    # 2. Moon (Mo)
    rules_Mo = {
        'Su': [3, 6, 7, 8, 10, 11], 'Mo': [1, 3, 6, 7, 9, 10, 11], 'Ma': [2, 3, 5, 6, 10, 11],
        'Me': [1, 3, 4, 5, 7, 8, 10, 11], 'Ju': [1, 2, 4, 7, 8, 10, 11], 'Ve': [3, 4, 5, 7, 9, 10, 11],
        'Sa': [3, 5, 6, 11], 'La': [3, 6, 10, 11]
    }
    for ref, pos in rules_Mo.items():
        for i in pos:
            b8v['Mo'][nxt(p21.GRashiN[ref], i) - 1] += 1

    # 3. Mars (Ma)
    rules_Ma = {
        'Su': [3, 5, 6, 10, 11], 'Mo': [3, 6, 11], 'Ma': [1, 2, 4, 7, 8, 10, 11],
        'Me': [3, 5, 6, 11], 'Ju': [6, 10, 11, 12], 'Ve': [6, 8, 11, 12],
        'Sa': [1, 4, 7, 8, 9, 10, 11], 'La': [1, 3, 6, 10, 11]
    }
    for ref, pos in rules_Ma.items():
        for i in pos:
            b8v['Ma'][nxt(p21.GRashiN[ref], i) - 1] += 1

    # 4. Mercury (Me)
    rules_Me = {
        'Su': [5, 6, 9, 11, 12], 'Mo': [2, 4, 6, 8, 10, 11], 'Ma': [1, 2, 4, 7, 8, 9, 10, 11],
        'Me': [1, 3, 5, 6, 9, 10, 11, 12], 'Ju': [6, 8, 11, 12], 'Ve': [1, 2, 3, 4, 5, 8, 9, 11],
        'Sa': [1, 2, 4, 7, 8, 9, 10, 11], 'La': [1, 2, 4, 6, 8, 10, 11]
    }
    for ref, pos in rules_Me.items():
        for i in pos:
            b8v['Me'][nxt(p21.GRashiN[ref], i) - 1] += 1

    # 5. Jupiter (Ju)
    rules_Ju = {
        'Su': [1, 2, 3, 4, 7, 8, 9, 10, 11], 'Mo': [2, 5, 7, 9, 11], 'Ma': [1, 2, 4, 7, 8, 10, 11],
        'Me': [1, 2, 4, 5, 6, 9, 10, 11], 'Ju': [1, 2, 3, 4, 7, 8, 10, 11], 'Ve': [2, 5, 6, 9, 10, 11],
        'Sa': [3, 5, 6, 12], 'La': [1, 2, 4, 5, 6, 7, 9, 10, 11]
    }
    for ref, pos in rules_Ju.items():
        for i in pos:
            b8v['Ju'][nxt(p21.GRashiN[ref], i) - 1] += 1

    # 6. Venus (Ve)
    rules_Ve = {
        'Su': [8, 11, 12], 'Mo': [1, 2, 3, 4, 5, 8, 9, 11, 12], 'Ma': [3, 5, 6, 9, 11, 12],
        'Me': [3, 5, 6, 9, 11], 'Ju': [5, 8, 9, 10, 11], 'Ve': [1, 2, 3, 4, 5, 8, 9, 10, 11],
        'Sa': [3, 4, 5, 8, 9, 10, 11], 'La': [1, 2, 3, 4, 5, 8, 9, 11]
    }
    for ref, pos in rules_Ve.items():
        for i in pos:
            b8v['Ve'][nxt(p21.GRashiN[ref], i) - 1] += 1

    # 7. Saturn (Sa)
    rules_Sa = {
        'Su': [1, 2, 4, 7, 8, 10, 11], 'Mo': [3, 6, 11], 'Ma': [3, 5, 6, 10, 11, 12],
        'Me': [6, 8, 9, 10, 11, 12], 'Ju': [5, 6, 11, 12], 'Ve': [6, 11, 12],
        'Sa': [3, 5, 6, 11], 'La': [1, 3, 4, 6, 10, 11]
    }
    for ref, pos in rules_Sa.items():
        for i in pos:
            b8v['Sa'][nxt(p21.GRashiN[ref], i) - 1] += 1

    # Calculate Sarvashtakavarga (SAV) - Sum across all 7 planets per Rashi
    sav = [sum(b8v[g][r] for g in b8v) for r in range(12)]

    p21.Ashtakvarga = {
        'BAV': b8v,
        'SAV': sav,
        'Checksum': sum(sav) # Validated against 337 baseline
    }