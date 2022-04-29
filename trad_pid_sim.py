import time
import turtle
from PID import PID
from plant import Drone
import matplotlib.pyplot as plt


TIMESTAMP = 0.001


def main():
    drone = Drone()

    # ziegler-nicholas model
    ku = 0.8
    tu = 20
    kp = 0.6 * ku
    ki = 1.75 * ku / tu
    kd = 0.075 * ku * tu
    pid = PID(kp, ki, kd)
    
    target = 100
    count = 0
    sim_time = 5

    time_array = [count]
    y_array = [drone.y]

    marker = turtle.Turtle()
    marker.penup()
    marker.left(180)
    marker.goto(15, target)
    marker.color('red')

    while count < sim_time:
        error = target - drone.y
        thrust = pid.compute(error, TIMESTAMP)

        drone.input(thrust, TIMESTAMP)

        time.sleep(TIMESTAMP)
        count += TIMESTAMP
        
        time_array.append(count)
        y_array.append(drone.y)

        if drone.y > 800 or drone.y < -800:
            print("Out of bounds")
            break
    turtle.bye()
    plt.plot(time_array, y_array)
    plt.axhline(y=100, color='r')
    plt.show()


if __name__ == '__main__':
    main()