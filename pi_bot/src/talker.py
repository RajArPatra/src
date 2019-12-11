import cv2 as cv
import rospy

from std_msgs.msg import Int32

def talker():
	pub = rospy.Publisher('raj', Int32, queue_size = 10)
	rospy.init_node('talker', anonymous = True)
	rate = rospy.Rate(10)

	count = 0
	while not rospy.is_shutdown():
		msg = Int32()
		msg.data = count
		
		pub.publish(msg)
		rate.sleep()
		count = count + 1

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
		
