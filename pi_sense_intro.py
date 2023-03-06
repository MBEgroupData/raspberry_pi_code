from sense_hat import SenseHat
from time import sleep

# PI SENSE HAT INTRODUCTION
#
# DESCRIPTION:
# This program reads the temperature, humidity, and pressure from the sense hat,
# and then prints out those values on the LED matrix on the sense hat in a scrolling message.
# It updates the values in the message every 10 seconds.
#
#
#
#
#
########################################################################################################




if __name__ == "__main__":
    sense = SenseHat()

    while(True):

        humidity = sense.get_humidity()
        temp = sense.get_temperature()
        pressure = sense.get_pressure()

        message = "Temp:{:.0f} C, Pressure: {:.0f} mbar, Humidity: {:.0f} rH ".format(temp,pressure,humidity)
        sense.show_message(message, text_colour=[255,0,0])
        sleep(10)

