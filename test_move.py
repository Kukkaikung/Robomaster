import robomaster
from robomaster import robot






def sub_position_handler(position_info):
    x, y, z = position_info
    print("chassis position: x:{0}, y:{1}, z:{2}".format(x, y, z))


    
if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_chassis = ep_robot.chassis

    x_val = 0.5
    y_val = 0.5
    z_val = 90

    ep_chassis.sub_position(freq=5, callback=sub_position_handler)

    # 前进 0.5米
    ep_chassis.move(x=x_val, y=0, z=0, xy_speed=2).wait_for_completed()

    # 后退 0.5米
    ep_chassis.move(x=0, y=-y_val, z=0, xy_speed=0.5).wait_for_completed()

    # 左移 0.6米
    ep_chassis.move(x=-x_val, y=0, z=0, xy_speed=2).wait_for_completed()

    # 右移 0.6米
    ep_chassis.move(x=0, y=y_val, z=0, xy_speed=0.5).wait_for_completed()

    # 左转 90度
    #ep_chassis.move(x=0, y=0, z=z_val, z_speed=45).wait_for_completed()

    # 右转 90度
    #ep_chassis.move(x=0, y=0, z=-z_val, z_speed=45).wait_for_completed()


    
    ep_chassis.unsub_position()

    ep_robot.close()