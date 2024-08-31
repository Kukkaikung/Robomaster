import time
from robomaster import robot
from robomaster import camera
import cv2

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="rndis")

    ep_camera = ep_robot.camera

    # 显示十秒图传
    ep_camera.start_video_stream(display=False, resolution=camera.STREAM_720P)
    time.sleep(10)
    img = ep_camera.read_cv2_image(strategy="newest")
    cv2.imshow("Robot", img)
    cv2.waitKey()
    time.sleep(1)
    filename = f"Test_camer.jpg"
    cv2.imwrite(filename, img)
    ep_camera.stop_video_stream()
    
    #print(f"Image saved as {filename}")
    ep_robot.close()