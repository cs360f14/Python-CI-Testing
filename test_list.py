#!/usr/bin/python3

################################
# File Name:    test_list.py
# Author:               Chadd Williams
# Date:                 11/7/2014
# Class:                CS 360
# Assignment:   Lecture Examples
# Purpose:              build some tests that will be run by nosetests
################################

from nose import with_setup

def test_simpleAddition():
	assert 1+2 == 3

def setUp():
	global theList 
	theList = []
	

def tearDown():
	pass

@with_setup(setUp, tearDown)
def test_listAppend():
	""" test that list append works

	Since this function's name begins with 'test' and the
	file name also begins with 'test', nosetests will 
	automatically discover and run this test when 
	nosetests is run
	"""
	theList.append(5)

	assert theList[0] == 5



def dictSetup():
	global mapping
	mapping = { str(x):x for x in range(99) }

def dictTeardown():
	pass

@with_setup(dictSetup, dictTeardown)
def test_dictSortedIterator():

	value = 0

	# the keys are strings, so they are sorted lexigraphically (1, 10, ...)
	# use the key parameter to convert the key to an integer and sort 
	# numerically
	for x in sorted(mapping.keys() , key=lambda data: int(data)) :
		print( value, mapping[x])
		assert value == mapping[x]
		value += 1

