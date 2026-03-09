"""
Tutorial here:
https://tango-controls.readthedocs.io/projects/pytango/en/latest/tutorial/servers.html
"""

from tango import DevState
from tango.server import Device
from tango.server import run, device_property, attribute, command
import time
import random
import string


class Clock(Device):
    _unique_name = ""

    model = device_property(
        dtype=str,
        default_value="",
    )

    def init_device(self):
        """
        Has to be overridden, otherwise it's not called at all.
        """
        super().init_device()
        self._unique_name = "".join(
            random.choices(string.ascii_letters + string.digits, k=10)
        )
        self.set_state(DevState.INIT)
        self.info_stream("init_device()")

    @attribute
    def time(self):
        return time.time()

    @command(dtype_in=str, dtype_out=str)
    def strftime(self, format):
        return time.strftime(format) + self._unique_name


if __name__ == "__main__":
    ServerName = "ClockSN"
    ServerInstance = "testSI2"

    run(
        (Clock,),
        args=[ServerName, ServerInstance],
    )
