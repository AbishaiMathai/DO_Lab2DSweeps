import pyvisa
import numpy as np
import time
import os
import matplotlib.pyplot as plt
import csv
import datetime

rm = pyvisa.ResourceManager()

# Connect to Keithley 2450 (adjust the address as necessary)
keithleyOne = rm.open_resource('USB0::0x05E6::0x2450::04586138::INSTR')

# Setup Keithley for voltage source, current measure
keithleyOne.write("*RST")

start_vol = -5
stop_vol = 5.1

volts_sent = np.arange(start_vol, stop_vol, 0.1)

cur_read = []
volt_read = []
keithleyOne.write(":OUTP ON")
plt.title("Current vs Voltage")
plt.ylabel("Current (A)")
plt.xlabel("Voltage (V)")
plt.grid(True)
plt.tight_layout()


for i in volts_sent:
    keithleyOne.write("SOUR:FUNC VOLT")
    keithleyOne.write("SENS:FUNC 'CURR'")
    keithleyOne.write("SOUR:VOLT:READ:BACK ON")
    keithleyOne.write(f"SOUR:VOLT {i}")
    cur = keithleyOne.query(":READ?")
    cur_read.append(float(cur))
    keithleyOne.write("SENS:FUNC 'VOLT'")
    vol = keithleyOne.query(":READ?")
    volt_read.append(float(vol))
    plt.scatter(float(vol),float(cur))
    plt.pause(0.2)
keithleyOne.write(":OUTP OFF")   

# Get current timestamp
timestamp = datetime.datetime.now()

# Save to CSV file with timestamp
# csv_file = f'output_data_{timestamp}.csv'
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Current (A)', 'Voltage (V)'])
#     writer.writerows(zip(cur_read, volt_read))

# print(f"Data saved to {csv_file}")
# plt.scatter(volt_read,cur_read)

# plot_file = f'output_plot_{timestamp}.png'
# plt.savefig(plot_file)

plt.show()
