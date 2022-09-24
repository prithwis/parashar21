#Copyright (c) 2022, Prithwis Mukerjee
#All rights reserved.
#
#This source code is licensed under the GNU GPL v3.0 -style license found in the
#LICENSE file in the root directory of this source tree. 
# --------------------------------------------------
# Yog information taken from '300 Important Combinations', BV Raman, Motilal Banarsidass Publishers, 10th Ed, 7th Reprint
#
#--------------------------------------------------

#
yogText={}
yogCond = {}
# -----------------------------------------------------------
# 13 Amala  Yog - Raman Page 26
# 
# -----------------------------------------------------------

#yogText['Amala_1'] = 'Amala_1 Yog | 10th from Lagna should have a benefic'
yogCond['Amala_1'] = {"$or" :
                        [
                        {"$and": [{'beneficG.Su': {'$eq': True}},{'GrahaBhava.Su' : {'$eq': 10}}]},
                        {"$and": [{'beneficG.Mo': {'$eq': True}},{'GrahaBhava.Mo' : {'$eq': 10}}]},
                        {"$and": [{'beneficG.Ma': {'$eq': True}},{'GrahaBhava.Ma' : {'$eq': 10}}]},
                        {"$and": [{'beneficG.Me': {'$eq': True}},{'GrahaBhava.Me' : {'$eq': 10}}]},
                        {"$and": [{'beneficG.Ju': {'$eq': True}},{'GrahaBhava.Ju' : {'$eq': 10}}]},
                        {"$and": [{'beneficG.Ve': {'$eq': True}},{'GrahaBhava.Ve' : {'$eq': 10}}]},
                        {"$and": [{'beneficG.Sa': {'$eq': True}},{'GrahaBhava.Sa' : {'$eq': 10}}]}
                        ]
                     }
# ----------------------------
#yogText['Amala_2'] = 'Amala_2 Yog | 10th from Moon should have a benefic'
yogCond['Amala_2'] = {"$or" :
                        [
                        {"$and": [{'GRashiN.Mo' : {'$eq': 1}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 10}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 10}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 10}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 10}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 10}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 10}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 2}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 11}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 11}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 11}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 11}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 11}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 11}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 3}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 12}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 12}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 12}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 12}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 12}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 12}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 4}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 1}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 1}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 1}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 1}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 1}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 1}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 5}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 2}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 2}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 2}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 2}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 2}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 2}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 6}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 3}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 3}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 3}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 3}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 3}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 3}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 7}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 4}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 4}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 4}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 4}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 4}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 4}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 8}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 5}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 5}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 5}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 5}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 5}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 5}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 9}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 6}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 6}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 6}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 6}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 6}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 6}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 10}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 7}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 7}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 7}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 7}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 7}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 7}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 11}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 8}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 8}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 8}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 8}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 8}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 8}}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 12}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{'GRashiN.Su' : {'$eq': 9}}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{'GRashiN.Ma' : {'$eq': 9}}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{'GRashiN.Me' : {'$eq': 9}}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{'GRashiN.Ju' : {'$eq': 9}}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{'GRashiN.Ve' : {'$eq': 9}}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{'GRashiN.Sa' : {'$eq': 9}}]}
                                         ]
                                  }
                                 ]
                                }
                        ]
                        }
# ----------------
yogText['Amala'] = 'Amala Yog | 10th from Moon OR Lagna should have a benefic'
yogCond['Amala'] = {"$or" : [yogCond['Amala_1'],yogCond['Amala_2']]}
# -----------------------------------------------------------
# 10 RajLakshana  Yog - Raman Page 28
# 
# -----------------------------------------------------------
yogText['RajLakshana'] = 'RajLakshana Yog | Jupiter, Venus, Mercury, Moon should be in Lagna or they should be in a Kendra'
yogCond['RajLakshana'] = {"$and":
                            [
                                {"$or":[{'GrahaBhava.Ju' : {'$eq': 1}},{'GrahaBhava.Ju' : {'$eq': 4}},{'GrahaBhava.Ju' : {'$eq': 7}},{'GrahaBhava.Ju' : {'$eq': 10}}]},
                                {"$or":[{'GrahaBhava.Ve' : {'$eq': 1}},{'GrahaBhava.Ve' : {'$eq': 4}},{'GrahaBhava.Ve' : {'$eq': 7}},{'GrahaBhava.Ve' : {'$eq': 10}}]},
                                {"$or":[{'GrahaBhava.Me' : {'$eq': 1}},{'GrahaBhava.Me' : {'$eq': 4}},{'GrahaBhava.Me' : {'$eq': 7}},{'GrahaBhava.Me' : {'$eq': 10}}]},
                                {"$or":[{'GrahaBhava.Mo' : {'$eq': 1}},{'GrahaBhava.Mo' : {'$eq': 4}},{'GrahaBhava.Mo' : {'$eq': 7}},{'GrahaBhava.Mo' : {'$eq': 10}}]}
                            ]
                         }
