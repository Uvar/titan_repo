# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:34:56 2020

@author: idh
"""
import os
import itertools as it
import numpy as np
import pandas as pd
from collections import namedtuple

titan = namedtuple("Titan", ["name", 'type', 'role'])

Moloch = titan("Moloch", "Fire", ["Tank"])
Angus = titan("Angus", "Earth", ["Tank"])
Sigurd = titan("Sigurd", "Water", ["Tank"])

Eden = titan("Eden", "Earth", ["Damage", "Utility"])
Nova = titan("Nova", "Water", ["Damage"])
Hyperion = titan("Hyperion", "Water", ["Damage", "Utility"])

Mairi = titan("Mairi", "Water", ["Utility"])
Ignis = titan("Ignis", "Fire", ["Utility"])
Avalon = titan("Avalon", "Earth", ["Utility"])

Vulcan = titan("Vulcan", "Fire", ["Damage"])
Sylva = titan("Sylva", "Earth", ["Damage"])
Araji = titan("Araji", "Fire", ["Damage"])

tanks = [Moloch, Angus, Sigurd]
damage = [Eden, Hyperion, Nova, Vulcan, Sylva, Araji]
utility = [Eden, Nova, Hyperion, Mairi, Ignis, Avalon]

titans = []
_ = [titans.append(ttn) for ttn in tanks+utility+damage if not ttn in titans]


def check_for_match(ttn_list1, ttn_list2):
    return np.array([ttn in ttn_list2 for ttn in ttn_list1]).all()

def names_only(ttn_list):
    return [ttn.name for ttn in ttn_list]

def check_amount_tanks(ttn_list):
    return sum(["Tank" in ttn.role for ttn in ttn_list])

def check_amount_utility(ttn_list):
    return sum(["Utility" in ttn.role for ttn in ttn_list])

def check_amount_damage(ttn_list):
    return sum(["Damage" in ttn.role for ttn in ttn_list])

def check_amount_fire(ttn_list):
    return sum(["Fire" in ttn.type for ttn in ttn_list])

def check_amount_water(ttn_list):
    return sum(["Water" in ttn.type for ttn in ttn_list])

def check_amount_earth(ttn_list):
    return sum(["Earth" in ttn.role for ttn in ttn_list])

def totem_active(ttn_list):
    return np.array([func(ttn_list) >=3 for func in 
                     [check_amount_fire, check_amount_water, check_amount_earth]]).any()
    
def print_summary_match(ttn_list1, ttn_list2):
    print("Team defending: {}\ntotem: {}\ntanks: {}\nutility: {}\ndamage: {}\n\n\
Team attacking: {}\ntotem: {}\ntanks: {}\nutility: {}\ndamage: {}".format(
          names_only(ttn_list1),
          totem_active(ttn_list1),
          check_amount_tanks(ttn_list1),
          check_amount_utility(ttn_list1),
          check_amount_damage(ttn_list1),
          names_only(ttn_list2),
          totem_active(ttn_list2),
          check_amount_tanks(ttn_list2),
          check_amount_utility(ttn_list2),
          check_amount_damage(ttn_list2))
          )
          
#TODO refactor repetitive statements to something prettier..
combinations = [draw for draw in it.combinations(titans, 5) if totem_active(draw)]
outcomes = {"y": 1, "n": -1}
if "current_state.csv" not in os.listdir():
    init = np.zeros(len(combinations), dtype=int)
    grid = pd.DataFrame({", ".join(names_only(c)): init for c in combinations})
    grid.index = grid.columns
    grid.index.name = "titan combination"
else:
    grid = pd.read_csv("current_state.csv", decimal=",", sep=";").set_index("titan combination")
for i,c1 in enumerate(combinations):
    for j,c2 in enumerate(combinations):
        if grid.iloc[j,i] != 0:
            continue
        print_summary_match(c1,c2)
        result = input("Did the attacking team win? [y/n]").lower()
        while result not in outcomes.keys():
            print("Answer not recognized...")
            result = input("Did the attacking team win? [y/n]").lower()
        result = int(outcomes[result])
        grid.iloc[j,i] = result
        cont = input("Want to continue now? [y/n]").lower()
        while cont not in outcomes.keys():
            print("Answer not recognized...")
            cont = input("Want to continue now? [y/n]").lower()
        if cont == "n":
            break
    if cont == "n":
        break
            
grid.to_csv("current_state.csv", decimal=',', sep=';')