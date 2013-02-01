import logging
from pprint import pprint

import gevent
from wemo.motion import WemoMotion
from wemo.switch import WemoSwitch

from wemo.upnp import WemoUPnP
from wemo.device import WemoDevice

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class StopBroadcasting(Exception): pass

NOOP = lambda *x:None

class Manager(object):
    def __init__(self, switch_callback=NOOP, motion_callback=NOOP):
        self.upnp = WemoUPnP(self.found_device)
        self._switch_callback = switch_callback
        self._motion_callback = motion_callback
        self.switches = {}
        self.motions = {}

    def discover(self, timeout=10):
        log.info("Beginning discovery of devices")
        self.upnp.server.set_spawn(2)
        self.upnp.server.start()
        with gevent.Timeout(timeout, StopBroadcasting) as timeout:
            try:
                while True:
                    try:
                        self.upnp.broadcast()
                        gevent.sleep(1)
                    except Exception as e:
                        raise StopBroadcasting(e)
            except StopBroadcasting:
               return

    def found_device(self, address, headers):
        usn = headers['usn']
        if usn.startswith('uuid:Socket'):
            switch = WemoSwitch(headers['location'])
            self.switches[switch.name] = switch
            self._switch_callback(switch)
        elif usn.startswith('uuid:Sensor'):
            motion = WemoMotion(headers['location'])
            self.motions[motion.name] = motion
            self._motion_callback(motion)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    manager = Manager()
