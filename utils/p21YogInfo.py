#Copyright (c) 2022, Prithwis Mukerjee
#All rights reserved.
#
#This source code is licensed under the GNU GPL v3.0 -style license found in the
#LICENSE file in the root directory of this source tree. 
# --------------------------------------------------
# Yog Texts, Conditions

#global yogText, yogCond
yogText={}
yogCond = {}

# --------------------------------------------------------------------------
# 3 Anapha Yog - Raman pg 19
yogText['Anapha'] = 'Anapha Yog |Planets other than Sun in 12th Place from Moon'
yogCond['Anapha'] = {"$or":[
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 1}},{'GRashiN.Su' : {'$ne': 12}},{"$or" : [{'GRashiN.Ma' : {'$eq': 12}},{'GRashiN.Ma' : {'$eq': 12}},{'GRashiN.Me' : {'$eq': 2}},{'GRashiN.Ju' : {'$eq': 12}},{'GRashiN.JVe' : {'$eq': 12}},{'GRashiN.Sa' : {'$eq': 12}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 2}},{'GRashiN.Su' : {'$ne': 1}},{"$or" : [{'GRashiN.Ma' : {'$eq': 1}},{'GRashiN.Ma' : {'$eq': 1}},{'GRashiN.Me' : {'$eq': 1}},{'GRashiN.Ju' : {'$eq': 1}},{'GRashiN.JVe' : {'$eq': 1}},{'GRashiN.Sa' : {'$eq': 1}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 3}},{'GRashiN.Su' : {'$ne': 2}},{"$or" : [{'GRashiN.Ma' : {'$eq': 2}},{'GRashiN.Ma' : {'$eq': 2}},{'GRashiN.Me' : {'$eq': 2}},{'GRashiN.Ju' : {'$eq': 2}},{'GRashiN.JVe' : {'$eq': 2}},{'GRashiN.Sa' : {'$eq': 2}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 4}},{'GRashiN.Su' : {'$ne': 3}},{"$or" : [{'GRashiN.Ma' : {'$eq': 3}},{'GRashiN.Ma' : {'$eq': 3}},{'GRashiN.Me' : {'$eq': 3}},{'GRashiN.Ju' : {'$eq': 3}},{'GRashiN.JVe' : {'$eq': 3}},{'GRashiN.Sa' : {'$eq': 3}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 5}},{'GRashiN.Su' : {'$ne': 4}},{"$or" : [{'GRashiN.Ma' : {'$eq': 4}},{'GRashiN.Ma' : {'$eq': 4}},{'GRashiN.Me' : {'$eq': 4}},{'GRashiN.Ju' : {'$eq': 4}},{'GRashiN.JVe' : {'$eq': 4}},{'GRashiN.Sa' : {'$eq': 4}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 6}},{'GRashiN.Su' : {'$ne': 5}},{"$or" : [{'GRashiN.Ma' : {'$eq': 5}},{'GRashiN.Ma' : {'$eq': 5}},{'GRashiN.Me' : {'$eq': 5}},{'GRashiN.Ju' : {'$eq': 5}},{'GRashiN.JVe' : {'$eq': 5}},{'GRashiN.Sa' : {'$eq': 5}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 7}},{'GRashiN.Su' : {'$ne': 6}},{"$or" : [{'GRashiN.Ma' : {'$eq': 6}},{'GRashiN.Ma' : {'$eq': 6}},{'GRashiN.Me' : {'$eq': 6}},{'GRashiN.Ju' : {'$eq': 6}},{'GRashiN.JVe' : {'$eq': 6}},{'GRashiN.Sa' : {'$eq': 6}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 8}},{'GRashiN.Su' : {'$ne': 7}},{"$or" : [{'GRashiN.Ma' : {'$eq': 7}},{'GRashiN.Ma' : {'$eq': 7}},{'GRashiN.Me' : {'$eq': 7}},{'GRashiN.Ju' : {'$eq': 7}},{'GRashiN.JVe' : {'$eq': 7}},{'GRashiN.Sa' : {'$eq': 7}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 9}},{'GRashiN.Su' : {'$ne': 8}},{"$or" : [{'GRashiN.Ma' : {'$eq': 8}},{'GRashiN.Ma' : {'$eq': 8}},{'GRashiN.Me' : {'$eq': 8}},{'GRashiN.Ju' : {'$eq': 8}},{'GRashiN.JVe' : {'$eq': 8}},{'GRashiN.Sa' : {'$eq': 8}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 10}},{'GRashiN.Su' : {'$ne': 9}},{"$or" : [{'GRashiN.Ma' : {'$eq': 9}},{'GRashiN.Ma' : {'$eq': 9}},{'GRashiN.Me' : {'$eq': 9}},{'GRashiN.Ju' : {'$eq': 9}},{'GRashiN.JVe' : {'$eq': 9}},{'GRashiN.Sa' : {'$eq': 9}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 11}},{'GRashiN.Su' : {'$ne': 10}},{"$or" : [{'GRashiN.Ma' : {'$eq': 10}},{'GRashiN.Ma' : {'$eq': 10}},{'GRashiN.Me' : {'$eq': 10}},{'GRashiN.Ju' : {'$eq': 10}},{'GRashiN.JVe' : {'$eq': 10}},{'GRashiN.Sa' : {'$eq': 10}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 12}},{'GRashiN.Su' : {'$ne': 11}},{"$or" : [{'GRashiN.Ma' : {'$eq': 11}},{'GRashiN.Ma' : {'$eq': 11}},{'GRashiN.Me' : {'$eq': 11}},{'GRashiN.Ju' : {'$eq': 11}},{'GRashiN.JVe' : {'$eq': 11}},{'GRashiN.Sa' : {'$eq': 11}}]}]}
                               ]
                        }
# --------------------------------------------------------------------------
# 2 Sunapha Yog - Raman pg 16
yogText['Sunapha'] = 'Sunapha Yog |Planets other than Sun in 2nd Place from Moon'
yogCond['Sunapha'] = {"$or":[
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 1}},{'GRashiN.Su' : {'$ne': 2}},{"$or" : [{'GRashiN.Ma' : {'$eq': 2}},{'GRashiN.Ma' : {'$eq': 2}},{'GRashiN.Me' : {'$eq': 2}},{'GRashiN.Ju' : {'$eq': 2}},{'GRashiN.JVe' : {'$eq': 2}},{'GRashiN.Sa' : {'$eq': 2}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 2}},{'GRashiN.Su' : {'$ne': 3}},{"$or" : [{'GRashiN.Ma' : {'$eq': 3}},{'GRashiN.Ma' : {'$eq': 3}},{'GRashiN.Me' : {'$eq': 3}},{'GRashiN.Ju' : {'$eq': 3}},{'GRashiN.JVe' : {'$eq': 3}},{'GRashiN.Sa' : {'$eq': 3}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 3}},{'GRashiN.Su' : {'$ne': 4}},{"$or" : [{'GRashiN.Ma' : {'$eq': 4}},{'GRashiN.Ma' : {'$eq': 4}},{'GRashiN.Me' : {'$eq': 4}},{'GRashiN.Ju' : {'$eq': 4}},{'GRashiN.JVe' : {'$eq': 4}},{'GRashiN.Sa' : {'$eq': 4}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 4}},{'GRashiN.Su' : {'$ne': 5}},{"$or" : [{'GRashiN.Ma' : {'$eq': 5}},{'GRashiN.Ma' : {'$eq': 5}},{'GRashiN.Me' : {'$eq': 5}},{'GRashiN.Ju' : {'$eq': 5}},{'GRashiN.JVe' : {'$eq': 5}},{'GRashiN.Sa' : {'$eq': 5}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 5}},{'GRashiN.Su' : {'$ne': 6}},{"$or" : [{'GRashiN.Ma' : {'$eq': 6}},{'GRashiN.Ma' : {'$eq': 6}},{'GRashiN.Me' : {'$eq': 6}},{'GRashiN.Ju' : {'$eq': 6}},{'GRashiN.JVe' : {'$eq': 6}},{'GRashiN.Sa' : {'$eq': 6}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 6}},{'GRashiN.Su' : {'$ne': 7}},{"$or" : [{'GRashiN.Ma' : {'$eq': 7}},{'GRashiN.Ma' : {'$eq': 7}},{'GRashiN.Me' : {'$eq': 7}},{'GRashiN.Ju' : {'$eq': 7}},{'GRashiN.JVe' : {'$eq': 7}},{'GRashiN.Sa' : {'$eq': 7}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 7}},{'GRashiN.Su' : {'$ne': 8}},{"$or" : [{'GRashiN.Ma' : {'$eq': 8}},{'GRashiN.Ma' : {'$eq': 8}},{'GRashiN.Me' : {'$eq': 8}},{'GRashiN.Ju' : {'$eq': 8}},{'GRashiN.JVe' : {'$eq': 8}},{'GRashiN.Sa' : {'$eq': 8}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 8}},{'GRashiN.Su' : {'$ne': 9}},{"$or" : [{'GRashiN.Ma' : {'$eq': 9}},{'GRashiN.Ma' : {'$eq': 9}},{'GRashiN.Me' : {'$eq': 9}},{'GRashiN.Ju' : {'$eq': 9}},{'GRashiN.JVe' : {'$eq': 9}},{'GRashiN.Sa' : {'$eq': 9}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 9}},{'GRashiN.Su' : {'$ne': 10}},{"$or" : [{'GRashiN.Ma' : {'$eq': 10}},{'GRashiN.Ma' : {'$eq': 10}},{'GRashiN.Me' : {'$eq': 10}},{'GRashiN.Ju' : {'$eq': 10}},{'GRashiN.JVe' : {'$eq': 10}},{'GRashiN.Sa' : {'$eq': 10}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 10}},{'GRashiN.Su' : {'$ne': 11}},{"$or" : [{'GRashiN.Ma' : {'$eq': 11}},{'GRashiN.Ma' : {'$eq': 11}},{'GRashiN.Me' : {'$eq': 11}},{'GRashiN.Ju' : {'$eq': 11}},{'GRashiN.JVe' : {'$eq': 11}},{'GRashiN.Sa' : {'$eq': 11}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 11}},{'GRashiN.Su' : {'$ne': 12}},{"$or" : [{'GRashiN.Ma' : {'$eq': 12}},{'GRashiN.Ma' : {'$eq': 12}},{'GRashiN.Me' : {'$eq': 12}},{'GRashiN.Ju' : {'$eq': 12}},{'GRashiN.JVe' : {'$eq': 12}},{'GRashiN.Sa' : {'$eq': 12}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 12}},{'GRashiN.Su' : {'$ne': 1}},{"$or" : [{'GRashiN.Ma' : {'$eq': 1}},{'GRashiN.Ma' : {'$eq': 1}},{'GRashiN.Me' : {'$eq': 1}},{'GRashiN.Ju' : {'$eq': 1}},{'GRashiN.JVe' : {'$eq': 1}},{'GRashiN.Sa' : {'$eq': 1}}]}]}
                               ]
                        }

# --------------------------------------------------------------------------
# 4 Dhurdhura Yog - Raman pg 20
yogText['Dhurdhura'] = 'Dhurdhura Yog : Planets on both sides of the Moon'
StrSunapha = yogCond['Sunapha']
StrAnapha = yogCond['Anapha']
yogCond['Dhurdhura'] = {"$and" :[StrSunapha,StrAnapha]}
# --------------------------------------------------------------------------
# 1 Gajakesari Yog - Raman pg 13
yogText['Gajakesari'] = 'Gajakesari Yog : Jupiter is in Kendra or 1,4,7,10th from Moon'
yogCond['Gajakesari'] = {"$or":[
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 1}},{"$or" : [{'GRashiN.Ju' : {'$eq': 1}},{'GRashiN.Ju' : {'$eq': 4}},{'GRashiN.Ju' : {'$eq': 7}},{'GRashiN.Ju' : {'$eq': 10}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 2}},{"$or" : [{'GRashiN.Ju' : {'$eq': 2}},{'GRashiN.Ju' : {'$eq': 5}},{'GRashiN.Ju' : {'$eq': 8}},{'GRashiN.Ju' : {'$eq': 11}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 3}},{"$or" : [{'GRashiN.Ju' : {'$eq': 3}},{'GRashiN.Ju' : {'$eq': 6}},{'GRashiN.Ju' : {'$eq': 9}},{'GRashiN.Ju' : {'$eq': 12}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 4}},{"$or" : [{'GRashiN.Ju' : {'$eq': 4}},{'GRashiN.Ju' : {'$eq': 7}},{'GRashiN.Ju' : {'$eq': 10}},{'GRashiN.Ju' : {'$eq': 1}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 5}},{"$or" : [{'GRashiN.Ju' : {'$eq': 5}},{'GRashiN.Ju' : {'$eq': 8}},{'GRashiN.Ju' : {'$eq': 11}},{'GRashiN.Ju' : {'$eq': 2}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 6}},{"$or" : [{'GRashiN.Ju' : {'$eq': 6}},{'GRashiN.Ju' : {'$eq': 9}},{'GRashiN.Ju' : {'$eq': 12}},{'GRashiN.Ju' : {'$eq': 3}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 7}},{"$or" : [{'GRashiN.Ju' : {'$eq': 7}},{'GRashiN.Ju' : {'$eq': 4}},{'GRashiN.Ju' : {'$eq': 10}},{'GRashiN.Ju' : {'$eq': 1}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 8}},{"$or" : [{'GRashiN.Ju' : {'$eq': 8}},{'GRashiN.Ju' : {'$eq': 11}},{'GRashiN.Ju' : {'$eq': 2}},{'GRashiN.Ju' : {'$eq': 5}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 9}},{"$or" : [{'GRashiN.Ju' : {'$eq': 9}},{'GRashiN.Ju' : {'$eq': 12}},{'GRashiN.Ju' : {'$eq': 3}},{'GRashiN.Ju' : {'$eq': 6}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 10}},{"$or" : [{'GRashiN.Ju' : {'$eq': 10}},{'GRashiN.Ju' : {'$eq': 1}},{'GRashiN.Ju' : {'$eq': 4}},{'GRashiN.Ju' : {'$eq': 7}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 11}},{"$or" : [{'GRashiN.Ju' : {'$eq': 11}},{'GRashiN.Ju' : {'$eq': 2}},{'GRashiN.Ju' : {'$eq': 5}},{'GRashiN.Ju' : {'$eq': 8}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 12}},{"$or" : [{'GRashiN.Ju' : {'$eq': 12}},{'GRashiN.Ju' : {'$eq': 3}},{'GRashiN.Ju' : {'$eq': 6}},{'GRashiN.Ju' : {'$eq': 9}}]}]}
                               ]
                        }

