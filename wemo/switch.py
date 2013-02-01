
from wemo.device import WemoDevice


class WemoSwitch(WemoDevice):

    def get_state(self):
        return self.get_service('basicevent').GetBinaryState()

    def set_state(self, state):
        self.get_service('basicevent').SetBinaryState(BinaryState=int(state))

    def off(self):
        return self.set_state(0)

    def on(self):
        return self.set_state(1)

