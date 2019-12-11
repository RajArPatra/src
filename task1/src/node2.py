import rospy
from std_msgs.msg import Int32

pub = rospy.Publisher('i2', Int32, queue_size = 10)
	
def callback(data):
	i = data.data ** 2
	msg = Int32()
	msg.data = i
	pub.publish(msg)

def listener():
	rospy.init_node('node2', anonymous = True)

	rospy.Subscriber('i1', Int32, callback)
	rospy.spin()
	
if __name__ == "__main__":
	listener()
