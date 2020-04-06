
import serial, string
import datetime

output = " "
ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1 ,timeout=5)
f = open('thing.txt', "w")
count = 0

while count < 10 : #True :
#   print ("----")
    while output != "" and output != "\n" and count < 10:
        print(count)
        count += 1
        #timestamp = datetime.datetime.
        curr = open("../data/currentData2.txt", "w")
        output = ser.readline()
        curr.write(str(output))
        f.write(datetime.datetime.now().strftime("%Y_%m%d_%H_%M_%s") + " " + str(output))
        curr.close()
        print (datetime.datetime.now().strftime("%Y_%m%d_%H_%M_%s") + " " + str(output).strip('\r\n'))
            