from sense_hat import SenseHat
import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#
# DESCRIPTION:
# This program continually reads the temperature value 
# from the sense hat and plots it in near real time.
#
#
#
#
#################################################################






def animate(i,sense,x_secs, x_datetime, ys):
    """ Update a plot with the current sensor data

    Keyword arguments:
    i -- a counter that is automatically updated when called by the animation function
    sense -- The reference to the Pi SenseHat
    x_secs -- the array holding the time of reading in seconds
    x_datetime -- the array holding the time of readings in a string format
    ys -- the array holding the sensor data being plotted
    """

    # Read info from the sensors


    #read the orientation in yaw direction
    raw = sense.get_temperature()

    # Add x and y to lists
    x_datetime.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    x_secs.append(time.time())
    ys.append(raw)

    # Limit x and y lists to 20 items
    x_datetime = x_datetime[-15:]
    ys = ys[-15:]

    # Draw x and y lists
    ax.clear()
    ax.plot(x_datetime, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.title('Temperature over Time')
    plt.ylabel('Temp (deg C)')



if __name__ == "__main__":
    #obtain a reference to the sense hat
    sense = SenseHat()
    #create the figure for the plot
    #and the arrays for the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x_datetime = []
    ys = []

    #create the animation function for the plot
    #and then display the plot
    ani = animation.FuncAnimation(fig, animate, fargs=(sense, x_secs,x_datetime, ys), interval=100)
    plt.show()
