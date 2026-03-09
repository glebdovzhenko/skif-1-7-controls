from sardana.pool.controller import ZeroDController
from sardana import State
import PyTango

class Keithley0DController(ZeroDController):
    """0D Controller for Keithley (2 channels only)"""

    ctrl_properties = {
        "TangoDevice": {
            "Type": str,
            "Description": "Full Tango device name (e.g. test/keithley/1)"
        }
    }

    def init(self, inst, props, *args, **kwargs):
        super().init(inst, props, *args, **kwargs)

        self._device = None
        self._last_values = [0.0, 0.0]  # ch1, ch2

        #device_name = self.TangoDevice
        #self._dev = PyTango.DeviceProxy(device_name)

    def AddDevice(self, axis):
        if self._device is None:
            self._device = PyTango.DeviceProxy(self.TangoDevice)

    def DeleteDevice(self, axis):
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write("DeleteDevice")
        pass

    def PreReadAll(self):
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write("PreReadAll")
        pass

    def StateOne(self, axis):
        return State.On, "OK"    
    
    def ReadAll(self):
        try:
            with open("output.txt", "w", encoding="utf-8") as f:
                f.write("ReadAll")
            values = self._device.Measure()

            if values is None:
                print("Measure returned None")
                return

            print("Measure returned:", values)

            self._last_values[0] = float(values[0])
            self._last_values[1] = float(values[1])

        except Exception as e:
            print("ReadAll error:", e)

    def ReadOne(self, axis):

        with open("output.txt", "w", encoding="utf-8") as f:
            f.write("ReadOne")
        value = self._last_values[axis - 1]

        if value is None:
            return 0.0

        return float(value)
    
    def StartAll(self):
        
        values = self._device.Measure()

        with open("output.txt", "w", encoding="utf-8") as f:
            f.write("StartAll")
            f.write(values)


        if values and len(values) >= 2:
            self._last_values = [float(values[0]), float(values[1])]
        else:
            self._last_values = [0.0, 0.0]

"""
    def ReadAll(self):
        self._last_values = list(self._device.Measure())
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(self._device.Measure(), list(self._device.Measure()))  

    def StartOne(self, axis):

        ch_values = self._device.Measure()  # returns tuple (ch1, ch2)
        time.sleep(1)
        self._last_values = list(ch_values)  # ch1, ch2
    
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(ch_values)  
   
        return self._last_values[axis - 1]  # axis=1 → ch1, axis=2 → ch2
    
    def StartAll(self):
        self._last_values = list(self._device.Measure())

    
    def ReadOne(self, axis):
        return self._last_values[axis - 1]
    
   def ReadAll(self):
       try:
           values = self._device.Measure()

            if values and len(values) >= 2:
              self._last_values = [float(values[0]), float(values[1])]
            else:
                # fallback 
              self._last_values = [0.0, 0.0]

       except Exception as e:
           print("Measure error:", e)
           self._last_values = [0.0, 0.0]
 """