# 8 Chatussagara  Yog - Raman Page 28
# -----------------------------------------------------------
yogText['Chatussagara'] = 'Chatussagara Yog | All the Kendras 1/4/7/10 are occupied by planets, Ra, Ke not counted here'
yogCond['Chatussagara'] = {"$and":
                            [
                                {"$or":
                                    [{'GrahaBhava.Su' : {'$eq': 1}},{'GrahaBhava.Mo' : {'$eq': 1}},{'GrahaBhava.Ma' : {'$eq': 1}},
                                    {'GrahaBhava.Me' : {'$eq': 1}},{'GrahaBhava.Ju' : {'$eq': 1}},{'GrahaBhava.Ve' : {'$eq': 1}}, {'GrahaBhava.Sa' : {'$eq': 1}}
                                    ]},
                                {"$or":
                                    [{'GrahaBhava.Su' : {'$eq': 4}},{'GrahaBhava.Mo' : {'$eq': 4}},{'GrahaBhava.Ma' : {'$eq': 4}},
                                    {'GrahaBhava.Me' : {'$eq': 4}},{'GrahaBhava.Ju' : {'$eq': 4}},{'GrahaBhava.Ve' : {'$eq': 4}}, {'GrahaBhava.Sa' : {'$eq': 4}}
                                    ]},
                                {"$or":
                                    [{'GrahaBhava.Su' : {'$eq': 7}},{'GrahaBhava.Mo' : {'$eq': 7}},{'GrahaBhava.Ma' : {'$eq': 7}},
                                    {'GrahaBhava.Me' : {'$eq': 7}},{'GrahaBhava.Ju' : {'$eq': 7}},{'GrahaBhava.Ve' : {'$eq': 7}}, {'GrahaBhava.Sa' : {'$eq': 7}}
                                    ]},
                                {"$or":
                                    [{'GrahaBhava.Su' : {'$eq': 10}},{'GrahaBhava.Mo' : {'$eq': 10}},{'GrahaBhava.Ma' : {'$eq': 10}},
                                    {'GrahaBhava.Me' : {'$eq': 10}},{'GrahaBhava.Ju' : {'$eq': 10}},{'GrahaBhava.Ve' : {'$eq': 10}}, {'GrahaBhava.Sa' : {'$eq': 10}}
                                    ]}
                            ]
                          }
