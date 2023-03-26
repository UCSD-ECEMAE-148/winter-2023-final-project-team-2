import cv2
import numpy as np
#from pyvesc import VESC
import time
import depthai as dai


# BOOST = "boost"
# BOOST_RPM = 8000

# SLOW = "slow"
# SLOW_RPM = 3000

# STOP = "stop"
# STOP_RPM = 0

# NORMAL = "normal"
# NORMAL_RPM = 5000


# SERIAL_PORT = "/dev/ttyACM0"

# def set_rpm(rpm):
#     with VESC(serial_port=SERIAL_PORT) as motor:
#         motor.set_duty_cycle(.02)
#         motor.set_rpm(rpm)
#     return
        

# def set_state(state):
#     if state == BOOST:
#         set_rpm(BOOST_RPM)
#         time.sleep(2)
#     elif state == SLOW:
#         set_rpm(SLOW_RPM)
#         time.sleep(2)
#     elif state == STOP:
#         set_rpm(STOP_RPM)
#         time.sleep(2)

#     set_rpm(NORMAL_RPM)

#     return
    


def contour_detection(imageFrame,depth_data): 
    # set_state(NORMAL)
    real_depth=0
    frame_result=0
    desparity=0
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Calculate total pixels in frame
    total_pixels = np.prod(imageFrame.shape[:2])
  
    # Set range for orange color and 
    # define mask
    orange_lower = np.array([5, 50, 50], np.uint8)
    orange_upper = np.array([15, 255, 255], np.uint8)
    orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)

    # Calculate porportion to frame
    orange_pixels = cv2.countNonZero(orange_mask)
    orange_percentage = orange_pixels / total_pixels
  
    # Set range for pink color and 
    # define mask
    pink_lower = np.array([140, 50, 50], np.uint8)
    pink_upper = np.array([180, 255, 255], np.uint8)
    pink_mask = cv2.inRange(hsvFrame, pink_lower, pink_upper)

    # Calculate porportion to frame
    pink_pixels = cv2.countNonZero(pink_mask)
    pink_percentage = pink_pixels / total_pixels

  
    # Set range for blue color and
    # define mask
    blue_lower = np.array([94, 50, 50], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    # Calculate porportion to frame
    blue_pixels = cv2.countNonZero(blue_mask)
    blue_percentage = blue_pixels / total_pixels

    kernel = np.ones((5, 5), "uint8")
      
    orange_mask = cv2.dilate(orange_mask, kernel)
    #pink_mask = cv2.dilate(pink_mask, kernel)
    blue_mask = cv2.dilate(blue_mask, kernel)

   
    # Creating contour to track orange color
    contours, hierarchy = cv2.findContours(orange_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for _, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 20000):
            x, y, w, h = cv2.boundingRect(contour)
            
           
            depth_data = cv2.rectangle(depth_data, (x, y), 
                                       (x+w, y+h), 
                                       (0, 0, 0), 2)
            
            frame_np = np.array(depth_data)
            frame_box = frame_np[int(x+0.45*w):int(x+0.55*w),int(y+0.45*h):int(y+0.55*h)]
            if(frame_box.any()):
                desparity = np.max(frame_box)
                if (desparity>0):
                    real_depth = (441.25 * 7.5)/desparity
            else:
                desparity = 0
                real_depth = 0

            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w-10, y + h-10),
                                       (0, 0, 0), 2)
            cv2.putText(imageFrame, "Orange Colour " + str(int(real_depth)) + "cm", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))    
  
    # Creating contour to track pink color
    contours, hierarchy = cv2.findContours(pink_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for _, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 20000):
            x, y, w, h = cv2.boundingRect(contour)
            
           
            depth_data = cv2.rectangle(depth_data, (x, y), 
                                       (x+w, y+h), 
                                       (0, 0, 255), 2)
            
            frame_np = np.array(depth_data)
            frame_box = frame_np[int(x+0.45*w):int(x+0.55*w),int(y+0.45*h):int(y+0.55*h)]
            if(frame_box.any()):
                desparity = np.max(frame_box)
                if (desparity>0):
                    real_depth = (441.25 * 7.5)/desparity
            else:
                desparity = 0
                real_depth = 0

            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w-10, y + h-10),
                                       (0, 255, 0), 2)
            cv2.putText(imageFrame, "Pink Colour " + str(int(real_depth)) + "cm", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (255, 255, 0))
     
    # Creating contour to track blue color
    contours, _ = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for _, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 20000):
            x, y, w, h = cv2.boundingRect(contour)
            
           
            depth_data = cv2.rectangle(depth_data, (x, y), 
                                       (x+w, y+h), 
                                       (0, 0, 255), 2)
            
            frame_np = np.array(depth_data)
            frame_box = frame_np[int(x+0.45*w):int(x+0.55*w),int(y+0.45*h):int(y+0.55*h)]
            if(frame_box.any()):
                desparity = np.max(frame_box)
                if (desparity>0):
                    real_depth = (441.25 * 7.5)/desparity
            else:
                desparity = 0
                real_depth = 0

            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w-10, y + h-10),
                                       (60, 255, 255), 2)

            cv2.putText(imageFrame, "Blue Colour "+  str(int(real_depth)) +"cm", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (60, 255, 255))
    
    if orange_percentage >= 0.4:
        print("ORANGE "+ str(int(real_depth)) + " cm away")
        # set_state(STOP)
    if blue_percentage >= 0.4:
        print("BLUE "+ str(int(real_depth))+ " cm away")
        # set_state(BOOST)
    if pink_percentage >= 0.4:
        print("PINK "+ str(int(real_depth))+ " cm away")
        # set_state(SLOW)

    return imageFrame




