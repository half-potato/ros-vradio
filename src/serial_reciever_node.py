#!/usr/bin/env python
import rospy, serial, math, time
from vradio.msg import Radio

class SerialReciever:
	def __init__(self):
		rospy.init_node("serial_reciever", anonymous=False)
		port = rospy.get_param("~port")
		self.ser = serial.Serial(port, 9600, timeout=0.1)
		self.sub = rospy.Publisher("physical_radio", Radio, queue_size=10)
		while True:
			msg = self.ser.readline()[2:]
			if msg!="":
				snums = msg.split("\t:")
				snums[-1] = snums[-1][:-2]
				try:
					nums = [int(i) for i in snums]
				except ValueError:
					continue
				newMsg = Radio()
				newMsg.chan1 = 0
				newMsg.chan2 = nums[0]
				newMsg.chan3 = nums[1]
				newMsg.chan4 = nums[2]
				newMsg.chan5 = nums[3]
				newMsg.chan6 = nums[4]
				newMsg.chan7 = nums[5]
				newMsg.chan8 = 0
				rospy.loginfo(newMsg)
        
if __name__ == "__main__":
    try:
        m = SerialReciever()
    except rospy.ROSInterruptException:
	m.ser.close()
        pass
