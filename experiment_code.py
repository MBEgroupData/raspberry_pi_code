from datetime import datetime
import time
from sense_hat import SenseHat
import requests
import json
from time import sleep

#color values to acheve 'black' or all LEDS off
k = (0,0,0)
white = (200,200,200)

if __name__ == "__main__":
    GROUP_NAME = "" ## put your group name inside the quotes## 
    
    #name of files to log data to
    LOG_FILE_SENSE = f"/home/User_1/{GROUP_NAME}_sense_hat_data.csv"

    with open(LOG_FILE_SENSE,'w') as senseLog:
        senseLog.write("Time,Temperature,Pressure,RelativeHumidity\n")

    #intialize sense hat
    sense = SenseHat()
    
    colors = []
    off = []
    on = []
    for i in range(0,64):
        colors.append(k)
        off.append(k)
        on.append(white)


    while True: 
        sleep(600)
        #get readings from the sense hat
        piTemp =sense.get_temperature()
        piPressure =sense.get_pressure()
        piHumid =sense.get_humidity()


        requests.post(f'https://rpi.mbelab.org/group/{GROUP_NAME}', json = {'time':datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),'temp':piTemp,'press':piPressure,'humid':piHumid,'leds':json.dumps(colors)})
        
        with open(LOG_FILE_SENSE,'a') as senseLog:
            senseLog.write(datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+",{},{},{}".format(piTemp,piPressure,piHumid))
            for color in colors:
                senseLog.write(",{},{},{}".format(color[0],color[1],color[2]))
            senseLog.write("\n")

        ## YOUR CODE GOES HERE ##        

        x = datetime.now()
        h = x.hour


        if h >= 22 or h<=6:
            sense.clear((0,0,0)) # make sure the leds are all off
            colors = off
        else:
            sense.set_pixels(on)
            colors = on

