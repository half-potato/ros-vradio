#!/usr/bin/env python
import rospy, serial, math
from vradio.msg import Radio

class SerialRadio:
    def __init__(self):
        rospy.init_node("serial_radio", anonymous=False)
        port = rospy.get_param("~port")
        radio = rospy.get_param("~radio")
        self.pub = rospy.Subscriber(radio, Radio, self.callback, queue_size=10)
        self.ser = serial.Serial(port, 9600, timeout=0.1)
        rospy.spin()
    def callback(self, data):
	print("Hi")
        #    	gear			  rudd			  elev
        msg = "S:" + str(data.chan2) + ":" + str(data.chan3) + ":" + str(data.chan4)
        #    	    aile			thro
        msg = msg + ":" + str(data.chan5) + ":" + str(data.chan6)
        self.ser.write(msg)
        
if __name__ == "__main__":
    try:
        m = SerialRadio()
    except rospy.ROSInterruptException:
        m.ser.close()
        pass
