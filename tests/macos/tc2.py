import pprint

class tc2:
    def __init__(self):
        pprint.pprint("In the constructor")

    def setup(self):
        pprint.pprint("In the setup")

    def test(self):
        pprint.pprint("In test")

    def teardown(self):
        pprint.pprint("In the teardown")


if __name__ == '__main__':
    tc = tc2()
    tc.setup()
    tc.test()
    tc.teardown()

