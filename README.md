# DO LAB Python Measurement Scripts

These scripts are built directly on top of the (amazing) QCoDeS standard. Normally QCoDeS would be sufficient for running measurements in the form of a simple script could be made on a case-by-case basis for running measurements. However, we intend to use LabVIEW for the purpose of providing our front end, so the code here could be considered a "back end" of sorts.

## Project Structure

This project provides scripts to initialize and run 1D and 2D sweeps using Keithley 2450s. In the future it may provide functionality for temperature controllers and lock-in amplifiers, however it is unclear if we will just do this within LabVIEW alone. Eventually I (Grant) plan to abstract these scripts to handle any select QCoDeS source measurement driver as opposed to a pre-programmed driver.

The code is currently in the form of python notebooks for the sake of fast development. When it is in a good enough state we will build them into .py scripts which can be integrated into LabVIEW.

## documentation on each script TODO
