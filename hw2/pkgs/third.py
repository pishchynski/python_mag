from action import Action


class ThirdAction(Action):
    def __init__(self):
        super(ThirdAction, self).__init__(priority=20,
                                          period=5,
                                          exact=16,
                                          critical=False)

    def do_action(self):
        print "SecondAction says 'Hello, dear instructor!'"
