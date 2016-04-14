#!/usr/bin/env python


num=3

def func():
	global num
	num = 5 
	print num

func()
print num

