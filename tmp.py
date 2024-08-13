def Keithley_Set_Source_Generic(keithley, parameter: str, value: float) -> float:
    """Generic implementation of a setter for source parameters on a keithley 2450. Returns the setpoint for the respective parameter.

    This should be replaced with an abstract implementation during the future rewrite for other SMUs. This is simply just a shorthand way to set either current/voltage depending on the set parameter.

    Typical usage example:
        Keithley_Set_Source_Generic(keithley1, "current", 1E-6)  # Puts 1uA through the source.
        Keithley_Set_Source_Generic(keithley2, "voltage", 5)     # Puts 5V through the source.

    Args:
        keithley (qcodes.instrument_drivers.Keithley.Keithley_2450.Keithley2450): The keithley device to be operated on. Initialize one with initialize_keithley()
        parameter (str): either "current" or "voltage".
        value (float): the setpoint for the given parameter.
    """

    if parameter == "current":
        keithley.source.current(value)
        current_setpoint = keithley.source.current()
        return current_setpoint
    elif parameter == "voltage":
        keithley.source.voltage(value)
        voltage_setpoint = keithley.source.voltage()
        return current_setpoint
    else:
        raise ValueError("Invalid parameter option, use either 'current' or 'voltage'")


def Keithley_Set_Sense_Generic(keithley, parameter: str) -> float:
    """Generic implementation of a setter for sense parameters on a keithley 2450. Returns the measured value for the respective parameter.

    This should be replaced with an abstract implementation during the future rewrite for other SMUs. This is simply a shorthand way to access sense parameters.

    Typical usage example:
        Keithley_Set_Sense_Generic(keithley1, "current")     # Sets sense to current for keithley1.
        Keithley_Set_Sense_Generic(keithley2, "voltage")     # Sets sense to voltage for keithley2.

    Args:
        keithley (qcodes.instrument_drivers.Keithley.Keithley_2450.Keithley2450): The keithley device to be operated on. Initialize one with initialize_keithley()
        parameter (str): either "current" or "voltage".
    """

    if parameter == "current":
        with keithley.output_enabled.set_to(True):
            current = keithley.sense.current()
            return current
    elif parameter == "voltage":
        with keithley.output_enabled.set_to(True):
            voltage = keithley.sense.voltage()
            return voltage
    else:
        raise ValueError("Invalid parameter option, use either 'current' or 'voltage'")


def Sweep2D(
    experiment,
    inner_keithley,
    inner_start: float,
    inner_stop: float,
    inner_samples: int,
    inner_sense: str,
    inner_source: str,
    outer_keithley,
    outer_start: float,
    outer_stop: float,
    outer_samples: int,
    outer_sense: str,
    outer_source: str,
):
    import numpy as np

    for i in np.linspace(outer_start, outer_stop, num=outer_samples):

        _do_imports()

        # I will likely need to implement a poll here to wait until the parameter is swept to the setpoint. 
        # It's very likely that the code will progress too quickly and initiate the 1D sweep on a value other than the intended value.

        Keithley_Set_Source_Generic(outer_keithley, outer_source, i)
        print(f"outer setpoint: {i}")
        measured_value = Keithley_Set_Sense_Generic(outer_keithley, outer_source)
        print(f"actual value: {measured_value}")

        # once the outer keithley has swept to the intended value, begin a sweep with the inner keithley.

        inner_keithley.sense.function(sense)
        inner_keithley.sense.range(sense_range)
        
        inner_keithley.source.function(source)
        inner_keithley.source.range(source_range)
        inner_keithley.source.sweep_setup(start, step, stop)

        # measurement needs to be initialized properly for outer keithley.
        # it's likely we will need to use our own system here.

        meas = Measurement(exp=experiment)
        meas.register_parameter(keithley.sense.sweep)

        with meas.run() as datasaver:
            datasaver.add_result((keithley.source.sweep_axis, keithley.source.sweep_axis()),
                                 (keithley.sense.sweep, keithley.sense.sweep()))

            dataid = datasaver.run_id

        # correctly plotting this poses a bit of a hassle, I'll leave it as a problem for future me.

Sweep2D(
    experiment=None,
    inner_keithley=None,
    inner_start=0,
    inner_stop=10,
    inner_samples=10,
    inner_sense=None,
    inner_source=None,
    outer_keithley=None,
    outer_start=0,
    outer_stop=10,
    outer_samples=10,
    outer_sense=None,
    outer_source=None
)
