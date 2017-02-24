#!/usr/local/bin/python3

# Author: David Kolet-Tassara

import argparse

parser = argparse.ArgumentParser(
	description='''This application converts values from supported units to Smoots. \n 
	Supported units include: \n
	inches, feet, yards, miles, American football fields, meters, leagues, \n
	astronomical units, light years, cubits, and hands.''')
parser.add_argument("value", help="value to convert")
parser.add_argument("units", help="inches, feet, meters, etc. See list above for supported units.")

args=parser.parse_args()

def convertInches(x):
	print(str(float(x)/67)+" smoots")

def convertFeet(x):
	print(str((float(x)*12)/67)+" smoots")

def convertMeters(x):
	print(str((float(x)*39.3701)/67)+" smoots")

def convertMiles(x):
	print(str((float(x)*63360)/67)+" smoots")

def convertLeagues(x):
	print(str((float(x)*218740)/67)+" smoots")

def convertYards(x):
	print(str((float(x)*36)/67)+" smoots")

def convertFootballFields(x):
	print(str((float(x)*3600)/67)+" smoots")

def convertAU(x):
	print(str((float(x)*5889679950000)/67)+" smoots")

def convertLightYear(x):
	print(str((float(x)*372461748000000000)/67)+" smoots")

def convertCubit(x):
	print(str((float(x)*18)/67)+" smoots")

def convertHand(x):
	print(str((float(x)*4)/67)+" smoots")

def convertKesselRun(x): #12 Parsecs
	print(str((float(x)*14578004300000000000)/67)+" smoots")

#convertFathom(x):
#convertKilometers(x):
#convertNauticalMile(x):
#convertChain(x):
#convertRod(x):
#convertLunarDistance(x):
#convertParsec(x):
#convertPlanck(l):
#convertFurlong(x):
#convertHorse(x):
#convertDoubleDeckerBus(x):
#convertHumanHair(x):


if args.units in ("in", "inches", "inch"):
	convertInches(args.value)
elif args.units in ("ft", "feet", "foot"):
	convertFeet(args.value)
elif args.units in ("meters", "m", "meter"):
	convertMeters(args.value)
elif args.units in ("miles", "mi", "mile"):
	convertMiles(args.value)
elif args.units in ("leagues", "league"):
	convertLeagues(args.value)
elif args.units in ("yard", "yards", "yrd", "yrds"):
	convertYards(args.value)
elif args.units in ("footballfields", "ff"):
	convertFootballFields(args.value)
elif args.units in ("au"):
	convertAU(args.value)
elif args.units in ("ly", "lightyears"):
	convertLightYear(args.value)
elif args.units in ("cubits"):
	convertCubit(args.value)
elif args.units in ("hand", "hands"):
	convertHand(args.value)
elif args.units in ("kesselrun", "kr", "solo", "han"):
	#despite rumors the record still stands
	convertKesselRun(args.value)
else:
	print("Units not recognized")