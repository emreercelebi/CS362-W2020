# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:31:42 2015

@author: ercelebe
"""

import Dominion
import random
from collections import defaultdict

import testUtility as MyUtility

#Get player names
player_names = MyUtility.get_player_names()

#number of curses and victory cards
nV, nC = MyUtility.get_curse_and_victory_values(player_names)


#Define box
box = MyUtility.get_box(nV)

supply_order = MyUtility.get_supply_order()

#Pick 10 cards from box to be in the supply.
supply = MyUtility.get_supply(box)


#Populate the cards that supply always has
#MyUtility.fill_supply(supply, player_names, nV, nC)
######## Attempt to introduce bug by not including Province cards in supply ########## 
def fill_supply_bug(supply, player_names, nV, nC):
    supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Estate()]*nV
    supply["Curse"]=[Dominion.Curse()]*nC

fill_supply_bug(supply, player_names, nV, nC)

#initialize the trash
trash = MyUtility.initialize_trash()

#Costruct the Player objects
players = MyUtility.build_players(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)