"""
Tutorial here:
https://tango-controls.readthedocs.io/projects/pytango/en/latest/tutorial/servers.html
"""

import tango


ServerName = "ClockSN"
ServerInstance = "testSI2"
DeviceClass = "Clock"
DeviceDomain = "test"
DeviceFamily = "Clock"
DeviceInstance = "2"

if __name__ == "__main__":
    db = tango.Database()
    dev_info = tango.DbDevInfo()

    dev_info.server = f"{ServerName}/{ServerInstance}"
    dev_info._class = f"{DeviceClass}"
    dev_info.name = f"{DeviceDomain}/{DeviceFamily}/{DeviceInstance}"

    db.add_device(dev_info)
