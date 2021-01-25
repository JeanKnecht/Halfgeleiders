import matplotlib.pyplot as plt
import serial
import numpy as np
plt.interactive(False)
ArduinoData = serial.Serial("com3", 9600)

run = True

millis = []
voltages = []

def makeGraph(millis, voltages):
    plt.axis
    plt.xticks(np.linspace(millis[0],millis[-1],10))
    plt.title("PWM(500Hz) visualisation")
    plt.xlabel("tijd(ms)")
    plt.ylabel("voltage(v)")

    plt.plot(millis, voltages)
    
    plt.show()

while run:
    if (ArduinoData.inWaiting()>0):
        for x in range(500):

            data = ArduinoData.readline().decode('utf-8')

            time_millis, voltage = data.split(" ")

            if "\x00" in time_millis:
                continue

            voltages.append(float(voltage.strip("\r\n")))
            millis.append(float(time_millis))

        
        makeGraph(millis, voltages)

        run = False
            
        


        


        