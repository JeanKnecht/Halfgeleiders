import matplotlib.pyplot as plt
import serial
import numpy as np
plt.interactive(False)
ArduinoData = serial.Serial("com3", 9600)

run = True

amps = []
voltages = []

def makeGraph(millis, voltages):
    plt.axis
    plt.xticks(np.linspace(voltages[0],voltages[-1],8))
    plt.title("I(U)-karakteristiek Led")
    plt.xlabel("U(volt)")
    plt.ylabel("I(mA)")

    plt.plot(amps, voltages, "bo")
    
    plt.show()

while run:
    if (ArduinoData.inWaiting()>0):
        for x in range(51):

            data = ArduinoData.readline().decode('utf-8')

            ampere, voltage = data.split(" ")

            if "\x00" in ampere:
                continue

            voltages.append(float(voltage.strip("\r\n")))
            amps.append(float(ampere))

        
        makeGraph(amps, voltages)

        run = False
       