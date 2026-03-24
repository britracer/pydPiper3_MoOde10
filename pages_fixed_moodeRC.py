#!/usr/bin/python.pydPiper
# coding: UTF-8
# MoOde Audio Player RPi1B with hifi DAC and Winstar OLED

from __future__ import unicode_literals


# Page Definitions
# See Page Format.txt for instructions and examples on how to modify your display settings

# Load the fonts needed for this system
FONTS = {
	'small': { 'default':True, 'file':'latin1_5x8_fixed.fnt','size':(5,8) },
	'large': { 'file':'Vintl01_10x16_fixed.fnt', 'size':(10,16) },
}

IMAGES = {
	'paused': {'file':'Aura_pause_inv.png' },
	'splash': {'file':'Aura_splash_inv.png' }
}

# Load the Widgets that will be used to produce the display pages
WIDGETS = {
	'splash': { 'type':'image', 'image':'splash' },
	'paused': { 'type':'image', 'image':'paused' },
        'titlepause': { 'type':'text', 'format':'{0}', 'variables':['title'], 'font':'small','varwidth':True,'effect':('scroll','left',5,2,25,'onloop',5,0) },
	'title': { 'type':'text', 'format':'{0}', 'variables':['title'], 'font':'small','varwidth':True,'effect':('scroll','left',5,1,25,'onloop',5,80) },
	'artistpause': { 'type':'text', 'format':'{0}', 'variables':['artist'], 'font':'small','varwidth':True,'effect':('scroll','left',5,2,25,'onloop',5,0) }, 
	'artist': { 'type':'text', 'format':'{0}', 'variables':['artist'], 'font':'small','varwidth':True,'effect':('scroll','left',5,1,25,'onloop',5,80) },
	'albumpause': { 'type':'text', 'format':'{0}', 'variables':['album'], 'font':'small','varwidth':True,'effect':('scroll','left',5,2,25,'onloop',5,0) },
	'album': { 'type':'text', 'format':'{0}', 'variables':['album'], 'font':'small','varwidth':True,'effect':('scroll','left',5,1,25,'onloop',5,80) },
	'trackpause': { 'type':'text', 'format':'<PAUSED>', 'font':'small', 'just':'center', 'size':(80,16), 'varwidth':True, 'effect':('scroll','left',5,5,25,'none',0,0) },
	'time': { 'type':'text', 'format':'{0}', 'variables':['utc|timezone+US/Eastern|strftime+%-I:%M'], 'font':'large', 'just':'right', 'varwidth':True, 'size':(50,16) },
	'ampm': { 'type':'text', 'format':'{0}', 'variables':['utc|timezone+US/Eastern|strftime+%p'], 'font':'small', 'varwidth':True },
	'showplay': { 'type':'text', 'format':'\ue000 PLAY', 'font':'large', 'varwidth':True, 'just':'center', 'size':(80,16) },
	'showstop': { 'type':'text', 'format':'\ue001 STOP', 'font':'large', 'varwidth':True, 'just':'center', 'size':(80,16) },
	'randomsymbol': { 'type':'text', 'format':'\ue002 ', 'font':'large', 'varwidth':True, 'size':(10,16) },
	'random': { 'type':'text', 'format':'Random\n{0}', 'variables':['random|onoff|Capitalize'], 'font':'small', 'varwidth':True, 'size':(65,16) },
	'repeatoncesymbol': { 'type':'text', 'format':'\ue003 ', 'font':'large', 'varwidth':True, 'size':(10,16) },
	'repeatonce': { 'type':'text', 'format':'Repeat Once\n{0}', 'variables':['single|onoff|Capitalize'], 'font':'small', 'varwidth':True, 'just':'center', 'size':(65,16) },
	'repeatallsymbol': { 'type':'text', 'format':'\ue004 ', 'font':'large', 'varwidth':True, 'size':(10,16) },
	'repeatall': { 'type':'text', 'format':'Repeat All\n{0}', 'variables':['repeat|onoff|Capitalize'], 'font':'small', 'varwidth':True, 'size':(65,16) },
	'radio': { 'type':'text', 'format':'RADIO -no data-', 'font':'small', 'varwidth':True, 'size':(80,16) },
}

