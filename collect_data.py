from datetime import datetime
from sense_hat import SenseHat
import time



# DATA COLLECTION SCRIPT
#
# DESCRIPTION:
# This script collects temperature, pressure, and relative humidity data from 
# the Raspberry Pi Sense Hat and writes the data to a CSV file.
#
# OUTPUT:
# file: sense_hat_data.csv (stores data obtained from sense hat)
#            
#
#########################################################################################




if __name__ == "__main__":


    #name of files to log data to
    LOG_FILE_SENSE = 

    #intialize sense hat
    sense = SenseHat()


    for i in range(0,40):
        
        #get readings from the sense hat


        with open(LOG_FILE_SENSE,'a') as senseLog:
            senseLog.write(datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+",{},{},{},".format(piTemp,piPressure,piHumid)+"\n")

        # wait before taking readings again

        