# -----------------------------------------------------------
# 7 Adhi Yog - Raman Page 25
# -----------------------------------------------------------
yogText['Adhi678'] = 'Adhi678 Yog | Benefics located in 6/7/8th  from Moon'
yogCond['Adhi678'] = {"$or" :
                        [
                        {"$and": [{'GRashiN.Mo' : {'$eq': 1}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 6}},{'GRashiN.Su' : {'$eq': 6+1}},{'GRashiN.Su' : {'$eq': 6+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 6}},{'GRashiN.Ma' : {'$eq': 6+1}},{'GRashiN.Ma' : {'$eq': 6+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 6}},{'GRashiN.Me' : {'$eq': 6+1}},{'GRashiN.Me' : {'$eq': 6+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 6}},{'GRashiN.Ju' : {'$eq': 6+1}},{'GRashiN.Ju' : {'$eq': 6+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 6}},{'GRashiN.Ve' : {'$eq': 6+1}},{'GRashiN.Ve' : {'$eq': 6+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 6}},{'GRashiN.Sa' : {'$eq': 6+1}},{'GRashiN.Sa' : {'$eq': 6+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 2}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 7}},{'GRashiN.Su' : {'$eq': 7+1}},{'GRashiN.Su' : {'$eq': 7+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 7}},{'GRashiN.Ma' : {'$eq': 7+1}},{'GRashiN.Ma' : {'$eq': 7+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 7}},{'GRashiN.Me' : {'$eq': 7+1}},{'GRashiN.Me' : {'$eq': 7+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 7}},{'GRashiN.Ju' : {'$eq': 7+1}},{'GRashiN.Ju' : {'$eq': 7+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 7}},{'GRashiN.Ve' : {'$eq': 7+1}},{'GRashiN.Ve' : {'$eq': 7+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 7}},{'GRashiN.Sa' : {'$eq': 7+1}},{'GRashiN.Sa' : {'$eq': 7+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 3}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 8}},{'GRashiN.Su' : {'$eq': 8+1}},{'GRashiN.Su' : {'$eq': 8+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 8}},{'GRashiN.Ma' : {'$eq': 8+1}},{'GRashiN.Ma' : {'$eq': 8+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 8}},{'GRashiN.Me' : {'$eq': 8+1}},{'GRashiN.Me' : {'$eq': 8+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 8}},{'GRashiN.Ju' : {'$eq': 8+1}},{'GRashiN.Ju' : {'$eq': 8+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 8}},{'GRashiN.Ve' : {'$eq': 8+1}},{'GRashiN.Ve' : {'$eq': 8+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 8}},{'GRashiN.Sa' : {'$eq': 8+1}},{'GRashiN.Sa' : {'$eq': 8+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 4}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 9}},{'GRashiN.Su' : {'$eq': 9+1}},{'GRashiN.Su' : {'$eq': 9+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 9}},{'GRashiN.Ma' : {'$eq': 9+1}},{'GRashiN.Ma' : {'$eq': 9+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 9}},{'GRashiN.Me' : {'$eq': 9+1}},{'GRashiN.Me' : {'$eq': 9+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 9}},{'GRashiN.Ju' : {'$eq': 9+1}},{'GRashiN.Ju' : {'$eq': 9+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 9}},{'GRashiN.Ve' : {'$eq': 9+1}},{'GRashiN.Ve' : {'$eq': 9+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 9}},{'GRashiN.Sa' : {'$eq': 9+1}},{'GRashiN.Sa' : {'$eq': 9+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 5}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 10}},{'GRashiN.Su' : {'$eq': 10+1}},{'GRashiN.Su' : {'$eq': 10+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 10}},{'GRashiN.Ma' : {'$eq': 10+1}},{'GRashiN.Ma' : {'$eq': 10+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 10}},{'GRashiN.Me' : {'$eq': 10+1}},{'GRashiN.Me' : {'$eq': 10+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 10}},{'GRashiN.Ju' : {'$eq': 10+1}},{'GRashiN.Ju' : {'$eq': 10+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 10}},{'GRashiN.Ve' : {'$eq': 10+1}},{'GRashiN.Ve' : {'$eq': 10+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 10}},{'GRashiN.Sa' : {'$eq': 10+1}},{'GRashiN.Sa' : {'$eq': 10+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 6}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 11}},{'GRashiN.Su' : {'$eq': 11+1}},{'GRashiN.Su' : {'$eq': 11+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 11}},{'GRashiN.Ma' : {'$eq': 11+1}},{'GRashiN.Ma' : {'$eq': 11+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 11}},{'GRashiN.Me' : {'$eq': 11+1}},{'GRashiN.Me' : {'$eq': 11+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 11}},{'GRashiN.Ju' : {'$eq': 11+1}},{'GRashiN.Ju' : {'$eq': 11+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 11}},{'GRashiN.Ve' : {'$eq': 11+1}},{'GRashiN.Ve' : {'$eq': 11+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 11}},{'GRashiN.Sa' : {'$eq': 11+1}},{'GRashiN.Sa' : {'$eq': 11+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 7}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 12}},{'GRashiN.Su' : {'$eq': 12+1}},{'GRashiN.Su' : {'$eq': 12+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 12}},{'GRashiN.Ma' : {'$eq': 12+1}},{'GRashiN.Ma' : {'$eq': 12+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 12}},{'GRashiN.Me' : {'$eq': 12+1}},{'GRashiN.Me' : {'$eq': 12+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 12}},{'GRashiN.Ju' : {'$eq': 12+1}},{'GRashiN.Ju' : {'$eq': 12+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 12}},{'GRashiN.Ve' : {'$eq': 12+1}},{'GRashiN.Ve' : {'$eq': 12+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 12}},{'GRashiN.Sa' : {'$eq': 12+1}},{'GRashiN.Sa' : {'$eq': 12+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 8}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 1}},{'GRashiN.Su' : {'$eq': 1+1}},{'GRashiN.Su' : {'$eq': 1+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 1}},{'GRashiN.Ma' : {'$eq': 1+1}},{'GRashiN.Ma' : {'$eq': 1+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 1}},{'GRashiN.Me' : {'$eq': 1+1}},{'GRashiN.Me' : {'$eq': 1+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 1}},{'GRashiN.Ju' : {'$eq': 1+1}},{'GRashiN.Ju' : {'$eq': 1+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 1}},{'GRashiN.Ve' : {'$eq': 1+1}},{'GRashiN.Ve' : {'$eq': 1+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 1}},{'GRashiN.Sa' : {'$eq': 1+1}},{'GRashiN.Sa' : {'$eq': 1+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 9}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 2}},{'GRashiN.Su' : {'$eq': 2+1}},{'GRashiN.Su' : {'$eq': 2+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 2}},{'GRashiN.Ma' : {'$eq': 2+1}},{'GRashiN.Ma' : {'$eq': 2+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 2}},{'GRashiN.Me' : {'$eq': 2+1}},{'GRashiN.Me' : {'$eq': 2+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 2}},{'GRashiN.Ju' : {'$eq': 2+1}},{'GRashiN.Ju' : {'$eq': 2+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 2}},{'GRashiN.Ve' : {'$eq': 2+1}},{'GRashiN.Ve' : {'$eq': 2+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 2}},{'GRashiN.Sa' : {'$eq': 2+1}},{'GRashiN.Sa' : {'$eq': 2+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 10}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 3}},{'GRashiN.Su' : {'$eq': 3+1}},{'GRashiN.Su' : {'$eq': 3+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 3}},{'GRashiN.Ma' : {'$eq': 3+1}},{'GRashiN.Ma' : {'$eq': 3+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 3}},{'GRashiN.Me' : {'$eq': 3+1}},{'GRashiN.Me' : {'$eq': 3+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 3}},{'GRashiN.Ju' : {'$eq': 3+1}},{'GRashiN.Ju' : {'$eq': 3+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 3}},{'GRashiN.Ve' : {'$eq': 3+1}},{'GRashiN.Ve' : {'$eq': 3+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 3}},{'GRashiN.Sa' : {'$eq': 3+1}},{'GRashiN.Sa' : {'$eq': 3+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 11}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 4}},{'GRashiN.Su' : {'$eq': 4+1}},{'GRashiN.Su' : {'$eq': 4+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 4}},{'GRashiN.Ma' : {'$eq': 4+1}},{'GRashiN.Ma' : {'$eq': 4+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 4}},{'GRashiN.Me' : {'$eq': 4+1}},{'GRashiN.Me' : {'$eq': 4+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 4}},{'GRashiN.Ju' : {'$eq': 4+1}},{'GRashiN.Ju' : {'$eq': 4+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 4}},{'GRashiN.Ve' : {'$eq': 4+1}},{'GRashiN.Ve' : {'$eq': 4+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 4}},{'GRashiN.Sa' : {'$eq': 4+1}},{'GRashiN.Sa' : {'$eq': 4+2}}]}]}
                                         ]
                                  }
                                 ]
                                },
                        {"$and": [{'GRashiN.Mo' : {'$eq': 12}},
                                 {"$or":[{"$and":[{'beneficG.Su': {'$eq': True}},{"$or":[{'GRashiN.Su' : {'$eq': 5}},{'GRashiN.Su' : {'$eq': 5+1}},{'GRashiN.Su' : {'$eq': 5+2}}]}]},
                                         {"$and":[{'beneficG.Ma': {'$eq': True}},{"$or":[{'GRashiN.Ma' : {'$eq': 5}},{'GRashiN.Ma' : {'$eq': 5+1}},{'GRashiN.Ma' : {'$eq': 5+2}}]}]},
                                         {"$and":[{'beneficG.Me': {'$eq': True}},{"$or":[{'GRashiN.Me' : {'$eq': 5}},{'GRashiN.Me' : {'$eq': 5+1}},{'GRashiN.Me' : {'$eq': 5+2}}]}]},
                                         {"$and":[{'beneficG.Ju': {'$eq': True}},{"$or":[{'GRashiN.Ju' : {'$eq': 5}},{'GRashiN.Ju' : {'$eq': 5+1}},{'GRashiN.Ju' : {'$eq': 5+2}}]}]},
                                         {"$and":[{'beneficG.Ve': {'$eq': True}},{"$or":[{'GRashiN.Ve' : {'$eq': 5}},{'GRashiN.Ve' : {'$eq': 5+1}},{'GRashiN.Ve' : {'$eq': 5+2}}]}]},
                                         {"$and":[{'beneficG.Sa': {'$eq': True}},{"$or":[{'GRashiN.Sa' : {'$eq': 5}},{'GRashiN.Sa' : {'$eq': 5+1}},{'GRashiN.Sa' : {'$eq': 5+2}}]}]}
                                         ]
                                  }
                                 ]
                                }
                        ]
                        }
