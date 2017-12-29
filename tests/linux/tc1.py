import pprint
import logging
import os

LOG = logging.getLogger(os.path.basename(__file__))

class tc1:
    def __init__(self):
        LOG.info("In the constructor")
        pprint.pprint("In the constructor")

    def setup(self):
        LOG.info("In the setup")
        pprint.pprint("In the setup")

    def test(self):
        LOG.info("In test")
        pprint.pprint("In test")

    def teardown(self):
        LOG.info("In the teardown")
        pprint.pprint("In the teardown")


if __name__ == '__main__':
    tc = tc1()
    tc.setup()
    tc.test()
    tc.teardown()

