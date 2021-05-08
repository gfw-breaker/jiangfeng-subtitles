#!/usr/bin/python
# coding: utf-8

import sys
import time
import datetime


fname = sys.argv[1]
ms = sys.argv[2]

file = open(fname)

def tt(t):
	segs = t.split(',')
	a = datetime.datetime.strptime(segs[0], '%H:%M:%S')	
	b = (a + datetime.timedelta(seconds=-7)).strftime('%H:%M:%S')
	return b + ',' + segs[1]	


def offset(line):
	t1 = line[0:12]
	t2 = line[17:29]
	return tt(t1) + ' --> ' + tt(t2)


while 1:
	line = file.readline()
	if not line:
		break
	if line.find('-->') != -1 :
		print offset(line)
	else :
		print line,

