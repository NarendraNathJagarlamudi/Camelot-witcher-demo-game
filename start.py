#This is the Starting point of the story. 
# Configure this file in your startExperienceManager file
# Try not to logic in this file except importing files.(should follow modularized coding practice)

# This is the main file

from Great_hall import Great_hall
from action import action
from alchemy import alchemy
from blacksmith import BlackSmith
from bridge import bridge
from create_character import Create_character
from Library import library
from create_location import Create_location
from Narration import Narration
from create_item import item
from purplepotion import *
from forestpath import forest_scene
from spookypath import spooky_path

action('ShowMenu()')
action('HideMenu()')

#CREATE LOCATIONS
lib = Create_location('lib', 'Library')
castle = Create_location('castle', 'GreatHall')
blacksmith = Create_location('blacksmith', 'Blacksmith')
city_location=Create_location('city', 'City')
hotel = Create_location('Hotel', 'Tavern')
forest_path=Create_location('forest','ForestPath')
bridge_path=Create_location('bridge','Bridge')
spookypath=Create_location('spooky','SpookyPath')
dungeon=Create_location('dungeon','Dungeon')
ruins=Create_location('Ruins', 'Ruins')
farm=Create_location('farm', 'Farm')
Alchemy=Create_location('Alchemy', 'AlchemyShop')
port=Create_location('Port', 'Port')




# CREATE Characters 
Evander=Create_character('Evander','D','Merchant', 'Spiky') #composite element/ object
Merchant=Create_character('Merchant', 'D','Merchant', 'Spiky') #composite element/ object
king=Create_character('king', 'D','king', 'Spiky')
spy=Create_character('Spy', 'D', 'Bandit', 'Spiky')
enemy=Create_character('Enemy','D','Bandit','Spiky')
princessaida=Create_character('aida','A','Queen','Ponytail')
kingbodyguard=Create_character('bodyguard','D','HeavyArmour','Spiky')
soldier=Create_character('soldier','D','HeavyArmour','Spiky')
yenefer=Create_character('yenefer', 'E', 'Witch', 'Ponytail')
witch=Create_character('witch', 'D', 'Witch', 'Ponytail')

#-----------


#-----------

# Calling location functions with parameters
# library(Evander, lib)
# Great_hall(Evander, king, castle)
# BlackSmith(Evander, Merchant)
alchemy()
#Hotel(Evander, spy, hotel)
#Castle(Evander, king, castle)
# forest_scene(Evander,enemy,forest_path)
# spooky_path(Evander,soldier,dungeon)





while(True):
    input()
