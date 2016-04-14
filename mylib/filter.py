#!/usr/bin/env python
from math import atan2
import time

class FILLTER_FUNC :
	#float Var
	Angle_Raw = 0
	Angle_Filtered = 0
	omega = 0
	dt = 0

	Angle_Delta = 0
	Angle_Recursive = 0
 	Angle_Confidence = 0
 
 	 #define Var
	Gry_offset = 0  #//The offset of the gyro
	Gyr_Gain = 131
	Angle_offset = 0 # // The offset of the accelerator
	RMotor_offset = 0 # // The offset of the Motor
	LMotor_offset = 0 # // The offset of the Motor

	#time Var
	now = 0
	preTime = 0
	pi = 3.14159

	#sensor Var
	ax=40
	ay=10
	az=90
	gx=0
	gy=0
	gz=0
	
	@classmethod
	def __init__(self):
		print "init filter"
		
	def filter(self):
		#global Val

		global Angle_Raw
		global Angle_Filtered
		global omega
		global dt

		global Angle_Delta
		global Angle_Recursive
		global Angle_Confidence

		global Gry_offset  #//The offset of the gyro
		global Gyr_Gain
		global Angle_offset # // The offset of the accelerator
		global RMotor_offset # // The offset of the Motor
		global LMotor_offset # // The offset of the Motor

		global ax
		global ay
		global az
		global g
		global gy
		global gz

		global preTime

		Angle_Raw=(atan2(ax, az) * 180 / pi + Angle_offset)
		now = int(round(time.time() * 1000))
		omega = gx / Gyr_Gain + Gry_offset;now = int(round(time.time() * 1000))
		timeChange = now - preTime
		preTime =  now
		dt = timeChange * 0x000001
		Angle_Delta = (Angle_Raw - Angle_Filtered) * 0.64;
		Angle_Recursive = Angle_Delta * dt + Angle_Recursive;
		Angle_Confidence = Angle_Recursive + (Angle_Raw - Angle_Filtered) * 1.6 + omega;
		Angle_Filtered = Angle_Confidence * dt + Angle_Filtered;
	
	def print_data(self):
		filter()
		print preTime
		print now
