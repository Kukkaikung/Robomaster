from robomaster import robot
import matplotlib.pyplot as plt
import time

# List to store position data
position_data = []

def sub_position_handler(position_info):
    x, y, z = position_info
    position_data.append((x, y, z))
    print("chassis position: x:{0}, y:{1}, z:{2}".format(x, y, z))

    global now_x_position
    global now_y_position

    now_x_position = x
    now_y_position = y



if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_chassis = ep_robot.chassis

    x_val = 0.6
    y_val = 0.6
    z_val = 0

    ep_chassis.sub_position(freq=5, callback=sub_position_handler)

    # Move the robot
    for i in range(5) :

            ep_chassis.move(x=x_val, y=0, z=0, xy_speed=0.8).wait_for_completed()
            if 0.6 - now_x_position != 0 :
                x_position = 0.6 - now_x_position
                print(f' นี่คือผลต่าง x : {x_position}')
                ep_chassis.move(x=x_position, y=0, z=0, xy_speed=0.8).wait_for_completed()
            time.sleep(1)
            
            ep_chassis.move(x=0, y=-y_val, z=0, xy_speed=0.8).wait_for_completed()
            if 0.6 + now_y_position != 0 :
                y_position = 0.6 + now_y_position
                print(f' นี่คือผลต่าง y : {y_position}')
                ep_chassis.move(x=0, y=-y_position, z=0, xy_speed=0.8).wait_for_completed()
            time.sleep(1)

            ep_chassis.move(x=-x_val, y=0, z=0, xy_speed=0.8).wait_for_completed()
            if now_x_position != 0 :
                x_position = -now_x_position
                print(f' นี่คือผลต่าง  x : {x_position}')
                ep_chassis.move(x=x_position, y=0, z=0, xy_speed=0.8).wait_for_completed()
            time.sleep(1)
            
            ep_chassis.move(x=0, y=y_val, z=0, xy_speed=0.8).wait_for_completed()
            if now_y_position != 0 :
                y_position = -now_y_position
                print(f' นี่คือผลต่าง y :{y_position}')
                ep_chassis.move(x=0, y=y_position, z=0, xy_speed=0.8).wait_for_completed()
            time.sleep(1)

    # Unsubscribe from position updates
    ep_chassis.unsub_position()

    # Save position data to a file
    with open("position_data.csv", "w") as f:
        for pos in position_data:
            f.write(f"{pos[0]},{pos[1]}\n")

    ep_robot.close()

    with open("position_data.csv", "r") as f:
        for line in f:
            x, y = map(float, line.strip().split(","))
            position_data.append((x, y))

    # Unpack position data into separate lists
    x_data, y_data = zip(*position_data)

    plt.figure(figsize=(10, 6))

    plt.plot(x_data,y_data)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Robot Position Over Time')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()