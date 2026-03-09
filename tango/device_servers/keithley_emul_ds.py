#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tango import DevState, AttrWriteType
from tango.server import Device, attribute, command, run

from meas_dev_emul import Meter


class KeithleyEmul(Device):

    # -------- Attributes --------

    AccTime = attribute(
        dtype=float,
        access=AttrWriteType.READ_WRITE,
        unit="s",
        label="Accumulation Time"
    )

    Channel1 = attribute(
        dtype=float,
        access=AttrWriteType.READ
    )

    Channel2 = attribute(
        dtype=float,
        access=AttrWriteType.READ
    )

    # -------- Initialization --------

    def init_device(self):
        super().init_device()

        self.meter = Meter()
        self._last_values = [0.0, 0.0]

        self.set_state(DevState.ON)

    # -------- Attribute methods --------

    def read_AccTime(self):
        return self.meter.acc_time

    def write_AccTime(self, value):
        self.meter.setAccTime(value)

    def read_Channel1(self):
        return self._last_values[0]

    def read_Channel2(self):
        return self._last_values[1]

    # -------- Commands --------

    @command(dtype_out=(float,))
    def Measure(self):
        self.set_state(DevState.RUNNING)

        self._last_values = self.meter.meas()

        self.set_state(DevState.ON)
        return self._last_values

    @command
    def Reset(self):
        self.meter.reset()
        self._last_values = [0.0, 0.0]
        self.set_state(DevState.ON)


if __name__ == "__main__":
    run([KeithleyEmul])