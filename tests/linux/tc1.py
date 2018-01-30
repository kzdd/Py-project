import pprint
import logging
import os
from library.host import Host
LOG = logging.getLogger(os.path.basename(__file__))

class tc1:
    def __init__(self):
        self.host_obj = Host("73.170.151.236")
        pprint.pprint("In the constructor")

    def setup(self):
        LOG.info("In the setup")
        pprint.pprint("In the setup")

    def test(self):
        LOG.info("In test")
        pprint.pprint("In test")
        cmd = "ls -al /"
        self.host_obj.execute(cmd)


    def teardown(self):
        LOG.info("In the teardown")
        pprint.pprint("In the teardown")


if __name__ == '__main__':
    tc = tc1()
    tc.setup()
    tc.test()
    tc.teardown()

