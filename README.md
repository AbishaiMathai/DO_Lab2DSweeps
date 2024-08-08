# DO LAB Python Measurement Scripts

These scripts are built directly on top of the (amazing) QCoDeS standard. Normally QCoDeS would be sufficient for running measurements in the form of a simple script could be made on a case-by-case basis for running measurements. However, we intend to use LabVIEW for the purpose of providing our front end, so the code here could be considered a "back end" of sorts.

To list available VISA devices run (we ought to put this into a proper script for LabVIEW eventually):

```python
import pyvisa
rm = pyvisa.ResourceManager()
rm.list_resources()
```

## TODO!

1. Create tests for each function
2. Sweep2D function
3. Documentation on each function
4. Abstract sweeps to handle any SMU as opposed to just Keithley 2450s 
5. Implement lock-in amplifiers and temperature controllers (?)

## Project Structure

The python-LabVIEW workflow is a bit weird since only functions can be called within the LabVIEW graph. Objects can be passed around, though, so we initialize anything that needs to be continuously worked with as an object. This includes SMUs and experiment files, currently. QCoDeS provides convenient class descriptions under the hood for these things.

The idea is to first open a python session with the corresponding node. Then we use a python node to call `initialize_keithley` and `initialize_experiment`. The refnum will then be plugged into `Sweep1D` or `Sweep2D` (or any other measurement). Everything is intended to be able to be strung together in a huge variety of ways.

## documentation on each script TODO
