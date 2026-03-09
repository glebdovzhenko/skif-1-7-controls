from sardana.pool.controller import MotorController
from sardana.pool.controller import Type
from tango import DeviceProxy
from sardana import State


class TangoXPSMotorTestController(MotorController):

    ctrl_properties = {
        "TangoDevice": {
            Type: str,
            "Description": "Full Tango device name"
        }
    }

    def init(self, inst, props, *args, **kwargs):
        super().init(inst, props, *args, **kwargs)

        self.device_name = props["TangoDevice"]
        self.dev = DeviceProxy(self.device_name)

    # ---- Mandatory methods ----


    def StateOne(self, axis):
        state = self.dev.state()

        if state.name == "MOVING":
            return State.Moving, ""
        elif state.name == "FAULT":
            return State.Fault, "Device in FAULT"
        else:
            return State.On, ""


    def ReadOne(self, axis):
        return self.dev.Position

    def StartOne(self, axis, position):
        self.dev.Position = position

    def StopOne(self, axis):
        self.dev.Stop()