# Assemble the widgets into canvases.  Only needed if you need to combine multiple widgets together so you can produce effects on them as a group.
CANVASES = {
	'playartist': { 'widgets': [ ('artist',0,0), ('title',0,8) ], 'size':(80,16) },
	'playalbum': { 'widgets': [ ('album',0,0), ('title',0,8) ], 'size':(80,16) },
	'playtitle': { 'widgets': [ ('title',0,0) ], 'size':(80,16) },
	'playartistpause': { 'widgets': [ ('artistpause',0,0), ('trackpause',0,8) ], 'size':(80,16) },
	'playalbumpause': { 'widgets': [ ('albumpause',0,0), ('trackpause',0,8) ], 'size':(80,16) },
	'playtitlepause': { 'widgets': [ ('titlepause',0,0), ('trackpause',0,8) ], 'size':(80,16) },
	'showrandom': { 'widgets': [ ('randomsymbol',0,0), ('random', 15,0) ], 'size':(80,16) },
	'showrepeatonce': { 'widgets': [ ('repeatoncesymbol',0,0), ('repeatonce', 15,0) ], 'size':(80,16) },
	'showrepeatall': { 'widgets': [ ('repeatallsymbol',0,0), ('repeatall', 15,0) ], 'size':(80,16) },
	'stoptime': { 'widgets': [ ('time',10,2), ('ampm',60,8) ], 'size':(80,16) },
	'blank': { 'widgets': [], 'size':(80,16) },
}

# Place the canvases into sequences to display when their condition is met
# More than one sequence can be active at the same time to allow for alert messages
# You are allowed to include a widget in the sequence without placing it on a canvas

# Note about Conditionals
# Conditionals must evaluate to a True or False resulting
# To access system variables, refer to them within the db dictionary (e.g. db['title'])
# To access the most recent previous state of a variable, refer to them within the dbp dictionary (e.g. dbp['title'])
SEQUENCES = [
	{	'name': 'seqSplash', 'canvases': [ { 'name':'splash', 'duration':9999 } ], 'conditional': "db['state']=='starting'" },
	{
		'name': 'seqPlay',
		'canvases': [
			{ 'name':'playartist', 'duration':20, 'conditional':"db['artist']" },
			{ 'name':'playalbum', 'duration':20, 'conditional':"db['album']" },
			{ 'name':'playtitle', 'duration':20, 'conditional':"db['title'] and not db['album'] and not db['artist']" },
			{ 'name':'radio', 'duration':9999, 'conditional':"not db['artist'] and not db['album'] and db['encoding']=='webradio'" },
		],
		'conditional': "db['state']=='play'"
	},
	{
		'name': 'seqStop',
		'canvases': [
			{ 'name':'playartistpause', 'duration':20, 'conditional':"not db['encoding']=='webradio'" },
			{ 'name':'playtitlepause', 'duration':20, 'conditional':"not db['encoding']=='webradio'" },
			{ 'name':'splash', 'duration':9999, 'conditional':"db['encoding']=='webradio' or dbp['state']=='starting' or not db['artist']" },
		],
		'conditional': "db['state']=='stop' or db['state']=='pause'"
	},
	{
		'name': 'seqCleardisplay',
		'canvases': [ { 'name':'blank', 'duration':1.5 } ],
		'conditional': "db['state'] != dbp['state']",
		'minimum':1,
	},
	{
		'name':'seqAnnounceRandom',
		'canvases': [ { 'name':'showrandom', 'duration':2 } ],
		'conditional': "db['random'] != dbp['random']",
		'minimum':2,
	},
	{
		'name':'seqAnnounceSingle',
		'canvases': [ { 'name':'showrepeatonce', 'duration':2 } ],
		'conditional': "db['single'] != dbp['single']",
		'minimum':2,
	},
	{
		'name':'seqAnnounceRepeat',
		'canvases': [ { 'name':'showrepeatall', 'duration':2 } ],
		'conditional': "db['repeat'] != dbp['repeat']",
		'minimum':2,
	}
]

