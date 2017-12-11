from action import Action


class FirstAction(Action):
    def __init__(self):
        super(FirstAction, self).__init__(priority=10,
                                          period=10,
                                          exact=5,
                                          critical=False)

    def do_action(self):
        print "FirstAction says 'Hello, Belarus!'"
