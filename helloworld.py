import pyvisa

# opens all connected devices
resourceManager=pyvisa.ResourceManager()

# assigns one instrument to a variable to control it using its VISA resource name
keithleyOne=resourceManager.open_resource("USB0::0x05E6::0x2450::04586138::INSTR")

# prints the query used on instrument
print(keithleyOne.query("*IDN?"))
#keithleyOne.write("DISP:TEXT \"Hello World\"")
#keithleyOne.write(":Digital:READ?")
#keithleyOne.write(":DIG:WRIT 63")
keithleyOne.write(":SYSTem:BEEPer 500,1")
# closes the instrument
keithleyOne.close()