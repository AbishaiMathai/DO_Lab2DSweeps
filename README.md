# Unnamed Cryomagnetics Fridge Project @ DO lab

This is based on [MeasureIt](https://github.com/nanophys/MeasureIt) which itself is based on the [QCoDeS Standard](https://github.com/microsoft/qcodes).

The goal of this is to simplify some of the code from MeasureIt (removing the cluttered repo structure and dependency on building the project as a package) such that it is only dependent on a few libraries and the local source code. More importantly though, we also want to extend the project to implement 2D sweep functionality with source measurement units alongside real time plotting of the data.

## TODO
- [x] (initial) clean up the cluttered project structure
- [ ] implement 2D sweep functionality to the GUI
    - [x] add "2D Sweeps" entry to the menu bar (top) along with the dropdown entry for "Create 2D Sweep" 
    - [x] when "Create 2D Sweep" is clicked open a new window
    - [x] fill the window with fields necessary for configuring and running a 2D sweep
    - [ ] implement the ability to send the 2D sweep to the sweep queue
- [ ] comment the GUI code
- [ ] create a new requirements file for ease of installation
- [ ] remove dependency on unmaintained local drivers wherever possible
- [x] we should follow best practices for a pyqt project, i.e. getting the ui files moved somewhere out of the root of the project
- [ ] implement features for controlling lock in amplifiers and temperature controllers

It's very likely we will need to move many things around in the UI when it comes to controlling lock in amplifiers and temperature controllers. I (Grant) suggest we replace the central field with a "tab" arrangement where we can swap between different pages for 1D sweep, 2D sweep, temperature control, etc. Everything can come together (as in many things can be done at once for each device) in the queue which will be overhauled to support these new devices.