# -----------------------------------------------------------
#yogText['Adhi6'] = 'Adhi6 Yog | Benefics located in 6th from Moon'


# -----------------------------------------------------------
# 6 Chandra Mangala Yog - page 24
# Comes in two flavours 
# -----------------------------------------------------------
#yogText['ChandraMangal1'] = 'Chandra Mangal Yog | Mars Conjoins Moon'
yogCond['ChandraMangal1'] = {'GConjunctsG2.Mo' : {'$in': ['Ma']}}
#
#yogText['ChandraMangal2'] = 'Chandra Mangal Yog | Mars and Moon in Mutual Aspect'
yogCond['ChandraMangal2'] = {"$and":
                                [
                                    {'GAspectedBy2.Ma' : {'$in': ['Mo']}} ,     # Ma aspected by Moon       
                                    {'GAspectedBy2.Mo' : {'$in': ['Ma']}}       # Moon aspected by Mars 
                                ]
                            }
#
yogText['ChandraMangal'] = 'Chandra Mangal Yog | Mars Conjoins Moon or  Mars and Moon in Mutual Aspect'
yogCond['ChandraMangal'] = {"$or":[yogCond['ChandraMangal1'],yogCond['ChandraMangal2']]}
#--------------------------------------------------
# 5 Kemadruma Yog - Raman pg 22
# -----------------------------------------------------------
yogText['Kemadruma'] = 'Kemadruma Yog : No planets on either sides of the Moon'
yogCond['Kemadruma'] = {"$or":[
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 1}},
                                            {'GRashiN.Su' : {'$ne': 2}},{'GRashiN.Su' : {'$ne': 12}},{'GRashiN.Ma' : {'$ne': 2}},{'GRashiN.Ma' : {'$ne': 12}},
                                            {'GRashiN.Me' : {'$ne': 2}},{'GRashiN.Me' : {'$ne': 12}},{'GRashiN.Ju' : {'$ne': 2}},{'GRashiN.Ju' : {'$ne': 12}},
                                            {'GRashiN.Ve' : {'$ne': 2}},{'GRashiN.Ve' : {'$ne': 12}},{'GRashiN.Sa' : {'$ne': 2}},{'GRashiN.Sa' : {'$ne': 12}},
                                            {'GRashiN.Ra' : {'$ne': 2}},{'GRashiN.Ra' : {'$ne': 12}},{'GRashiN.Ke' : {'$ne': 2}},{'GRashiN.Ke' : {'$ne': 12}}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 2}},
                                            {'GRashiN.Su' : {'$ne': 3}},{'GRashiN.Su' : {'$ne': 1}},{'GRashiN.Ma' : {'$ne': 3}},{'GRashiN.Ma' : {'$ne': 1}},
                                            {'GRashiN.Me' : {'$ne': 3}},{'GRashiN.Me' : {'$ne': 1}},{'GRashiN.Ju' : {'$ne': 3}},{'GRashiN.Ju' : {'$ne': 1}},
                                            {'GRashiN.Ve' : {'$ne': 3}},{'GRashiN.Ve' : {'$ne': 1}},{'GRashiN.Sa' : {'$ne': 3}},{'GRashiN.Sa' : {'$ne': 1}},
                                            {'GRashiN.Ra' : {'$ne': 3}},{'GRashiN.Ra' : {'$ne': 1}},{'GRashiN.Ke' : {'$ne': 3}},{'GRashiN.Ke' : {'$ne': 1}}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 3}},
                                            {'GRashiN.Su' : {'$ne': 4}},{'GRashiN.Su' : {'$ne': 2}},{'GRashiN.Ma' : {'$ne': 4}},{'GRashiN.Ma' : {'$ne': 2}},
                                            {'GRashiN.Me' : {'$ne': 4}},{'GRashiN.Me' : {'$ne': 2}},{'GRashiN.Ju' : {'$ne': 4}},{'GRashiN.Ju' : {'$ne': 2}},
                                            {'GRashiN.Ve' : {'$ne': 4}},{'GRashiN.Ve' : {'$ne': 2}},{'GRashiN.Sa' : {'$ne': 4}},{'GRashiN.Sa' : {'$ne': 2}},
                                            {'GRashiN.Ra' : {'$ne': 4}},{'GRashiN.Ra' : {'$ne': 2}},{'GRashiN.Ke' : {'$ne': 4}},{'GRashiN.Ke' : {'$ne': 2}}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 4}},
                                            {'GRashiN.Su' : {'$ne': 5}},{'GRashiN.Su' : {'$ne': 3}},{'GRashiN.Ma' : {'$ne': 5}},{'GRashiN.Ma' : {'$ne': 3}},
                                            {'GRashiN.Me' : {'$ne': 5}},{'GRashiN.Me' : {'$ne': 3}},{'GRashiN.Ju' : {'$ne': 5}},{'GRashiN.Ju' : {'$ne': 3}},
                                            {'GRashiN.Ve' : {'$ne': 5}},{'GRashiN.Ve' : {'$ne': 3}},{'GRashiN.Sa' : {'$ne': 5}},{'GRashiN.Sa' : {'$ne': 3}},
                                            {'GRashiN.Ra' : {'$ne': 5}},{'GRashiN.Ra' : {'$ne': 3}},{'GRashiN.Ke' : {'$ne': 5}},{'GRashiN.Ke' : {'$ne': 3}}]},
                                 { "$and":[{'GRashiN.Mo' : {'$eq': 5}},
                                            {'GRashiN.Su' : {'$ne': 6}},{'GRashiN.Su' : {'$ne': 4}},{'GRashiN.Ma' : {'$ne': 6}},{'GRashiN.Ma' : {'$ne': 4}},
                                            {'GRashiN.Me' : {'$ne': 6}},{'GRashiN.Me' : {'$ne': 4}},{'GRashiN.Ju' : {'$ne': 6}},{'GRashiN.Ju' : {'$ne': 4}},
                                            {'GRashiN.Ve' : {'$ne': 6}},{'GRashiN.Ve' : {'$ne': 4}},{'GRashiN.Sa' : {'$ne': 6}},{'GRashiN.Sa' : {'$ne': 4}},
                                            {'GRashiN.Ra' : {'$ne': 6}},{'GRashiN.Ra' : {'$ne': 4}},{'GRashiN.Ke' : {'$ne': 6}},{'GRashiN.Ke' : {'$ne': 4}}]},
                                 { "$and":[{'GRashiN.Mo' : {'$eq': 6}},
                                            {'GRashiN.Su' : {'$ne': 7}},{'GRashiN.Su' : {'$ne': 5}},{'GRashiN.Ma' : {'$ne': 7}},{'GRashiN.Ma' : {'$ne': 5}},
                                            {'GRashiN.Me' : {'$ne': 7}},{'GRashiN.Me' : {'$ne': 5}},{'GRashiN.Ju' : {'$ne': 7}},{'GRashiN.Ju' : {'$ne': 5}},
                                            {'GRashiN.Ve' : {'$ne': 7}},{'GRashiN.Ve' : {'$ne': 5}},{'GRashiN.Sa' : {'$ne': 7}},{'GRashiN.Sa' : {'$ne': 5}},
                                            {'GRashiN.Ra' : {'$ne': 7}},{'GRashiN.Ra' : {'$ne': 5}},{'GRashiN.Ke' : {'$ne': 7}},{'GRashiN.Ke' : {'$ne': 5}}]},
                                 { "$and":[{'GRashiN.Mo' : {'$eq': 7}},
                                            {'GRashiN.Su' : {'$ne': 8}},{'GRashiN.Su' : {'$ne': 6}},{'GRashiN.Ma' : {'$ne': 8}},{'GRashiN.Ma' : {'$ne': 6}},
                                            {'GRashiN.Me' : {'$ne': 8}},{'GRashiN.Me' : {'$ne': 6}},{'GRashiN.Ju' : {'$ne': 8}},{'GRashiN.Ju' : {'$ne': 6}},
                                            {'GRashiN.Ve' : {'$ne': 8}},{'GRashiN.Ve' : {'$ne': 6}},{'GRashiN.Sa' : {'$ne': 8}},{'GRashiN.Sa' : {'$ne': 6}},
                                            {'GRashiN.Ra' : {'$ne': 8}},{'GRashiN.Ra' : {'$ne': 6}},{'GRashiN.Ke' : {'$ne': 8}},{'GRashiN.Ke' : {'$ne': 6}}]},
                                 { "$and":[{'GRashiN.Mo' : {'$eq': 8}},
                                            {'GRashiN.Su' : {'$ne': 9}},{'GRashiN.Su' : {'$ne': 7}},{'GRashiN.Ma' : {'$ne': 9}},{'GRashiN.Ma' : {'$ne': 7}},
                                            {'GRashiN.Me' : {'$ne': 9}},{'GRashiN.Me' : {'$ne': 7}},{'GRashiN.Ju' : {'$ne': 9}},{'GRashiN.Ju' : {'$ne': 7}},
                                            {'GRashiN.Ve' : {'$ne': 9}},{'GRashiN.Ve' : {'$ne': 7}},{'GRashiN.Sa' : {'$ne': 9}},{'GRashiN.Sa' : {'$ne': 7}},
                                            {'GRashiN.Ra' : {'$ne': 9}},{'GRashiN.Ra' : {'$ne': 7}},{'GRashiN.Ke' : {'$ne': 9}},{'GRashiN.Ke' : {'$ne': 7}}]},
                                 { "$and":[{'GRashiN.Mo' : {'$eq': 9}},
                                            {'GRashiN.Su' : {'$ne': 10}},{'GRashiN.Su' : {'$ne': 8}},{'GRashiN.Ma' : {'$ne': 10}},{'GRashiN.Ma' : {'$ne': 8}},
                                            {'GRashiN.Me' : {'$ne': 10}},{'GRashiN.Me' : {'$ne': 8}},{'GRashiN.Ju' : {'$ne': 10}},{'GRashiN.Ju' : {'$ne': 8}},
                                            {'GRashiN.Ve' : {'$ne': 10}},{'GRashiN.Ve' : {'$ne': 8}},{'GRashiN.Sa' : {'$ne': 10}},{'GRashiN.Sa' : {'$ne': 8}},
                                            {'GRashiN.Ra' : {'$ne': 10}},{'GRashiN.Ra' : {'$ne': 8}},{'GRashiN.Ke' : {'$ne': 10}},{'GRashiN.Ke' : {'$ne': 8}}]},
                                 { "$and":[{'GRashiN.Mo' : {'$eq': 10}},
                                            {'GRashiN.Su' : {'$ne': 11}},{'GRashiN.Su' : {'$ne': 9}},{'GRashiN.Ma' : {'$ne': 11}},{'GRashiN.Ma' : {'$ne': 9}},
                                            {'GRashiN.Me' : {'$ne': 11}},{'GRashiN.Me' : {'$ne': 9}},{'GRashiN.Ju' : {'$ne': 11}},{'GRashiN.Ju' : {'$ne': 9}},
                                            {'GRashiN.Ve' : {'$ne': 11}},{'GRashiN.Ve' : {'$ne': 9}},{'GRashiN.Sa' : {'$ne': 11}},{'GRashiN.Sa' : {'$ne': 9}},
                                            {'GRashiN.Ra' : {'$ne': 11}},{'GRashiN.Ra' : {'$ne': 9}},{'GRashiN.Ke' : {'$ne': 11}},{'GRashiN.Ke' : {'$ne': 9}}]},
                                 { "$and":[{'GRashiN.Mo' : {'$eq': 11}},
                                            {'GRashiN.Su' : {'$ne': 12}},{'GRashiN.Su' : {'$ne': 10}},{'GRashiN.Ma' : {'$ne': 12}},{'GRashiN.Ma' : {'$ne': 10}},
                                            {'GRashiN.Me' : {'$ne': 12}},{'GRashiN.Me' : {'$ne': 10}},{'GRashiN.Ju' : {'$ne': 12}},{'GRashiN.Ju' : {'$ne': 10}},
                                            {'GRashiN.Ve' : {'$ne': 12}},{'GRashiN.Ve' : {'$ne': 10}},{'GRashiN.Sa' : {'$ne': 12}},{'GRashiN.Sa' : {'$ne': 10}},
                                            {'GRashiN.Ra' : {'$ne': 12}},{'GRashiN.Ra' : {'$ne': 10}},{'GRashiN.Ke' : {'$ne': 12}},{'GRashiN.Ke' : {'$ne': 10}}]},
                                 { "$and":[{'GRashiN.Mo' : {'$eq': 12}},
                                            {'GRashiN.Su' : {'$ne': 1}},{'GRashiN.Su' : {'$ne': 11}},{'GRashiN.Ma' : {'$ne': 1}},{'GRashiN.Ma' : {'$ne': 11}},
                                            {'GRashiN.Me' : {'$ne': 1}},{'GRashiN.Me' : {'$ne': 11}},{'GRashiN.Ju' : {'$ne': 1}},{'GRashiN.Ju' : {'$ne': 11}},
                                            {'GRashiN.Ve' : {'$ne': 1}},{'GRashiN.Ve' : {'$ne': 11}},{'GRashiN.Sa' : {'$ne': 1}},{'GRashiN.Sa' : {'$ne': 11}},
                                            {'GRashiN.Ra' : {'$ne': 1}},{'GRashiN.Ra' : {'$ne': 11}},{'GRashiN.Ke' : {'$ne': 1}},{'GRashiN.Ke' : {'$ne': 11}}]}
                               ]
                        }


