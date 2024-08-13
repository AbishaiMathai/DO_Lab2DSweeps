# Unnamed Cryomagnetics Fridge Project @ DO lab

This is based on [MeasureIt](https://github.com/nanophys/MeasureIt) which itself is based on the [QCoDeS Standard](https://github.com/microsoft/qcodes).

The goal of this is to simplify some of the code from MeasureIt (removing the cluttered repo structure and dependency on building the project as a package) such that it is only dependent on a few libraries and the local source code. More importantly though, we also want to extend the project to implement 2D sweep functionality with source measurement units alongside real time plotting of the data.

## TODO
- [x] (initial) clean up the cluttered project structure
- [ ] implement 2D sweep functionality to the GUI
- [ ] create a new requirements file for ease of installation
- [ ] remove dependency on unmaintained local drivers wherever possible
- [ ] we should follow best practices for a pyqt project, see below

## Refactoring

While we have already made some progress fixing the original organizational issues with MeasureIt, we can do better. Typical pyqt-based projects follow a structure similar to that shown below. We ought to restructure our project to more closely follow this to stay organized.

```
├── main.py
├── ui_main.py
├── Modules
│   ├── Time_Data_Recorder
│   │   ├── TDR.py
│   │   ├── ui_TDR.py
│   ├── Spectral_Testing
│   └── Other_Modules
└── Third_Party_libraries
    ├── HDF5
    ├── Pyacq
    ├── Plotting
    └── Other
```
