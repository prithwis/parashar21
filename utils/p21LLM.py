#Copyright (c) 2022, Prithwis Mukerjee
#All rights reserved.
#
#This source code is licensed under the GNU GPL v3.0 -style license found in the
#LICENSE file in the root directory of this source tree. 
# --------------------------------------------------
# Global Variables
import p21

def R601_GenerateLLMInput03(filename="LLMInput_Natal.txt"):

    import os

    # -------------------------------------------------------
    # Determine analysis type and output filename
    # -------------------------------------------------------

    analysisMode = "Natal"

    if os.path.exists(filename):
        filename = "LLMInput_Gochar.txt"
        analysisMode = "Gochar"

    # -------------------------------------------------------
    lines = []

    def add(text=""):
        lines.append(text)

    # -------------------------------------------------------
    # Name mappings
    # -------------------------------------------------------

    grahaName = {
        "La": "Lagna",
        "Su": "Sun",
        "Mo": "Moon",
        "Ma": "Mars",
        "Me": "Mercury",
        "Ju": "Jupiter",
        "Ve": "Venus",
        "Sa": "Saturn",
        "Ra": "Rahu",
        "Ke": "Ketu"
    }

    rashiName = {
        1: "Aries",
        2: "Taurus",
        3: "Gemini",
        4: "Cancer",
        5: "Leo",
        6: "Virgo",
        7: "Libra",
        8: "Scorpio",
        9: "Sagittarius",
        10: "Capricorn",
        11: "Aquarius",
        12: "Pisces"
    }

    def GName(g):
        return grahaName.get(g, g)

    def GList(lst):
        return [GName(x) for x in lst]

    def RName(r):
        return rashiName.get(int(r), r)


    gender = "Unknown"
    if hasattr(p21, "ck") and len(p21.ck) > 0:
        gender = genderName.get(p21.ck[0].upper(), p21.ck[0])

    # -------------------------------------------------------
    # Header
    # -------------------------------------------------------

    add("HOROSCOPE DATA FOR JYOTISHA REASONING")
    add("=====================================")
    add("")
    add("Analysis : " + analysisMode)
    add("Chart Type : " + str(p21.AnalysisType))
    add("Gender : " + gender)


    if hasattr(p21, "pTags"):
        add("Tags : " + str(p21.pTags))

    add("")


    # -------------------------------------------------------
    # House Lordship
    # -------------------------------------------------------

    add("HOUSE LORDSHIP")
    add("--------------")

    for house in range(1, len(p21.Lord)):
        add(f"House {house} lord is {GName(p21.Lord[house])}")

    add("")


    # -------------------------------------------------------
    # Planetary Information
    # -------------------------------------------------------

    add("PLANETARY INFORMATION")
    add("---------------------")

    grahaOrder = [
        "La", "Su", "Mo", "Ma", "Me",
        "Ju", "Ve", "Sa", "Ra", "Ke"
    ]

    for graha in grahaOrder:

        if graha not in p21.GrahaBhava:
            continue

        add("")
        add(GName(graha) + ":")

        add(f"- Occupies Bhava {p21.GrahaBhava[graha]}")

        if graha in p21.GRashiN:
            add(f"- Located in Rashi {RName(p21.GRashiN[graha])}")

        if graha in p21.GrahaLordBhav:
            add(f"- Lord of Bhavas {p21.GrahaLordBhav[graha]}")

        if p21.exaltG.get(graha, False):
            add("- Exalted")

        if p21.debilG.get(graha, False):
            add("- Debilitated")

        if p21.ownHouseG.get(graha, False):
            add("- In own house")

        if p21.inFriendG.get(graha, False):
            add("- In friendly house")

        if p21.inEnemyG.get(graha, False):
            add("- In enemy house")

        if p21.beneficG.get(graha, False):
            add("- Functional benefic")

        if p21.maleficG.get(graha, False):
            add("- Functional malefic")

        if p21.GRet.get(graha, False):
            add("- Retrograde")

        # Future addition:
        # Nakshatra
        # Pada

        if graha in p21.GLon:
            add(f"- Absolute celestial longitude {p21.GLon[graha]} degrees")

    add("")


    # -------------------------------------------------------
    # Planetary Aspects
    # -------------------------------------------------------

    add("PLANETARY ASPECTS")
    add("-----------------")

    for graha, targets in p21.GAspects2.items():
        add(f"{GName(graha)} aspects {GList(targets)}")

    add("")


    # -------------------------------------------------------
    # Planets Aspected By
    # -------------------------------------------------------

    add("PLANETS ASPECTED BY")
    add("--------------------")

    for graha, sources in p21.GAspectedBy2.items():
        add(f"{GName(graha)} is aspected by {GList(sources)}")

    add("")


    # -------------------------------------------------------
    # Planetary Conjunctions
    # -------------------------------------------------------

    add("PLANETARY CONJUNCTIONS")
    add("-----------------------")

    for graha, targets in p21.GConjunctsG2.items():
        add(f"{GName(graha)} conjuncts {GList(targets)}")

    add("")


    # -------------------------------------------------------
    # House Lord Relationships
    # -------------------------------------------------------

    add("HOUSE LORD RELATIONSHIPS")
    add("-------------------------")

    for lord, grahas in p21.BLConjunctsG2.items():
        add(f"Lord of Bhava {lord} conjuncts {GList(grahas)}")

    add("")


    # -------------------------------------------------------
    # Lord Lord Relationships
    # -------------------------------------------------------

    add("LORD LORD RELATIONSHIPS")
    add("-----------------------")

    for lord, others in p21.BLConjunctsBL2.items():
        others = [int(x) for x in others]
        add(f"Lord of Bhava {lord} connected with Lords {others}")

    add("")


    # -------------------------------------------------------
    # Bhava Aspects
    # -------------------------------------------------------

    add("BHAVA ASPECTS")
    add("--------------")

    for bhav in sorted(p21.BAspectedBy2.keys(), key=int):
        add(
            f"Bhava {bhav} receives aspect from "
            f"{GList(p21.BAspectedBy2[bhav])}"
        )

    add("")


    # -------------------------------------------------------
    # Bhava Aspected By Lords
    # -------------------------------------------------------

    add("BHAVA ASPECTED BY LORDS")
    add("------------------------")

    for bhav in sorted(p21.BAspectedByBL2.keys(), key=int):
        add(
            f"Bhava {bhav} receives aspect from Lords "
            f"{p21.BAspectedByBL2[bhav]}"
        )

    add("")


    # -------------------------------------------------------
    # Yogas
    # -------------------------------------------------------

    add("IDENTIFIED YOGAS")
    add("----------------")

    for yoga in p21.yogsFound:
        add(yoga)


    # -------------------------------------------------------
    # Write file
    # -------------------------------------------------------

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
