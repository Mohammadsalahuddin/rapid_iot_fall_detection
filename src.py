import pygatt
import time
import struct

device = pygatt.GATTToolBackend()

#Rapid IoT Mac Address which is located at the back of the device
BLE_ADDRESS = '00:60:37:0A:B1:2A'

#Starting of the main fetching program
try:
    device.start()     #Starting the BLE  service
    rapid_iot = device.connect(BLE_ADDRESS)     #connect to the Rapid IoT prototying kit
    
    while True:      #Loop to continuously fetch the vallues

        # Value fetching, can be done with a loop too but I did this for easy interpretation
        
        light_initial = rapid_iot.char_read("227b5ea3-54f4-423c-95e4-7f9f10a78508")    #Ambient Light Value in bytearray     
        air_initial = rapid_iot.char_read("227b5ea3-54f4-423c-95e4-7f9f10a78509")      #Air Quality Value in bytearray
        pressure_initial = rapid_iot.char_read("227b5ea3-54f4-423c-95e4-7f9f10a7850b")  #Pressure Value in bytearray
        co2_initial = rapid_iot.char_read("227b5ea3-54f4-423c-95e4-7f9f10a7850a")   #CO@ Level
        
        #converting bytearray to normal value and accessing the actual value(in Tuple)
        
        light_value = struct.unpack('i',light_initial)     
        light_value1 = light_value[0]     

        air_value = struct.unpack('i',air_initial)
        air_value1 = air_value[0]

        pressure_value = struct.unpack('i',pressure_initial)
        pressure_value1 = pressure_value[0]
	pressure_value1 = pressure_value1/1000.0

        co2_value = struct.unpack('i',co2_initial)
        co2_value1 = co2_value[0]

        #Printing the obtained values
        print "--------------- Rapid IoT Sensor Values-------------------------"
        print "Ambient Light Value:"+str(light_value1)
        print "Air Quality Value(TVOC):"+str(air_value1)
        print "Pressure Value:"+str(pressure_value1)
        print "CO2 Value:"+str(co2_value1)
        print "----------------------------------------------------------------"

        
        time.sleep(5)      #A time delay of 5 seconds before reading the value
        
    
finally:
    device.stop()      #stop the BLE Adapter
