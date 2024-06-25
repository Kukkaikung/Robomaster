from robomaster import robot


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_chassis = ep_robot.chassis

    x_val = 0.6
    y_val = 0.6
    z_val = 90

    # 前进 0.5米
    ep_chassis.move(x=x_val, y=0, z=0, xy_speed=1).wait_for_completed()

    # 后退 0.5米
    #ep_chassis.move(x=0, y=-y_val, z=0, xy_speed=1).wait_for_completed()

    # 左移 0.6米
    #ep_chassis.move(x=-x_val, y=0, z=0, xy_speed=1).wait_for_completed()

    # 右移 0.6米
    #ep_chassis.move(x=0, y=y_val, z=0, xy_speed=1).wait_for_completed()

    # 左转 90度
    #ep_chassis.move(x=0, y=0, z=z_val, z_speed=45).wait_for_completed()

    # 右转 90度
    #ep_chassis.move(x=0, y=0, z=-z_val, z_speed=45).wait_for_completed()

    ep_robot.close()