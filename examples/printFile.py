#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import sequenceParser

if len(sys.argv) > 2:
	print( 'printFile takes only one path.' )
	sys.exit()

path = os.curdir
if len(sys.argv) == 2 :
	path = sys.argv[1]

sequenceParser.printFileInDirectory( path )

