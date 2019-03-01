import pygatt
import time
import struct

device = pygatt.GATTToolBackend()

#Rapid IoT kit Mac Address which is located at the back of the device
BLE_ADDRESS = '00:60:37:0A:B1:2A'

#Starting of the main fetching program
try:
    device.start()     #Starting the BLE  service
    rapid_iot = device.connect(BLE_ADDRESS)     #connect to the Rapid IoT prototying kit
    
    while True:      #Loop to continuously fetch the vallues

        # Value fetching, can be done with a loop too but I did this for easy interpretation
        
        fall_data = rapid_iot.char_read("ef771bab-10ff-4cdf-98f1-86e8a136423a")    #Fall Detection data    
       
        #converting bytearray to normal value and accessing the actual value(in Tuple)
        
        fall_value = struct.unpack('i',fall_data)     
        fall_value1 = fall_value[0]     

        #Printing the obtained values
        print "--------------- Rapid IoT kit Fall Detection Value---------------------"
        print "Fall Detection Value:"+str(fall_value1)
        print "----------------------------------------------------------------"

        
        time.sleep(5)      #A time delay of 5 seconds before reading the value
        
    
finally:
    device.stop()      #stop the BLE Adapter
