import rospy
from std_msgs.msg import Int32

def callback(data):
		print data.data
	
def listener():
 	rospy.init_node('node3' , anonymous=True)
 	rospy.Subscriber('i2', Int32, callback)
 	rospy.spin()
 	
if __name__ == "__main__":
	listener()
	
