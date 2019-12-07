#!/usr/bin/env python
from __future__ import print_function

import roslib

import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from nav_msgs.msg import OccupancyGrid
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
    def __init__(self):
        self.image_pub = rospy.Publisher("image_topic_2",Image, queue_size=1)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/bdkr/env_observer/hokuyo_left/occupancy_grid",OccupancyGrid,self.callback, queue_size=1)
        self.image2_sub = rospy.Subscriber("/image_topic_2",Image,self.callback2, queue_size=1)

    def callback2(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "8UC1")
        except CvBridgeError as e:
            print(e)
        #print(data)
        cv2.imwrite('test.png', cv_image)
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)
            

    def callback(self,data):
        try:
            image = Image()
            image.header = data.header
            image.width = data.info.width
            image.height = data.info.height
            image.encoding = "mono8"
            image.is_bigendian = 0
            image.step = data.info.width
            image.data = map(lambda x: x+1, data.data)
            #image.data = data.data

            #np_arr = np.fromstring(image.data, np.uint8)
            #np_arr = np.array(image.data)
            
            #v_image = cv2.imdecode(np_arr, 1)
            #print(image)
                  
            self.image_pub.publish(image)
            #bridge = CvBridge()
            #cv_image = self.bridge.imgmsg_to_cv2(image2, "8UC1")
        except CvBridgeError as e:
            print(e)

        #rows,cols,channels = np_arr.shape
        #if cols > 60 and rows > 60 :
        #    cv2.circle(cv_image, (50,50), 10, 255)
                
        #cv2.imshow("Image window", cv_image)
        #cv2.waitKey(3)
        #try:
        #    self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "mono8"))
        #except CvBridgeError as e:
        #    print(e)
def main(args):
    rospy.init_node('image_converter', anonymous=True)
    ic = image_converter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
