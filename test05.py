# -*-coding:utf-8-*-
# Copyright (c) 2020 DJI.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
from robomaster import robot
from robomaster import camera
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="rndis")

    ep_camera = ep_robot.camera

    # บันทึกเวลาการทำงานของกล้อง
    times = []

    ep_camera.start_video_stream(display=True, resolution=camera.STREAM_360P)
    start_time = time.time()
    for i in range(10):
        current_time = time.time() - start_time
        times.append(current_time)
        time.sleep(1)  # บันทึกเวลาในแต่ละวินาที
    ep_camera.stop_video_stream()

    ep_robot.close()

    # สร้างกราฟแสดงเวลาที่กล้องทำงาน
    plt.plot(times, [1] * len(times), 'ro')  # จุดแดงสำหรับแต่ละเวลาที่บันทึกได้
    plt.xlabel('Time (s)')
    plt.ylabel('Camera Active')
    plt.title('Camera Active Time')
    plt.show()
