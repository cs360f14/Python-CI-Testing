Python-CI-Testing
=================

[![Build Status](https://travis-ci.org/chaddcw/Python-CI-Testing.svg)](https://travis-ci.org/chaddcw/Python-CI-Testing)

A repository to demonstrate Python and Travis CI testing

* docTestExample.py - this file demonstrates DocTest testing
* unittestExample.py - this file demonstrates simple unittests
  * You can demonstrate a failing testcase by uncommenting test_thistestwillfail
* cards.py - this file contains a class to be unittested
* unittestCards.py - this file contains unittests for cards.py
* unittestSimpleJSONExample.py - this file requires Travis-CI to install simplejson before running the tests.
* test_UnitTests.py - add a copy of unittestExample.py that will be picked up by nosetests
* test_list.py - added a new file for nosetests