# --------------------------------------------------------------------------
# 3 Anapha Yog - Raman pg 19
# -----------------------------------------------------------
yogText['Anapha'] = 'Anapha Yog |Planets other than Sun in 12th Place from Moon'
yogCond['Anapha'] = {"$or":[
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 1}},{'GRashiN.Su' : {'$ne': 12}},{"$or" : [{'GRashiN.Ma' : {'$eq': 12}},{'GRashiN.Ma' : {'$eq': 12}},{'GRashiN.Me' : {'$eq': 12}},{'GRashiN.Ju' : {'$eq': 12}},{'GRashiN.Ve' : {'$eq': 12}},{'GRashiN.Sa' : {'$eq': 12}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 2}},{'GRashiN.Su' : {'$ne': 1}},{"$or" : [{'GRashiN.Ma' : {'$eq': 1}},{'GRashiN.Ma' : {'$eq': 1}},{'GRashiN.Me' : {'$eq': 1}},{'GRashiN.Ju' : {'$eq': 1}},{'GRashiN.Ve' : {'$eq': 1}},{'GRashiN.Sa' : {'$eq': 1}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 3}},{'GRashiN.Su' : {'$ne': 2}},{"$or" : [{'GRashiN.Ma' : {'$eq': 2}},{'GRashiN.Ma' : {'$eq': 2}},{'GRashiN.Me' : {'$eq': 2}},{'GRashiN.Ju' : {'$eq': 2}},{'GRashiN.Ve' : {'$eq': 2}},{'GRashiN.Sa' : {'$eq': 2}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 4}},{'GRashiN.Su' : {'$ne': 3}},{"$or" : [{'GRashiN.Ma' : {'$eq': 3}},{'GRashiN.Ma' : {'$eq': 3}},{'GRashiN.Me' : {'$eq': 3}},{'GRashiN.Ju' : {'$eq': 3}},{'GRashiN.Ve' : {'$eq': 3}},{'GRashiN.Sa' : {'$eq': 3}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 5}},{'GRashiN.Su' : {'$ne': 4}},{"$or" : [{'GRashiN.Ma' : {'$eq': 4}},{'GRashiN.Ma' : {'$eq': 4}},{'GRashiN.Me' : {'$eq': 4}},{'GRashiN.Ju' : {'$eq': 4}},{'GRashiN.Ve' : {'$eq': 4}},{'GRashiN.Sa' : {'$eq': 4}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 6}},{'GRashiN.Su' : {'$ne': 5}},{"$or" : [{'GRashiN.Ma' : {'$eq': 5}},{'GRashiN.Ma' : {'$eq': 5}},{'GRashiN.Me' : {'$eq': 5}},{'GRashiN.Ju' : {'$eq': 5}},{'GRashiN.Ve' : {'$eq': 5}},{'GRashiN.Sa' : {'$eq': 5}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 7}},{'GRashiN.Su' : {'$ne': 6}},{"$or" : [{'GRashiN.Ma' : {'$eq': 6}},{'GRashiN.Ma' : {'$eq': 6}},{'GRashiN.Me' : {'$eq': 6}},{'GRashiN.Ju' : {'$eq': 6}},{'GRashiN.Ve' : {'$eq': 6}},{'GRashiN.Sa' : {'$eq': 6}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 8}},{'GRashiN.Su' : {'$ne': 7}},{"$or" : [{'GRashiN.Ma' : {'$eq': 7}},{'GRashiN.Ma' : {'$eq': 7}},{'GRashiN.Me' : {'$eq': 7}},{'GRashiN.Ju' : {'$eq': 7}},{'GRashiN.Ve' : {'$eq': 7}},{'GRashiN.Sa' : {'$eq': 7}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 9}},{'GRashiN.Su' : {'$ne': 8}},{"$or" : [{'GRashiN.Ma' : {'$eq': 8}},{'GRashiN.Ma' : {'$eq': 8}},{'GRashiN.Me' : {'$eq': 8}},{'GRashiN.Ju' : {'$eq': 8}},{'GRashiN.Ve' : {'$eq': 8}},{'GRashiN.Sa' : {'$eq': 8}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 10}},{'GRashiN.Su' : {'$ne': 9}},{"$or" : [{'GRashiN.Ma' : {'$eq': 9}},{'GRashiN.Ma' : {'$eq': 9}},{'GRashiN.Me' : {'$eq': 9}},{'GRashiN.Ju' : {'$eq': 9}},{'GRashiN.Ve' : {'$eq': 9}},{'GRashiN.Sa' : {'$eq': 9}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 11}},{'GRashiN.Su' : {'$ne': 10}},{"$or" : [{'GRashiN.Ma' : {'$eq': 10}},{'GRashiN.Ma' : {'$eq': 10}},{'GRashiN.Me' : {'$eq': 10}},{'GRashiN.Ju' : {'$eq': 10}},{'GRashiN.Ve' : {'$eq': 10}},{'GRashiN.Sa' : {'$eq': 10}}]}]},
                                  { "$and":[{'GRashiN.Mo' : {'$eq': 12}},{'GRashiN.Su' : {'$ne': 11}},{"$or" : [{'GRashiN.Ma' : {'$eq': 11}},{'GRashiN.Ma' : {'$eq': 11}},{'GRashiN.Me' : {'$eq': 11}},{'GRashiN.Ju' : {'$eq': 11}},{'GRashiN.Ve' : {'$eq': 11}},{'GRashiN.Sa' : {'$eq': 11}}]}]}
                               ]
                        }
# --------------------------------------------------------------------------
# 2 Sunapha Yog - Raman pg 16
# -----------------------------------------------------------
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
# -----------------------------------------------------------
yogText['Dhurdhura'] = 'Dhurdhura Yog | Planets on both sides of the Moon'
StrSunapha = yogCond['Sunapha']
StrAnapha = yogCond['Anapha']
yogCond['Dhurdhura'] = {"$and" :[StrSunapha,StrAnapha]}
# --------------------------------------------------------------------------
# 1 Gajakesari Yog - Raman pg 13
# -----------------------------------------------------------
yogText['Gajakesari'] = 'Gajakesari Yog | Jupiter is in Kendra or 1,4,7,10th from Moon'
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
# --------------------------------------------------------------------------------- END
print(len(list(yogText.keys())), 'Yogs on record')
#for y in list(yogText.keys()):
for i,y in enumerate(yogText.keys()):
    print(i, ':',yogText[y])
