import robomaster
from robomaster import robot
import time
import matplotlib.pyplot as plt

# List to store position data
position_data = []

def sub_position_handler(position_info):
    x, y, z = position_info
    position_data.append((x, y, z))
    print("chassis position: x:{0}, y:{1}, z:{2}".format(x, y, z))

def save_position_data(file_name):
    with open(file_name, "w") as f:
        for pos in position_data:
            f.write(f"{pos[0]},{pos[1]}\n")

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_chassis = ep_robot.chassis

    x_val = 0.5
    y_val = 0.5
    z_val = 90

    ep_chassis.sub_position(freq=5, callback=sub_position_handler)

    # Move the robot
    ep_chassis.move(x=x_val, y=0, z=0, xy_speed=1).wait_for_completed()
    ep_chassis.unsub_position()
    save_position_data("position_data_1.csv")
    
    ep_chassis.sub_position(freq=5, callback=sub_position_handler)
    ep_chassis.move(x=0, y=-y_val, z=0, xy_speed=1).wait_for_completed()
    ep_chassis.unsub_position()
    save_position_data("position_data_2.csv")
    
    ep_chassis.sub_position(freq=5, callback=sub_position_handler)
    ep_chassis.move(x=-x_val, y=0, z=0, xy_speed=1).wait_for_completed()
    ep_chassis.unsub_position()
    save_position_data("position_data_3.csv")
    
    ep_chassis.sub_position(freq=5, callback=sub_position_handler)
    ep_chassis.move(x=0, y=y_val, z=0, xy_speed=1).wait_for_completed()
    ep_chassis.unsub_position()
    save_position_data("position_data_4.csv")

    ep_robot.close()

    # Read and combine position data from files
    position_data = []
    for i in range(1, 5):
        with open(f"position_data_{i}.csv", "r") as f:
            for line in f:
                x, y = map(float, line.strip().split(","))
                position_data.append((x, y))

    # Unpack position data into separate lists
    x_data, y_data = zip(*position_data)

    plt.figure(figsize=(10, 6))

    plt.plot(y_data,x_data, label='X Coordinate')
    # plt.plot(y_data, label='Y Coordinate')

    plt.xlabel('Time (arbitrary units)')
    plt.ylabel('Position (units)')
    plt.title('Robot Position Over Time')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()