# Initialize the webcam
#cap = cv2.VideoCapture(0)
#Using DepthAI


pipeline = dai.Pipeline()

cam_rgb = pipeline.create(dai.node.ColorCamera)
cam_rgb.setPreviewSize(640, 400)
cam_rgb.setInterleaved(False)
cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)

xout_rgb = pipeline.create(dai.node.XLinkOut)
xout_rgb.setStreamName('rgb')
cam_rgb.preview.link(xout_rgb.input)



# left and right cam
# Closer-in minimum depth, disparity range is doubled (from 95 to 190):
extended_disparity = True
# # Better accuracy for longer distance, fractional disparity 32-levels:
subpixel = False
# # Better handling for occlusions:
lr_check = True

# # Define sources and outputs
monoLeft = pipeline.create(dai.node.MonoCamera)
monoRight = pipeline.create(dai.node.MonoCamera)
depth = pipeline.create(dai.node.StereoDepth)
xout = pipeline.create(dai.node.XLinkOut)

xout.setStreamName('disparity')

# # Properties
monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)
 
# # Create a node that will produce the depth map (using disparity output as it's easier to visualize depth this way)
depth.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_DENSITY)
# Options: MEDIAN_OFF, KERNEL_3x3, KERNEL_5x5, KERNEL_7x7 (default)
depth.initialConfig.setMedianFilter(dai.MedianFilter.KERNEL_7x7)
depth.setLeftRightCheck(lr_check)
depth.setExtendedDisparity(extended_disparity)
depth.setSubpixel(subpixel)

# # Linking
monoLeft.out.link(depth.left)
monoRight.out.link(depth.right)
depth.disparity.link(xout.input)


# Output queue will be used to get the disparity frames from the outputs defined above
device = dai.Device(pipeline)
q = device.getOutputQueue(name='disparity', maxSize=4, blocking=False)
output = device.getOutputQueue(name='rgb', maxSize=4, blocking=False)


while True:
    inDisparity = q.get()  # blocking call, will wait until a new data has arrived
    frame = inDisparity.getFrame()
    
    frame = (frame * (255 / depth.initialConfig.getMaxDisparity())).astype(np.uint8)
    
    in_rgb = output.get()
    frame_rgb = in_rgb.getCvFrame()
    
    result = contour_detection(frame_rgb,frame)
    
    cv2.imshow('RGB', result)
    # Check if the user pressed the 'q' key to quit
    if cv2.waitKey(1) == ord('q'):
         break

# Release the webcam and close all windows
#cap.release()
cv2.destroyAllWindows()