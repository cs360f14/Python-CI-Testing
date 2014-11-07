#!/usr/bin/python3

################################
# File Name:	unittestSimpleJSONExample.py
# Author:		Chadd Williams
# Date:			11/7/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Demonstrate unit tests with SimpleJSON
################################

# adapted from https://docs.python.org/3/library/unittest.html

# python3 -m unittest unittestSimpleJSONExample -v

import random
import unittest
import simplejson

class TestListFunctions(unittest.TestCase):

	listSize = 10

	def setUp(self):
		""" the text fixture, necessary setup for the tests to run
		"""
		self.theList = list(range(self.listSize))

		# shuffle the list
		random.shuffle(self.theList)
		
	def tearDown(self):
		""" nothing to tear down here
		
		If your test created a database or built a network connection
		you might delete the database or close the network connection
		here.  You might also close files you opened, close your
		TK windows if this is GUI program, or kill threads if this is
		a multithreaded application
		"""
		pass # nothing to do


	def test_dumps(self):
		# straight from the simplejson docs
		# http://simplejson.readthedocs.org/en/latest/#module-simplejson
		
		strResult = simplejson.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
		self.assertEqual(strResult, '["foo", {"bar": ["baz", null, 1.0, 2]}]')
		
